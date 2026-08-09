---
title: "OSV-SCALIBR"
weight: 4
type: docs
categories: ["guide"]
tags: ["OSV-SCALIBR"]
---

OSV-SCALIBR (Software Composition Analysis LIBRary) is an open source software composition analysis library developed by Google. It supports various programming languages and aims to provide fast and accurate analysis results. It offers core functionality for generating a Software Bill of Materials (SBOM), but because it is provided as a library rather than as a standalone executable, users need to write their own code to integrate it.

### 1 Introduction to OSV-SCALIBR

- **Key Features**:
    - Support for various programming languages (Python, Go, Java, etc.)
    - Analysis of package manifest files (requirements.txt, pom.xml, go.mod, etc.)
    - Dependency information extraction
    - Vulnerability information integration (using the OSV database)
    - Fast analysis speed
- **Advantages**:
    - Support for various programming languages
    - Fast analysis speed
    - Provides the latest vulnerability information through OSV database integration
    - Flexible integration possibilities
    - Open source license
- **Disadvantages**:
    - Provided as a library rather than as a standalone executable
    - Users need to write their own code to integrate it
    - SBOM generation functionality must be implemented directly
    - Lack of documentation and community support

### 2 Installing OSV-SCALIBR

Because OSV-SCALIBR is provided as a library, you need to install it through the package manager appropriate for the programming language you intend to use. This guide explains how to install it in a Python environment.

1. **Confirm Python and pip Are Installed**:
    - Before installing OSV-SCALIBR, confirm that Python and pip are installed on the system.
    - Run the following command in the command prompt or terminal to check the Python version.
    
    ```bash
    python --version
    
    ```
    
    - Python 3.7 or higher must be installed.
    - To check the pip version, run the following command.
    
    ```bash
    pip --version
    
    ```
    
    - If Python and pip are not installed, download and install them from the official Python website (https://www.python.org/downloads/).
2. **Install OSV-SCALIBR**:
    - Run the following command to install the OSV-SCALIBR library.
    
    ```bash
    pip install osv-db
    
    ```
    
3. **Verify the Installation**:
    - Run the Python interpreter and enter the following code to confirm that OSV-SCALIBR was installed correctly.
    
    ```python
    import osv
    print(osv.__version__)
    
    ```
    
    - If the OSV-SCALIBR version information is printed, the installation completed successfully.

### 3 OSV-SCALIBR Usage Guide

Because OSV-SCALIBR is provided as a library, you need to write your own code to generate an SBOM. The following is a basic example of generating an SBOM using OSV-SCALIBR in a Python environment.

1. **Install Required Libraries**:
    - In addition to `osv-db`, install the libraries needed to generate an SBOM (e.g., `spdx-tools`).
    
    ```bash
    pip install spdx-tools
    
    ```
    
2. **Write the Code**:
    - The following is example code that extracts dependency information from a `requirements.txt` file, checks vulnerability information using OSV-SCALIBR, and then generates an SBOM in SPDX format.
    
    ```python
    import osv
    from spdx_tools.spdx.model import Document, Package
    from spdx_tools.spdx.builder import Builder
    from spdx_tools.spdx.validation.document_validator import validate_full
    import os
    
    def create_sbom_from_requirements(requirements_file):
        """
        Extracts dependency information from a requirements.txt file,
        checks vulnerability information using OSV-SCALIBR, and then
        generates an SBOM in SPDX format.
        """
    
        # 1. Read the requirements.txt file
        dependencies = []
        with open(requirements_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    package_name, package_version = line.split("==")
                    dependencies.append((package_name, package_version))
    
        # 2. Create the OSV API client
        client = osv.Client()
    
        # 3. Create the SPDX document
        document = Document(
            spdx_version="SPDX-2.2",
            data_license="CC0-1.0",
            spdx_id="SPDXRef-DOCUMENT",
            name="SBOM for " + requirements_file,
        )
        document.creators = ["Tool: OSV-SCALIBR Example Script", "Organization: Your Organization"]
    
        # 4. Add package information and check vulnerability information
        for package_name, package_version in dependencies:
            # Query vulnerability information using the OSV API
            vulnerabilities = client.get_vulnerabilities(package_name, package_version)
    
            # Create the package
            package = Package(
                name=package_name,
                spdx_id=f"SPDXRef-Package-{package_name}",
                version=package_version,
                # TODO: License information needs to be added.
            )
    
            # If vulnerability information exists, add a comment
            if vulnerabilities:
                comment = f"Vulnerabilities found: {len(vulnerabilities)}"
                package.comment = comment
    
            document.packages.append(package)
    
        # 5. Validate and output
        validation_messages = validate_full(document)
        if validation_messages:
            print("Validation errors:")
            for message in validation_messages:
                print(message)
        else:
            # Convert the SPDX document to a string (using spdx-tools)
            from spdx_tools.spdx.writer.write_anything import write_anything
            output_file = "sbom.spdx"
            write_anything(document, output_file, "tag", check_licenses=False)
            print(f"SPDX document generated successfully! File: {output_file}")
    
    # Example run
    # The requirements.txt file must be in the current directory.
    if os.path.exists("requirements.txt"):
        create_sbom_from_requirements("requirements.txt")
    else:
        print("Error: could not find the requirements.txt file.")
    
    ```
    
3. **Run the Code**:
    - Save the code above as a Python file (e.g., `sbom_generator.py`), and run the following command.
    
    ```bash
    python sbom_generator.py
    
    ```
    
4. **Check the Results**:
    - If the code runs successfully, a `sbom.spdx` file is generated. This file contains the SBOM written in SPDX format.

### 4 Precautions When Using OSV-SCALIBR

- Because OSV-SCALIBR is provided as a library, you need to write your own code to generate an SBOM.
- Because OSV-SCALIBR does not provide every function needed for SBOM generation, you need to implement the required functionality yourself or use it together with other libraries.
- OSV-SCALIBR's documentation can be somewhat lacking, and community support may not be very active.
- The code example generates an SBOM based on a `requirements.txt` file, but a real environment may need support for various package managers.
- The code example does not add license information directly. In an actual SBOM, you need to accurately determine and add the license information for each package.

### 5 Example of a Generated SBOM (Inferred)

An SBOM (in SPDX format) generated using OSV-SCALIBR would have a structure like the following. (The actual content depends on the contents of the `requirements.txt` file.)

```
SPDXVersion: SPDX-2.2
DataLicense: CC0-1.0
SPDXID: SPDXRef-DOCUMENT
Name: SBOM for requirements.txt
Creator: Tool: OSV-SCALIBR Example Script
Created: 2025-02-11T00:00:00Z

# Package Information
PackageName: requests
SPDXID: SPDXRef-Package-requests
PackageVersion: 2.28.1
# Comment: Vulnerability found: 1 (may vary depending on the OSV database)

PackageName: urllib3
SPDXID: SPDXRef-Package-urllib3
PackageVersion: 1.24.13

# Relationships
# (Dependency relationship information between each package)

```

**Note**: the example above merely shows the format of an SBOM that OSV-SCALIBR could generate; the actual SBOM content depends on the code and the dependency analysis results. Additional information such as license information and origin information needs to be added by modifying the code directly.

### 6 Additional Information

- OSV-SCALIBR GitHub repository: (no information)
- OSV (Open Source Vulnerabilities) database: https://osv.dev/
- SPDX official website: https://spdx.dev/

**Caution**: because OSV-SCALIBR is a library, this guide alone may not be enough to complete SBOM generation. It requires an understanding of Python programming and SBOM generation, along with additional code.
