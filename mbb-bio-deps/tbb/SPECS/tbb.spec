%global upver 2017
%global uprel 7

%define name		opt-tbb
%define src_name	tbb
%define release		1
%define version		%{upver}.%{uprel}
%define buildroot 	%{_topdir}/%{name}-%{version}
%define installroot 	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _mandir		%{installroot}/share/man
%define _defaultdocdir	%{installroot}/share/docs
%define debug_package 	%{nil}

buildRoot:	%{buildroot}
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: The Threading Building Blocks library abstracts low-level threading details
License: ASL 2.0
Group:   Development/Tools
URL:     http://threadingbuildingblocks.org/

Source: https://github.com/01org/tbb/archive/%{upver}_U%{uprel}.tar.gz

BuildRequires: gcc-c++
BuildRequires: python2-devel
BuildRequires: swig

%description
Threading Building Blocks (TBB) is a C++ runtime library that
abstracts the low-level threading details necessary for optimal
multi-core performance.  It uses common C++ templates and coding style
to eliminate tedious threading implementation work.

TBB requires fewer lines of code to achieve parallelism than other
threading models.  The applications you write are portable across
platforms.  Since the library is also inherently scalable, no code
maintenance is required as more processor cores become available.


%package devel
Summary: The Threading Building Blocks C++ headers and shared development libraries
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and shared object symlinks for the Threading Building
Blocks (TBB) C++ libraries.

%prep
%setup -q -n %{src_name}-%{upver}_U%{uprel}

# For repeatable builds, don't query the hostname or architecture
sed -i 's/"`hostname -s`" ("`uname -m`"/fedorabuild (%{_arch}/' \
    build/version_info_linux.sh

# Fix libdir on 64-bit systems
if [ "%{_libdir}" != "%{_prefix}/lib" ]; then
  sed -i.orig 's/"lib"/"%{_lib}"/' cmake/TBBMakeConfig.cmake
  touch -r cmake/TBBMakeConfig.cmake.orig cmake/TBBMakeConfig.cmake
  rm cmake/TBBMakeConfig.cmake.orig
fi

%build

make -j `nproc` %{?_smp_mflags} tbb_build_prefix=obj \
  CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}

pushd build/obj_release
    for file in libtbb{,malloc{,_proxy}}; do
        install -p -D -m 755 ${file}.so.2 $RPM_BUILD_ROOT/%{_libdir}
        ln -s $file.so.2 $RPM_BUILD_ROOT/%{_libdir}/$file.so
    done
popd

pushd include
    find tbb -type f ! -name \*.htm\* -exec \
        install -p -D -m 644 {} $RPM_BUILD_ROOT/%{_includedir}/{} \
    \;
popd

# Install the cmake files
mkdir -p $RPM_BUILD_ROOT%{_libdir}/cmake
cp -a cmake $RPM_BUILD_ROOT%{_libdir}/cmake/%{name}
rm $RPM_BUILD_ROOT%{_libdir}/cmake/%{name}/README.rst

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc doc/Release_Notes.txt README.md
%{_libdir}/*.so.2

%files devel
%doc CHANGES cmake/README.rst
%{_includedir}/tbb
%{_libdir}/*.so
%{_libdir}/cmake/

