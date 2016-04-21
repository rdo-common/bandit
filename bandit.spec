Name: bandit
Version: 1.0.1
Release: 1%{?dist}
Summary: A framework for performing security analysis of Python source code
License: ASL 2.0
URL: https://wiki.openstack.org/wiki/Security/Projects/Bandit
Source0: https://pypi.python.org/packages/source/b/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: python3-PyYAML
Requires: python3-stevedore
Requires: python3-appdirs
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-pbr

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
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%check
# the tests requires internet access, with pip install being run
# so they are disabled for now, since koji block outgoing connexion
# tox -epy27

%files
%doc AUTHORS ChangeLog README.rst
%doc doc
%doc examples
%license LICENSE
%{_bindir}/bandit
%{_bindir}/bandit-baseline
%{_bindir}/bandit-config-generator
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog

* Thu Apr 21 2016 Michael Scherer <misc@zarb.org> - 1.0.1-1
- update to 1.0.1
- port to python3
- drop the /etc configuration directory, as upstream did remove config file

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
