%define upstream_name    Catalyst-Plugin-Authentication-Store-DBIC
%define upstream_version 0.11

Name:		perl-Catalyst-P-A-Store-DBIC
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2
Epoch:		1

Summary:	Authentication and authorization against a Class::DBI model
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Authentication) >= 0.06
BuildRequires:  perl(Catalyst::Model::DBIC::Schema)
BuildRequires:  perl(Catalyst::Plugin::Authorization::Roles)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Class::DBI)
BuildRequires:	perl(DBI)
BuildRequires:  perl(DBIx::Class)
BuildRequires:	perl(Set::Object) >= 1.14
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
Provides:	perl-%{upstream_name}
Obsoletes:	perl-%{upstream_name}
BuildArch:	noarch
Buildroot:	%_tmppath/%{name}-%{version}-%{release}

%description
This Catalyst plugin uses a DBIx::Class (or Class::DBI) object to
authenticate a user.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%perl_vendorlib/Catalyst
%_mandir/*/*

