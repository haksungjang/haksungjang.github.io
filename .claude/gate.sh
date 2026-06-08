#!/usr/bin/env bash
# quality-gate: 커밋 전 통과해야 하는 검증.
# Hugo 정적 사이트의 실질적 검증은 "프로덕션 빌드 성공" 여부.
set -euo pipefail

cd "$(dirname "$0")/.."

echo "==> Hugo 프로덕션 빌드 검증"
npm run build:production

echo "==> gate 통과"
