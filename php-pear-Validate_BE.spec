%define		_status		beta
%define		_pearname	Validate_BE
Summary:	%{_pearname} - Validation class for Belgium
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Belgii
Name:		php-pear-%{_pearname}
Version:	0.1.4
Release:	4
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4a9d0bc28d432b3ed2801ba729758c48
URL:		http://pear.php.net/package/Validate_BE/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
Obsoletes:	php-pear-Validate_BE-tests
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
%{php_pear_dir}/data/Validate_BE/package_BE.xml
