#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Devel-OverloadInfo
#    Version:           0.005
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Devel\:\:OverloadInfo
#

Name:           opt-perl-Devel-OverloadInfo
Version:        0.005
Release:        1%{?dist}
Summary:        introspect overloaded operators
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-OverloadInfo/
BuildRoot:      /tmp/cpantorpm/Devel-OverloadInfo-0.005-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/I/IL/ILMARI/Devel-OverloadInfo-0.005.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Devel::OverloadInfo) = 0.005
Requires:       opt-perl
Requires:       opt-perl(MRO::Compat)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(Sub::Identify)
Requires:       opt-perl(overload)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(MRO::Compat)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(Sub::Identify)
BuildRequires:  opt-perl(overload)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Devel::OverloadInfo returns information about L<overloaded|overload>
operators for a given class (or object), including where in the inheritance
hierarchy the overloads are declared and where the code implementing them
is.

%prep

%setup  -n Devel-OverloadInfo-0.005
chmod -R u+w %{_builddir}/Devel-OverloadInfo-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site SITEPREFIX=/opt/perl INSTALLSITEARCH=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi INSTALLSITELIB=/opt/perl/lib/site_perl/5.26.0 INSTALLSITEBIN=/opt/perl/bin INSTALLSITESCRIPT=/opt/perl/bin INSTALLSITEMAN1DIR=/opt/perl/man/man1 INSTALLSITEMAN3DIR=/opt/perl/man/man3 INSTALLSCRIPT=/opt/perl/bin
make %{?_smp_mflags}

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   make test
fi

%install

rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 0.005-1
- Generated using cpantorpm
