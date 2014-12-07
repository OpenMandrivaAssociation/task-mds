Summary:	Meta package for the Mandriva Directory Server
Name:		task-mds
Version:	2.4.0
Release:	12
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.0-3mdv2011.0
+ Revision: 670666
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.0-2mdv2011.0
+ Revision: 607979
- rebuild

* Wed May 19 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.0-1mdv2010.1
+ Revision: 545355
- fix #59365 (Please tighten required packages versions)

* Thu Apr 29 2010 Anne Nicolas <ennael@mandriva.org> 2.4.0-0.0.1mdv2010.1
+ Revision: 540939
- fix version number

* Tue Apr 27 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-0.0.1mdv2010.1
+ Revision: 539771
- prepare for new versions and adjust deps

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.2-3mdv2010.1
+ Revision: 524166
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.3.2-2mdv2010.0
+ Revision: 427282
- rebuild

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 2.3.2-1mdv2009.1
+ Revision: 316127
- 2.3.2
- fix deps

* Fri Aug 22 2008 Thierry Vignaud <tv@mandriva.org> 2.3.1-2mdv2009.0
+ Revision: 275186
- rebuild

* Thu Aug 07 2008 Funda Wang <fwang@mandriva.org> 2.3.1-1mdv2009.0
+ Revision: 265856
- bump version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-5mdv2009.0
+ Revision: 265747
- rebuild early 2009.0 package (before pixel changes)

* Mon May 05 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-4mdv2009.0
+ Revision: 201264
- versionnate obsoletes/provides

* Mon May 05 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-3mdv2009.0
+ Revision: 201259
- rename as task-mds
- rename as task-mds

* Tue Apr 22 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-2mdv2009.0
+ Revision: 196516
- fix deps

* Mon Jan 07 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-1mdv2008.1
+ Revision: 146287
- import mds

