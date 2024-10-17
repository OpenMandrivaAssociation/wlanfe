%define name	wlanfe
%define version	1.0.1
%define release 8

Name: 	 	%{name}
Summary: 	Wireless lan configuration tool
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		https://se.rious.net/wlanfe.php
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

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-7mdv2010.0
+ Revision: 434755
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-6mdv2009.0
+ Revision: 262002
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-5mdv2009.0
+ Revision: 256032
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-3mdv2008.1
+ Revision: 135463
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import wlanfe


* Sat Jul 17 2004 Austin Acton <austin@mandrake.org> 1.0.1-3mdk
- fix buildrequires
- new menu

* Wed Apr 23 2003 Austin Acton <aacton@yorku.ca> 1.0.1-2mdk
- fix requires gksu

* Wed Apr 9 2003 Austin Acton <aacton@yorku.ca> 1.0.1-1mdk
- initial package
