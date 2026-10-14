#!/usr/bin/env python3
"""배포 직후 바뀐 페이지를 IndexNow로 검색엔진(Bing, 네이버, Yandex 등)에 알린다.

- 키: static/ 아래 "<키>.txt" 파일(내용이 파일명과 같은 32자리 16진수)에서 읽는다.
  사이트에 공개되는 값이라 저장소에 두어도 된다.
- 대상: 빌드 결과(public/)의 언어별 sitemap에서 lastmod가 최근 N시간 안인 URL.
  enableGitInfo로 lastmod가 커밋 시각을 따르므로, 이번 배포에서 바뀐 페이지가 잡힌다.

사용법: python3 .github/scripts/indexnow.py [--hours 24] [--dry-run]
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.request

HOST = "haksungjang.github.io"
SITE = f"https://{HOST}"


def find_key():
    for path in glob.glob("static/*.txt"):
        stem = os.path.splitext(os.path.basename(path))[0]
        if re.fullmatch(r"[0-9a-f]{32}", stem) and open(path).read().strip() == stem:
            return stem
    sys.exit("IndexNow 키 파일(static/<키>.txt)을 찾지 못했습니다.")


def recent_urls(hours):
    since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=hours)
    urls = []
    for sm in glob.glob("public/**/sitemap.xml", recursive=True):
        text = open(sm, encoding="utf-8").read()
        for loc, lastmod in re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", text):
            try:
                when = dt.datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
            except ValueError:
                continue
            if when.tzinfo is None:
                when = when.replace(tzinfo=dt.timezone.utc)
            if when >= since and loc.startswith(SITE):
                urls.append(loc)
    for extra in ("/llms.txt", "/en/llms.txt"):
        urls.append(SITE + extra)
    return sorted(set(urls))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    key = find_key()
    urls = recent_urls(args.hours)[:10000]
    print(f"IndexNow 대상 {len(urls)}건")
    for u in urls:
        print("  " + u)
    if args.dry_run:
        return
    body = json.dumps({
        "host": HOST,
        "key": key,
        "keyLocation": f"{SITE}/{key}.txt",
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"IndexNow 응답 {resp.status}")
    except urllib.error.HTTPError as e:
        # 알림 실패가 배포 자체를 실패로 만들지 않도록 경고만 남긴다
        print(f"::warning::IndexNow 응답 {e.code}: {e.read()[:200]!r}")


if __name__ == "__main__":
    main()
