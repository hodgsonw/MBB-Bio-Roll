%define name			parasail
%define src_name		parasail
%define release		1
%define version 	1.0.0
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Pairwise Sequence Alignment Library
License: 		Battelle BSD-style
Packager:	Glen Newton <Glen.Newton@agr.gc.ca>
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-v%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics
URL:			https://github.com/jeffdaily/parasail
AutoReq:		yes


%description
parasail is a SIMD C (C99) library containing implementations of the Smith-Waterman (local), Needleman-Wunsch (global), and semi-global pairwise sequence alignment algorithms. Here, semi-global means insertions before the start or after the end of either the query or target sequence are not penalized. parasail implements most known algorithms for vectorized pairwise sequence alignment, including diagonal [Wozniak, 1997], blocked [Rognes and Seeberg, 2000], striped [Farrar, 2007], and prefix scan [Daily, 2015]. Therefore, parasail is a reference implementation for these algorithms in addition to providing an implementation of the best-performing algorithm(s) to date on today's most advanced CPUs.
Need to add /opt/parasail/lib to LD_LIBRARY_PATH


%prep
%setup -q

%build
./configure
make --jobs=`nproc`  prefix=%{installroot} 

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
