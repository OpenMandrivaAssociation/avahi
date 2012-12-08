%define client_name		%{name}-client
%define common_name		%{name}-common
%define core_name		%{name}-core
%define dns_sd_name		%{name}-compat-libdns_sd
%define glib_name		%{name}-glib
%define gobject_name	%{name}-gobject
%define howl_name		%{name}-compat-howl
%define qt3_name		%{name}-qt3
%define qt4_name		%{name}-qt4
%define ui_name			%{name}-ui
%define ui_gtk3_name	%{name}-ui-gtk3

%define dns_sd_old_name	mDNSResponder
%define howl_old_name	howl

%define client_major	3
%define common_major	3
%define core_major	7
%define dns_sd_major	1
%define glib_major	1
%define gobject_major	0
%define howl_major	0
%define qt3_major	1
%define qt4_major	1
%define ui_major	0
%define ui_gtk3_major	0

%define lib_client_name	%mklibname %{client_name} %{client_major}
%define develnameclient	%mklibname -d %{client_name}
%define lib_common_name	%mklibname %{common_name} %{common_major}
%define develnamecommon	%mklibname -d %{common_name}
%define lib_core_name	%mklibname %{core_name} %{core_major}
%define develnamecore	%mklibname -d %{core_name}
%define lib_dns_sd_name	%mklibname %{dns_sd_name} %{dns_sd_major}
%define develnamedns_sd	%mklibname -d %{dns_sd_name}
%define lib_glib_name	%mklibname %{glib_name} %{glib_major}
%define develnameglib	%mklibname -d %{glib_name}
%define lib_gobject_name	%mklibname %{gobject_name} %{gobject_major}
%define develnamegobject	%mklibname -d %{gobject_name}
%define lib_howl_name	%mklibname %{howl_name} %{howl_major}
%define develnamehowl	%mklibname -d %{howl_name}
%define lib_qt3_name	%mklibname %{qt3_name}_ %{qt3_major}
%define develnameqt3	%mklibname -d %{qt3_name}
%define lib_qt4_name	%mklibname %{qt4_name}_ %{qt4_major}
%define develnameqt4	%mklibname -d %{qt4_name}
### not worth it to fix now b/c 1 > 0, but ui_major should be used not qt3_major
%define lib_ui_name		%mklibname %{ui_name} %{qt3_major}
%define develnameui		%mklibname -d %{ui_name}
%define lib_ui_gtk3_name	%mklibname %{ui_gtk3_name}_ %{ui_gtk3_major}
%define develnameui_gtk3	%mklibname -d %{ui_gtk3_name}

%define lib_dns_sd_old_name	%mklibname %{dns_sd_old_name} 1
%define lib_howl_old_name	%mklibname %{howl_old_name} 0
%define lib_howl_fake_EVR   1.0.0-7

%define build_mono 1
%{?_with_mono: %{expand: %%global build_mono 1}} 
%{?_without_mono: %{expand: %%global build_mono 0}} 

%ifarch %arm %mips
%define build_mono 0
%endif

%define build_qt3 1
%{?_with_qt3: %{expand: %%global build_qt3 1}}
%{?_without_qt3: %{expand: %%global build_qt3 0}}

%define build_qt4 1
%{?_with_qt4: %{expand: %%global build_qt4 1}}
%{?_without_qt4: %{expand: %%global build_qt4 0}}

%define build_gtk3 1
%{?_with_gtk3: %{expand: %%global build_gtk3 1}}
%{?_without_gtk3: %{expand: %%global build_gtk3 0}}

%define build_systemd 1
%{?_with_systemd: %{expand: %%global build_systemd 1}}
%{?_without_systemd: %{expand: %%global build_systemd 0}}

%define build_bootstrap 0
%{?_with_bootstrap: %{expand: %%global build_bootstrap 1}}
%if %{build_bootstrap}
%define build_mono 0
%define build_qt3 0
%define build_qt4 0
%define build_gtk3 0
%define build_systemd 0
%endif

Summary:	Avahi service discovery (mDNS/DNS-SD) suite
Name:		avahi
Version:	0.6.31
Release:	5
License:	LGPLv2+
Group:		System/Servers
Url:		http://avahi.org/

Source0:	http://avahi.org/download/%{name}-%{version}.tar.gz
Source1:	avahi-hostname.sh

BuildRequires:	cap-devel
BuildRequires:	expat-devel >= 2.0.1
BuildRequires:	gdbm-devel
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(libdaemon)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pygtk2.0
%if %{build_qt3}
BuildRequires:	pkgconfig(qt-mt)
%endif
%if %{build_qt4}
BuildRequires:	pkgconfig(QtCore)
%endif
%if %{build_gtk3}
BuildRequires:	pkgconfig(gtk+-3.0)
%endif
%if %{build_systemd}
BuildRequires:	systemd-units
%endif

Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires(post): dbus
Requires(preun): dbus
Suggests:	nss_mdns

