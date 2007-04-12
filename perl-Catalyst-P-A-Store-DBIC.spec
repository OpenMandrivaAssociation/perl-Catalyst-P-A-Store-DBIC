%define realname Catalyst-Plugin-Authentication-Store-DBIC
%define abbrevname Catalyst-P-A-Store-DBIC
%define name	perl-%{abbrevname}
%define	modprefix Catalyst

%define version	0.07
%define release	%mkrel 1

Summary:	Authentication and authorization against a Class::DBI model
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Authentication) >= 0.06
BuildRequires:	perl(DBI)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Set::Object) >= 1.14
Provides:	perl-%{realname}
Obsoletes:	perl-%{realname}
BuildArch:	noarch
Buildroot:	%_tmppath/%{name}-%{version}-%{release}-buildroot

%description
This Catalyst plugin uses a DBIx::Class (or Class::DBI) object to
authenticate a user.


%prep
%setup -q -n %realname-%version

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%perl_vendorlib/%{modprefix}
%_mandir/*/*

%clean
rm -rf %{buildroot}



