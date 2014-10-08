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
%define lib_qt3_name %mklibname %{qt3_name}_ %{qt3_major}
%define develnameqt3 %mklibname %{qt3_name} -d
%define lib_qt4_name %mklibname %{qt4_name}_ %{qt4_major}
%define develnameqt4 %mklibname %{qt4_name} -d
%define lib_ui_name %mklibname %{ui_name} %{ui_major}
%define develnameui %mklibname %{ui_name} -d
%define lib_ui_gtk3_name %mklibname %{ui_gtk3_name}_ %{ui_gtk3_major}
%define develnameui_gtk3 %mklibname %{ui_gtk3_name} -d

%ifnarch %{arm} %{mips} aarch64
%bcond_without mono
%else
%bcond_with mono
%endif

%bcond_with	qt3
%bcond_without	qt4
%bcond_without	gtk3
%bcond_with	pygtk
%bcond_without	systemd
%bcond_with	python

Summary:	Avahi service discovery (mDNS/DNS-SD) suite
Name:		avahi
Version:	0.6.31
Release:	18
License:	LGPLv2+
Group:		System/Servers
Url:		http://avahi.org/
Source0:	http://avahi.org/download/%{name}-%{version}.tar.gz
Source1:	avahi-hostname.sh
Source100:	%{name}.rpmlintrc
Patch0:		avahi-0.6.31-gtk-is-broken-beyond-repair-gtk-die-die-die.patch
Patch1:		avahi-0.6.31.workaround.patch
BuildRequires:	intltool
%if %{with pygtk}
BuildRequires:	pygtk2.0
%endif
BuildRequires:	cap-devel
BuildRequires:	expat-devel >= 2.0.1
BuildRequires:	gdbm-devel
BuildRequires:	pkgconfig(dbus-1)
%if %{with python}
BuildRequires:	pkgconfig(dbus-python)
%endif
BuildRequires:	pkgconfig(libdaemon)
BuildRequires:	pkgconfig(libglade-2.0)
%if %{with qt3}
BuildRequires:	pkgconfig(qt-mt)
%endif
%if %{with qt4}
BuildRequires:	pkgconfig(QtCore)
%endif
%if %{with gtk3}
BuildRequires:	pkgconfig(gtk+-3.0)
%endif
%if %{with systemd}
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

%files -f avahi.lang
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/services/
%config(noreplace) %{_sysconfdir}/%{name}/hosts
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-daemon.conf
%config(noreplace) %{_sysconfdir}/%{name}/avahi-autoipd.action
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/%{name}-dbus.conf
%if !%{with systemd}
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
%if %{with python}
%{_libdir}/avahi/service-types.db
%endif
%if %{with systemd}
%{_unitdir}/avahi-daemon.service
%{_unitdir}/avahi-daemon.socket
%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service
%endif

%pre
%_pre_useradd %{name} %{_var}/%{name} /bin/false
%_pre_useradd %{name}-autoipd %{_var}/%{name} /bin/false

%postun
%_postun_userdel %{name}
%_postun_userdel %{name}-autoipd

%post
%systemd_post %{name}-daemon

%preun
%systemd_preun %{name}-daemon

#----------------------------------------------------------------------------

%package dnsconfd
Summary:	Avahi DNS configuration server
Group:		System/Servers
Requires:	%{name} = %{EVRD}
Requires(post,preun):	rpm-helper
Conflicts:	avahi < 0.6.31-8

%description dnsconfd
avahi-dnsconfd is a small daemon which may be used to configure
conventional DNS servers using mDNS in a DHCP-like fashion.
Especially useful on IPv6.

%files dnsconfd
%{_sysconfdir}/%{name}/%{name}-dnsconfd.action
%if !%{with systemd}
%{_initrddir}/%{name}-dnsconfd
%else
%{_unitdir}/avahi-dnsconfd.service
%endif
%{_sbindir}/%{name}-dnsconfd
%{_mandir}/man8/%{name}-dnsconfd.8*
%{_mandir}/man8/%{name}-dnsconfd.action.8*

%post dnsconfd
%systemd_post %{name}-dnsconfd

%preun dnsconfd
%systemd_preun %{name}-dnsconfd

#----------------------------------------------------------------------------

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
%{_mandir}/man1/bssh.1*
%{_mandir}/man1/bvnc.1*
%if %{with python}
%{_datadir}/applications/%{name}-discover.desktop
%endif
%{_datadir}/%{name}/interfaces/%{name}-discover.ui

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
%{_mandir}/man1/%{name}-discover.1*
%{_mandir}/man1/%{name}-bookmarks.1*
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
if [ "$1" = "0" -a -x %{_bindir}/monodoc ]; then %{_bindir}/monodoc --make-index > /dev/null
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
Provides:	%{dns_sd_name}-devel = %{EVRD}

%description -n %{develnamedns_sd}
Avahi devel compatibility library for libdns_sd.

%files -n %{develnamedns_sd}
%{_includedir}/%{name}-compat-libdns_sd
%{_libdir}/libdns_sd.so
%{_libdir}/pkgconfig/%{name}-compat-libdns_sd.pc

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
Provides:	%{howl_name}-devel = %{EVRD}

%description -n %{develnamehowl}
Avahi devel compatibility library for libdns_sd for howl.

%files -n %{develnamehowl}
%{_includedir}/%{name}-compat-howl
%{_libdir}/libhowl.so
%{_libdir}/pkgconfig/%{name}-compat-howl.pc
%{_libdir}/pkgconfig/howl.pc

#----------------------------------------------------------------------------