%description
Avahi is a system which facilitates service discovery on a local
network -- this means that you can plug your laptop or computer into a
network and instantly be able to view other people who you can chat
with, find printers to print to or find files being shared. This kind
of technology is already found in MacOS X (branded 'Rendezvous',
'Bonjour' and sometimes 'ZeroConf') and is very convenient.

%package dnsconfd
Group:		System/Servers
Summary:	Avahi DNS configuration server
Requires:	%{name} = %{version}-%{release}
Requires(post):	rpm-helper
Requires(preun): rpm-helper

%description dnsconfd
avahi-dnsconfd is a small daemon which may be used to configure
conventional DNS servers using mDNS in a DHCP-like fashion.
Especially useful on IPv6.

%package x11
Group:		System/Servers
Summary:	Graphical tools for Avahi
Requires:	%{name} = %{version}-%{release}

%description x11
Graphical tools for Avahi.
It includes avahi-discover-standalone.

%package	python
Group:		System/Libraries
Summary:	Python bindings and utilities for Avahi
Requires:	pygtk2.0-libglade python-twisted-core
Requires:	python-twisted-web dbus-python avahi 
Requires:	%{name}-x11

%description python
Python bindings and utilities for Avahi.
It includes avahi-bookmarks and avahi-discover.

%if %{build_mono}
%package sharp
Group:		System/Libraries
Summary:	Mono bindings for Avahi
BuildRequires:	mono-devel mono-tools
BuildRequires:	pkgconfig(gtk-sharp-2.0)
#gw this is needed by mono-find-requires:
BuildRequires:	avahi-ui-devel
Requires:	%{lib_client_name} = %{version}-%{release}
Requires:	%{lib_common_name} = %{version}-%{release}
Requires:	%{lib_glib_name} = %{version}-%{release}

%description sharp
Mono bindings for Avahi.

%package sharp-doc
Summary:	Development documentation for avahi-sharp
Group:		Development/Other
Requires(post):	mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description sharp-doc
This package contains the API documentation for the avahi-sharp in
Monodoc format.
%endif

%package -n %{lib_client_name}
Group:		System/Libraries
Summary:	Library for avahi-client

%description -n %{lib_client_name}
Library for avahi-client.

%package -n %{develnameclient}
Group:		Development/C
Summary:	Devel library for avahi-client
Provides:	%{client_name}-devel = %{version}-%{release}
Provides:	lib%{client_name}-devel = %{version}-%{release}
Requires:	%{lib_client_name} = %{version}-%{release}
Obsoletes:	%{mklibname -d %{client_name} 3} < 0.6.31

%description -n %{develnameclient}
Devel library for avahi-client.

%package -n %{lib_common_name}
Group:		System/Libraries
Summary:	Library for avahi-common

%description -n %{lib_common_name}
Library for avahi-common.

%package -n %{develnamecommon}
Group:		Development/C
Summary:	Devel library for avahi-common
Provides:	%{common_name}-devel = %{version}-%{release}
Provides:	lib%{common_name}-devel = %{version}-%{release}
Requires:	%{lib_common_name} = %{version}-%{release}
Obsoletes:	%{mklibname -d %{common_name} 3} < 0.6.31

%description -n %{develnamecommon}
Devel library for avahi-common.

%package -n %{lib_core_name}
Group:		System/Libraries
Summary:	Library for avahi-core

%description -n %{lib_core_name}
Library for avahi-core.

%package -n %{develnamecore}
Group:		Development/C
Summary:	Devel library for avahi-core
Provides:	%{core_name}-devel = %{version}-%{release}
Provides:	lib%{core_name}-devel = %{version}-%{release}
Requires:	%{lib_core_name} = %{version}-%{release}
Obsoletes:	%{mklibname -d %{core_name} 5} < 0.6.31

%description -n %{develnamecore}
Devel library for avahi-core.

%package -n %{lib_dns_sd_name}
Group:		System/Libraries
Summary:	Avahi compatibility library for libdns_sd
Obsoletes:	%{lib_dns_sd_old_name} < 0.6.31
Provides:	%{lib_dns_sd_old_name}

%description -n %{lib_dns_sd_name}
Avahi compatibility library for libdns_sd

%package -n %{develnamedns_sd}
Group:		Development/C
Summary:	Avahi devel compatibility library for libdns_sd
Provides:	%{dns_sd_name}-devel = %{version}-%{release}
Provides:	lib%{dns_sd_name}-devel = %{version}-%{release}
Requires:	%{lib_dns_sd_name} = %{version}-%{release}
Obsoletes:	%{lib_dns_sd_old_name}-devel < 0.6.31
Provides:	%{lib_dns_sd_old_name}-devel
Provides:	%{dns_sd_old_name}-devel = %{version}-%{release}
Provides:	lib%{dns_sd_old_name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d %{dns_sd_name} 1} < 0.6.31

%description -n %{develnamedns_sd}
Avahi devel compatibility library for libdns_sd.

%package -n %{lib_glib_name}
Group:		System/Libraries
Summary:	Library for avahi-glib

