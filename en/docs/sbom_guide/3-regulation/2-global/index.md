# India, Korea, and Other Jurisdictions

> Summarizes SBOM recommendation guidelines from India's CERT-In and other jurisdictions, including Korea.

---

LLMS index: [llms.txt](/llms.txt)

---

Jurisdictions outside the United States and the European Union are generally at the recommendation
stage. There is no legal enforcement or sanction, but these function as best practices that
influence procurement and contracting practices.

## India: CERT-In Technical Guidelines

The Indian Computer Emergency Response Team (CERT-In) published the *Technical Guidelines on
Software Bill of Materials (SBOM)*. This is a voluntary guideline aimed at government agencies,
the public sector, essential services, and software producing and service companies, covering the
value of SBOMs, best practices, minimum elements, and vulnerability tracking procedures. It has no
legal force, but it influences government procurement and contracting practices.

In July 2025, CERT-In expanded this guideline to also cover Quantum BOM (QBOM), Cryptography BOM
(CBOM), AI BOM (AIBOM), and Hardware BOM (HBOM). This is an example of how the bill of materials
concept is spreading beyond software into cryptography, AI, and hardware. The expansion into AI
BOM is covered further in [5. Tools and Automation](../../5-tools/) and in the separate
[AI SBOM Compliance Guide](../../../ai-sbom_guide/).

The first edition of this guide began as a Korean translation of this CERT-In document. The
current edition updates that skeleton with current primary sources from the United States and the
European Union, and broadens it to a general practitioner's perspective.

## Korea: Software Supply Chain Security Guidelines

In Korea, the Ministry of Science and ICT, the National Intelligence Service, and the Korea
Internet & Security Agency (KISA), among others, published the Software Supply Chain Security
Guidelines 1.0 in May 2024. It recommends SBOM generation and vulnerability inspection procedures,
and the use of the National Institute of Standards and Technology (NIST) Secure Software
Development Framework (SSDF).

However, this is only an administrative guideline, and Korea's current legal system does not yet
have legislation that imposes a mandatory reporting obligation at the product level, as the EU
Cyber Resilience Act does. Even so, Korean companies exporting software to the EU and the United
States must directly meet the requirements of those markets, so building SBOM capability is a
practical necessity regardless of domestic regulation.

## Practical Implications

The legal standing differs by jurisdiction, but the skeleton of the data required converges. A
well-built SBOM system, built once, can satisfy the requirements of multiple jurisdictions at the
same time. If the system is designed around the strictest requirement among your export markets
(currently the EU CRA), the recommendations of other jurisdictions are largely subsumed within it.

## Sources

Indian Computer Emergency Response Team (CERT-In). *Technical Guidelines on Software Bill of
Materials (SBOM)*, CIGU-2024-0002. <https://www.cert-in.org.in/>. Ministry of Science and ICT,
National Intelligence Service, Korea Internet & Security Agency (2024). *Software Supply Chain
Security Guidelines 1.0*. <https://www.kisa.or.kr/>. (all accessed: June 14, 2026)
