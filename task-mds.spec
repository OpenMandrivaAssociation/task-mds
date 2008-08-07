Summary:	Meta package for the Mandriva Directory Server
Name:		task-mds
Version:	2.2.0
Release:	%mkrel 5
License:	GPL
Group:		System/Servers
URL:		http://mds.mandriva.org/
Requires:	mmc-agent
Requires:	mmc-web-base
Requires:	mmc-web-mail
Requires:	mmc-web-network
Requires:	mmc-web-proxy
Requires:	mmc-web-samba
Requires:	python-mmc-base
Requires:	python-mmc-samba
Requires:	python-mmc-mail
Requires:	python-mmc-network
Requires:	python-mmc-proxy
Provides:	mds = %version
Obsoletes:	mds <= 2.2.0
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This meta package installs the required components for the Mandriva Directory
Server.

%files