%description -n %{lib_glib_name}
Library for avahi-glib.

%package -n %{develnameglib}
Group:		Development/C
Summary:	Devel library for avahi-glib
Provides:	%{glib_name}-devel = %{version}-%{release}
Provides:	lib%{glib_name}-devel = %{version}-%{release}
Requires:	%{lib_glib_name} = %{version}-%{release}
Obsoletes:	%{mklibname -d %{glib_name} 1} < 0.6.31

%description -n %{develnameglib}
Devel library for avahi-glib.

%package -n %{lib_gobject_name}
Group:		System/Libraries
Summary:	Library for avahi-gobject

%description -n %{lib_gobject_name}
Library for avahi-gobject.

%package -n %{develnamegobject}
Group:		Development/C
Summary:	Devel library for avahi-gobject
Provides:	%{gobject_name}-devel = %{version}-%{release}
Provides:	lib%{gobject_name}-devel = %{version}-%{release}
Requires:	%{lib_gobject_name} = %{version}-%{release}

%description -n %{develnamegobject}
Devel library for avahi-gobject.

%package -n %{lib_howl_name}
Group:		System/Libraries
Summary:	Avahi compatibility library for howl
Obsoletes:	%{lib_howl_old_name} < 0.6.31
Provides:	%{lib_howl_old_name} = %{lib_howl_fake_EVR}

%description -n %{lib_howl_name}
Avahi compatibility library for howl.

%package -n %{develnamehowl}
Group:		Development/C
Summary:	Avahi devel compatibility library for libdns_sd for howl
Provides:	%{howl_name}-devel = %{version}-%{release}
Provides:	lib%{howl_name}-devel = %{version}-%{release}
Requires:	%{lib_howl_name} = %{version}-%{release}
Obsoletes:	%{lib_howl_old_name}-devel < 0.6.31
Provides:	%{lib_howl_old_name}-devel = %{lib_howl_fake_EVR}
Provides:	%{howl_old_name}-devel = %{version}-%{release}
Provides:	lib%{howl_old_name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d %{howl_name} 0} < 0.6.31

%description -n %{develnamehowl}
Avahi devel compatibility library for libdns_sd for howl.

%if %{build_qt3}
%package -n %{lib_qt3_name}
Group:		System/Libraries
Summary:	Library for avahi-qt3

%description -n %{lib_qt3_name}
Library for avahi-qt3.

%package -n %{develnameqt3}
Group:		Development/C
Summary:	Devel library for avahi-qt3
Provides:	%{qt3_name}-devel = %{version}-%{release}
Provides:	lib%{qt3_name}-devel = %{version}-%{release}
Requires:	%{lib_qt3_name} = %{version}-%{release}
Obsoletes:	%{mklibname -d %{qt3_name}_ 1} < 0.6.31

%description -n %{develnameqt3}
Devel library for avahi-qt3.
%endif

%if %{build_qt4}
%package -n %{lib_qt4_name}
Group:		System/Libraries
Summary:	Library for avahi-qt4

%description -n %{lib_qt4_name}
Library for avahi-qt4.

%package -n %{develnameqt4}
Group:		Development/C
Summary:	Devel library for avahi-qt4
Provides:	%{qt4_name}-devel = %{version}-%{release}
Provides:	lib%{qt4_name}-devel = %{version}-%{release}
Requires:	%{lib_qt4_name} = %{version}-%{release}
Obsoletes:	%{mklibname -d %{qt4_name}_ 1} < 0.6.31

%description -n %{develnameqt4}
Devel library for avahi-qt4.
%endif

%package -n %{lib_ui_name}
Group:		System/Libraries
Summary:	Library for avahi-ui

%description -n %{lib_ui_name}
Library for avahi-ui.

%package -n %{develnameui}
Group:		Development/C
Summary:	Devel library for avahi-ui
Provides:	%{ui_name}-devel = %{version}-%{release}
Provides:	lib%{ui_name}-devel = %{version}-%{release}
Requires:	%{lib_ui_name} = %{version}-%{release}
Obsoletes:	%{mklibname -d %{ui_name} 1} < 0.6.31

%description -n %{develnameui}
Devel library for avahi-ui.

%if %{build_gtk3}
%package -n %{lib_ui_gtk3_name}
Group:		System/Libraries
Summary:	Library for avahi-gtk3

%description -n %{lib_ui_gtk3_name}
Library for avahi-gtk3.

%package -n %{develnameui_gtk3}
Group:		Development/C
Summary:	Devel library for avahi-gtk3
Provides:	%{ui_gtk3_name}-devel = %{version}-%{release}
Requires:	%{lib_ui_gtk3_name} = %{version}-%{release}

%description -n %{develnameui_gtk3}
Devel library for avahi-gtk3.
%endif

%prep
%setup -q
cp %{SOURCE1} avahi-hostname.sh

%build
export PKG_CONFIG_PATH=/usr/lib/qt4/%{_lib}/pkgconfig
%configure2_5x \
	--disable-static \
