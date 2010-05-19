Summary:	Meta package for the Mandriva Directory Server
Name:		task-mds
Version:	2.4.0
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://mds.mandriva.org/
Requires:	mmc-agent >= 3.0.0
Requires:	mmc-web-base >= 3.0.0
Requires:	mmc-web-ppolicy >= 3.0.0
Requires:	python-mmc-base >= 3.0.0
Requires:	python-mmc-core >= 3.0.0
Requires:	python-mmc-ppolicy >= 3.0.0
Requires:	mmc-web-bulkimport >= 2.4.0
Requires:	mmc-web-mail >= 2.4.0
Requires:	mmc-web-network >= 2.4.0
Requires:	mmc-web-proxy >= 2.4.0
Requires:	mmc-web-samba >= 2.4.0
Requires:	mmc-web-sshlpk >= 2.4.0
Requires:	mmc-web-userquota >= 2.4.0
Requires:	python-mmc-bulkimport >= 2.4.0
Requires:	python-mmc-mail >= 2.4.0
Requires:	python-mmc-network >= 2.4.0
Requires:	python-mmc-proxy >= 2.4.0
Requires:	python-mmc-samba >= 2.4.0
Requires:	python-mmc-sshlpk >= 2.4.0
Requires:	python-mmc-userquota >= 2.4.0
Requires:	mmc-check-password >= 3.0.0
Provides:	mds = %version
Obsoletes:	mds <= 2.2.0
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This meta package installs the required components for the Mandriva Directory
Server.

%files
