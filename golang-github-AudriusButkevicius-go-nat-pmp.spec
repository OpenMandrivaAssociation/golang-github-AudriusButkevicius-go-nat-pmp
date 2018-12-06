# https://github.com/AudriusButkevicius/go-nat-pmp
%global goipath github.com/AudriusButkevicius/go-nat-pmp
%global commit  452c97607362b2ab5a7839b8d1704f0396b640ca
%global date    20160522

%gometa

Name:           golang-github-AudriusButkevicius-go-nat-pmp
Version:        0
Release:        0.7%{?dist}
Summary:        Go language client for the NAT-PMP protocol
License:        ASL 2.0

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.7.20160522git452c976
- Use forgeautosetup instead of gosetup.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.20160522git452c976
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git452c976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git452c976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git452c976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git452c976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.git452c976
- First package for Fedora


