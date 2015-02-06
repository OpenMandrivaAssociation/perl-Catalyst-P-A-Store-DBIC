%define upstream_name    Catalyst-Plugin-Authentication-Store-DBIC
%define upstream_version 0.11

Name:		perl-Catalyst-P-A-Store-DBIC
Version:	%perl_convert_version %{upstream_version}
Release:	6
Epoch:		1

Summary:	Authentication and authorization against a Class::DBI model
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Authentication) >= 0.06
BuildRequires:  perl(Catalyst::Model::DBIC::Schema)
BuildRequires:  perl(Catalyst::Plugin::Authorization::Roles)
BuildRequires:  perl(Catalyst::Plugin::Session::State)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Class::DBI)
BuildRequires:	perl(DBI)
BuildRequires:  perl(DBIx::Class)
BuildRequires:	perl(Set::Object) >= 1.14
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildArch:	noarch
%rename perl-%{upstream_name}

%description
This Catalyst plugin uses a DBIx::Class (or Class::DBI) object to
authenticate a user.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1:0.110.0-3mdv2011.0
+ Revision: 680725
- mass rebuild

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.110.0-2mdv2011.0
+ Revision: 552189
- rebuild

* Sun Jul 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.110.0-1mdv2010.0
+ Revision: 395099
- adding missing buildrequires
- update to 0.11
- using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1:0.07-4mdv2009.0
+ Revision: 241156
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.07-2mdv2008.0
+ Revision: 85928
- rebuild


* Mon Aug 07 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-07 23:43:23 (54246)
- Version 0.07- Added BuildRequires perl(DBI)

* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 21:13:16 (53630)
- import perl-Catalyst-P-A-Store-DBIC-0.06-1mdk

* Tue May 16 2006 Scott Karns <scottk@mandriva.org> 1:0.06-1mdk
- Updated to release 0.06

* Fri Apr 14 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.05002-2mdk
- Abbreviate rpm name to fit in the 64 char limit

* Mon Mar 20 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.05002-1mdk
- New release 0.05002

* Thu Jan 12 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-1mdk
- Initial MDV RPM

