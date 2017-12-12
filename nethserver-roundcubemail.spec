Summary: NethServer configuration for Roundcube mail client
Name: nethserver-roundcubemail
Version: 1.2.9
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: nethserver-httpd, nethserver-mysql, nethserver-mail-server
Requires: roundcubemail, php-mysql

%description
NethServer configuration for Roundcube mail client

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{version}-%{release}-filelist

%files -f %{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue Dec 12 2017 Davide Principi <davide.principi@nethesis.it> - 1.2.9-1
- Mails sent without attachments - Bug NethServer/dev#5397

* Mon May 29 2017 Davide Principi <davide.principi@nethesis.it> - 1.2.8-1
- Roundcube web access permission error - Bug NethServer/dev#5304

* Mon May 22 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.7-1
- Default userPrincipalName is not an email address - Bug NethServer/dev#5284

* Thu Jan 26 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.6-1
- Cleanup: remove deprecated events - nethserver-roundcubemail#9

* Thu Dec 15 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.5-1
- Roundcube duplicate accounts with short legacy format - Bug NethServer/dev#5151
- Enable LDAPs protocol on Active Directory clients - NethServer/dev#5161
- Roundcube: too many redirects - Bug NethServer/dev#5175
- Empty users in roundcube public LDAP Addressbook - Bug NethServer/dev#5156

* Thu Nov 10 2016 Davide Principi <davide.principi@nethesis.it> - 1.2.4-1
- Roundcube: no LDAP addressbook with OpenLDAP - Bug NethServer/dev#5146

* Thu Sep 01 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.3-1
- Apache vhost-default template expansion - NethServer/dev#5088

* Wed Aug 24 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.2-1
- Missing Roundcube disclaimer - Bug NethServer/dev#5075

* Thu Jul 21 2016 Davide Principi <davide.principi@nethesis.it> - 1.2.1-1
- First install of roundcube gives template error - Bug NethServer/dev#5053

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.2.0-1
- First NS7 release

* Tue Nov 10 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- Roundcube install fail - php-mysql not installed - Bug #3309 [NethServer]

* Wed Nov 12 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.1.0-1.ns6
- Upgrade Roundcubemail to the current version of epel   - Enhancement #2902 [NethServer]
- Roundcube webmail access from the Internet - Enhancement #2886 [NethServer]

* Mon Aug 18 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- Roundcube: installation fails - Bug #2802 [NethServer]

* Fri Jun 06 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- Roundcube: add dashboard widget - Enhancement #2707

* Wed Feb 26 2014 Davide Principi <davide.principi@nethesis.it> - 0.0.2-1.ns6
- Experimental Roundcube webmail package - Enhancement #2511 [NethServer]


