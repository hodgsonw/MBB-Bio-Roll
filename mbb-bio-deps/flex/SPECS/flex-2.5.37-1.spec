#
### define _topdir	 	/home/rpmbuild/rpms/flex 
%define name		flex
%define release		1
%define version 	2.5.37
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		flex 
License: 		Boost Software License 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz 
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
Flex is a tool for generating scanners. A scanner, sometimes called a
tokenizer, is a program which recognizes lexical patterns in text. The flex
program reads user-specified input files, or its standard input if no file
names are given, for a description of a scanner to generate. The description is
in the form of pairs of regular expressions and C code, called rules. Flex
generates a C source file named, "lex.yy.c", which defines the function
yylex(). The file "lex.yy.c" can be compiled and linked to produce an
executable. When the executable is run, it analyzes its input for occurrences
of text matching the regular expressions for each rule. Whenever it finds a
match, it executes the corresponding C code.

%prep
%setup -q 

%build
./configure  --prefix=%{installroot}
make 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}


%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin/* 
