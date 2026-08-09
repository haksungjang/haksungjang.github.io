# Adoption Roadmap

> Summarizes the activities organizations undertake to build an SBOM program in stages, from establishing the foundation to operational maturity.

---

LLMS index: [llms.txt](/llms.txt)

---

Introducing an SBOM program into an organization is not a one-time effort. A staged approach is
more realistic: establish the foundation (Foundational), settle generation and integration into
practice (Developing), and mature operations (Scaling). The stage breakdown below is the common
framework presented by both the US NTIA and India's CERT-In guidelines; the order of activities is
only illustrative and can be adjusted to fit an organization's security needs, timeline, and
resources.

![A maturity path that expands SBOM adoption through three stages — Foundational, Developing, and Scaling](./adoption-stages.png)

**Figure 1.** The three stages of SBOM adoption *(source: reconstructed from NTIA 2021 and CERT-In
technical guidelines; collected June 14, 2026)*

## Stage 1: Building the Foundation

The first SBOM an organization encounters is usually one received from a supplier during
procurement. The purpose of this stage is to establish how the organization handles SBOM in the
first place.

- **Identify critical assets and establish a plan**: Develop a plan that defines roles and
  responsibilities, timelines, and resource requirements, and obtain stakeholder buy-in for the new
  process.
- Decide on the format and minimum requirements: Before creating SBOMs, determine the format (SPDX
  or CycloneDX) and the minimum data requirements. This ensures a standard structure that can be
  processed consistently across the supply chain.
- Identify security requirements, storage, and tools: Define classification and handling
  procedures, and set up a secure repository for SBOMs.
- Obtain SBOMs through procurement: Specify the requirement for suppliers to provide SBOMs in
  purchase orders or contracts, and specify which elements are to be provided, when, and by what
  method.

## Stage 2: Generation and Integration

This stage involves establishing secure configuration management, consistently referencing
components with unique identifiers, and embedding generation itself into the development process.

- Assign unique identifiers: Pin each component with
  [an identifier such as PURL](../2-standards/2-identifiers/) so that traceability is not lost even
  if a supplier or component name changes, or a different version is released under the same name.
- Map supplier SBOMs to internal SBOMs: Create internal SBOMs based on the SBOMs suppliers provide,
  and record the author and timestamp to manage integrity and update history.
- **Integrate with the SSDLC and CI/CD**: Integrate SBOM generation into the Secure Software
  Development Life Cycle (SSDLC) and continuous integration/continuous deployment (CI/CD) pipeline.
  Generating SBOMs automatically at build time improves both accuracy and timeliness. See
  [5. Tools and Automation](../5-tools/) for tool selection.
- Secure configuration management: Apply access control, encryption, and regular audits to manage
  SBOMs securely.

## Stage 3: Operational Maturity and Scaling

The final stage involves fully weaving SBOM into vulnerability management and incident response,
and continuously updating the program.

- Strengthen vulnerability tracking: Establish a process for cross-referencing SBOM components
  against vulnerability databases to assess impact and mitigation. Detailed methods are covered in
  [6. Vulnerability Management](../6-vulnerability/).
- Integrate incident response: Establish a process for using SBOM to quickly determine, for a newly
  disclosed vulnerability, whether the organization is affected or has already been compromised.
- Maintain regular review and awareness: Periodically check that components and dependencies match
  the latest records, and keep the organization aware of new formats, data elements, and industry
  trends.

## Choosing a Starting Point

Follow the three stages in order, but there is no need to aim for perfection from the start. A
realistic first step is to pick one or two of the most important products, automatically generate
SBOMs in the build pipeline, and feed them into a vulnerability scanner. Once you confirm the
program works for one product, expanding it across the full portfolio reduces the cost of trial and
error.

## Sources

NTIA (2021). *The Minimum Elements For a Software Bill of Materials (SBOM)*. CERT-In. *Technical
Guidelines on Software Bill of Materials (SBOM)*. CISA SBOM Resource Hub
<https://www.cisa.gov/sbom>. (all accessed: June 14, 2026)
