# SW360

LLMS index: [llms.txt](/llms.txt)

---

(Updated on August 29, 2023.)

A company that develops and distributes products containing open source needs to collect and track information such as the version and license of the open source used, for each product and release version. This allows the company to carry out proper open source compliance activities.

In particular, when a security vulnerability is reported for a specific open source version at NVD \(https://nvd.nist.gov/vuln\), a company that cannot trace which products use that version ends up unable to determine which products need the security patch applied, leaving its products exposed to the vulnerability.

This makes tracking open source information a necessity. Companies address this either by building their own system or by purchasing and using a commercial service. SW360 is open source software sponsored by the Eclipse Foundation, providing a web application and repository for collecting and tracking software Bill of Materials (BOM) information.

![https://www.eclipse.org/sw360/](./sw3601.png)

_<center>< https://www.eclipse.org/sw360/ ></center>_

## Key Features

SW360 provides a web-based UI, and its key functions are as follows.

* Tracking components used in a product
* Security vulnerability assessment
* License obligation management
* Generating legal documents such as notices

![https://www.eclipse.org/sw360/](https://lh3.googleusercontent.com/MPrOy70nOVSCRiorql9Momzi18lG66Liqttyutjwc9LAhVUwqmVf8xyeEkg085Pm1OYxwPRzyh68Th93ZlKA3fjG5_PnsBQijwUGkRa7o72h8Jco_7BcIwfoR7FGu8hsZA8n5ASq)

## Installation

SW360 is composed as follows.

* Frontend : Liferay-\(Tomcat-\)based portal application
* Backend : Tomcat-based thrift service
* Database : CouchDB

For details on the project structure and the software required for installation, see the Required software section of the README. : https://github.com/eclipse-sw360/sw360

SW360 offers the following installation methods. Users can choose one of them for installation.

1. Can be deployed via Docker. : https://github.com/eclipse-sw360/sw360/blob/main/README_DOCKER.md
2. Can install SW360's components individually. : [https://github.com/eclipse/sw360](https://github.com/eclipse/sw360)
3. Vagrant-based \([https://www.vagrantup.com/](https://www.vagrantup.com/)\) installation: Vagrant is a tool for managing virtualized instances, and sw360vagrant provides an environment for deploying SW360 all at once. : [https://github.com/sw360/sw360vagrant](https://github.com/sw360/sw360vagrant)
   - The Vagrant-based installation guide can be found [here](https://openchain-project.github.io/OpenChain-KWG/guide/nipa_openchain/appendix/3-tools/sw360/#%EC%84%A4%EC%B9%98). (Note: because the code has changed since the guide was written, it may not work correctly.)

This guide introduces the method of deploying with `Docker`. For details, refer to the README. : https://github.com/eclipse-sw360/sw360/blob/main/README_DOCKER.md


### 1. Download the Code

Download the code to build the Docker image. The tested code can be obtained here. : https://github.com/haksungjang/sw360/tree/docker_build

```sh
git clone -b docker_build https://github.com/haksungjang/sw360.git
```

### 2. Build

First, install [Docker](https://www.docker.com/). (Note that a [paid purchase](https://www.docker.com/pricing/) may be required for corporate developer use.)

Build by running `docker_build.sh` as shown below.

```sh
cd sw360
./docker_build.sh
```

Once the build completes successfully, you can check the created images as shown below.

```sh
docker image ls

REPOSITORY                       TAG              IMAGE ID       CREATED          SIZE
eclipse-sw360/sw360              18-development   ab0fd848bf80   8 minutes ago    2.95GB
eclipse-sw360/sw360              latest           ab0fd848bf80   8 minutes ago    2.95GB
ghcr.io/eclipse-sw360/sw360      18-development   ab0fd848bf80   8 minutes ago    2.95GB
ghcr.io/eclipse-sw360/sw360      latest           ab0fd848bf80   8 minutes ago    2.95GB
eclipse-sw360/binaries           18-development   aa7debf0a1fc   8 minutes ago    347MB
eclipse-sw360/binaries           latest           aa7debf0a1fc   8 minutes ago    347MB
ghcr.io/eclipse-sw360/binaries   18-development   aa7debf0a1fc   8 minutes ago    347MB
ghcr.io/eclipse-sw360/binaries   latest           aa7debf0a1fc   8 minutes ago    347MB
eclipse-sw360/base               18-development   e5147733fc88   37 minutes ago   1.52GB
eclipse-sw360/base               latest           e5147733fc88   37 minutes ago   1.52GB
ghcr.io/eclipse-sw360/base       18-development   e5147733fc88   37 minutes ago   1.52GB
ghcr.io/eclipse-sw360/base       latest           e5147733fc88   37 minutes ago   1.52GB
ghcr.io/eclipse-sw360/thrift     0.18.1           0012d7998058   4 weeks ago      152MB
ghcr.io/eclipse-sw360/thrift     latest           0012d7998058   4 weeks ago      152MB
eclipse-sw360/thrift             0.18.1           0012d7998058   4 weeks ago      152MB
eclipse-sw360/thrift             latest           0012d7998058   4 weeks ago      152MB
```

### 3. Run

Run the created images with the `docker-compose up` command.

```
docker-compose up
```

Once it runs successfully, you can see three containers running as shown below.

```
docker ps 

CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS                   PORTS                                              NAMES
4299fd39010c   eclipse-sw360/sw360   "/app/entry_point.sh"    3 minutes ago   Up 3 minutes             0.0.0.0:8080->8080/tcp, 0.0.0.0:11311->11311/tcp   sw360
13fd5696b140   postgres:14           "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes (healthy)   0.0.0.0:5438->5432/tcp                             sw360-postgresdb-1
7bb70f2daaf4   couchdb               "tini -- /docker-ent…"   3 minutes ago   Up 3 minutes (healthy)   4369/tcp, 9100/tcp, 0.0.0.0:5984->5984/tcp         sw360-couchdb-1
```

At this point, accessing `http://localhost:8080/` takes you to the following screen.

![](./liferay.png)


## Configuration

After installing SW360 successfully, you need to perform the initial configuration following the procedure below. For details, see: [SW360 Initial Setup Configuration](https://eclipse.dev/sw360/docs/deployment/legacy/deploy-liferay7.4/)

### 1. User and Login Configuration

Log in with the following account to perform the configuration.

* id : setup@sw360.org
* pw : sw360fossy

Once you log in, a Not Found message appears as shown below.

![](./liferay1.png)

Click the item icon (cube shape) in the upper right of the screen and select the `Control Panel` tab.

![](./liferay2.png)

Enable `SECURITY` > `Password Policies` > `Default Password Policy` > `PASSWORD CHANGES` > `Change Requried`.

![](./liferay3.png)

Then, back in the `Control Panel` tab, select `CONFIGURATION` > `Instance Settings`. This shows the `PLATFORM` menu.

![](./liferay4.png)

There, select `Users`. Then go into the `Default User Associations` menu, check `Apply to Existing Users`, and `Save`.

![](./liferay5.png)

Now, under `Instance Settings` > `PLATFORM`, select `User Authentication`. Go into `General` and uncheck all items. (You can check and enable any items needed for administrative purposes.) Then `Save`.

![](./liferay6.png)

Finally, you need to enable jQuery and Font Awesome. To do this, go into `CONFIGURATION` > `System Settings` in the `Control Panel` tab, where you can find `Third Party` under `PLATFORM`.

![](./liferay7.png)

Go into `Third Party` and enable `JQuery` and `Font Awesome` respectively.

![](./liferay8.png)

![](./liferay9.png)

Restart your browser for the changes to take effect.

### 2. Import LAR Files

To configure SW360, you need to import the `*.lar` files. To do this, you need to go into the menu, and the menu button is in the upper left of the screen.

![](./liferay10.png)

In the menu, go into `Publishing` > `Import`.

![](./liferay11.png)

Click the `+` button on the right to upload a LAR file. The LAR files are located under the `frontend/configuration` folder in the SW360 source files. (e.g., https://github.com/haksungjang/sw360/tree/docker_build/frontend/configuration)

First, upload the `Public_Pages_7_4_3_18_GA18.lar` file and click the `Continue` button.

![](./liferay12.png)

On the File Summary screen, you can see the details of the uploaded LAR file.

![](./liferay13.png)

Change `AUTHORSHIP OF THE CONTENT` at the bottom to `Use the Current User as Author` and click the `Import` button.

![](./liferay14.png)

You can then see that the import completed successfully.

![](./liferay15.png)

Similarly, import the `Private_Pages_7_4_3_18_GA18.lar` file. On the File Summary screen, change `PAGES` > `Private Pages` as shown below.

![](./liferay16.png)

Then select the `PERMISSIONS`, `UPDATE DATA`, and `AUTHORSHIP OF THE CONTENT` items as shown in the image below, and click the `Import` button to perform the import.

![](./liferay17.png)

After completing this, click the `Home` button at the top of the menu.

![](./liferay18.png)

This takes you to the `Welcome to SW360!` screen shown below.

![](./liferay19.png)

Click the `Start` button to go into the SW360 main screen. (All items are empty at this point.)

![](./liferay20.png)

### 3. User Account Configuration (for Testing)

In the SW360 menu, select `Admin` > `User`.

![](./liferay21.png)

In the `UPLOAD USERS` menu at the bottom of the screen, upload the user list for testing. (The user list for testing can be downloaded here. : [test_users_with_passwords_12345.csv](https://github.com/haksungjang/sw360/blob/main/frontend/configuration/test_users_with_passwords_12345.csv) )


![](./liferay22.png)

You can then see that a list of 9 users has been uploaded, as shown below.

![](./liferay23.png)

Try logging in again with the `user@@sw360.org` account, one of the users shown in the list. The password is `12345`.


## Basic Workflow

### 1. Registering Licenses

When you first install SW360, you need to first register the open source licenses you use frequently. A license includes the following information.

* Full Name
* Short Name
* License Type
* GPL-2.0 Compatibility \(e.g., yes, no\)
* License Text

Selecting Menu &gt; Licenses &gt; Add License takes you to the Create License screen shown below.

![](https://lh6.googleusercontent.com/8bn6z_39PK5WrjP7mzhHrTwfM5PU19QT3TiQnAatOYywVwcGLJGFMmMgMkzh4CKAPM0SOOy7VDoboaj9OKpD1QEZv6KWOeWxZfqGA_2geYrYOBm2kOVzrNOmGPVK-8hzJvBZ-klT)

Registering licenses one by one manually like this can be quite tedious, but fortunately SW360 provides a feature to import the SPDX License List all at once. Click Menu &gt; Admin &lt; Import SPDX Information.

![](https://lh5.googleusercontent.com/d8ZK-dD34z1yKZn-szPNrN7iT4zg1EQnKnAv4QcPslSR0-laETy37ArojuweqSsxpWuvGXtdF5FabiWk57So-bD_iiEx7eVIR6tWDsYO2SkaCdlKr6ELDN9y_NdkqWFbQgRF2lXN)

The SPDX License List is then automatically registered shortly after. At Menu &gt; Licenses, you can confirm that 338 licenses have been registered.

![](https://lh6.googleusercontent.com/Ucjuo09uJKhEhACZ90y98PszgSiCGtlDotH8mbTXJ2ePnF3TquzNX2yWzOCENTKNk1UjMJhyFgHxTCH6lxvZJg1l07M0hCc-v-14loAJ0efUU9V9hqS9mUabAT9QNysYL8E2tgIf)

### 2. Registering Components and Releases

In SW360, a Component is a single unit of software. Various forms of software can fall into this category, for example:

* Open source software
* Libraries
* Third-party software

A Component includes the following information.

* Component Name
* Main Licenses
* Categories \(e.g., Library, Cloud, Mobile, ...\)
* Component Type \(e.g., OSS, Internal, InnerSource, Service, Freeware\)
* Default Vendor
* Homepage URL

A Release is the unit that refers to a single Version within a Component. Accordingly, one Component can have multiple Releases. A Release is created and managed under a single Component.

A Release includes the following information.

* Component Name
* Version
* License
* Download URL
* CPE ID \(e.g., cpe:2.3:a:apache:maven:3.0.4\)

For example, if you need to register zlib-1.2.8, you first register zlib as a Component, then register zlib 1.2.8 as a Release. Selecting Menu &gt; Components &gt; Add Component takes you to the Create Component screen, where you can register information about zlib.

![](https://lh6.googleusercontent.com/0a3ecmmFzumTZTaoWCOZPKkQIZLJwbPoAaduCTfwQMH_N67DPaMpTkerA4LOynwkl_nLkNT-pRh-rKzj4XHtBjoTkVMW9g06Rywryk3wbAj-Y3ONDg16VcGepMEm7m7Y8M3iDWyH)

Once you create the Component, you can register information for the zlib-1.2.8 version at Components &gt; Releases &gt; Add Release.

![](https://lh4.googleusercontent.com/ynUEB5-rGVYDirFghLx2v3tUt-uh-WL3YTN0siaGZWBrWQKYnIiV3B04mvdv3nZUW7t_U2Gl8msV_es1X181uq95YAp1bnqa0e3QLshhd1zhqk6z8ubPeEfo74cKdwho95_NyI1J)

When versions 1.2.8 and 1.2.11 are each registered as Releases under the single zlib Component, the Release Overview screen shows 2 Releases existing, as below.

![](https://lh3.googleusercontent.com/GxgMJQbNjRBNxMTMBvqEXNFNElXGXoCnaksCMs46ydREIrqrj7dFxMK0YkvjviHYMCiHY07xlR-Xixpa_C5nMFLzih0dXZAtv-6yKg4RdADJxr5qmDwhAEopVOaVNqzVWc3gMpLq)

SW360 provides a feature for importing information for multiple Components at once. At Menu &gt; Admin &gt; Import / Export, you can enter the Component information you want to register into the CSV template and then import it.

![](https://lh5.googleusercontent.com/VInFwWAV-1lG1E7zFQPvn1GIlYPPY5ToGbSa49Brg7XuB-AwyCEHA9han0EUij1KX3c8aN2UZ1mKkN-5Y4BNv8LOV3O5YoypLQ7EF43QFPAU9L18XT57Ec5eoneswtGtt3rMSPoQ)

Note that, as of February 2020, this feature may not yet work reliably.

### 3. Creating a Project

A Project refers to a single product. Depending on the type of business, it may be a product, a service, or software. Under a Project, you register and manage the Components/Releases used in the product.

When creating a Project, you register the following information.

* Project Name
* Version
* Project type \(e.g., Product, Customer Project, Service, Internal Project, InnerSource\)

You can create a Project via Menu &gt; Projects &gt; Add Project.

![](https://lh6.googleusercontent.com/6gNtLci53U6zaU6Th5SHousuZ4VUijzuYjiJJlB0R6JwiHG4ggjb0RcnRYDkZCBhE2dMP2gGbT4qmB2FE5O8EW8hTfv1lgM4_XN0vzQUkttfTbX2cF0aNftHYuUy9EXczT2LzLO5)

Once you create the Project, register the Releases or sub-Projects it includes. Selecting the Project at Menu &gt; Projects lets you register Linked Projects and Linked Releases under "Linked Releases and Projects."

![](https://lh4.googleusercontent.com/ZjD7r7EzxfdQ4bhw4ODsChydb6Vgqj1m4Ad0cWlYtyYXO40MCbPpTHHcy-wJmbHeA_FxTa66Mpza6-9ohu0e93b7BaGb7Zc9soTA3mGCHGnyGURukRUnJS_duI7T8IL2aTgMFzjB)

The following is the screen after registering OpenSSL 1.0.1 and zlib 1.2.8 as Linked Releases in a Project named SuperCalc.

![](https://lh3.googleusercontent.com/tZCshPwxtukNLvfL-f-LfNOH-4ATof0bIGxpghVKXQ9QMBgoc_t0ROJMYafS9V4PuRaOOEW9zp25yk0gFA_kcaoRN83UKwUaFhaXxSWg7xPWvsYoJ_-pZkROkey1mYVTqGxKsCRu)

### 4. Security Vulnerability Management

SW360 can automatically check whether registered Releases have security vulnerabilities. To do this, SW360 provides a feature for scheduling periodic collection of CVE information. At Menu &gt; Admin &gt; Schedule, you can set a schedule to collect CVE SEARCH information every 24 hours.

![](https://lh5.googleusercontent.com/V2AJbexZqJJqwFYD1kFpjdZ7zVM9PCd-I_6MSBu3djO2Gi6gQxxQpKoqqsETxDaSkpDXOKFOp9h0Fps1xYHEphesVX9ECwBwnSX5cWdziXoohh-CMmqRh_wVkwUD8dZE9w1raJRk)

Once this schedule is set, SW360 collects CVE information from the CVE Search site \([https://cve.circl.lu/](https://cve.circl.lu/)\) at the scheduled time. The collected CVE information can be checked at Menu &gt; Vulnerabilities.

![](https://lh3.googleusercontent.com/dpIMyX7qCMdnibNihuL6RBSKg2fEckbOBPWJEtw08mY4quhv6Hh3BlgFIeydPOS6N8rF6ZSs4hpZgBGcXbcJI9saFDyfv4i-TCvxV5z-4LD9ZXpKah0jQU45j3iibxFpYoa7Hj9u)

Once the Vulnerabilities information has been collected, you can query whether a created Project has security vulnerabilities. In the SuperCalc Project created above, you can confirm that 85 security vulnerabilities were reported.

![](https://lh5.googleusercontent.com/lGeLbWHIBk6y2OSOXskcp4A2c5od0eTH6n7U5YG0p4cwTrrX02b6TpeRqJ7VXg5aUE7qDP2X2f8o4Rj1JsPHhZ-CUdLiy80O532Cgw-h_P9r-jHdL61QaXhFOPxIjTlX1cg9XPk5)

By registering and managing the software a company develops and distributes in SW360 this way, you can manage it in a form that minimizes risk not only for open source compliance but also for security vulnerabilities.

SW360 also offers most of its functionality via a REST API in addition to the Web Interface above, making integration with other tools such as FOSSology possible. : [https://github.com/eclipse/sw360/wiki/Dev-REST-API](https://github.com/eclipse/sw360/wiki/Dev-REST-API)

In other words, integrating this into DevOps by, for example, importing the analysis results of a source code scanning tool into SW360, and automating the registration of Projects and Releases, would greatly increase efficiency.
