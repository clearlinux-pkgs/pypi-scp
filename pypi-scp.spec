#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-scp
Version  : 0.14.4
Release  : 28
URL      : https://files.pythonhosted.org/packages/01/96/82028abe87441ae172ce9df2eeb46274130475bfeeb4dedeaddaf75b16a9/scp-0.14.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/96/82028abe87441ae172ce9df2eeb46274130475bfeeb4dedeaddaf75b16a9/scp-0.14.4.tar.gz
Summary  : scp module for paramiko
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: pypi-scp-license = %{version}-%{release}
Requires: pypi-scp-python = %{version}-%{release}
Requires: pypi-scp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(paramiko)

%description
======================
        
        The scp.py module uses a paramiko transport to send and receive files via the
        scp1 protocol. This is the protocol as referenced from the openssh scp program,
        and has only been tested with this implementation.
        
        
        Example
        -------

%package license
Summary: license components for the pypi-scp package.
Group: Default

%description license
license components for the pypi-scp package.


%package python
Summary: python components for the pypi-scp package.
Group: Default
Requires: pypi-scp-python3 = %{version}-%{release}

%description python
python components for the pypi-scp package.


%package python3
Summary: python3 components for the pypi-scp package.
Group: Default
Requires: python3-core
Provides: pypi(scp)
Requires: pypi(paramiko)

%description python3
python3 components for the pypi-scp package.


%prep
%setup -q -n scp-0.14.4
cd %{_builddir}/scp-0.14.4
pushd ..
cp -a scp-0.14.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656406480
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-scp
cp %{_builddir}/scp-0.14.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-scp/a393ab05655034ea1176ada5f33586112407ff71
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-scp/a393ab05655034ea1176ada5f33586112407ff71

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
