#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	TableHash
Summary:	DBIx::TableHash - Tie a hash to a mysql table + SQL utils
Summary(pl):	DBIx::TableHash - powi±zanie hasza z tabel± mysql oraz narzêdzia SQL
Name:		perl-DBIx-TableHash
Version:	1.04
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-DBI
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DBHash object is designed to tie a hash to a table or a subset of
records in a table in a DBI database (only tested with mysql in the
current version, but expected to work with any vendor).

%description -l pl
Obiekt DBHash s³u¿y do powi±zania hasza z tabel± lub podzbiorem
rekordów w tabeli w bazie danych DBI (testowane tylko z aktualn±
wersj± mysql, ale powinno dzia³aæ z ka¿d± baz±).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
