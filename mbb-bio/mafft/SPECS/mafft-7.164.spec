# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/mafft
%define name			mafft
%define release		2
%define version 	7.164
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:		%{buildroot}
Summary: 		Multiple alignment program for amino acid or nucleotide sequences
License: 		Public Domain /w restrictions (http://mafft.cbrc.jp/alignment/software/license66.txt)
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}-with-extensions-src.tgz
Prefix: 		/opt/bio
URL:			http://mafft.cbrc.jp/alignment/software/
Group: 			Development/Tools
AutoReq:		yes

%description
MAFFT is a multiple sequence alignment program for unix-like operating systems.  It offers a range of multiple alignment methods, L-INS-i (accurate; for alignment of <~200 sequences), FFT-NS-2 (fast; for alignment of<~10,000 sequences), etc.

%prep
%setup -q -n mafft-7.164-with-extensions

%build
cd core
make   -pipe --jobs=`nproc` PREFIX=%{installroot}
cd ..
cd extensions
make  -pipe --jobs=`nproc` PREFIX=%{installroot}
cd ..

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cd core
make install PREFIX=$RPM_BUILD_ROOT%{installroot}
cd ..
cd %{buildroot}/opt/bio/mafft/bin
rm mafft-distance; ln -s ../libexec/mafft/mafft-distance 
rm mafft-profile; ln -s ../libexec/mafft/mafft-profile 
cd %{_topdir}/BUILD/%{name}-%{version}-with-extensions
cd extensions
make install PREFIX=$RPM_BUILD_ROOT%{installroot}
cd ..

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root)
%{installroot}/bin
%{installroot}/libexec
