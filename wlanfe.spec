%define name	wlanfe
%define version	1.0.1
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Wireless lan configuration tool
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://se.rious.net/wlanfe.php
License:	GPL
Group:		System/Configuration/Networking
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk-devel
Requires:	gksu prism2-utils

%description
WlanFe is a GTK+ front end for the Linux WLAN-NG tools.
This allows you to control a wireless networkig card.

%prep
%setup -q

%build
%make CC="gcc $RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
cp %name %buildroot/%_bindir

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=gksu %{name}
Icon=networking_configuration_section
Name=WLanFE
Comment=Wireless LAN Configuration
Categories=Network;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop

