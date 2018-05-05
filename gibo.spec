Name: gibo
Version: 1.0.6
Release: 1%{?dist}
Summary: A shell script for easily accessing gitignore boilerplates
Group: Development
License: Unlicense
URL: https://github.com/simonwhitaker/gibo
Source0: https://github.com/simonwhitaker/gibo/archive/%{version}.tar.gz
# See https://github.com/simonwhitaker/gibo/pull/24
Patch0: 0001-Remove-broken-she-bang-line.patch
BuildArch: noarch

%description
gibo (short for .gitignore boilerplates) is a shell script to help you easily
access .gitignore boilerplates from github.com/github/gitignore.

%package bash-completion
Summary: Bash tab-completion scripts for gibo
Requires: bash-completion

%description bash-completion
Install this package if you want intelligent bash tab-completion for gibo.

%package zsh-completion
Summary: Bash tab-completion scripts for gibo
Requires: zsh

%description zsh-completion
Install this package if you want intelligent zsh tab-completion for gibo.

%global debug_package %{nil}

%prep
%setup -q
%patch0 -p1

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{name} %{buildroot}/%{_bindir}
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
install -p gibo-completion.bash %{buildroot}%{_datarootdir}/bash-completion/completions/gibo
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions
install -p -m 644 gibo-completion.zsh %{buildroot}%{_datarootdir}/zsh/site-functions/_gibo

%files
%doc README.md UNLICENSE
%{_bindir}/%{name}

%files bash-completion
%{_datarootdir}/bash-completion/completions/gibo

%files zsh-completion
%{_datarootdir}/zsh/site-functions/_gibo

%changelog