%if %{with qt3}
%package -n %{lib_qt3_name}
Summary:	Library for avahi-qt3
Group:		System/Libraries
Conflicts:	%{_lib}libavahi-ui1 < 0.6.31-15
Obsoletes:	%{_lib}libavahi-ui1 < 0.6.31-15

%description -n %{lib_qt3_name}
Library for avahi-qt3.

%files -n %{lib_qt3_name}
%{_libdir}/lib%{name}-qt3.so.%{qt3_major}*
%endif

#----------------------------------------------------------------------------

%if %{with qt3}
%package -n %{develnameqt3}
Summary:	Devel library for avahi-qt3
Group:		Development/C
Requires:	%{lib_qt3_name} = %{EVRD}
Provides:	%{qt3_name}-devel = %{EVRD}

%description -n %{develnameqt3}
Devel library for avahi-qt3.

%files -n %{develnameqt3}
%{_includedir}/%{name}-qt3
%{_libdir}/lib%{name}-qt3.so
%{_libdir}/pkgconfig/%{name}-qt3.pc
%endif

#----------------------------------------------------------------------------

%if %{with qt4}
%package -n %{lib_qt4_name}
Summary:	Library for avahi-qt4
Group:		System/Libraries

%description -n %{lib_qt4_name}
Library for avahi-qt4.

%files -n %{lib_qt4_name}
%{_libdir}/lib%{name}-qt4.so.%{qt4_major}*
%endif

#----------------------------------------------------------------------------

%if %{with qt4}
%package -n %{develnameqt4}
Summary:	Devel library for avahi-qt4
Group:		Development/C
Provides:	%{qt4_name}-devel = %{EVRD}
Requires:	%{lib_qt4_name} = %{EVRD}

%description -n %{develnameqt4}
Devel library for avahi-qt4.

%files -n %{develnameqt4}
%{_includedir}/%{name}-qt4
%{_libdir}/lib%{name}-qt4.so
%{_libdir}/pkgconfig/%{name}-qt4.pc
%endif

#----------------------------------------------------------------------------

%package -n %{lib_ui_name}
Summary:	Library for avahi-ui
Group:		System/Libraries

%description -n %{lib_ui_name}
Library for avahi-ui.

%files -n %{lib_ui_name}
%{_libdir}/lib%{name}-ui.so.%{ui_major}*

#----------------------------------------------------------------------------

%package -n %{develnameui}
Summary:	Devel library for avahi-ui
Group:		Development/C
Requires:	%{lib_ui_name} = %{EVRD}
Provides:	%{ui_name}-devel = %{EVRD}
Obsoletes:	%{_lib}avahi-ui1 < 0.6.31-6

%description -n %{develnameui}
Devel library for avahi-ui.

%files -n %{develnameui}
%{_includedir}/%{name}-ui
%{_libdir}/lib%{name}-ui.so
%{_libdir}/pkgconfig/%{name}-ui.pc

#----------------------------------------------------------------------------

%if %{with gtk3}
%package -n %{lib_ui_gtk3_name}
Summary:	Library for avahi-gtk3
Group:		System/Libraries

%description -n %{lib_ui_gtk3_name}
Library for avahi-gtk3.

%files -n %{lib_ui_gtk3_name}
%{_libdir}/lib%{name}-ui-gtk3.so.%{ui_gtk3_major}*
%endif

#----------------------------------------------------------------------------

%if %{with gtk3}
%package -n %{develnameui_gtk3}
Summary:	Devel library for avahi-gtk3
Group:		Development/C
Requires:	%{lib_ui_gtk3_name} = %{EVRD}
Provides:	%{ui_gtk3_name}-devel = %{EVRD}

%description -n %{develnameui_gtk3}
Devel library for avahi-gtk3.

%files -n %{develnameui_gtk3}
%{_libdir}/libavahi-ui-gtk3.so
%{_libdir}/pkgconfig/avahi-ui-gtk3.pc
%endif

#----------------------------------------------------------------------------

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
%configure \
	--disable-static \
	--with-distro=mandriva \
%if !%{with mono}
	--disable-mono \
%endif
%if !%{with qt3}
	--disable-qt3 \
%endif
%if !%{with qt4}
	--disable-qt4 \
%endif
	--localstatedir=/run \
	--with-avahi-priv-access-group="avahi" \
	--enable-compat-libdns_sd \
	--enable-compat-howl \
	--enable-introspection=no \
%if %{with systemd}
	--with-systemdsystemunitdir=%{_unitdir} \
%endif
%if !%{with gtk3}
	--disable-gtk3 \
%endif
%if !%{with pygtk}
	--disable-pygtk \
%endif
%if !%{with python}
	--disable-python
%endif

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_localstatedir}/avahi

rm -f %{buildroot}/%{_sysconfdir}/%{name}/services/ssh.service
ln -s avahi-compat-howl.pc %{buildroot}%{_libdir}/pkgconfig/howl.pc
%if "%{_lib}" != "lib" && %{with mono}
mkdir -p %{buildroot}%{_prefix}/lib
mv %{buildroot}%{_libdir}/mono %{buildroot}%{_prefix}/lib
perl -pi -e "s/%{_lib}/lib/" %{buildroot}%{_libdir}/pkgconfig/avahi-{,ui-}sharp.pc
%endif

# install hostname.d hook
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig/network-scripts/hostname.d/
install -m755 avahi-hostname.sh %{buildroot}/%{_sysconfdir}/sysconfig/network-scripts/hostname.d/avahi

%if %{with systemd}
rm -rf %{buildroot}%{_initrddir}/%{name}-daemon
rm -rf %{buildroot}%{_initrddir}/%{name}-dnsconfd
%endif

rm -f %{buildroot}%{_sysconfdir}/avahi/services/sftp-ssh.service

%find_lang %{name}

