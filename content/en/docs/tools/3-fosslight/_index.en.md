---
title: "FOSSLight"
weight: 3
type: docs
categories: ["guide"]
tags: ["fosslight"]
---

FOSSLight is an open source project led by LG Electronics that uses various scanners to analyze source code, binaries, and dependencies, and generates a Software Bill of Materials (SBOM). In particular, FOSSLight Hub supports the compliance process by providing open source management, license management, and vulnerability management functions.

### 1 Introduction to FOSSLight

- **Key Features**:
    - Integration of various scanners: integrates and uses various open source scanners such as ScanCode Toolkit, SPDX Tools, CycloneDX, and Fossology
    - Support for various analysis targets: supports various analysis targets such as source code, binaries, container images, and Linux packages
    - SBOM generation and management: generates and manages SBOMs in various formats (SPDX, CycloneDX, Excel, Text)
    - License information detection and management: accurately detects and manages open source license information
    - Vulnerability information integration: integrates with external vulnerability databases such as NVD and CVE to provide vulnerability information
    - FOSSLight Hub: provides open source management, license management, and vulnerability management functions through a web-based UI
- **Advantages**:
    - High extensibility: various scanners can be integrated and used as plugins
    - Web-based UI: provides a user-friendly interface through FOSSLight Hub
    - Support for various report formats: reports can be generated in various formats such as SPDX, CycloneDX, Excel, and Text
    - Open source license
- **Disadvantages**:
    - Complex initial setup: initial setup can be somewhat complex because various scanners need to be integrated
    - FOSSLight Hub installation required: FOSSLight Hub must be installed separately to use the web-based UI

### 2 Installing FOSSLight

FOSSLight consists of FOSSLight Scanner and FOSSLight Hub. FOSSLight Scanner runs various scanners to generate analysis results, while FOSSLight Hub provides a web-based UI that integrates, manages, and visualizes the scanner results.

**This section explains how to install FOSSLight Scanner and FOSSLight Hub together using Docker Compose.**

