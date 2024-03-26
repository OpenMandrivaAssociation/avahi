# pulseaudio uses avahi, wine uses pulseaudio
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define client_name %{name}-client
%define common_name %{name}-common
%define core_name %{name}-core
%define dns_sd_name %{name}-compat-libdns_sd
%define glib_name %{name}-glib
%define gobject_name %{name}-gobject
%define howl_name %{name}-compat-howl
%define libevent_name %{name}-libevent
%define qt5_name %{name}-qt5
%define ui_gtk3_name %{name}-ui-gtk3

%define client_major 3
%define common_major 3
%define core_major 7
%define dns_sd_major 1
%define glib_major 1
%define gobject_major 0
%define howl_major 0
%define libevent_major 1
%define qt5_major 1
%define ui_major 0
%define ui_gtk3_major 0

%define lib_client_name %mklibname %{client_name} %{client_major}
%define develnameclient %mklibname %{client_name} -d
%define lib_common_name %mklibname %{common_name} %{common_major}
%define develnamecommon %mklibname %{common_name} -d
%define lib_core_name %mklibname %{core_name} %{core_major}
%define develnamecore %mklibname %{core_name} -d
%define lib_dns_sd_name %mklibname %{dns_sd_name} %{dns_sd_major}
%define develnamedns_sd %mklibname %{dns_sd_name} -d
%define lib_glib_name %mklibname %{glib_name} %{glib_major}
%define develnameglib %mklibname %{glib_name} -d
%define lib_gobject_name %mklibname %{gobject_name} %{gobject_major}
%define develnamegobject %mklibname %{gobject_name} -d
%define lib_howl_name %mklibname %{howl_name} %{howl_major}
%define develnamehowl %mklibname %{howl_name} -d
%define lib_libevent_name %mklibname %{libevent_name}_ %{libevent_major}
%define develnamelibevent %mklibname %{libevent_name} -d
%define lib_qt5_name %mklibname %{qt5_name}_ %{qt5_major}
%define develnameqt5 %mklibname %{qt5_name} -d
%define lib_ui_gtk3_name %mklibname %{ui_gtk3_name}_ %{ui_gtk3_major}
%define develnameui_gtk3 %mklibname %{ui_gtk3_name} -d

%define lib32_client_name %mklib32name %{client_name} %{client_major}
%define devel32nameclient %mklib32name %{client_name} -d
%define lib32_common_name %mklib32name %{common_name} %{common_major}
%define devel32namecommon %mklib32name %{common_name} -d
%define lib32_core_name %mklib32name %{core_name} %{core_major}
%define devel32namecore %mklib32name %{core_name} -d
%define lib32_dns_sd_name %mklib32name %{dns_sd_name} %{dns_sd_major}
%define devel32namedns_sd %mklib32name %{dns_sd_name} -d
%define lib32_glib_name %mklib32name %{glib_name} %{glib_major}
%define devel32nameglib %mklib32name %{glib_name} -d
%define lib32_gobject_name %mklib32name %{gobject_name} %{gobject_major}
%define devel32namegobject %mklib32name %{gobject_name} -d
%define lib32_howl_name %mklib32name %{howl_name} %{howl_major}
%define devel32namehowl %mklib32name %{howl_name} -d
%define lib32_libevent_name %mklib32name %{libevent_name}_ %{libevent_major}
%define devel32namelibevent %mklib32name %{libevent_name} -d

%ifnarch %{arm} %{mips} aarch64 %{ix86} riscv64
%bcond_with mono
%else
%bcond_with mono
%endif

%bcond_without gtk3
%bcond_with python

