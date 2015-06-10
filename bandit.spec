Name: bandit
Version: 0.11.0
Release: 1%{?dist}
Summary: A framework for performing security analysis of Python source code
License: ASL 2.0
URL: https://wiki.openstack.org/wiki/Security/Projects/Bandit
Source0: http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: PyYAML
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
mv -f %{buildroot}/%{python2_sitelib}/%{name}/config %{buildroot}/%{_sysconfdir}/bandit

%check
# the tests requires internet access, with pip install being run
# so they are disabled for now, since koji block outgoing connexion
# tox -epy27

%files
%doc AUTHORS ChangeLog README.md
%doc docs examples
%license LICENSE
%{_bindir}/bandit
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}-%{version}-py%{python2_version}.egg-info
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.yaml
%dir %{_sysconfdir}/%{name}

%changelog
* Wed Jun 10 2015 Michael Scherer <misc@zarb.org> 0.11.0-1
- new version 0.11.0

* Fri May 01 2015 Michael Scherer <misc@zarb.org> 0.10.1-1
- Initial package
