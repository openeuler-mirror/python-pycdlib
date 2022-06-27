%global _empty_manifest_terminate_build 0
Name:           python-pycdlib
Version:        1.12.0
Release:        1
Summary:        Pure python ISO manipulation library
License:        LGPLv2
URL:            http://github.com/clalancette/pycdlib
Source0:        https://files.pythonhosted.org/packages/a2/15/9f0f0b4d97ea2fd4969207a89cf657d63ddee6fa8b972cd4e99ce28ea096/pycdlib-1.12.0.tar.gz
BuildArch:      noarch
%description
PyCdlib is a pure python library to parse, write (master), and create ISO9660
files, suitable for writing to a CD or USB.The original ISO9660 (including
ISO9660-1999) specification is supported, as well the El Torito, Joliet, Rock
Ridge, and UDF extensions.Please see for much more documentation.

%package -n python3-pycdlib
Summary:        Pure python ISO manipulation library
Provides:       python-pycdlib
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  genisoimage
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

%description -n python3-pycdlib
PyCdlib is a pure python library to parse, write (master), and create ISO9660
files, suitable for writing to a CD or USB.The original ISO9660 (including
ISO9660-1999) specification is supported, as well the El Torito, Joliet, Rock
Ridge, and UDF extensions.Please see for much more documentation.

%package help
Summary:        Pure python ISO manipulation library
Provides:       python3-pycdlib-doc

%description help
PyCdlib is a pure python library to parse, write (master), and create ISO9660
files, suitable for writing to a CD or USB.The original ISO9660 (including
ISO9660-1999) specification is supported, as well the El Torito, Joliet, Rock
Ridge, and UDF extensions.Please see for much more documentation.

%prep
%autosetup -n pycdlib-%{version}

%build
%py3_build

%install
%py3_install

install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
PYCDLIB_TRACK_WRITES=1 py.test-%{python3_version} -v tests
%{__python3} setup.py test

%files -n python3-pycdlib -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Jun 09 2022 OpenStack_SIG <openstack@openeuler.org> - 1.12.0-1
- Upgrade package python3-pycdlib to version 1.12.0

* Mon Apr 12 2021 orange-snn <songnannan2@huawei.com> - 1.11.0-1
- package init for lorax
