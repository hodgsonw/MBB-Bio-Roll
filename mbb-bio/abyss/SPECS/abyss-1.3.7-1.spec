# This is a  spec file for abyss

### define _topdir	 	/home/rpmbuild/rpms/abyss
%define name		abyss
%define release		1
%define version 	1.3.7
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary:        ABySS is a de novo, parallel, paired-end sequence assembler that is designed for short reads.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-%{release}.bin.patch0
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://www.bcgsc.ca/platform/bioinfo/software/abyss
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-3|http://www.bcgsc.ca/platform/bioinfo/software/abyss	
AutoReq:	yes

%description 
ABySS is a de novo, parallel, paired-end sequence assembler that is designed for
short reads. The single-processor version is useful for assembling genomes up to
100 Mbases in size. The parallel version is implemented using MPI and is capable
of assembling larger genomes. 

%prep
%setup -q
%patch -P 0 -p1

%build
./configure --disable-popcnt --enable-maxk=160 --with-boost=/usr/include/boost
#./configure --disable-popcnt --enable-maxk=160 --with-boost=/opt/bio/boost/include
make

%install
mkdir -p %{buildroot}%{installroot}
mkdir -p %{buildroot}/usr/share/man/man1
make install prefix=%{buildroot}%{installroot}
rm -r %{buildroot}%{installroot}/share
cd doc
cp ABYSS.1 abyss-pe.1 abyss-tofastq.1 %{buildroot}/usr/share/man/man1

%files
%defattr(755,root,root,755)
%{installroot}
%doc
/usr/share/man/man1/ABYSS.1.gz
/usr/share/man/man1/abyss-pe.1.gz
/usr/share/man/man1/abyss-tofastq.1.gz
%defattr(644,root,root,755)
/usr/share/man/man1/ABYSS.1.gz
/usr/share/man/man1/abyss-pe.1.gz
/usr/share/man/man1/abyss-tofastq.1.gz