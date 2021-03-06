#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Module
%define	pnam	Pluggable-Fast
Summary:	Module::Pluggable::Fast - Fast plugins with instantiation
Summary(pl.UTF-8):	Module::Pluggable::Fast - szybkie wtyczki z tworzeniem instancji
Name:		perl-Module-Pluggable-Fast
Version:	0.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e0eeb561a04bb4f28a4f06774bf315f2
URL:		http://search.cpan.org/dist/Module-Pluggable-Fast/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-UNIVERSAL-require
%endif
Requires:	perl-dirs >= 1.0-5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is similar to Module::Pluggable but instantiates plugins
as soon as they're found, useful for code generators like
Class::DBI::Loader.

%description -l pl.UTF-8
Ten moduł jest podobny do Module::Pluggable, ale tworzy instancje
wtyczek zaraz po znalezieniu ich, co jest przydatne dla generatorów
kodu, takich jak Class::DBI::Loader.

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
%doc Changes README
%{perl_vendorlib}/Module/Pluggable/*.pm
%{_mandir}/man3/*
