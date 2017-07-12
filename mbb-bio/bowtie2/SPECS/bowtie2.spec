# This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/bowtie2
%define name		bowtie2
%define release		1
%define version 	2.3.2 
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
Source: 		%{name}-%{version}-source.zip
Prefix: 		/opt/bio
Group: 			Development/Tools
URL:			http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
AutoReq:		yes
Packager:		Iyad Kandalaft <Iyad.Kandalaft@agr.gc.ca>

BuildRequires:	opt-tbb-devel

%description
Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s or 1,000s of characters, and particularly good at aligning to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the genome with an FM Index to keep its memory footprint small: for the human genome, its memory footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local, and paired-end alignment modes.

%prep
%setup -q -n %{name}-%{version}

%build
export CPLUS_INCLUDE_PATH=$(dirname $(dirname $(rpm -ql opt-tbb-devel | grep tbb.h$)))
export LD_RUN_PATH=$(dirname $(rpm -ql opt-tbb | grep "libtbb.so"))
export LIBRARY_PATH=$LD_RUN_PATH
make -j `nproc` DESTDIR=$RPM_BUILD_ROOT prefix=%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make DESTDIR=$RPM_BUILD_ROOT prefix=%{installroot} install


%files
%defattr(755,root,root)
%{installroot}
