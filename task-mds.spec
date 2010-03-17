Summary:	Meta package for the Mandriva Directory Server
Name:		task-mds
Version:	2.3.2
Release:	%mkrel 3
License:	GPL
Group:		System/Servers
URL:		http://mds.mandriva.org/
Requires:	mmc-agent >= %{version}
Requires:	mmc-web-base >= %{version}
Requires:	mmc-web-mail >= %{version}
Requires:	mmc-web-network >= %{version}
Requires:	mmc-web-proxy >= %{version}
Requires:	mmc-web-samba >= %{version}
Requires:	python-mmc-base >= %{version}
Requires:	python-mmc-samba >= %{version}
Requires:	python-mmc-mail >= %{version}
Requires:	python-mmc-network >= %{version}
Requires:	python-mmc-proxy >= %{version}
Provides:	mds = %version
Obsoletes:	mds <= 2.2.0
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This meta package installs the required components for the Mandriva Directory
Server.

%files
