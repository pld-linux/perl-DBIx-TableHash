#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	TableHash
Summary:	DBIx::TableHash - Tie a hash to a MySQL table + SQL utils
Summary(pl.UTF-8):	DBIx::TableHash - powiązanie hasza z tabelą MySQL oraz narzędzia SQL
Name:		perl-DBIx-TableHash
Version:	1.04
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83106f75a33d37b0685ded08322711ba
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-DBI
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DBHash object is designed to tie a hash to a table or a subset of
records in a table in a DBI database (only tested with MySQL in the
current version, but expected to work with any vendor).

%description -l pl.UTF-8
Obiekt DBHash służy do powiązania hasza z tabelą lub podzbiorem
rekordów w tabeli w bazie danych DBI (testowane tylko z aktualną
wersją MySQL, ale powinno działać z każdą bazą).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
