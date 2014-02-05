%define client_name %{name}-client
%define common_name %{name}-common
%define core_name %{name}-core
%define dns_sd_name %{name}-compat-libdns_sd
%define glib_name %{name}-glib
%define gobject_name %{name}-gobject
%define howl_name %{name}-compat-howl
%define qt3_name %{name}-qt3
%define qt4_name %{name}-qt4
%define ui_name %{name}-ui
%define ui_gtk3_name %{name}-ui-gtk3

%define client_major 3
%define common_major 3
%define core_major 7
%define dns_sd_major 1
%define glib_major 1
%define gobject_major 0
%define howl_major 0
%define qt3_major 1
%define qt4_major 1
%define ui_major 0
%define ui_gtk3_major 0

%define lib_client_name %mklibname %{client_name} %{client_major}
%define develnameclient %mklibname -d %{client_name}
%define lib_common_name %mklibname %{common_name} %{common_major}
%define develnamecommon %mklibname -d %{common_name}
%define lib_core_name %mklibname %{core_name} %{core_major}
%define develnamecore %mklibname -d %{core_name}
%define lib_dns_sd_name %mklibname %{dns_sd_name} %{dns_sd_major}
%define develnamedns_sd %mklibname -d %{dns_sd_name}
%define lib_glib_name %mklibname %{glib_name} %{glib_major}
%define develnameglib %mklibname -d %{glib_name}
%define lib_gobject_name %mklibname %{gobject_name} %{gobject_major}
%define develnamegobject %mklibname -d %{gobject_name}
%define lib_howl_name %mklibname %{howl_name} %{howl_major}
%define develnamehowl %mklibname -d %{howl_name}
%define lib_qt3_name %mklibname %{qt3_name}_ %{qt3_major}
%define develnameqt3 %mklibname -d %{qt3_name}
%define lib_qt4_name %mklibname %{qt4_name}_ %{qt4_major}
%define develnameqt4 %mklibname -d %{qt4_name}
### not worth it to fix now b/c 1 > 0, but ui_major should be used not qt3_major
%define lib_ui_name %mklibname %{ui_name} %{ui_major}
%define develnameui %mklibname -d %{ui_name}
%define lib_ui_gtk3_name %mklibname %{ui_gtk3_name}_ %{ui_gtk3_major}
%define develnameui_gtk3 %mklibname -d %{ui_gtk3_name}

%define build_mono 1
%{?_with_mono: %{expand: %%global build_mono 1}} 
%{?_without_mono: %{expand: %%global build_mono 0}} 

%ifarch %arm %mips aarch64
%define build_mono 0
%endif

%define build_qt3 0
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
Release:	14
License:	LGPLv2+
Group:		System/Servers
Url:		http://avahi.org/
Source0:	http://avahi.org/download/%{name}-%{version}.tar.gz
Source1:	avahi-hostname.sh
Source100:	%{name}.rpmlintrc
Patch0:		avahi-0.6.31-gtk-is-broken-beyond-repair-gtk-die-die-die.patch
Patch1:		avahi-0.6.31.workaround.patch
BuildRequires:	intltool
BuildRequires:	pygtk2.0
BuildRequires:	cap-devel
BuildRequires:	expat-devel >= 2.0.1
BuildRequires:	gdbm-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(libdaemon)
BuildRequires:	pkgconfig(libglade-2.0)
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

Requires(pre,preun,post,postun): rpm-helper
Requires(post,preun): dbus
Suggests:	nss_mdns

Requires(post):		rpm-helper
Requires(preun):	rpm-helper
Requires(post):		dbus
Requires(preun):	dbus

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
Requires(post,preun):	rpm-helper
Conflicts:	avahi < 0.6.31-8

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
Requires:	pygtk2.0-libglade
Requires:	python-twisted-core
Requires:	python-twisted-web
Requires:	python-dbus
Requires:	%{name} 
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
#BuildRequires:	avahi-ui-devel
Requires:	%{lib_client_name} = %{version}-%{release}
Requires:	%{lib_common_name} = %{version}-%{release}
Requires:	%{lib_glib_name} = %{version}-%{release}

%description sharp
Mono bindings for Avahi.

%package sharp-doc
Summary:	Development documentation for avahi-sharp
Group:		Development/Other
Requires(post,postun):	mono-tools >= 1.1.9

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
Requires:	%{lib_client_name} = %{version}-%{release}

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
Requires:	%{lib_common_name} = %{version}-%{release}

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
Requires:	%{lib_core_name} = %{version}-%{release}

%description -n %{develnamecore}
Devel library for avahi-core.

%package -n %{lib_dns_sd_name}
Group:		System/Libraries
Summary:	Avahi compatibility library for libdns_sd

%description -n %{lib_dns_sd_name}
Avahi compatibility library for libdns_sd

%package -n %{develnamedns_sd}
Group:		Development/C
Summary:	Avahi devel compatibility library for libdns_sd
Provides:	%{dns_sd_name}-devel = %{version}-%{release}
Requires:	%{lib_dns_sd_name} = %{version}-%{release}

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
Requires:	%{lib_glib_name} = %{version}-%{release}

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
Requires:	%{lib_gobject_name} = %{version}-%{release}

%description -n %{develnamegobject}
Devel library for avahi-gobject.

%package -n %{lib_howl_name}
Group:		System/Libraries
Summary:	Avahi compatibility library for howl

%description -n %{lib_howl_name}
Avahi compatibility library for howl.

%package -n %{develnamehowl}
Group:		Development/C
Summary:	Avahi devel compatibility library for libdns_sd for howl
Provides:	%{howl_name}-devel = %{version}-%{release}
Requires:	%{lib_howl_name} = %{version}-%{release}

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
Requires:	%{lib_qt3_name} = %{version}-%{release}

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
Requires:	%{lib_qt4_name} = %{version}-%{release}

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
Requires:	%{lib_ui_name} = %{version}-%{release}
Obsoletes:	%{_lib}avahi-ui1 < 0.6.31-6

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
%apply_patches
cp %{SOURCE1} avahi-hostname.sh
find . -name "Makefile*" -o -name "*.in" -o -name "*.ac" |sort |uniq |xargs sed -i -e 's,localstatedir\@/run,localstatedir\@,g;s,localstatedir}/run,localstatedir},g'
for f in config.guess config.sub ; do
        test -f /usr/share/libtool/config/$f || continue
        find . -type f -name $f -exec cp /usr/share/libtool/config/$f \{\} \;
done
aclocal -I common
automake -a
autoconf

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
	--localstatedir=/run \
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
%makeinstall_std

mkdir -p %{buildroot}%{_localstatedir}/avahi

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

rm -f %{buildroot}%{_sysconfdir}/avahi/services/sftp-ssh.service

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
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/%{name}-dbus.conf
%if !%{build_systemd}
 %{_initrddir}/%{name}-daemon
%endif
%attr(0755,avahi,avahi) %dir %{_localstatedir}/avahi
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
%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service
%endif

%files dnsconfd
%{_sysconfdir}/%{name}/%{name}-dnsconfd.action
%if !%{build_systemd}
%{_initrddir}/%{name}-dnsconfd
%else
%{_unitdir}/avahi-dnsconfd.service
%endif
%{_sbindir}/%{name}-dnsconfd
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

