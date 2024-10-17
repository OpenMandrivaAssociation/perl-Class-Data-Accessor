%define upstream_name	Class-Data-Accessor
%define upstream_version	0.04004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Inheritable, overridable class and instance data accessor creation
License:	Artistic/GPL
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildArch:	noarch

%description
Class::Data::Accessor is the marriage of Class::Accessor and
Class::Data::Inheritable into a single module. It is used for creating
accessors to class data that overridable in subclasses as well as in
class instances.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Class

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.40.40-3mdv2011.0
+ Revision: 680816
- mass rebuild

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.40-2mdv2011.0
+ Revision: 552188
- rebuild

* Sun Jul 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.40-1mdv2010.0
+ Revision: 395092
- update to 0.04004
- using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.03-4mdv2009.0
+ Revision: 241176
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-2mdv2008.0
+ Revision: 86082
- rebuild


* Wed May 24 2006 Scott Karns <scottk@mandriva.org> 0.03-1mdk
- Updated to 0.03

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-2mdk
- Add BuildRequires

* Tue May 02 2006 Scott Karns <scottk@mandriva.org> 0.02-1mdk
- First Mandriva release

