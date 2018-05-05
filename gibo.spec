Name: gibo
Version: 1.0.6
Release: 1%{?dist}
Summary: A shell script for easily accessing gitignore boilerplates
Group: Development
License: Unlicense
URL: https://github.com/simonwhitaker/gibo
Source0: https://github.com/simonwhitaker/gibo/archive/%{version}.tar.gz
BuildArch: noarch

%description
gibo (short for .gitignore boilerplates) is a shell script to help you easily
access .gitignore boilerplates from github.com/github/gitignore.

%global debug_package %{nil}

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{name} %{buildroot}/%{_bindir}

%files
%{_bindir}/%{name}

%changelog