%if !%{build_mono}
    --disable-mono \
%endif
%if !%{build_qt3}
    --disable-qt3 \
%endif
%if !%{build_qt4}
    --disable-qt4 \
%endif
  --localstatedir=%{_var} \
  --with-avahi-priv-access-group="avahi" \
  --enable-compat-libdns_sd \
  --enable-compat-howl \
  --enable-introspection=no \
%if %{build_systemd}
  --with-systemdsystemunitdir=%{_unitdir} \
%endif
%if !%{build_gtk3}
  --disable-gtk3
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_sysconfdir}/%{name}/services/ssh.service
ln -s avahi-compat-howl.pc %{buildroot}%{_libdir}/pkgconfig/howl.pc
%if "%{_lib}" != "lib" && %{build_mono}
mkdir -p %{buildroot}%{_prefix}/lib
mv %{buildroot}%{_libdir}/mono %{buildroot}%{_prefix}/lib
perl -pi -e "s/%{_lib}/lib/" %{buildroot}%{_libdir}/pkgconfig/avahi-{,ui-}sharp.pc
%endif

# install hostname.d hook
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig/network-scripts/hostname.d/
install -m755 avahi-hostname.sh %{buildroot}/%{_sysconfdir}/sysconfig/network-scripts/hostname.d/avahi

%if %{build_systemd}
rm -rf %{buildroot}%{_initrddir}/%{name}-daemon
rm -rf %{buildroot}%{_initrddir}/%{name}-dnsconfd
%endif

%find_lang %{name}

%pre
%_pre_useradd %{name} %{_var}/%{name} /bin/false
%_pre_useradd %{name}-autoipd %{_var}/%{name} /bin/false

%postun
%_postun_userdel %{name}
%_postun_userdel %{name}-autoipd

%post
%_post_service %{name}-daemon

%preun
%_preun_service %{name}-daemon

%post dnsconfd
%_post_service %{name}-dnsconfd

%preun dnsconfd
%_preun_service %{name}-dnsconfd

%if %{build_mono}
%post sharp-doc
%{_bindir}/monodoc --make-index > /dev/null
%postun sharp-doc
if [ "$1" = "0" -a -x %{_bindir}/monodoc ]; then %{_bindir}/monodoc --make-index > /dev/null
fi
%endif

%files -f avahi.lang
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/services/
%config(noreplace) %{_sysconfdir}/%{name}/hosts
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-daemon.conf
%config(noreplace) %{_sysconfdir}/%{name}/avahi-autoipd.action
%config(noreplace) %{_sysconfdir}/%{name}/services/sftp-ssh.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/%{name}-dbus.conf
%if !%{build_systemd}
 %{_initrddir}/%{name}-daemon
%endif
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
%{_sbindir}/avahi-dnsconfd
%{_datadir}/%{name}/%{name}-service.dtd
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/%{name}/service-types
%{_mandir}/man1/%{name}-browse-domains.1*
%{_mandir}/man1/%{name}-browse.1*
%{_mandir}/man1/%{name}-publish.1*
%{_mandir}/man1/%{name}-publish-address.1*
%{_mandir}/man1/%{name}-publish-service.1*
%{_mandir}/man1/%{name}-resolve.1*
%{_mandir}/man1/%{name}-resolve-address.1*
%{_mandir}/man1/%{name}-resolve-host-name.1*
%{_mandir}/man1/%{name}-set-host-name.1*
%{_mandir}/man5/%{name}-daemon.conf.5*
%{_mandir}/man5/%{name}.hosts.5*
%{_mandir}/man5/%{name}.service.5*
%{_mandir}/man8/%{name}-daemon.8*
%{_mandir}/man8/avahi-autoipd*
%dir %{_libdir}/avahi
%{_libdir}/avahi/service-types.db
%if %{build_systemd}
%{_unitdir}/avahi-daemon.service
%{_unitdir}/avahi-daemon.socket
%{_unitdir}/avahi-dnsconfd.service
%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service
%endif

%files dnsconfd
%{_sysconfdir}/%{name}/%{name}-dnsconfd.action
%if !%{build_systemd}
 %{_initrddir}/%{name}-dnsconfd
%endif%{_sbindir}/%{name}-dnsconfd
%{_mandir}/man8/%{name}-dnsconfd.8*
%{_mandir}/man8/%{name}-dnsconfd.action.8*

%files x11
%{_bindir}/%{name}-discover-standalone
%{_bindir}/bshell
%{_bindir}/bssh
%{_bindir}/bvnc
%{_datadir}/applications/bssh.desktop
%{_datadir}/applications/bvnc.desktop
%{_mandir}/man1/bssh.1*
%{_mandir}/man1/bvnc.1*
%{_datadir}/applications/%{name}-discover.desktop
%{_datadir}/%{name}/interfaces/%{name}-discover.ui

