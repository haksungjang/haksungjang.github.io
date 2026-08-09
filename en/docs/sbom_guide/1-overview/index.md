# SBOM Overview

> An overview of what an SBOM is and why it is needed, covering software supply chain threats and the benefits an SBOM provides.

---

LLMS index: [llms.txt](/llms.txt)

---

## What Is an SBOM

A Software Bill of Materials (SBOM) is a machine-readable list of all the components and
libraries that make up a software product, along with the dependency relationships among them.
It carries over the manufacturing concept of a Bill of Materials into software. Just as a
finished vehicle has a specification sheet recording which parts came from which supplier, an
SBOM records which open source and commercial components, at which versions, went into an
application.

Most modern software is filled more with components brought in from outside than with code
written in-house. Those external components can carry vulnerabilities, come with license
obligations attached, and in turn depend on still other components. An SBOM makes this chain of
dependencies visible, providing a common data layer that security, license management, and asset
management can all reference.

## Why It Matters: The Collapse of Supply Chain Trust

Two supply chain incidents raised the SBOM onto the policy agenda. In the SolarWinds incident
that came to light in December 2020, attackers poisoned the legitimate update path of the Orion
software itself. A backdoor spread along with that update to the many organizations that trusted
and installed it. It was a structure in which a compromise at a single point upstream in the
supply chain spread across the entire downstream.

A year later, in December 2021, a remote code execution vulnerability in the Java logging
library Log4j (CVE-2021-44228, commonly known as Log4Shell) was disclosed. What this incident
exposed was not a breach itself but an absence of visibility. Log4j was buried deep as an
indirect dependency in countless products, so few organizations could give an immediate answer
to the question, "where in our products does this library exist?" If every piece of software had
already had a machine-readable component list in place, determining the scope of impact would
have taken a single query. This experience gave direct momentum to the SBOM agenda.

After that, the SBOM moved beyond recommendation into regulation. The United States opened a
path to requiring SBOMs for software delivered to the federal government through Executive Order
14028 in 2021, and the European Union made producing an SBOM a legal obligation through the
Cyber Resilience Act (CRA). The detailed regulatory landscape is covered in
[3. Regulatory Landscape](../3-regulation/).

## Benefits of an SBOM

The value of an SBOM is not limited to security alone. The same data — a component list — serves
multiple purposes at once.

- **Vulnerability management and incident response**: When a new vulnerability is disclosed,
  affected components can be looked up immediately to set response priorities.
- Supply chain risk management: The provenance and trustworthiness of external components are
  assessed and reflected in procurement and supplier management.
- License compliance: Tracking the license of each component prevents obligation violations and
  conflicts in advance.
- Regulatory compliance: Meets transparency requirements and provides the evidence needed for
  regulatory reporting and audits.
- Asset management and operational efficiency: Knowing exactly what is in use makes lifecycle
  management easier.

## Who Creates and Uses It

The value of an SBOM does not come from a single organization producing it alone; it is realized
when it flows along the supply chain. The third edition of CISA's *Framing Software Component
Transparency* organizes the actors around an SBOM into three perspectives: producers (Produce)
who make software, choosers (Choose) who select which software to use, and operators (Operate)
who run it. It is common for a single organization to hold all three roles at once, as with a
company that develops its own products while also bringing in external libraries and operating
infrastructure.

The core of this structure is the chain of supplier-consumer relationships. When an upstream
producer creates an SBOM and passes it downstream, the downstream chooser uses it to assess risk
before adoption, and the operator looks up the scope of impact immediately when a new
vulnerability is disclosed. What Log4Shell showed was precisely a break in this chain. Because
producers had not passed along a component list, operators could not know what libraries existed
in their own assets.

Interests diverge subtly across actors. Consumers want a deeper, more complete SBOM, while
producers, concerned about trade secrets and attack surface exposure, want to narrow the scope of
disclosure. Where regulation sets the floor of obligation, and how it adjusts the scope of
disclosure, are the mechanisms that resolve this tension. Sharing and disclosure scope are
covered in [7. Sharing and Governance](../7-governance/).

The next section looks at [levels and types](./1-types/) according to the depth of information
an SBOM carries.

## Sources

The factual basis for this section is compiled in this guide's background research materials.
Executive Order 14028 (86 FR 26633, May 12, 2021), CVE-2021-44228 (NVD), and the third edition
of CISA's *Framing Software Component Transparency* (September 3, 2024) were used as primary
sources. For the full set of sources, see [3. Regulatory Landscape](../3-regulation/) and the
bottom of each section.

---

Section pages:

- [SBOM Levels and Classification](/en/docs/sbom_guide/1-overview/1-types/): Summarizes SBOM levels based on the depth of information they contain, and classification based on when they are generated.
