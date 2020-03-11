%global srcname ssm-cache
%global longname %{srcname}-python
# When bootstrapping Python, we cannot test this yet
%bcond_without tests

Name:           python-%{srcname}
Version:        2.9
Release:        1%{?dist}
Summary:        AWS System Manager Parameter Store caching client for Python

License:        MIT
URL:            https://github.com/alexcasalboni/%{srcname}-python
Source0:        %{url}/archive/%{version}/%{longname}-%{version}.tar.gz
BuildArch:      noarch

%description
AWS System Manager Parameter Store caching client for Python by Alex Casalboni

%package -n python3-%{srcname}
Summary:        AWS System Manager Parameter Store caching client for Python

BuildRequires:  python3-coverage
BuildRequires:  python3-setuptools
%if %{with tests}
%else
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-pygments
BuildRequires:  python3-pypandoc
BuildRequires:  python3-coveralls
BuildRequires:  python3-placebo
BuildRequires:  python3-pylint
BuildRequires:  python3-freezegun
%endif

Requires:       python3-boto3
Requires:       python3-future

%description -n python3-%{srcname}
AWS System Manager Parameter Store caching client for Python

%prep
%autosetup -p1 -n %{longname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check %{python3} setup.py test
%endif

%files -n python3-%{srcname}
%dir %{python3_sitelib}/tests
%dir %{python3_sitelib}/ssm_cache
%dir %{python3_sitelib}/ssm_cache-*.egg-info
%{python3_sitelib}/ssm_cache/
%{python3_sitelib}/ssm_cache-*.egg-info/
%{python3_sitelib}/tests/

%license LICENSE
%doc README.md

%changelog
* Wed Mar 11 2020 David Duncan <davdunc@amazon.com> - 2.9-1
- Initial package build

