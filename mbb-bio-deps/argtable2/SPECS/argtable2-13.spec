# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name			argtable2
%define src_name		argtable2
%define release		1
%define version 	13
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Argtable is an ANSI C command line parser.
License: 		LGPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Libraries
URL:			http://argtable.sourceforge.net/
AutoReq:		yes

%description
Argtable is an ANSI C library for parsing GNU style command line
options with a minimum of fuss. It enables a programs command line
syntax to be defined in the source code as an array of argtable
structs. The command line is then parsed according to that
specification and the resulting values are returned in those same
structs where they are accessible to the main program. Both tagged
(-v, --verbose, --foo=bar) and untagged arguments are supported, as
are multiple instances of each argument. Syntax error handling is
automatic and the library also provides the means for generating a
textual description of the command line syntax. 


%prep
%setup -q

%build
./configure
make prefix=%{installroot}

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}
#find $RPM_BUILD_ROOT%{installroot} -type f -exec sed -i 's|/root/rpms/amos/amos-3.1.0-root/|/|g' {} \;

%files
%defattr(755,root,root,755)
%{installroot}
