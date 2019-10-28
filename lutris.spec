Summary:	Lutris – open source gaming platform for GNU/Linux
Name:		lutris
Version:	0.5.1.2
Release:	2
License:	GPL v3
Group:		Applications
Source0:	https://lutris.net/releases/%{name}_%{version}.tar.xz
# Source0-md5:	ed2795994bf78f05816076ed634959e8
URL:		https://lutris.net/
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lutris is an open source gaming platform for GNU/Linux. It makes
gaming on Linux easier by taking care of managing, installing and
providing optimal settings for games.

Lutris does not sell games, you have to provide your own copy of the
games unless they are Open Source or Freeware. The games can be
installed anywhere you want on your system, the tool does not impose
anything.

Lutris relies on various programs referenced as 'runners' to provide a
vast library of games. These runners (with the exception of Steam and
Web browsers) are provided by Lutris, you don't need to install them
with your package manager.


%prep
%setup -q -n %{name}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README.rst
%attr(755,root,root) %{_bindir}/lutris
%attr(755,root,root) %{_bindir}/lutris-wrapper
%{_datadir}/metainfo/net.lutris.Lutris.appdata.xml
%{_desktopdir}/net.lutris.Lutris.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%attr(755,root,root) %{_datadir}/%{name}/bin/*
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/media
%{_datadir}/%{name}/ui
%{_datadir}/polkit-1/actions/net.lutris.*.policy
%{py3_sitescriptdir}/%{name}
%{py3_sitescriptdir}/%{name}-%{version}-py*.egg-info
