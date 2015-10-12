
### define _topdir	 	/home/rpmbuild/rpms/cdhit
%define name		cd-hit
%define release		2
%define prefix		v
%define version 	4.6.4
%define date		2015-0603
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		cd-hit
License: 		GPL-2|https://github.com/weizhongli/cdhit
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{prefix}%{version}-%{date}.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
CD-HIT is a program for clustering DNA/protein sequence database at high
identity with tolerance.

%prep
%setup -q -n cd-hit-v4.6.4-2015-0603

%build
make openmp=yes
for f in *.pl; do sed -i 's/#!\/usr\/bin\/perl/#!\/usr\/bin\/env perl/' ${f}; done

%install

mkdir -p $RPM_BUILD_ROOT%{installroot}
make install PREFIX=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
