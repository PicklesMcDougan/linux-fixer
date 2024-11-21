Name:           linux-fixer 
Version:        1.0
Release:        1%{?dist}
Summary:        Fixes all linux

License:        GPL
URL:            https://github.com/PicklesMcDougan/linux-fixer
Source0:        linux-fixer.tar.bz2

%description
A wonderful tool to fix any linux issues

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 linux-fixer.py %{buildroot}%{_bindir}/linux-fixer.py

%files
%{_bindir}/linux-fixer.py


%changelog
* Wed Nov 20 2024 John Castranio <jcastran@redhat.com>
- 
