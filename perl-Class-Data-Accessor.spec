%define module	Class-Data-Accessor
%define name	perl-%{module}
%define modprefix Class
%define version	0.03
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Inheritable, overridable class and instance data accessor creation
License:	Artistic/GPL
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Carp)
Buildrequires:  perl(Module::Build)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Class::Data::Accessor is the marriage of Class::Accessor and
Class::Data::Inheritable into a single module. It is used for creating
accessors to class data that overridable in subclasses as well as in
class instances.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}


