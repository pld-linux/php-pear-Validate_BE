%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	BE
%define		_status		alpha
%define		_pearname	Validate_BE

Summary:	%{_pearname} - Validation class for Belgium
Summary(pl):	%{_pearname} - Klasa sprawdzaj±ca poprawno¶æ dla Belgii
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	16955011605a140b1d58ea82821d8c54
URL:		http://pear.php.net/package/Validate_BE/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Pakiet do sprawdzania poprawno¶ci dla Belgii danych takich jak:
- kod pocztowy
- numer konta bankowego
- wiadomo¶æ Structured Bank Transfer (transfer miêdzy dwoma bankami
  krajowymi)
- VAT
- narodowy numer identyfikacyjny (National ID)
- numer dowodu osobistego
- SIS CARD ID

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/{LICENSE,docs/Validate_BE.txt}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/BE.php
%dir %{php_pear_dir}/data/Validate_BE
%{php_pear_dir}/data/Validate_BE/BE_postcodes.txt

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_BE/tests
