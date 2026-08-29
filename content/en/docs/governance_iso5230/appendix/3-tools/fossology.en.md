---
title: "FOSSology"
weight: 1
type: docs
---
For open source compliance, a source code scanning tool can be used to detect the open source and license information contained within software.

![https://www.fossology.org/](../fossology1.png)

_<center>< https://www.fossology.org/ ></center>_

The Linux Foundation's FOSSology project is a tool that develops this kind of scanning tool and has released it as open source so that anyone can use it freely.

## Key Features

FOSSology is a web-based program that allows users to log in to the website and upload individual files or software packages. FOSSology detects license text and copyright information within the uploaded files. It is a good idea for developers to use FOSSology when they want to check the license and copyright information of the open source they intend to use. FOSSology scans all files within the open source package uploaded by the developer, automatically detects license-related text and copyright information in each file, and generates this as a report. For more details on FOSSology's key features, refer to the following page: [https://www.fossology.org/features/](https://www.fossology.org/features/)

## Installation

To use FOSSology within a company, a FOSSology server must be built in-house. To do this, FOSSology must be installed on a Linux-based server system. FOSSology can be installed using the following three methods.

1. Using Docker
2. Using Vagrant and VirtualBox
3. Installing via a source build

Here, the simplest method, using Docker, is explained.

FOSSology publishes a containerized Docker image through Docker Hub \(https://hub.docker.com/\). : [https://hub.docker.com/r/fossology/fossology](https://hub.docker.com/r/fossology/fossology)

The pre-built Docker image can be run using the following command.

```text
$ docker run -p 8081:80 fossology/fossology
```

The Docker image can be accessed using the following URL and account information. : http://\[IP\_OF\_DOCKER\_HOST\]:8081/repo

* Username : fossy
* Passwd : fossy

For more details on installation, refer to the following page. : [https://github.com/fossology/fossology/blob/master/README.md](https://github.com/fossology/fossology/blob/master/README.md)

## Test Server

If it is difficult to build a system to install FOSSology, the test server provided by the FOSSology Project can be used. The FOSSology project provides an environment for testing. \(The test server may be discontinued without notice.\)

Users can access the FOSSology test server with the following account to try out FOSSology's features.

{{< alert  >}}
Test server URL: [https://fossology.osuosl.org/](https://fossology.osuosl.org/)

* Username: fossy
* Password: fossy
{{< /alert  >}}

![FOSSology test server login screen introducing key features such as upload, license scanning, and copyright detection](../fossology2.png)

## Basic Workflow

The basic usage procedure for FOSSology is as follows.

* To check the license and copyright information of the open source you want to use, compress the open source's source code into a single file and upload it to FOSSology.
* To do this, select menu &gt; Upload &gt; From File.

![Uploading a compressed source archive via FOSSology's Upload > From File menu](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/Oywr9jqM09g1SfxfZ-2HERmYA_8)

* Select the file to upload and click the Upload button.
* Once the upload is complete, the analysis is automatically performed by the Job Agent.
* The status of the analysis in progress can be checked at menu &gt; Jobs &gt; My Recent Jobs.

![Checking analysis progress for an uploaded file in FOSSology's Jobs > My Recent Jobs menu](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/9IKts-8lH7YK_Dat124-hEw_q4I)

* Once the analysis is complete, the results can be checked at menu &gt; Browse.

![Viewing completed license analysis results in FOSSology's Browse menu](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/C62vBvaVNeBLAqrRrx-XKoeuMhg)

* Selecting an individual file allows you to check the license-related text detected by FOSSology.

![Viewing the license-related text FOSSology detected for an individual file](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/9idwgtBqNj7YAl7Wg0i98QJ5b4w)

* menu &gt; Browser &gt; select a file or directory &gt; Copyright/Email/Url/Author shows the Copyright/Email/Url/Author information detected by FOSSology.

![Viewing copyright, email, URL, and author information FOSSology detected, in the Copyright/Email/Url/Author menu](https://t1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/9399/image/NrjeCqal75rJ1bwGLPPmjhBEn4Q)

After checking whether the results analyzed in this way by FOSSology are valid, users can exclude incorrectly detected items from the analysis results. FOSSology describes this as the Clearing process, and for more details, refer to the following page: [https://www.fossology.org/get-started/basic-workflow/](https://www.fossology.org/get-started/basic-workflow/)

In this way, you can easily check what the license of the open source you want to use is and what the copyright information looks like.
