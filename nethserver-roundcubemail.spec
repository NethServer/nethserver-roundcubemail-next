Summary: NethServer configuration for Roundcube mail client
Name: nethserver-roundcubemail
Version: 1.1.2
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

%changelog
* Wed Aug 24 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- Missing Roundcube disclaimer - Bug #3417

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