Summary:	Avahi service discovery (mDNS/DNS-SD) suite
Name:		avahi
Version:	0.8
Release:	18
License:	LGPLv2+
Group:		System/Servers
Url:		https://avahi.org/
Source0:	https://avahi.org/download/%{name}-%{version}.tar.gz
Source1:	avahi-hostname.sh
Source2:	%{name}.sysusers
Source100:	%{name}.rpmlintrc
Patch0:		avahi-0.6.31-gtk-is-broken-beyond-repair-gtk-die-die-die.patch
Patch1:		avahi-0.6.31.workaround.patch
Patch2:		avahi-0.8-fix-avahi-libevent.pc.in.patch
Patch3:		0006-avahi-dnsconfd.service-Drop-Also-avahi-daemon.socket.patch
Patch4:		0010-fix-bytestring-decoding-for-proper-display.patch
Patch5:		0011-avahi_dns_packet_consume_uint32-fix-potential-undefi.patch
Patch6:		https://github.com/lathiat/avahi/commit/9d31939e55280a733d930b15ac9e4dda4497680c.patch
BuildRequires:	intltool
BuildRequires:	doxygen
BuildRequires:	xmltoman
BuildRequires:	graphviz
BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(expat)
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libevent)
%if %{with python}
BuildRequires:	pkgconfig(dbus-python)
%endif
BuildRequires:	pkgconfig(libdaemon)
BuildRequires:	pkgconfig(Qt5Core)
%if %{with gtk3}
BuildRequires:	pkgconfig(gtk+-3.0)
%endif
BuildRequires:	pkgconfig(libsystemd)
# For _presetdir and friends
BuildRequires:	systemd-rpm-macros
%if %{with compat32}
#BuildRequires:	devel(libintl)
BuildRequires:	devel(libexpat)
BuildRequires:	devel(libdbus-1)
BuildRequires:	devel(libsystemd)
BuildRequires:	devel(libevent-2.1)
BuildRequires:	devel(libgdbm)
BuildRequires:	devel(libdaemon)
BuildRequires:	devel(libglib-2.0)
BuildRequires:	devel(libffi)
BuildRequires:	devel(libcap)
%endif
%systemd_requires
Requires(post,preun): dbus
Requires(pre):	glibc
Requires(pre):	shadow
Requires(pre):	passwd
Requires:	nss_mdns

%description
Avahi is a system which facilitates service discovery on a local
network -- this means that you can plug your laptop or computer into a
network and instantly be able to view other people who you can chat
with, find printers to print to or find files being shared. This kind
of technology is already found in MacOS X (branded 'Rendezvous',
'Bonjour' and sometimes 'ZeroConf') and is very convenient.