%files python
%{_bindir}/%{name}-bookmarks
%{_bindir}/%{name}-discover
%{py_puresitedir}/%{name}/*.py*
%{py_puresitedir}/avahi_discover/
%{_mandir}/man1/%{name}-discover.1*
%{_mandir}/man1/%{name}-bookmarks.1*

%if %{build_mono}
%files sharp
%{_prefix}/lib/mono/%{name}-sharp/%{name}-sharp.dll
%{_prefix}/lib/mono/gac/%{name}-sharp/
%{_libdir}/pkgconfig/%{name}-sharp.pc
%{_prefix}/lib/mono/%{name}-ui-sharp/%{name}-ui-sharp.dll
%{_prefix}/lib/mono/gac/%{name}-ui-sharp/
%{_libdir}/pkgconfig/%{name}-ui-sharp.pc

%files sharp-doc
%{_usr}/lib/monodoc/sources/%{name}-sharp-docs.source
%{_usr}/lib/monodoc/sources/%{name}-sharp-docs.tree
%{_usr}/lib/monodoc/sources/%{name}-sharp-docs.zip
%{_usr}/lib/monodoc/sources/%{name}-ui-sharp-docs.source
%{_usr}/lib/monodoc/sources/%{name}-ui-sharp-docs.tree
%{_usr}/lib/monodoc/sources/%{name}-ui-sharp-docs.zip
%endif

%files -n %{lib_client_name}
%{_libdir}/lib%{name}-client.so.%{client_major}*

%files -n %{lib_common_name}
%{_libdir}/lib%{name}-common.so.%{common_major}*

%files -n %{lib_core_name}
%{_libdir}/lib%{name}-core.so.%{core_major}*

%files -n %{lib_dns_sd_name}
%{_libdir}/libdns_sd.so.%{dns_sd_major}*

%files -n %{lib_glib_name}
%{_libdir}/lib%{name}-glib.so.%{glib_major}*

%files -n %{lib_gobject_name}
%{_libdir}/lib%{name}-gobject.so.%{gobject_major}*

%files -n %{lib_howl_name}
%{_libdir}/libhowl.so.%{howl_major}*

%if %{build_qt3}
%files -n %{lib_qt3_name}
%{_libdir}/lib%{name}-qt3.so.%{qt3_major}*
%endif

%if %{build_qt4}
%files -n %{lib_qt4_name}
%{_libdir}/lib%{name}-qt4.so.%{qt4_major}*
%endif

%files -n %{lib_ui_name}
%{_libdir}/lib%{name}-ui.so.%{ui_major}*

%files -n %{develnameclient}
%{_includedir}/%{name}-client
%{_libdir}/lib%{name}-client.so
%{_libdir}/pkgconfig/%{name}-client.pc

%files -n %{develnamecommon}
%{_includedir}/%{name}-common
%{_libdir}/lib%{name}-common.so

%files -n %{develnamecore}
%{_includedir}/%{name}-core
%{_libdir}/lib%{name}-core.so
%{_libdir}/pkgconfig/%{name}-core.pc

%files -n %{develnamedns_sd}
%{_includedir}/%{name}-compat-libdns_sd
%{_libdir}/libdns_sd.so
%{_libdir}/pkgconfig/%{name}-compat-libdns_sd.pc

%files -n %{develnameglib}
%{_includedir}/%{name}-glib
%{_libdir}/lib%{name}-glib.so
%{_libdir}/pkgconfig/%{name}-glib.pc

%files -n %{develnamegobject}
%{_includedir}/%{name}-gobject
%{_libdir}/lib%{name}-gobject.so
%{_libdir}/pkgconfig/%{name}-gobject.pc


%files -n %{develnamehowl}
%{_includedir}/%{name}-compat-howl
%{_libdir}/libhowl.so
%{_libdir}/pkgconfig/%{name}-compat-howl.pc
%{_libdir}/pkgconfig/howl.pc

%if %{build_qt3}
%files -n %{develnameqt3}
%{_includedir}/%{name}-qt3
%{_libdir}/lib%{name}-qt3.so
%{_libdir}/pkgconfig/%{name}-qt3.pc
%endif

%if %{build_qt4}
%files -n %{develnameqt4}
%{_includedir}/%{name}-qt4
%{_libdir}/lib%{name}-qt4.so
%{_libdir}/pkgconfig/%{name}-qt4.pc
%endif

%files -n %{develnameui}
%{_includedir}/%{name}-ui
%{_libdir}/lib%{name}-ui.so
%{_libdir}/pkgconfig/%{name}-ui.pc

%if %{build_gtk3}
%files -n %{lib_ui_gtk3_name}
%{_libdir}/lib%{name}-ui-gtk3.so.%{ui_gtk3_major}*

%files -n %{develnameui_gtk3}
%{_libdir}/libavahi-ui-gtk3.so
%{_libdir}/pkgconfig/avahi-ui-gtk3.pc
%endif



%changelog
* Thu Feb 16 2012 Götz Waschk <waschk@mandriva.org> 0.6.31-2
+ Revision: 775266
- reenable mono

* Thu Feb 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.6.31-1
+ Revision: 774825
- disabled mono build, deps are broken
- new version 0.6.31
- cleaned up spec

* Sat Nov 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.6.30-5
+ Revision: 733640
- removed dep loop
- added not about wrong major used for ui_name

* Wed Nov 16 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.6.30-4
+ Revision: 731053
- added _ after gtk3 name for major
- fixed ui_gtk3_major typo
- add back BR
- remove - for _ in gtk3 macro names.. oops
- fixed typoes for gtk3 naming
- fixed ui-gtk3 name
  aligned systemd _with macro to be like build_ macros
  more clean ups for bracketing of macros
  b/c of build failure switched with-systemd...
  removed old obsoletes & provides
  converted BRs to pkgconfig provides
- rebuild
  removed defattr
  disabled static build
  removed .la files
  cleaned up spec
  added build with gtk3
  removed old ldconfig scriptlets
  removed clean section
  removed mkrel
  remove BuildRoot

* Thu Sep 22 2011 Götz Waschk <waschk@mandriva.org> 0.6.30-2
+ Revision: 700862
- rebuild

* Tue Sep 06 2011 Götz Waschk <waschk@mandriva.org> 0.6.30-1
+ Revision: 698491
- new version

  + Matthew Dawkins <mattydaw@mandriva.org>
    - added qt3 build option
    - and included systemd in with the bootstrap build option

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.29-1
+ Revision: 646045
- 0.6.29
- drop the CVE-2011-1002 fix, it's fixed with 0.6.29

* Thu Feb 24 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.28-3
+ Revision: 639581
- sync with MDVSA-2011:037

* Mon Jan 24 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.6.28-2
+ Revision: 632480
- Enable systemd support.

* Fri Nov 05 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.6.28-1mdv2011.0
+ Revision: 593734
- Updated to 0.6.28.

* Sun Oct 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.27-5mdv2011.0
+ Revision: 591176
- python-devel isn't a BR, python Makefile is going to be moved to python main package

* Sun Oct 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.27-4mdv2011.0
+ Revision: 590920
- add missing BR, python-devel

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Sun Oct 10 2010 Funda Wang <fwang@mandriva.org> 0.6.27-2mdv2011.0
+ Revision: 584584
- rebuild for new mono

* Tue Aug 17 2010 Emmanuel Andry <eandry@mandriva.org> 0.6.27-1mdv2011.0
+ Revision: 570971
- New version 0.6.27
- new avahi core major 7
- disable gtk3 and introspection for now
- update files list

* Thu Apr 08 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.6.25-5mdv2010.1
+ Revision: 532971
- Install hostname.d file (#25617).
  Suggest nss_mdns to help resolve .local names.
  Fix glade packaging issue between avahi-x11 and avahi-python.

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.25-4mdv2010.1
+ Revision: 520015
- rebuilt for 2010.1

* Fri Sep 25 2009 Olivier Blin <blino@mandriva.org> 0.6.25-3mdv2010.0
+ Revision: 448777
- do not build mono support on arm and mips (from Arnaud Patard)

* Sun Jun 28 2009 Raphaël Gertz <rapsys@mandriva.org> 0.6.25-2mdv2010.0
+ Revision: 390222
- Fix chroot install bug when $NETWORKING is not set

* Thu May 28 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.6.25-1mdv2010.0
+ Revision: 380502
- Updated to 0.6.25.
  Dropped P0 (integrated upstream).

* Sun Apr 19 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.24-2mdv2009.1
+ Revision: 368029
- Add upstream patch fixng CVE-2009-0758

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.24-1mdv2009.1
+ Revision: 318718
- new major
- rebuild for python 2.6
- new release 0.6.24

* Sat Nov 08 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.23-2mdv2009.1
+ Revision: 300969
- rebuild for changed xcb

* Fri Jul 18 2008 Götz Waschk <waschk@mandriva.org> 0.6.23-1mdv2009.0
+ Revision: 238063
- new version
- drop patch
- update license

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Frederic Crozat <fcrozat@mandriva.com> 0.6.22-5mdv2009.0
+ Revision: 214326
- Fix BuildRequires
- Patch0 (SVN): fix typo in Makefile.am, fixing build
- Remove old obsolete (and false) option in configure

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new qtlibs location

* Mon Mar 03 2008 Olivier Blin <blino@mandriva.org> 0.6.22-3mdv2008.1
+ Revision: 177826
- add avahi-autoipd user and group (#33885)

  + Götz Waschk <waschk@mandriva.org>
    - fix dep on avahi in libavahi-client

* Fri Dec 21 2007 Götz Waschk <waschk@mandriva.org> 0.6.22-2mdv2008.1
+ Revision: 136229
- fix devel obsoletes

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Götz Waschk <waschk@mandriva.org> 0.6.22-1mdv2008.1
+ Revision: 131028
- new version
- drop patches
- update file list
- add package for libavahi-gobject

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 06 2007 Götz Waschk <waschk@mandriva.org> 0.6.21-5mdv2008.1
+ Revision: 115983
- fix buildrequires

* Thu Dec 06 2007 Götz Waschk <waschk@mandriva.org> 0.6.21-3mdv2008.1
+ Revision: 115849
- new devel name

* Fri Aug 17 2007 Funda Wang <fwang@mandriva.org> 0.6.21-2mdv2008.0
+ Revision: 65177
- fix desktop conflict bewteen x11 and python sub package

* Mon Aug 13 2007 Olivier Blin <blino@mandriva.org> 0.6.21-1mdv2008.0
+ Revision: 62591
- add patch to allow build with dbus < 1.1.1 (from upstream SVN)
- 0.6.21

* Sun Jun 24 2007 Olivier Blin <blino@mandriva.org> 0.6.20-2mdv2008.0
+ Revision: 43749
- 0.6.20 (and drop upstream patches)

* Thu Jun 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.19-2mdv2008.0
+ Revision: 36904
- rebuild for expat

* Mon May 14 2007 Olivier Blin <blino@mandriva.org> 0.6.19-1mdv2008.0
+ Revision: 26632
- 0.6.19
- fix zssh build (patches from upstream SVN)
- zssh/zvnc are renamed bssh/bvnc
- package avahi-ui-sharp files in main avahi-sharp package (for now)

* Thu Apr 19 2007 Olivier Blin <blino@mandriva.org> 0.6.18-1mdv2008.0
+ Revision: 14986
- add ui applications in avahi-x11 and create ui library packages
- really use qt4 major macro
- use linux inotify header instead of glibc one to get up-to-date inotify (for IN_ONLYDIR)
- workaround pkgconfig path for qt4
- 0.6.18


* Mon Feb 05 2007 Götz Waschk <waschk@mandriva.org> 0.6.17-1mdv2007.0
+ Revision: 116186
- new version
- new major for libavahi-core
- drop the patches, the problems are fixed upstream

* Fri Jan 19 2007 Götz Waschk <waschk@mandriva.org> 0.6.16-3mdv2007.1
+ Revision: 110596
- don't log broken packets

* Wed Jan 10 2007 Götz Waschk <waschk@mandriva.org> 0.6.16-2mdv2007.1
+ Revision: 106954
- don't restart dbus on package installation

* Thu Dec 28 2006 Olivier Blin <oblin@mandriva.com> 0.6.16-1mdv2007.1
+ Revision: 102392
- use --with-avahi-priv-access-group configure option instead of patch0
- drop dbus patch (merged upstream)
- 0.6.16

* Mon Dec 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.15-4mdv2007.1
+ Revision: 98368
- Rebuild against new Python

  + Gwenole Beauchesne <gbeauchesne@mandriva.com>
    - help bootstrap builds
    - generate debug packages on x86_64

  + Frederic Crozat <fcrozat@mandriva.com>
    - Patch1 (Fedora): fix build with dbus 1.0
      Patch2 (Fedora) ia64: unaligned access errors seen  during startup of avahi-daemon

* Mon Nov 06 2006 Olivier Blin <oblin@mandriva.com> 0.6.15-2mdv2007.1
+ Revision: 77003
- 0.6.15

* Sat Nov 04 2006 Götz Waschk <waschk@mandriva.org> 0.6.14-2mdv2007.1
+ Revision: 76544
- fix avahi-sharp-doc content

* Fri Oct 27 2006 Götz Waschk <waschk@mandriva.org> 0.6.14-1mdv2007.0
+ Revision: 72946
- Import avahi

* Fri Oct 27 2006 Götz Waschk <waschk@mandriva.org> 0.6.14-1mdv2007.1
- add autoipd to the avahi package
- new version

* Fri Sep 22 2006 Götz Waschk <waschk@mandriva.org> 0.6.13-5mdv2007.0
- split monodoc docs to separate package

* Wed Sep 20 2006 Götz Waschk <waschk@mandriva.org> 0.6.13-4mdv2007.0
- fix avahi-sharp pkgconfig file for x86_64

* Thu Sep 14 2006 Götz Waschk <waschk@mandriva.org> 0.6.13-3mdv2007.0
- fix avahi-sharp path on x86_64

* Mon Aug 28 2006 Olivier Blin <blino@mandriva.com> 0.6.13-2mdv2007.0
- Patch0: don't use NetworkManager-specific netdev group to grant
  access to all methods, use avahi group instead (this means don't
  allow full access to anyone by default)

* Sun Aug 27 2006 Götz Waschk <waschk@mandriva.org> 0.6.13-1mdv2007.0
- update file list
- New release 0.6.13

* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 0.6.12-2mdv2007.0
- Rebuild with latest dbus

* Sun Jul 23 2006 Olivier Blin <blino@mandriva.com> 0.6.12-1mdv2007.0
- New release 0.6.12

* Wed Jul 19 2006 Götz Waschk <waschk@mandriva.org> 0.6.11-4mdv2007.0
- fix postun script of the sharp binding

* Sun Jul 02 2006 Stefan van der Eijk <stefan@mandriva.org> 0.6.11-3
- fix typo

* Sun Jul 02 2006 Stefan van der Eijk <stefan@mandriva.org> 0.6.11-2
- BuildRequires

* Tue Jun 27 2006 Götz Waschk <waschk@mandriva.org> 0.6.11-1
- New release 0.6.11

* Thu Jun 22 2006 Laurent MONTEL <lmontel@mandriva.com> 0.6.10-4
- Rebuild

* Tue Jun 20 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.6.10-3mdv2007.0
- rebuild for new png lib on x86_64

* Thu May 18 2006 Laurent MONTEL <lmontel@mandriva.com> 0.6.10-2
- Rebuild

* Sun May 07 2006 Götz Waschk <waschk@mandriva.org> 0.6.10-1mdk
- New release 0.6.10

* Thu May 04 2006 Frederic Crozat <fcrozat@mandriva.com> 0.6.9-5mdk
- add requires on dbus for post/preun

* Wed Apr 19 2006 Götz Waschk <waschk@mandriva.org> 0.6.9-4mdk
- enable mono

* Wed Mar 08 2006 Olivier Blin <oblin@mandriva.com> 0.6.9-3mdk
- move avahi-discover-standalone in new sub-package avahi-x11
  (not to make avahi command line tools require X, thanks Pixel)
- move avahi-discover.glade in avahi-python

* Sat Mar 04 2006 Michael Scherer <misc@mandriva.org> 0.6.9-2mdk
-add qt4 subpackage, now this is in main

* Fri Mar 03 2006 Götz Waschk <waschk@mandriva.org> 0.6.9-1mdk
- New release 0.6.9

* Thu Mar 02 2006 Götz Waschk <waschk@mandriva.org> 0.6.8-3mdk
- spec fixes
- fix howl compat package

* Wed Mar 01 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.6.8-2mdk
- fix major

* Thu Feb 23 2006 Götz Waschk <waschk@mandriva.org> 0.6.8-1mdk
- New release 0.6.8

* Wed Feb 15 2006 Götz Waschk <waschk@mandriva.org> 0.6.7-1mdk
- update file list
- New release 0.6.7

* Fri Feb 10 2006 Michael Scherer <misc@mandriva.org> 0.6.6-3mdk
- do not advertise ssh service by default ( and place the file in openssh itself )

* Tue Jan 31 2006 Olivier Blin <oblin@mandriva.com> 0.6.6-2mdk
- obsolete our old daemons (howl/tmdns/mDNSResponder)
- don't restart messagebus service twice on upgrade
  (thanks to Frederic Crozat for all these points)
- fake provides version for howl compat package, to allow libhowl0 to
  be replaced by libavahi-compat-howl0

* Tue Jan 31 2006 Olivier Blin <oblin@mandriva.com> 0.6.6-1mdk
- 0.6.6
- buildrequire dbus-python

* Fri Jan 27 2006 Michael Scherer <misc@mandriva.org> 0.6.5-9mdk
- fix requires on python package ( no need to pull the whole twisted stack )
- exchange avahi-bookmarks and avahi-browse ( the python script was not in the python package )

* Thu Jan 26 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.6.5-8mdk
- don't built qt4 bindings by default as long as qt4 is in contrib

* Wed Jan 25 2006 Olivier Blin <oblin@mandriva.com> 0.6.5-7mdk
- make the client library require the daemon
- make the compat packages obsolete howl and mDNSResponder libraries
- split dnsconfd in a sub package

* Tue Jan 24 2006 Götz Waschk <waschk@mandriva.org> 0.6.5-6mdk
- fix buildrequires

* Tue Jan 24 2006 Götz Waschk <waschk@mandriva.org> 0.6.5-5mdk
- fix buildrequires

* Tue Jan 24 2006 Götz Waschk <waschk@mandriva.org> 0.6.5-4mdk
- fix buildrequires

* Mon Jan 23 2006 Olivier Blin <oblin@mandriva.com> 0.6.5-3mdk
- remove the "don't install me" watchdog (who said forgetfulness?)
  in compat libraries, i.e. don't conflict with our own Provides

* Mon Jan 23 2006 Olivier Blin <oblin@mandriva.com> 0.6.5-2mdk
- don't call autogen.sh, no longer needed

* Mon Jan 23 2006 Olivier Blin <oblin@mandriva.com> 0.6.5-1mdk
- New release 0.6.5
- drop Patch0,1,2 (merged upstream)

* Fri Jan 20 2006 Olivier Blin <oblin@mandriva.com> 0.6.4-3mdk
- Patch0: use initscript lock subsys

* Thu Jan 19 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-2mdk
- added lib64 fixes in the pkgconfig files (P2)

* Wed Jan 18 2006 Olivier Blin <oblin@mandriva.com> 0.6.4-1mdk
- initial Mandriva release
- Patch0: create Mandriva initscripts
- Patch1: fix typo in avahi-dnsconfd(8) (thanks to Michael Scherer)

