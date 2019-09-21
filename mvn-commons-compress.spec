#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-compress
Version  : 1.10
Release  : 9
URL      : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.10/commons-compress-1.10.jar
Source0  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.10/commons-compress-1.10.jar
Source1  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.10/commons-compress-1.10.pom
Source2  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.11/commons-compress-1.11.jar
Source3  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.11/commons-compress-1.11.pom
Source4  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.14/commons-compress-1.14.jar
Source5  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.14/commons-compress-1.14.pom
Source6  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.15/commons-compress-1.15.jar
Source7  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.15/commons-compress-1.15.pom
Source8  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.16.1/commons-compress-1.16.1.jar
Source9  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.16.1/commons-compress-1.16.1.pom
Source10  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.18/commons-compress-1.18.jar
Source11  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.18/commons-compress-1.18.pom
Source12  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.4.1/commons-compress-1.4.1.jar
Source13  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.4.1/commons-compress-1.4.1.pom
Source14  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.5/commons-compress-1.5.jar
Source15  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.5/commons-compress-1.5.pom
Source16  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.6/commons-compress-1.6.jar
Source17  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.6/commons-compress-1.6.pom
Source18  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar
Source19  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.pom
Source20  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.9/commons-compress-1.9.jar
Source21  : https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.9/commons-compress-1.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-compress-data = %{version}-%{release}
Requires: mvn-commons-compress-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-compress package.
Group: Data

%description data
data components for the mvn-commons-compress package.


%package license
Summary: license components for the mvn-commons-compress package.
Group: Default

%description license
license components for the mvn-commons-compress package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-commons-compress
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-commons-compress/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.10
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.10/commons-compress-1.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.10/commons-compress-1.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.11
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.11/commons-compress-1.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.11
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.11/commons-compress-1.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.14
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.14/commons-compress-1.14.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.14
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.14/commons-compress-1.14.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.15
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.15/commons-compress-1.15.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.15
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.15/commons-compress-1.15.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.16.1
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.16.1/commons-compress-1.16.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.16.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.16.1/commons-compress-1.16.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.18
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.18/commons-compress-1.18.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.18
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.18/commons-compress-1.18.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.4.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.4.1/commons-compress-1.4.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.4.1
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.4.1/commons-compress-1.4.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.5
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.5/commons-compress-1.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.5
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.5/commons-compress-1.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.6
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.6/commons-compress-1.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.6
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.6/commons-compress-1.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.8.1
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.8.1
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.9
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.9/commons-compress-1.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.9
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.9/commons-compress-1.9.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.10/commons-compress-1.10.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.10/commons-compress-1.10.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.11/commons-compress-1.11.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.11/commons-compress-1.11.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.14/commons-compress-1.14.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.14/commons-compress-1.14.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.15/commons-compress-1.15.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.15/commons-compress-1.15.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.16.1/commons-compress-1.16.1.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.16.1/commons-compress-1.16.1.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.18/commons-compress-1.18.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.18/commons-compress-1.18.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.4.1/commons-compress-1.4.1.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.4.1/commons-compress-1.4.1.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.5/commons-compress-1.5.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.5/commons-compress-1.5.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.6/commons-compress-1.6.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.6/commons-compress-1.6.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.9/commons-compress-1.9.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-compress/1.9/commons-compress-1.9.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-commons-compress/LICENSE.txt
