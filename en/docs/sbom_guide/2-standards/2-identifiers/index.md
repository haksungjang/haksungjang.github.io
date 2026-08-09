# Identifiers and Licenses

> Covers the PURL, CPE, and SWID identifiers used to consistently point to components, and how to notate SPDX license identifiers.

---

LLMS index: [llms.txt](/llms.txt)

---

If the same component is named differently across SBOMs, automated matching breaks down, because
there is no way for a machine to know that "Apache Tomcat," "tomcat," and "Apache Software
Foundation Tomcat" are the same thing. This is why an identifier system that consistently points
to components, and a convention for notating licenses with standard codes, are both necessary.

## Three Identifiers: PURL, CPE, SWID

The three identifiers used together in practice serve different roles. They are not mutually
exclusive, so recording them together where possible is recommended.

| Identifier | Maintained by | Primary use |
|---|---|---|
| PURL (Package URL) | Community (purl-spec) | Precisely points to a component within a package manager ecosystem |
| CPE (Common Platform Enumeration) | NIST | Notates a product with a consistent name to look up its CVEs |
| SWID (Software Identification Tag) | ISO/IEC 19770-2 | Structured metadata for product, version, and producing entity |

**Table 1.** Identifiers used together in an SBOM *(source: purl-spec, NIST NVD,
ISO/IEC 19770-2. Retrieved 2026-06-14)*

A Package URL points to a component within a package manager ecosystem in the following format.

```
pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1
pkg:npm/lodash@4.17.21
pkg:pypi/requests@2.31.0
```

After `pkg:` come the ecosystem type (maven, npm, pypi, etc.), namespace, name, and version.
Because the same component can be pointed to with the same string everywhere, it links
automatically to vulnerability databases and license databases.

CPE was developed by MITRE in the mid-2000s and is now maintained by NIST. It notates products
under a fixed naming rule and is used to look up the vulnerabilities (CVEs) corresponding to a
product. SWID is a tag format standardized as ISO/IEC 19770-2 that structurally describes a
product's version and producing/distributing entity, and it is mainly used in asset management.
The CISA 2025 minimum elements draft updating "Other Unique Identifiers" to "Software
Identifiers" also reflects the maturing of this identifier ecosystem.

## License Notation: SPDX License Identifiers

License management is one of the earliest use cases for an SBOM. Recording exactly which license
each component is distributed under is what prevents obligation violations and conflicts in
advance. Free-text descriptions cannot be matched automatically, so standard codes are used.

[SPDX license identifiers](https://spdx.org/licenses/) assign each license a unique code such as
`Apache-2.0`, `MIT`, or `GPL-3.0-only`. When multiple licenses apply together, they are combined
with a license expression.

```
Apache-2.0 OR MIT
GPL-2.0-only WITH Classpath-exception-2.0
(MIT AND BSD-3-Clause)
```

`OR` indicates a choice among multiple licenses, `AND` indicates multiple licenses applying
simultaneously, and `WITH` indicates combination with an exception clause.

The principles to follow in practice are as follows.

- The license of every individual component, not just the license of the product as a whole,
  must be visible.
- When encountering a license not on the standard list, assign it an identifier with a prefix
  indicating its source (for example, a `LicenseRef-` prefix) to track it.
- If the license text has been trivially modified but its meaning has not changed materially,
  use the same identifier as the original.
- Analyze license compatibility to identify in advance the conflicts that can arise when
  combining components under different licenses.

Even when a license field is auto-extracted by a tool, its accuracy is a separate matter.
Precisely identifying non-standard licenses, handling dual licensing, and confirming compliance
with licenses that carry field-of-use restrictions remain the responsibility of people and
policy. The boundary of automation is covered in [5. Tools and Automation](../../5-tools/).

## Sources

Package URL specification <https://github.com/package-url/purl-spec>. NIST.
*Common Platform Enumeration (CPE)* <https://nvd.nist.gov/products/cpe>. ISO/IEC 19770-2:2015.
SPDX License List <https://spdx.org/licenses/>. SPDX License Expressions
<https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/>. (All retrieved: 2026-06-14)
