# roundcubemail specific version
%define rcm_version 1.5.2
# roundcubemail specific name
%define rcm_name roundcubemail

Summary: NethServer configuration for Roundcube mail client
Name: nethserver-roundcubemail
Version: 1.5.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
Source1: https://github.com/roundcube/%{rcm_name}/releases/download/%{rcm_version}/%{rcm_name}-%{rcm_version}-complete.tar.gz
Source2: https://github.com/alexandregz/twofactor_gauthenticator/archive/master.zip
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: nethserver-httpd, nethserver-mysql, nethserver-mail-server
Obsoletes: roundcubemail
Requires: nethserver-rh-php73-php-fpm
Requires: rh-php73-php-pspell

%description
NethServer configuration for Roundcube mail client

%prep
%setup

%build
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

%{genfilelist} %{buildroot} --file /etc/sudoers.d/50_nsapi_nethserver_roundcubemail 'attr(0440,root,root)' > %{version}-%{release}-filelist

mkdir -p %{buildroot}/etc/%{rcm_name}
mkdir -p %{buildroot}/usr/share/%{rcm_name}
tar xzvf %{SOURCE1}
cp -r %{rcm_name}-%{rcm_version}/* %{buildroot}%{_datadir}/%{rcm_name}

# Link to config file
ln -s /etc/%{rcm_name}/config.inc.php     %{buildroot}%{_datadir}/%{rcm_name}/config/config.inc.php

# Temp directory
mkdir -p %{buildroot}/usr/share/%{rcm_name}/temp

# Logs
mkdir -p %{buildroot}/var/log/%{rcm_name}

# GPG keys
mkdir -p %{buildroot}/usr/share/%{rcm_name}/enigma

# Plugins directory 2FA
mkdir -p %{buildroot}/usr/share/%{rcm_name}/plugins/twofactor_gauthenticator/
unzip %{SOURCE2}
cp -a twofactor_gauthenticator-master/* %{buildroot}/usr/share/%{rcm_name}/plugins/twofactor_gauthenticator/

%files -f %{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
%{_datadir}/%{rcm_name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{rcm_name}
%dir %attr(0750,apache,apache) %{_datadir}/%{rcm_name}/temp
%dir %attr(0750,apache,apache) %{_datadir}/%{rcm_name}/enigma
%dir %attr(0750,apache,apache) /var/log/%{rcm_name}
%dir %attr(0755,root,root) %{_datadir}/%{rcm_name}/plugins/twofactor_gauthenticator
%dir %attr(0755,root,root) /etc/%{rcm_name}

%changelog
* Tue Jul 06 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.5.0-1
- Roundcubemail 1.4.11 - NethServer/dev#6541

* Tue Oct 01 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.4.0-1
- Sudoers based authorizations for Cockpit UI - NethServer/dev#5805

* Tue Sep 03 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.2-1
- Cockpit. List correct application version - Nethserver/dev#5819

* Tue Jul 09 2019 Davide Principi <davide.principi@nethesis.it> - 1.3.1-1
- Cockpit legacy apps implementation - NethServer/dev#5782

* Fri Feb 01 2019 Davide Principi <davide.principi@nethesis.it> - 1.3.0-1
- SMTP sender/login validation - NethServer/dev#5672

* Thu Oct 11 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.2.10-1
- Merge pull request #13 from stephdl/saveEvent
- NethServer/dev#5600
- Roundcubemail subscribed to nethserver-sssd-save

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


