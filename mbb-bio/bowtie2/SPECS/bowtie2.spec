# This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/bowtie2
%define name		bowtie2
%define release		1
%define version 	2.2.6 
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define insSet		x86_64
%define debug_package	%{nil} 


BuildRoot:		%{buildroot}
Summary: 		An ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences.
License: 		Artistic License
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.bz2
Prefix: 		/opt/bio
Group: 			Development/Tools
URL:			https://github.com/BenLangmead/bowtie2
AutoReq:		yes
Packager:	Glen Newton <Glen.Newton@agr.gc.ca>

%description
Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s or 1,000s of characters, and particularly good at aligning to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the genome with an FM Index to keep its memory footprint small: for the human genome, its memory footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local, and paired-end alignment modes.

%prep
%setup -q -n %{name}-%{version}

%build
make  --jobs=`nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
strip bowtie2-inspect-l bowtie2-inspect-s bowtie2-build-s bowtie2-build-l bowtie2-align-s bowtie2-align-l
mkdir $RPM_BUILD_ROOT%{installroot}/bin
cp bowtie2*  $RPM_BUILD_ROOT%{installroot}/bin
cp -r doc example scripts third_party VERSION MANUAL $RPM_BUILD_ROOT%{installroot}


%files
%defattr(755,root,root)
%{installroot}
