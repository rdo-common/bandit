Name: bandit
Version: 0.13.2
Release: 2%{?dist}
Summary: A framework for performing security analysis of Python source code
License: ASL 2.0
URL: https://wiki.openstack.org/wiki/Security/Projects/Bandit
Source0: https://pypi.python.org/packages/source/b/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: PyYAML
Requires: python-stevedore
Requires: python-appdirs
BuildRequires: python2-devel
BuildRequires: python-pip
BuildRequires: python-pbr

%description
Bandit provides a framework for performing security analysis of Python source
code, utilizing the ast module from the Python standard library.

The ast module is used to convert source code into a parsed tree of Python
syntax nodes. Bandit allows users to define custom tests that are performed
against those nodes. At the completion of testing, a report is generated
that lists security issues identified within the target source code.
%prep
%setup -q

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
# bandit install his configuration file in %{python2_sitelib}/%{name}, so that's the easiest fix
mkdir -p %{buildroot}/%{_sysconfdir}
mv -f %{buildroot}/%{_prefix}/%{_sysconfdir}/bandit  %{buildroot}/%{_sysconfdir}/bandit

%check
# the tests requires internet access, with pip install being run
# so they are disabled for now, since koji block outgoing connexion
# tox -epy27

%files
%doc AUTHORS ChangeLog README.rst
%doc docs examples
%license LICENSE
%{_bindir}/bandit
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}-%{version}-py%{python2_version}.egg-info
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.yaml
%dir %{_sysconfdir}/%{name}
%{_datarootdir}/%{name}

%changelog
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 Michael Scherer <misc@zarb.org> 0.13.2-1
- new version 0.13.2
- add requires on python-stevedore, fix #1254589

* Sat Jul 11 2015 Michael Scherer <misc@zarb.org> 0.12.0-1
- new version 0.12.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Michael Scherer <misc@zarb.org> 0.11.0-1
- new version 0.11.0

* Fri May 01 2015 Michael Scherer <misc@zarb.org> 0.10.1-1
- Initial package
