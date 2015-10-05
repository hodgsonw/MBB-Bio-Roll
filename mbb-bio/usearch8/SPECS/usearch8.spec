### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/usearch8
%define name              usearch
%define release           1.1756
%define version           8
%define installroot       /opt/bio/%{name}%{version}

Summary:   Extreme high-throughput sequence analysis. 
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    usearch8.1.1756_i86linux32
License:   Individual use, non-transferrable license.
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Group:     Development/Tools
#BuildRoot: %{buildroot}
Prefix:    /opt/bio
Vendor:    Robert C. Edgar, PhD.
Url:       http://drive5.com/cgi-bin/upload3.py?license=2015100212161422523
AutoReq:   yes

%description
USEARCH is a unique sequence analysis tool with thousands of users world-wide. USEARCH offers search and clustering algorithms that are often orders of magnitude faster than BLAST. 

%prep
cp ../SOURCES/usearch8.1.1756_i86linux32 .  
#%setup -n %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
mv usearch8.1.1756_i86linux32 usearch8
cp usearch8 $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/