1. **Install Docker and Docker Compose**:
    - Before installing FOSSLight, confirm that Docker and Docker Compose are installed on the system.
    - Docker installation instructions vary by operating system, so refer to the official Docker documentation (https://docs.docker.com/get-docker/).
    - Docker Compose is a tool for running and managing multiple containers simultaneously using Docker. For Docker Compose installation instructions, refer to the official Docker documentation (https://docs.docker.com/compose/install/).
2. **Clone the FOSSLight Repository**:
    - Run the following command to clone the FOSSLight GitHub repository.
    
    ```bash
    git clone <https://github.com/fosslight/fosslight_hub.git>
    cd fosslight_hub
    
    ```
    
3. **Configure the Docker Compose File**:
    - The `fosslight_hub` directory contains a `docker-compose.yml` file. You can open this file in a text editor and change the FOSSLight Hub configuration.
    
    ```yaml
    version: "3.7"
    services:
      fosslight_db:
        image: mariadb:10.6.4
        container_name: fosslight_db
        volumes:
          - fosslight_db:/var/lib/mysql
        restart: always
        environment:
          - MYSQL_ROOT_PASSWORD=fosslight
          - MYSQL_DATABASE=fosslight_db
          - MYSQL_USER=fosslight
          - MYSQL_PASSWORD=fosslight
    
      fosslight_web:
        image: fosslight/fosslight_hub:latest
        container_name: fosslight_web
        ports:
          - "8080:8080"
        restart: always
        environment:
          - FOSSLightDB_HOST=fosslight_db
          - FOSSLightDB_PORT=3306
          - FOSSLightDB_USER=fosslight
          - FOSSLightDB_PASSWORD=fosslight
          - FOSSLightDB_NAME=fosslight_db
        depends_on:
          - fosslight_db
    
      fosslight_scanner:
        image: fosslight/fosslight_scanner:latest
        container_name: fosslight_scanner
        restart: always
        volumes:
          - ./upload:/home/fosslight_scanner/upload
          - ./result:/home/fosslight_scanner/result
    volumes:
      fosslight_db:
    
    ```
    
    - You can change the port number, database settings, and so on as needed.
4. **Run FOSSLight**:
    - Run the following command to start FOSSLight.
    
    ```bash
    docker-compose up -d
    
    ```
    
    - This command runs FOSSLight Hub, FOSSLight Scanner, and the MariaDB database as Docker containers.
5. **Verify the FOSSLight Installation**:
    - In a web browser, access `http://localhost:8080` to confirm that you can reach FOSSLight Hub.
    - If the FOSSLight Hub web UI is displayed, the installation completed successfully.
    
    **Figure 2.1: FOSSLight Hub Web UI**
    
    (Insert screenshot of the FOSSLight Hub web UI)
    

### 3 FOSSLight Usage Guide

FOSSLight can be used through a web UI (FOSSLight Hub) and a CLI (FOSSLight Scanner).

**3.1 Using FOSSLight Hub**

FOSSLight Hub provides functionality, through a web UI, to manage open source projects, check scan results, and generate various reports.

1. **Register a Project**:
    - Access FOSSLight Hub and register a new project.
    - Enter information such as the project name, description, and owner.
    
    **Figure 2.2: FOSSLight Hub Project Registration Screen**
    
    (Insert screenshot of the FOSSLight Hub project registration screen)
    
2. **Upload Scan Results**:
    - Upload the scan results generated using FOSSLight Scanner to FOSSLight Hub.
    - The scan result file must be in SPDX, CycloneDX, or FOSSLight JSON format.
    
    **Figure 2.3: FOSSLight Hub Scan Result Upload Screen**
    
    (Insert screenshot of the FOSSLight Hub scan result upload screen)
    
3. **Check Scan Results**:
    - Check the uploaded scan results.
    - FOSSLight Hub visually presents SBOM information, license information, and vulnerability information.
    
    **Figure 2.4: FOSSLight Hub Scan Result Review Screen**
    
    (Insert screenshot of the FOSSLight Hub scan result review screen)
    
4. **Generate Reports**:
    - Generate various reports based on the scan results.
    - You can choose the report format: SPDX, CycloneDX, Excel, or Text.
    
    **Figure 2.5: FOSSLight Hub Report Generation Screen**
    
    (Insert screenshot of the FOSSLight Hub report generation screen)
    

**3.2 Using FOSSLight Scanner**

FOSSLight Scanner provides functionality, through the CLI, to scan source code, binaries, and container images and generate an SBOM.

1. **Run a Scan**:
    - Run the following command to execute a scan.
    
    ```bash
    docker run --rm -v $(pwd)/upload:/home/fosslight_scanner/upload -v $(pwd)/result:/home/fosslight_scanner/result fosslight/fosslight_scanner -p /home/fosslight_scanner/upload/<scan target> -o /home/fosslight_scanner/result/<result file name> -f <result format>
    
    ```
    
    - Each option is explained as follows.
        - `-rm`: automatically removes the container after it runs.
        - `v $(pwd)/upload:/home/fosslight_scanner/upload`: shares the `upload` directory in the current directory with the `/home/fosslight_scanner/upload` directory inside the container. You need to copy the file or directory to be scanned into this directory.
        - `v $(pwd)/result:/home/fosslight_scanner/result`: shares the `result` directory in the current directory with the `/home/fosslight_scanner/result` directory inside the container. The scan result file is saved to this directory.
        - `p /home/fosslight_scanner/upload/<scan target>`: specifies the path to the file or directory to be scanned.
        - `o /home/fosslight_scanner/result/<result file name>`: specifies the name of the scan result file.
        - `f <result format>`: specifies the scan result format (spdx, cyclonedx, fosslight_json).
    - Example:
    
    ```bash
    docker run --rm -v $(pwd)/upload:/home/fosslight_scanner/upload -v $(pwd)/result:/home/fosslight_scanner/result fosslight/fosslight_scanner -p /home/fosslight_scanner/upload/my_project -o /home/fosslight_scanner/result/my_project_sbom.json -f fosslight_json
    
    ```
    
2. **Check the Scan Results**:
    - Once the scan completes, the scan result file is generated in the `result` directory.
    - You can check the scan result file using a text editor or FOSSLight Hub.

### 4 Precautions When Using FOSSLight

- Because FOSSLight integrates and uses various scanners, you need to understand the characteristics and usage of each scanner.
- Because FOSSLight Hub requires a web server and a database, you need to install it with system resource requirements in mind.
- FOSSLight Scanner requires permission to access the file or directory being scanned.

### 5 Troubleshooting

- **Docker execution error**: confirm that Docker is installed correctly, and check for permission issues.
    - Try running with administrator privileges using the `sudo docker run ...` command.
- **Scan error**: confirm that the path to the file or directory being scanned is correct, and check that you have permission to access that file or directory.
- **FOSSLight Hub access error**: confirm that the Docker container is running properly, and check that the port forwarding is configured correctly.

### 6 Additional Information

- FOSSLight official website: https://fosslight.org/
- FOSSLight GitHub repository: https://github.com/fosslight/fosslight_hub
- SPDX official website: https://spdx.dev/
- CycloneDX official website: https://cyclonedx.org/
