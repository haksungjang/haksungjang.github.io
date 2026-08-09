# How to Write Copyright Statements in Source Code

> Introduces why copyright statements are needed in source code and how to write them correctly.

---

LLMS index: [llms.txt](/llms.txt)

---

> Hello.
> 
> [Matija Šuklje](https://matija.suklje.name/), a well-known attorney in the open source field, recently [introduced](https://matija.suklje.name/how-and-why-to-properly-write-copyright-statements-in-your-code) why copyright statements are needed in source code and how to write them correctly.
> 
> The post below is based on the original article above. Most of it is translated directly from the original so that the author's intent is faithfully conveyed.

---

I started out thinking of this as a simple copyright notice guide for developers, but since there was no unified guide for how to display copyright information, writing the guide wasn't easy. In the end, I decided to write a new one.

I tried to strike a balance while keeping the following points in mind.

1. For developers who simply want a quick answer for what to do
2. For FOSS compliance staff and lawyers who want to understand not just the best practices but also the reasoning behind them

If you are extremely short on time, check the minimal guide in [TL;DR](#tldr). If you have about 2 minutes, read the [actual HowTo a bit lower below](#the-correct-way-to-write-a-copyright-statement-and-license-notice).

Of course, if you have about 20 minutes, the best option is to read it from start to finish.

## TL;DR

Add a copyright and license statement in the following format to every source code file you write.
```yaml
SPDX-FileCopyrightText: © {$year_of_file_creation} {$name_of_copyright_holder} <{$contact}>

SPDX-License-Identifier: {$SPDX_license_name}
```

For example, if I wrote a source code file today and released it under the [BSD-3-Clause license][bsd-3-clause], I would add the following content in the header comment at the top of the file.

```yaml
SPDX-FileCopyrightText: © 2020 Matija Šuklje <matija@suklje.name>

SPDX-License-Identifier: BSD-3-Clause
```

For reference, following the [REUSE.software][reuse] project's guide lets you verify that every file has been marked appropriately.

<!--TODO: enable once this style gets implemented in https://github.com/fsfe/reuse-tool/issues/329

!!! tip "Using the REUSE helper tool"

    If you will be doing this for many files, it makes sense to use tooling. Luckily the [REUSE helper tool][reuse_tool] can help with that as well.
    
    To implement the example above, I would call the following:
    
    ```.fish
    reuse addheader --copyright-style spdx-symbol --copyright "Matija Šuklje <matija@suklje.name>" --year (date +%Y)
    ```
    
    And while you are at it, check the [other features of the REUSE helper tool][reuse_tool], to manage also licensing info.
    -->


## What is Copyright?

**Copyright** is (following the [Berne Convention][berne]) **automatically generated** when an author creates a work. Every work is protected by copyright, and the copyright holder is granted exclusive rights over the work. So if you want other users to be able to use your work (source code, text, images, other media, etc.), you must grant them a license. The dictionary definition of a license is "permission granted by a competent authority to exercise a certain right," and exercising that right without such permission constitutes an unlawful act such as copyright infringement.

Likewise, if you want to copy, modify, or otherwise work with someone else's source code, you **must be granted the necessary permission**. In other words, you must obtain a license. And if that license imposes certain obligations as a condition for granting permission to exercise the right, you must also comply with those obligations in order to exercise the right.

In any case, you must comply with the basic requirements of copyright law, and at minimum this requires the following two things.

-   **Attribution**: Identify the copyright holder and/or author. (Especially in jurisdictions that recognize moral rights)
    
-   **License**: Since a license is the only way to grant someone other than the copyright holder permission to use the code, it's good practice to state the license and provide the full license text. This applies both to the Outbound license you grant to others and the Inbound license you receive from others (when using third-party works such as copied code or libraries).

> **Inbound vs. Outbound Licenses**
> 
> The license you grant to your users (downstream) is called the Outbound license, because it governs the rights of code flowing out (out) from you. Conversely, from the perspective of users of that same code, it is considered the Inbound license, because it governs the rights of code flowing in (in) to them.
> Simply put, a license that describes incoming rights is called an Inbound license, and a license that describes outgoing rights is called an Outbound license.
> The good news is that attribution is a right of the author, not an obligation. Also, users are only obligated to preserve attribution if the author has exercised their right of attribution. In other words, if the author did not provide attribution, users don't need to go out of their way to add it themselves.


## Why Should You Add a Copyright Statement?

Before the United States joined the Berne Convention in 1989, U.S. copyright law required an explicit copyright notice in order for a work to be protected. However, under the Berne Convention, copyright is generated automatically even without a copyright statement. Even so, copyright statements are still useful.

> While a copyright statement is not legally required, in practice it is extremely useful as evidence of who holds the copyright in a given work. It is also of great help for compliance purposes and for tracking code.


A copyright statement is practically necessary for the following reasons.

1.  Most licenses require a copyright statement.
2.  Even where a license does not require it, the copyright law of most jurisdictions does.
3.  (Even without such a requirement) a user may want to contact the original author for legal or technical reasons.

Therefore, it makes sense to include the author's name and contact information in a work.

## The Correct Way to Write a Copyright Statement and License Notice

### Copyright Statement

A good copyright statement should consist of the following information.

-   ​[the © symbol](https://haksung.gitbook.io/oss/research/license/copyright-statements#c)​
    
-   Year: the year the source code file was first written. Once written, [do not modify it further](https://haksung.gitbook.io/oss/research/license/copyright-statements#undefined-6).
    
-   Copyright holder name: usually the author, but it may be the author's employer. It could also be a different legal entity or individual under a CLA.
    
-   [a valid contact](https://haksung.gitbook.io/oss/research/license/copyright-statements#undefined-8): information for contacting the copyright holder
    

For example, if you wrote a source code file today, you would add a copyright statement like the following in the header at the top of the file.

```
© 2020 Matija Šuklje <matija@suklje.name>
```

### License Notice

It's also very important to state the license under which the code is released. Using an [SPDX ID](https://spdx.org/ids) lets you clearly identify the license of the code. If the license notice isn't clear, it can cause confusion for the users who see it.

### REUSE.software

The [REUSE.software](https://reuse.software/) project provides a best practice for writing copyright statements and license notices using SPDX tags.

-   Copyright statement tag: SPDX-FileCopyrightText
    
-   License notice tag: SPDX-License-Identifier
    

The example below is a copyright statement and license notice that takes all of the above into account and complies with both the SPDX and REUSE.software requirements.

```yaml
SPDX-FileCopyrightText: © 2020 Matija Šuklje <matija@suklje.name>

SPDX-License-Identifier: BSD-3-Clause
```


Now check that every source code file you have written includes this comment!

## FAQ

### Why should the year be included?

Some people argue that omitting the year and keeping things simple would actually make copyright statements easier to maintain. In fact, this is also the policy of Microsoft and GitHub.

I agree that omitting the year greatly simplifies the task, but keeping it helps clarify an otherwise ambiguous timeline in the codebase. It can also be useful for determining when an invention was first disclosed to the public, which can be particularly useful for patent defense.

Taking these considerations into account, Liferay's new policy is to record the year the file was created and not change the year afterward.

### Why shouldn't you keep changing the year?

You've probably seen copyright statements like this:

```
Copyright (C) 1992, 1995, 2000, 2001, 2003 CompanyX Inc.
```

This practice of continually adding years is widespread, based on the idea that it extends the period of copyright protection. Unfortunately, though, this practice is useless and can even be harmful.

Moreover, adding a year every time a new change or contribution is received is legally questionable when you think it through. The issue is that not every contribution is original or substantial enough to give rise to a copyright claim. So, to avoid this problem, you would first need to determine whether each contribution is original enough to be protected by copyright under the law, and only then add a year to the copyright statement accordingly.

On the other hand, copyright lasts for at least 50 years (usually 70 years) after the death of the author (or, if the copyright holder is a legal entity, after publication). So the risk of losing the ability to claim copyright due to the expiration of the protection period, simply because you didn't keep adding years to the copyright statement, is very low.

Furthermore, a single source code file is generally just one of many files that make up a piece of software. As the software grows, new files will be added, and when a new creation year is added to each new file, the copyright statement for the software as a whole, as a work, already ends up including the latest year.

> **Don't pollute your Git/VCS history**
> 
> If you add a new year statement to every file every year, this unnecessarily lengthens the Git/VCS history, consumes repository space, and can get in the way when you're looking for genuinely important information.

### What about expressing the year as a range?

Expressing the year as a range (e.g., 1999-2020) is subject to all the same considerations mentioned in the question above, because it also needs to be updated every year.

In some cases, a range is specified in a form like '{$year}-present'. This too is largely subject to the points mentioned above, and it can add further confusion. What 'present' means is abstract. What does 'present' refer to?

-   The time the file was last modified?
    
-   The time the package was released?
    
-   The time it was first downloaded?
    
-   The time it was last run?
    
-   Or right now, this very moment?
    

As you can see, 'present' isn't a helpful marker at all.

### Isn't Git/Mercurial better for tracking copyright information?

Not always. Git (and other VCSs) is excellent at managing metadata, but you should be cautious about relying on it entirely.

First, Git has an 'Author' field separate from the 'Committer' field. Not only does each contributor put different kinds of values into the 'Author' field, but even if you assume the person entered in the 'Author' field is actually the author, that author may not be the copyright holder.

More importantly, when a file is moved out of a repository, its metadata disappears. If you only distribute compressed source code, or copy each file into a new codebase by forking or rebasing a repository, the tracking data up to that point is no longer available.

These issues are resolved by including copyright and license information directly in every file. The [REUSE.software](https://reuse.software/) best practice handles this very well.

### Why use the © symbol?

Someone might argue that the English word "Copyright" is used more often and that many people are already familiar with it, but if you actually look at copyright law, you'll find that using "©" (the Copyright Sign) is not the only way to make a copyright statement.

> As one example from the EU, Article 175(1) of Slovenia's ZASP states that an exclusive copyright holder may mark their work with "(c)" or "©".
> Meanwhile, in the United States, 17 U.S. Code § 401(b)(1) specifies the way to mark a work as follows:
> "the symbol © (the letter C in a circle), or the word “Copyright”, or the abbreviation “Copr.”"


Also, using © is reasonable because it is the "common global denominator."

Whether or not people like the © symbol may be a matter of taste, but from a practical standpoint it isn't actually all that important. As explained above, since copyright is generated automatically, the symbol you use doesn't change the legal risk.

### Why should you leave a contact address? What if there are two or more authors?

Contact information isn't required by copyright law, but it's very useful for practical reasons.

A user may want to contact the code's author or copyright holder for legal or technical questions. They may want to ask how the code works or request a modification. They might discover a license issue and want to help resolve it, or need to request a separate license. Contact information is a great help in all of these cases.

-   Since email is still a commonly used contact method today, providing the copyright holder's email address is the best option.
    
-   In cases where copyright is highly distributed or held by a legal entity, it may make more sense to provide the URL of the project's or the entity's homepage.
    
-   If a project lists copyright holders in a file such as AUTHORS or CONTRIBUTORS, providing a link to that file is also a good option.
    

### What is Public Domain?

Public Domain generally refers to a work whose copyright term has expired, but it's a tricky concept that requires care.

In some jurisdictions (e.g., the United States, the United Kingdom), a copyright holder can waive their copyright and donate the work to the public domain, but in most jurisdictions (e.g., most EU member states) this isn't possible. This means that, depending on the jurisdiction, even if an author states that they are dedicating their work to the public domain, that statement may fail to meet the legal requirements to actually be effective, and the copyright in the work may still remain solely with the copyright holder.

For this reason, open source compliance professionals who take copyright and licensing seriously are very wary of a "this is public domain" label.

Copyright holders can mitigate this problem in the following two ways.

-   If you want to waive your copyright in your own work and dedicate it, use a very permissive license such as [CC0-1.0](https://spdx.org/licenses/CC0-1.0) instead of the phrase "public domain."
    
-   Leave your name and contact information in the "SPDX-FileCopyrightText:" field. This lets a user who is curious about the copyright holder's intent, or who runs into any ambiguity, reach out to resolve the issue.
    

### How should copyright be handled in minified JavaScript?

Modern minifiers offer an option to preserve copyright and license information even while removing comments. Use this option when minifying code to keep the copyright and license information intact.

> Even if source code is converted into another language, or compiled, or transformed into another form, the copyright holder retains exclusive rights over all of it. So even when using minified code, you still need a valid license.

### What's the problem with an "All rights reserved" statement?

You've probably seen the phrase "All rights reserved" in copyright statements before. Copyright law doesn't require this expression. I suspect it's simply copied from something people saw used on a music CD or in a book. But in open source, this expression causes confusion.

"All rights reserved" clearly contradicts an open source license. An open source license grants everyone the right to use, study, share, and improve the code. "All rights reserved," on the other hand, states that all of these rights are granted solely to the copyright holder.

"All rights reserved" only brings problems like this, without offering any benefit, so it should not be used in open source.
