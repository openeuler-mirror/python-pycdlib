%global srcname pycdlib

Name:           python-%{srcname}
Summary:        A pure python ISO9660 read and write library
Version:        1.11.0
Release:        1
License:        LGPLv2
URL:            https://github.com/clalancette/%{srcname}
Source0:        https://github.com/clalancette/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel genisoimage python3-pytest

%description
Pycdlib is a pure python library for reading, writing, and otherwise\
manipulating ISO9660 files.  It is focused on speed, correctness, and\
conformance to the various standards around ISO9660, including ISO9660 itself,\
the Joliet extensions, the Rock Ridge extensions, the El Torito boot\
extensions, and UDF.

%package -n python3-%{srcname}
Summary:        python3 for %{srcname}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python3 for %{srcname}

%package -n %{srcname}-tools
Summary:        Tools that rely on %{srcname}
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n %{srcname}-tools
Some tools that use the %{srcname} library.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYCDLIB_TRACK_WRITES=1 py.test-%{python3_version} -v tests

%files -n python3-%{srcname}
%license COPYING
%doc README.md examples/
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%files -n %{srcname}-tools
%license COPYING
%{_bindir}/pycdlib-explorer
%{_bindir}/pycdlib-extract-files
%{_bindir}/pycdlib-genisoimage
%{_mandir}/man1/*

%changelog
* Mon Apr 12 2021 orange-snn <songnannan2@huawei.com> - 1.11.0-1
- package init for lorax
