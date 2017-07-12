# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name		freebayes
%define release		1
%define version 	1.1.0
%define buildroot 	%{_topdir}/%{name}-%{version}
%define installroot 	/opt/bio/%{name}
%define gcc_491_path	/opt/bio/gcc491/bin
%define ld_library_path	/opt/bio/gcc491/lib64
%define debug_package	%{nil}

BuildRoot:	%{buildroot}
Summary: 	Bayesian haplotype-based genetic polymorphism discovery and genotyping.
License: 		MIT
Name: 			%{name}
Version: 		%{version}
Packager:  	Iyad Kandalaft <Iyad.Kandalaft@agr.gc.ca>
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.gz
Prefix: 	/opt/bio
Group: 		Applications/BioInformatics/SNP
URL:		https://arxiv.org/abs/1207.3907
AutoReq:		yes
BuildRequires:	gcc491

%description
https://arxiv.org/abs/1207.3907

The direct detection of haplotypes from short-read DNA sequencing data requires changes to existing small-variant detection methods. Here, we develop a Bayesian statistical framework which is capable of modeling multiallelic loci in sets of individuals with non-uniform copy number. We then describe our implementation of this framework in a haplotype-based variant detector, FreeBayes. 


%prep
%setup -q

%build
export PATH=%{gcc_491_path}:$PATH
export LD_LIBRARY_PATH=%{ld_library_path}
make -pe --jobs=`nproc` prefix=%{installroot} 

%install
BIN_PATH=%{buildroot}%{installroot}/bin
mkdir -p $BIN_PATH
# make install copies binaries to /usr/bin.  Must manually copy binaries to buildroot
cp bin/freebayes bin/bamleftalign $BIN_PATH

%files
%defattr(755,root,root,755)
%{installroot}