%files -f avahi.lang
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/services
%config(noreplace) %{_sysconfdir}/%{name}/hosts
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-daemon.conf
%config(noreplace) %{_sysconfdir}/%{name}/avahi-autoipd.action
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/%{name}-dbus.conf
%attr(0755,avahi,avahi) %dir %{_localstatedir}/lib/avahi
%{_sysconfdir}/sysconfig/network-scripts/hostname.d/avahi
%{_bindir}/%{name}-browse
%{_bindir}/%{name}-browse-domains
%{_bindir}/%{name}-publish
%{_bindir}/%{name}-publish-address
%{_bindir}/%{name}-publish-service
%{_bindir}/%{name}-resolve
%{_bindir}/%{name}-resolve-address
%{_bindir}/%{name}-resolve-host-name
%{_bindir}/%{name}-set-host-name
%{_sbindir}/%{name}-daemon
%{_sbindir}/avahi-autoipd
%{_datadir}/%{name}/%{name}-service.dtd
%{_datadir}/dbus-1/interfaces/*.xml
%doc %{_mandir}/man1/%{name}-browse-domains.1*
%doc %{_mandir}/man1/%{name}-browse.1*
%doc %{_mandir}/man1/%{name}-publish.1*
%doc %{_mandir}/man1/%{name}-publish-address.1*
%doc %{_mandir}/man1/%{name}-publish-service.1*
%doc %{_mandir}/man1/%{name}-resolve.1*
%doc %{_mandir}/man1/%{name}-resolve-address.1*
%doc %{_mandir}/man1/%{name}-resolve-host-name.1*
%doc %{_mandir}/man1/%{name}-set-host-name.1*
%doc %{_mandir}/man5/%{name}-daemon.conf.5*
%doc %{_mandir}/man5/%{name}.hosts.5*
%doc %{_mandir}/man5/%{name}.service.5*
%doc %{_mandir}/man8/%{name}-daemon.8*
%doc %{_mandir}/man8/avahi-autoipd*
%dir %{_libdir}/avahi
%if %{with python}
%{_libdir}/avahi/service-types.db
%endif
%{_presetdir}/86-avahi-daemon.preset
%{_unitdir}/avahi-daemon.service
%{_unitdir}/avahi-daemon.socket
%{_sysusersdir}/%{name}.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -d %{_localstatedir}/lib/avahi -s /bin/false -c "Avahi mDNS/DNS-SD daemon" %{name}

getent group %{name}-autoipd >/dev/null || groupadd -r %{name}-autoipd
getent passwd %{name}-autoipd >/dev/null || useradd -r -g %{name}-autoipd -d %{_localstatedir}/lib/avahi -s /bin/false -c "Avahi IPv4LL daemon" %{name}-autoipd

exit 0

%post
%systemd_post avahi-daemon.socket

%preun
%systemd_preun avahi-daemon.socket

%postun
%systemd_postun_with_restart avahi-daemon.socket

#----------------------------------------------------------------------------

%package dnsconfd
Summary:	Avahi DNS configuration server
Group:		System/Servers
Requires:	%{name} = %{EVRD}
Conflicts:	avahi < 0.6.31-8

%description dnsconfd
avahi-dnsconfd is a small daemon which may be used to configure
conventional DNS servers using mDNS in a DHCP-like fashion.
Especially useful on IPv6.

%post dnsconfd
%systemd_post avahi-dnsconfd.service

%preun dnsconfd
%systemd_preun avahi-dnsconfd.service

%postun dnsconfd
%systemd_postun_with_restart avahi-dnsconfd.service

%files dnsconfd
%{_sysconfdir}/%{name}/%{name}-dnsconfd.action
%{_presetdir}/86-avahi-dnsconfd.preset
%{_unitdir}/avahi-dnsconfd.service
%{_sbindir}/%{name}-dnsconfd
%doc %{_mandir}/man8/%{name}-dnsconfd.8*
%doc %{_mandir}/man8/%{name}-dnsconfd.action.8*

#----------------------------------------------------------------------------

%if %{with gtk3}
%package x11
Summary:	Graphical tools for Avahi
Group:		System/Servers
Requires:	%{name} = %{EVRD}

%description x11
Graphical tools for Avahi.
It includes avahi-discover-standalone.

%files x11
%{_bindir}/%{name}-discover-standalone
%{_bindir}/bshell
%{_bindir}/bssh
%{_bindir}/bvnc
%{_datadir}/applications/bssh.desktop
%{_datadir}/applications/bvnc.desktop
%{_datadir}/%{name}/interfaces/%{name}-discover.ui
%if %{with python}
%{_datadir}/applications/%{name}-discover.desktop
%endif
%endif

#----------------------------------------------------------------------------

%if %{with python}
%package python
Summary:	Python bindings and utilities for Avahi
Group:		System/Libraries
Requires:	pygtk2.0-libglade
Requires:	python-twisted-core
Requires:	python-twisted-web
Requires:	python-dbus
Requires:	%{name}
Requires:	%{name}-x11

%description python
Python bindings and utilities for Avahi.
It includes avahi-bookmarks and avahi-discover.

%files python
%{_bindir}/%{name}-bookmarks
%{_bindir}/%{name}-discover
%{py_puresitedir}/%{name}/*.py*
%{py_puresitedir}/avahi_discover/
%doc %{_mandir}/man1/%{name}-discover.1*
%doc %{_mandir}/man1/%{name}-bookmarks.1*
%endif

#----------------------------------------------------------------------------

%if %{with mono}
%package sharp
Summary:	Mono bindings for Avahi
Group:		System/Libraries
BuildRequires:	mono-tools
BuildRequires:	mono-devel
BuildRequires:	pkgconfig(gtk-sharp-2.0)
#gw this is needed by mono-find-requires:
#BuildRequires:	avahi-ui-devel
Requires:	%{lib_client_name} = %{EVRD}
Requires:	%{lib_common_name} = %{EVRD}
Requires:	%{lib_glib_name} = %{EVRD}

%description sharp
Mono bindings for Avahi.

%files sharp
%{_prefix}/lib/mono/%{name}-sharp/%{name}-sharp.dll
%{_prefix}/lib/mono/gac/%{name}-sharp/
%{_libdir}/pkgconfig/%{name}-sharp.pc
%{_prefix}/lib/mono/%{name}-ui-sharp/%{name}-ui-sharp.dll
%{_prefix}/lib/mono/gac/%{name}-ui-sharp/
%{_libdir}/pkgconfig/%{name}-ui-sharp.pc
%endif

#----------------------------------------------------------------------------

%if %{with mono}
%package sharp-doc
Summary:	Development documentation for avahi-sharp
Group:		Development/Other
Requires(post,postun):	mono-tools

%description sharp-doc
This package contains the API documentation for the avahi-sharp in
Monodoc format.

%files sharp-doc
%{_usr}/lib/monodoc/sources/%{name}-sharp-docs.source
%{_usr}/lib/monodoc/sources/%{name}-sharp-docs.tree
%{_usr}/lib/monodoc/sources/%{name}-sharp-docs.zip
%{_usr}/lib/monodoc/sources/%{name}-ui-sharp-docs.source
%{_usr}/lib/monodoc/sources/%{name}-ui-sharp-docs.tree
%{_usr}/lib/monodoc/sources/%{name}-ui-sharp-docs.zip

%post sharp-doc
%{_bindir}/monodoc --make-index > /dev/null

%postun sharp-doc
if [ "$1" = "0" ] && [ -x %{_bindir}/monodoc ]; then
    %{_bindir}/monodoc --make-index > /dev/null
fi

%endif

#----------------------------------------------------------------------------

%package -n %{lib_client_name}
Summary:	Library for avahi-client
Group:		System/Libraries

%description -n %{lib_client_name}
Library for avahi-client.

%files -n %{lib_client_name}
%{_libdir}/lib%{name}-client.so.%{client_major}*

#----------------------------------------------------------------------------

%package -n %{develnameclient}
Summary:	Devel library for avahi-client
Group:		Development/C
Requires:	%{lib_client_name} = %{EVRD}
Requires:	%{develnamecommon} = %{EVRD}
Provides:	%{client_name}-devel = %{EVRD}

%description -n %{develnameclient}
Devel library for avahi-client.

%files -n %{develnameclient}
%{_includedir}/%{name}-client
%{_libdir}/lib%{name}-client.so
%{_libdir}/pkgconfig/%{name}-client.pc

#----------------------------------------------------------------------------

%package -n %{lib_common_name}
Summary:	Library for avahi-common
Group:		System/Libraries

%description -n %{lib_common_name}
Library for avahi-common.

%files -n %{lib_common_name}
%{_libdir}/lib%{name}-common.so.%{common_major}*

#----------------------------------------------------------------------------

%package -n %{develnamecommon}
Summary:	Devel library for avahi-common
Group:		Development/C
Requires:	%{lib_common_name} = %{EVRD}
Provides:	%{common_name}-devel = %{EVRD}

%description -n %{develnamecommon}
Devel library for avahi-common.

%files -n %{develnamecommon}
%{_includedir}/%{name}-common
%{_libdir}/lib%{name}-common.so

#----------------------------------------------------------------------------

%package -n %{lib_core_name}
Summary:	Library for avahi-core
Group:		System/Libraries

%description -n %{lib_core_name}
Library for avahi-core.

%files -n %{lib_core_name}
%{_libdir}/lib%{name}-core.so.%{core_major}*

#----------------------------------------------------------------------------

%package -n %{develnamecore}
Summary:	Devel library for avahi-core
Group:		Development/C
Requires:	%{lib_core_name} = %{EVRD}
Requires:	%{develnamecommon} = %{EVRD}
Provides:	%{core_name}-devel = %{EVRD}

%description -n %{develnamecore}
Devel library for avahi-core.

%files -n %{develnamecore}
%{_includedir}/%{name}-core
%{_libdir}/lib%{name}-core.so
%{_libdir}/pkgconfig/%{name}-core.pc

#----------------------------------------------------------------------------

%package -n %{lib_dns_sd_name}
Summary:	Avahi compatibility library for libdns_sd
Group:		System/Libraries

%description -n %{lib_dns_sd_name}
Avahi compatibility library for libdns_sd.

%files -n %{lib_dns_sd_name}
%{_libdir}/libdns_sd.so.%{dns_sd_major}*

#----------------------------------------------------------------------------

%package -n %{develnamedns_sd}
Summary:	Avahi devel compatibility library for libdns_sd
Group:		Development/C
Requires:	%{lib_dns_sd_name} = %{EVRD}
Requires:	%{develnameclient} = %{EVRD}
Provides:	%{dns_sd_name}-devel = %{EVRD}

%description -n %{develnamedns_sd}
Avahi devel compatibility library for libdns_sd.

%files -n %{develnamedns_sd}
%{_includedir}/%{name}-compat-libdns_sd
%{_libdir}/libdns_sd.so
%{_libdir}/pkgconfig/%{name}-compat-libdns_sd.pc
%{_libdir}/pkgconfig/libdns_sd.pc

#----------------------------------------------------------------------------

%package -n %{lib_glib_name}
Summary:	Library for avahi-glib
Group:		System/Libraries

%description -n %{lib_glib_name}
Library for avahi-glib.

%files -n %{lib_glib_name}
%{_libdir}/lib%{name}-glib.so.%{glib_major}*

#----------------------------------------------------------------------------

%package -n %{develnameglib}
Summary:	Devel library for avahi-glib
Group:		Development/C
Requires:	%{lib_glib_name} = %{EVRD}
Requires:	%{develnamecommon} = %{EVRD}
Provides:	%{glib_name}-devel = %{EVRD}

%description -n %{develnameglib}
Devel library for avahi-glib.

%files -n %{develnameglib}
%{_includedir}/%{name}-glib
%{_libdir}/lib%{name}-glib.so
%{_libdir}/pkgconfig/%{name}-glib.pc

#----------------------------------------------------------------------------

%package -n %{lib_gobject_name}
Summary:	Library for avahi-gobject
Group:		System/Libraries

%description -n %{lib_gobject_name}
Library for avahi-gobject.

%files -n %{lib_gobject_name}
%{_libdir}/lib%{name}-gobject.so.%{gobject_major}*

#----------------------------------------------------------------------------

%package -n %{develnamegobject}
Summary:	Devel library for avahi-gobject
Group:		Development/C
Requires:	%{lib_gobject_name} = %{EVRD}
Requires:	%{develnameglib} = %{EVRD}
Provides:	%{gobject_name}-devel = %{EVRD}

%description -n %{develnamegobject}
Devel library for avahi-gobject.

%files -n %{develnamegobject}
%{_includedir}/%{name}-gobject
%{_libdir}/lib%{name}-gobject.so
%{_libdir}/pkgconfig/%{name}-gobject.pc

#----------------------------------------------------------------------------

%package -n %{lib_howl_name}
Summary:	Avahi compatibility library for howl
Group:		System/Libraries

%description -n %{lib_howl_name}
Avahi compatibility library for howl.

%files -n %{lib_howl_name}
%{_libdir}/libhowl.so.%{howl_major}*

#----------------------------------------------------------------------------

%package -n %{develnamehowl}
Summary:	Avahi devel compatibility library for libdns_sd for howl
Group:		Development/C
Requires:	%{lib_howl_name} = %{EVRD}
Requires:	%{develnamecore} = %{EVRD}
Provides:	%{howl_name}-devel = %{EVRD}

%description -n %{develnamehowl}
Avahi devel compatibility library for libdns_sd for howl.

%files -n %{develnamehowl}
%{_includedir}/%{name}-compat-howl
%{_libdir}/libhowl.so
%{_libdir}/pkgconfig/%{name}-compat-howl.pc
%{_libdir}/pkgconfig/howl.pc

#----------------------------------------------------------------------------

%package -n %{lib_libevent_name}
Summary:	Library for avahi-libevent
Group:		System/Libraries

%description -n %{lib_libevent_name}
Library for avahi-libevent.

%files -n %{lib_libevent_name}
%{_libdir}/lib%{name}-libevent.so.%{libevent_major}*

%package -n %{develnamelibevent}
Summary:	Devel library for avahi-libevent
Group:		Development/C
Provides:	%{libevent_name}-devel = %{EVRD}
Requires:	%{lib_libevent_name} = %{EVRD}
Requires:	%{develnamecore} = %{EVRD}

%description -n %{develnamelibevent}
Devel library for avahi-libevent.

%files -n %{develnamelibevent}
%{_includedir}/%{name}-libevent
%{_libdir}/lib%{name}-libevent.so
%{_libdir}/pkgconfig/%{name}-libevent.pc

#----------------------------------------------------------------------------

%package -n %{lib_qt5_name}
Summary:	Library for avahi-qt5
Group:		System/Libraries

%description -n %{lib_qt5_name}
Library for avahi-qt5.

%files -n %{lib_qt5_name}
%{_libdir}/lib%{name}-qt5.so.%{qt5_major}*

%package -n %{develnameqt5}
Summary:	Devel library for avahi-qt5
Group:		Development/C
Provides:	%{qt5_name}-devel = %{EVRD}
Requires:	%{lib_qt5_name} = %{EVRD}
Requires:	%{develnamecore} = %{EVRD}

%description -n %{develnameqt5}
Devel library for avahi-qt5.

%files -n %{develnameqt5}
%{_includedir}/%{name}-qt5
%{_libdir}/lib%{name}-qt5.so
%{_libdir}/pkgconfig/%{name}-qt5.pc

#----------------------------------------------------------------------------

%if %{with gtk3}
%package -n %{lib_ui_gtk3_name}
Summary:	Library for avahi-gtk3
Group:		System/Libraries

%description -n %{lib_ui_gtk3_name}
Library for avahi-gtk3.

%files -n %{lib_ui_gtk3_name}
%{_libdir}/lib%{name}-ui-gtk3.so.%{ui_gtk3_major}*

#----------------------------------------------------------------------------

%package -n %{develnameui_gtk3}
Summary:	Devel library for avahi-gtk3
Group:		Development/C
Requires:	%{lib_ui_gtk3_name} = %{EVRD}
Requires:	%{develnamecommon} = %{EVRD}
Provides:	%{ui_gtk3_name}-devel = %{EVRD}

%description -n %{develnameui_gtk3}
Devel library for avahi-gtk3.

%files -n %{develnameui_gtk3}
%{_includedir}/avahi-ui/avahi-ui.h
%{_libdir}/libavahi-ui-gtk3.so
%{_libdir}/pkgconfig/avahi-ui-gtk3.pc
%endif

#----------------------------------------------------------------------------

%if %{with compat32}
%package -n %{lib32_client_name}
Summary:	Library for avahi-client (32-bit)
Group:		System/Libraries

%description -n %{lib32_client_name}
Library for avahi-client.

%files -n %{lib32_client_name}
%{_prefix}/lib/lib%{name}-client.so.%{client_major}*

#----------------------------------------------------------------------------

%package -n %{devel32nameclient}
Summary:	Devel library for avahi-client (32-bit)
Group:		Development/C
Requires:	%{lib32_client_name} = %{EVRD}
Requires:	%{devel32namecommon} = %{EVRD}
Requires:	%{develnameclient} = %{EVRD}

%description -n %{devel32nameclient}
Devel library for avahi-client.

%files -n %{devel32nameclient}
%{_prefix}/lib/lib%{name}-client.so
%{_prefix}/lib/pkgconfig/%{name}-client.pc

#----------------------------------------------------------------------------

%package -n %{lib32_common_name}
Summary:	Library for avahi-common (32-bit)
Group:		System/Libraries

%description -n %{lib32_common_name}
Library for avahi-common.

%files -n %{lib32_common_name}
%{_prefix}/lib/lib%{name}-common.so.%{common_major}*

#----------------------------------------------------------------------------

%package -n %{devel32namecommon}
Summary:	Devel library for avahi-common (32-bit)
Group:		Development/C
Requires:	%{develnamecommon} = %{EVRD}
Requires:	%{lib32_common_name} = %{EVRD}

%description -n %{devel32namecommon}
Devel library for avahi-common.

%files -n %{devel32namecommon}
%{_prefix}/lib/lib%{name}-common.so

#----------------------------------------------------------------------------

%package -n %{lib32_core_name}
Summary:	Library for avahi-core (32-bit)
Group:		System/Libraries

%description -n %{lib32_core_name}
Library for avahi-core.

%files -n %{lib32_core_name}
%{_prefix}/lib/lib%{name}-core.so.%{core_major}*

#----------------------------------------------------------------------------

%package -n %{devel32namecore}
Summary:	Devel library for avahi-core (32-bit)
Group:		Development/C
Requires:	%{develnamecore} = %{EVRD}
Requires:	%{lib32_core_name} = %{EVRD}
Requires:	%{devel32namecommon} = %{EVRD}

%description -n %{devel32namecore}
Devel library for avahi-core.

%files -n %{devel32namecore}
%{_prefix}/lib/lib%{name}-core.so
%{_prefix}/lib/pkgconfig/%{name}-core.pc

#----------------------------------------------------------------------------

%package -n %{lib32_dns_sd_name}
Summary:	Avahi compatibility library for libdns_sd (32-bit)
Group:		System/Libraries

%description -n %{lib32_dns_sd_name}
Avahi compatibility library for libdns_sd.

%files -n %{lib32_dns_sd_name}
%{_prefix}/lib/libdns_sd.so.%{dns_sd_major}*

#----------------------------------------------------------------------------

%package -n %{devel32namedns_sd}
Summary:	Avahi devel compatibility library for libdns_sd (32-bit)
Group:		Development/C
Requires:	%{lib32_dns_sd_name} = %{EVRD}
Requires:	%{devel32nameclient} = %{EVRD}
Requires:	%{develnamedns_sd} = %{EVRD}

%description -n %{devel32namedns_sd}
Avahi devel compatibility library for libdns_sd.

%files -n %{devel32namedns_sd}
%{_prefix}/lib/libdns_sd.so
%{_prefix}/lib/pkgconfig/%{name}-compat-libdns_sd.pc
%{_prefix}/lib/pkgconfig/libdns_sd.pc

#----------------------------------------------------------------------------

%package -n %{lib32_glib_name}
Summary:	Library for avahi-glib (32-bit)
Group:		System/Libraries

%description -n %{lib32_glib_name}
Library for avahi-glib.

%files -n %{lib32_glib_name}
%{_prefix}/lib/lib%{name}-glib.so.%{glib_major}*

#----------------------------------------------------------------------------

%package -n %{devel32nameglib}
Summary:	Devel library for avahi-glib (32-bit)
Group:		Development/C
Requires:	%{develnameglib} = %{EVRD}
Requires:	%{lib32_glib_name} = %{EVRD}
Requires:	%{devel32namecommon} = %{EVRD}

%description -n %{devel32nameglib}
Devel library for avahi-glib.

%files -n %{devel32nameglib}
%{_prefix}/lib/lib%{name}-glib.so
%{_prefix}/lib/pkgconfig/%{name}-glib.pc

#----------------------------------------------------------------------------

%package -n %{lib32_gobject_name}
Summary:	Library for avahi-gobject (32-bit)
Group:		System/Libraries

%description -n %{lib32_gobject_name}
Library for avahi-gobject.

%files -n %{lib32_gobject_name}
%{_prefix}/lib/lib%{name}-gobject.so.%{gobject_major}*

#----------------------------------------------------------------------------

%package -n %{devel32namegobject}
Summary:	Devel library for avahi-gobject (32-bit)
Group:		Development/C
Requires:	%{develnamegobject} = %{EVRD}
Requires:	%{lib32_gobject_name} = %{EVRD}
Requires:	%{devel32nameglib} = %{EVRD}

%description -n %{devel32namegobject}
Devel library for avahi-gobject.

%files -n %{devel32namegobject}
%{_prefix}/lib/lib%{name}-gobject.so
%{_prefix}/lib/pkgconfig/%{name}-gobject.pc

#----------------------------------------------------------------------------

%package -n %{lib32_howl_name}
Summary:	Avahi compatibility library for howl (32-bit)
Group:		System/Libraries

%description -n %{lib32_howl_name}
Avahi compatibility library for howl.

%files -n %{lib32_howl_name}
%{_prefix}/lib/libhowl.so.%{howl_major}*

#----------------------------------------------------------------------------

%package -n %{devel32namehowl}
Summary:	Avahi devel compatibility library for libdns_sd for howl (32-bit)
Group:		Development/C
Requires:	%{develnamehowl} = %{EVRD}
Requires:	%{lib32_howl_name} = %{EVRD}
Requires:	%{devel32namecore} = %{EVRD}

%description -n %{devel32namehowl}
Avahi devel compatibility library for libdns_sd for howl.

%files -n %{devel32namehowl}
%{_prefix}/lib/libhowl.so
%{_prefix}/lib/pkgconfig/%{name}-compat-howl.pc
%{_prefix}/lib/pkgconfig/howl.pc

#----------------------------------------------------------------------------

%package -n %{lib32_libevent_name}
Summary:	Library for avahi-libevent (32-bit)
Group:		System/Libraries

%description -n %{lib32_libevent_name}
Library for avahi-libevent.

%files -n %{lib32_libevent_name}
%{_prefix}/lib/lib%{name}-libevent.so.%{libevent_major}*

%package -n %{devel32namelibevent}
Summary:	Devel library for avahi-libevent (32-bit)
Group:		Development/C
Requires:	%{develnamelibevent} = %{EVRD}
Requires:	%{lib32_libevent_name} = %{EVRD}
Requires:	%{devel32namecore} = %{EVRD}

%description -n %{devel32namelibevent}
Devel library for avahi-libevent.

%files -n %{devel32namelibevent}
%{_prefix}/lib/lib%{name}-libevent.so
%{_prefix}/lib/pkgconfig/%{name}-libevent.pc
%endif

%prep
%autosetup -p1
cp %{SOURCE1} avahi-hostname.sh

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32 \
	--localstatedir=%{_var} \
	--disable-static \
	--with-xml=expat \
	--with-distro=mandriva \
	--disable-mono \
	--disable-qt3 \
	--disable-qt5 \
	--with-avahi-priv-access-group="avahi" \
	--enable-compat-libdns_sd \
	--enable-compat-howl \
	--enable-introspection=no \
	--with-systemdsystemunitdir=%{_unitdir} \
	--disable-gtk3 \
	--disable-gtk \
	--disable-python
cd ..
%endif

mkdir build
cd build
%configure \
	--localstatedir=%{_var} \
	--disable-static \
	--with-xml=expat \
	--with-distro=mandriva \
%if !%{with mono}
	--disable-mono \
%endif
	--disable-qt3 \
	--with-avahi-priv-access-group="avahi" \
	--enable-compat-libdns_sd \
	--enable-compat-howl \
	--enable-introspection=no \
	--with-systemdsystemunitdir=%{_unitdir} \
%if !%{with gtk3}
	--disable-gtk3 \
%endif
	--disable-gtk \
%if !%{with python}
	--disable-python
%endif


%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
ln -s avahi-compat-howl.pc %{buildroot}%{_prefix}/lib/pkgconfig/howl.pc
ln -s avahi-compat-libdns_sd.pc %{buildroot}%{_prefix}/lib/pkgconfig/libdns_sd.pc
%endif
%make_install -C build

mkdir -p %{buildroot}%{_localstatedir}/lib/avahi

ln -s avahi-compat-howl.pc %{buildroot}%{_libdir}/pkgconfig/howl.pc
ln -s avahi-compat-libdns_sd.pc %{buildroot}%{_libdir}/pkgconfig/libdns_sd.pc

%if "%{_lib}" != "lib" && %{with mono}
mkdir -p %{buildroot}%{_prefix}/lib
mv %{buildroot}%{_libdir}/mono %{buildroot}%{_prefix}/lib
perl -pi -e "s/%{_lib}/lib/" %{buildroot}%{_libdir}/pkgconfig/avahi-{,ui-}sharp.pc
%endif

# install hostname.d hook
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig/network-scripts/hostname.d/
install -m755 avahi-hostname.sh %{buildroot}/%{_sysconfdir}/sysconfig/network-scripts/hostname.d/avahi

install -D -m644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf

# (tpg) enable services
install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-avahi-daemon.preset << EOF
enable avahi-daemon.socket
EOF

cat > %{buildroot}%{_presetdir}/86-avahi-dnsconfd.preset << EOF
enable avahi-dnsconfd.service
EOF

# (tpg) remove this crap
rm -rf %{buildroot}%{_initrddir}/%{name}-daemon
rm -rf %{buildroot}%{_initrddir}/%{name}-dnsconfd

# remove example
rm -fv %{buildroot}%{_sysconfdir}/avahi/services/ssh.service
rm -fv %{buildroot}%{_sysconfdir}/avahi/services/sftp-ssh.service

%find_lang %{name}
