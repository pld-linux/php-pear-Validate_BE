%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	BE
%define		_status		beta
%define		_pearname	Validate_BE

Summary:	%{_pearname} - Validation class for Belgium
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Belgii
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	3
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	17c86b481351c3a6014345aa7bc1e670
URL:		http://pear.php.net/package/Validate_BE/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-common >= 3:4.2.0
Requires:	php-pear-Validate >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for Belgium such as:
- Postal Code
- Bank Account Number
- Structured Bank Transfer message (National transfer from one bank
  account to another)
- VAT
- National ID
- Identity Card Number (not ready)
- SIS CARD ID (belgian "sacurita sociale" ID)

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Belgii danych takich jak:
- kod pocztowy
- numer konta bankowego
- wiadomość Structured Bank Transfer (transfer między dwoma bankami
  krajowymi)
- VAT
- narodowy numer identyfikacyjny (National ID)
- numer dowodu osobistego
- SIS CARD ID

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/docs/Validate_BE.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/BE.php
%dir %{php_pear_dir}/data/Validate_BE
%{php_pear_dir}/data/Validate_BE/BE_postcodes.txt

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
