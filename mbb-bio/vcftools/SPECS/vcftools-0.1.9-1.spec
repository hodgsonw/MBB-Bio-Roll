# This is a  spec file for mira genome assembler
#make sure to run: 
# export PERL5LIB=/opt/bio/vcftools/perl 
# else the perl scripts won't work 


### define _topdir	 	/home/rpmbuild/rpms/vcftools
%define name		vcftools
%define release		1
%define version 	0.1.9
%define installroot 	/opt/bio/%{name}
%define buildroot       %{_topdir}/%{name}-%{version}-root


BuildRoot:	%{buildroot}
Summary:	vcftools
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}_%{version}.tar.gz
Patch0:		%{name}_%{version}.patch
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        LGPL-3|http://vcftools.sourceforge.net/license.html	
AutoReq:	no
# Test::Most is already installed 

%description
Welcome to VCFtools - a program package designed for working with VCF files,
such as those generated by the 1000 Genomes Project. The aim of VCFtools is to
provide methods for working with VCF files: validating, merging, comparing and
calculate some basic population genetic statistics. 


%prep
%setup -q -n %{name}_%{version} 
%patch -P 0 -p1


%build
# script actually doesn't work in two parts, it jumps straight to install
#make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
echo Directory `pwd`
make install PREFIX=$RPM_BUILD_ROOT%{installroot} 

%files
%defattr(-,root,root)
%dir %attr(0755,root,root) %{installroot}
%dir %attr(0755,root,root) %{installroot}/bin
%dir %attr(0755,root,root) %{installroot}/lib
%{installroot}