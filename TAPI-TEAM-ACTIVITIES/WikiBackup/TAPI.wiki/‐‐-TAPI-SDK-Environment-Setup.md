# Prerequisites
Although T-API SDK artifacts and related software tools can be configured to run on windows platform, it is recommended to use an Linux platform.

# Hardware Requirements
Hardware requirements are difficult to define, since they can depend by many factors. We would recommend the following for using TAPI
* 2 core CPU
* 4 GB RAM
* 20 GB hard disk space
* 1 NIC
 
# Install Virtual Machine (if applicable)
The _Oracle VirtualBox_ (latest version) software and _Ubuntu_ OS (16.04.3 LTS) can be downloaded for free from the following sites
* https://www.virtualbox.org/wiki/Downloads
* https://www.ubuntu.com/download/desktop

* Update the Ubuntu OS

`sudo apt-get update`

`sudo apt-get upgrade`

# Install Oracle Java 8
`sudo apt-get install software-properties-common -y && \`

`sudo add-apt-repository ppa:webupd8team/java -y && \`

`sudo apt-get update && \`

`echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | sudo debconf-set-selections && \`

`cd /var/lib/dpkg/info && \`

`sudo sed -i 's|JAVA_VERSION=8u151|JAVA_VERSION=8u162|' oracle-java8-installer.* && \`

`sudo sed -i 's|PARTNER_URL=http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/|PARTNER_URL=http://download.oracle.com/otn-pub/java/jdk/8u162-b12/0da788060d494f5095bf8624735fa2f1/|' oracle-java8-installer.* && \`

`sudo sed -i 's|SHA256SUM_TGZ="c78200ce409367b296ec39be4427f020e2c585470c4eed01021feada576f027f"|SHA256SUM_TGZ="68ec82d47fd9c2b8eb84225b6db398a72008285fafc98631b1ff8d2229680257"|' oracle-java8-installer.* && \`

`sudo sed -i 's|J_DIR=jdk1.8.0_151|J_DIR=jdk1.8.0_162|' oracle-java8-installer.* && \`

`sudo apt-get install oracle-java8-installer oracle-java8-set-default –y && \`

`sudo echo “JAVA_HOME=’/usr/lib/jvm/java-8-oracle’” >> /etc/environment`

# Install Eclipse Modeling Tools package
The TAPI team is in the process of migrating to the latest eclipse version (oyygen), but the process is still not complete. Meanwhile it is recommended that the Eclipse Mars.2 version be used for TAPI since the Papyrus UML model files are rendered differently across different Eclipse versions

* Download and install Eclipse Mars.2 Modeling Tools package from the following link

  http://www.eclipse.org/downloads/packages/eclipse-modeling-tools/mars2

* Extract the downloaded archive to your home directory - you will find all the flies extracted to _eclipse_ folder
* Make changes to the _eclipse.ini_ in the eclipse folder so that it appears as follows

`-startup`

`plugins/org.eclipse.equinox.launcher_1.3.100.v20150511-1540.jar`

`--launcher.library`

`plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.300.v20150602-1417`

`-product`

`org.eclipse.epp.package.modeling.product`

`--launcher.defaultAction`

`openFile`

`--launcher.XXMaxPermSize`

`256M`

`-showsplash`

`org.eclipse.platform`

`--launcher.XXMaxPermSize`

`256m`

`--launcher.defaultAction`

`openFile`

`--launcher.GTK_version`

`2`

`--launcher.appendVmargs`

`-vmargs`

`-Dosgi.requiredJavaVersion=1.8`

`-Xms256m`

### _The following training video by Nigel Davis (Ciena) provides a good introduction to using the Eclipse-Papyrus modeling environment._

https://wiki.onap.org/display/DW/Modeling+tools
