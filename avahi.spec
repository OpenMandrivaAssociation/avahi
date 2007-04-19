%define name avahi
%define version 0.6.18

%define release %mkrel 1

%define client_name     %{name}-client
%define common_name     %{name}-common
%define core_name       %{name}-core
%define dns_sd_name     %{name}-compat-libdns_sd
%define glib_name       %{name}-glib
%define howl_name       %{name}-compat-howl
%define qt3_name        %{name}-qt3
%define qt4_name        %{name}-qt4

%define dns_sd_old_name mDNSResponder
%define howl_old_name   howl

%define client_major 3
%define common_major 3
%define core_major 5
%define dns_sd_major 1
%define glib_major 1
%define howl_major 0
%define qt3_major 1
%define qt4_major 1

%define lib_client_name %mklibname %{client_name} %{client_major}
%define lib_common_name %mklibname %{common_name} %{common_major}
%define lib_core_name   %mklibname %{core_name} %{core_major}
%define lib_dns_sd_name %mklibname %{dns_sd_name} %{dns_sd_major}
%define lib_glib_name   %mklibname %{glib_name} %{glib_major}
%define lib_howl_name   %mklibname %{howl_name} %{howl_major}
%define lib_qt3_name    %mklibname %{qt3_name}_ %{qt3_major}
%define lib_qt4_name    %mklibname %{qt4_name}_ %{qt3_major}

%define lib_dns_sd_old_name %mklibname %{dns_sd_old_name} 1
%define lib_howl_old_name   %mklibname %{howl_old_name} 0
%define lib_howl_fake_EVR   1.0.0-7mdk

%define build_mono 1
%{?_with_mono: %{expand: %%global build_mono 1}} 
%{?_without_mono: %{expand: %%global build_mono 0}} 

%define build_qt4 1
%{?_with_qt4: %{expand: %%global build_qt4 1}}
%{?_without_qt4: %{expand: %%global build_qt4 0}}

%define build_bootstrap 0
%{?_with_bootstrap: %{expand: %%global build_bootstrap 1}}
%if %{build_bootstrap}
%define build_mono 0
%define build_qt4 0
%endif

Summary: Avahi service discovery (mDNS/DNS-SD) suite
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://avahi.org/download/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Servers
Url: http://avahi.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	daemon-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-python
BuildRequires:	libexpat-devel
BuildRequires:	libgdbm-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	pygtk2.0
BuildRequires:	qt3-devel
%if %build_qt4
BuildRequires:	qt4-devel
%endif
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires(post): dbus
Requires(preun): dbus
Obsoletes: howl
Provides: howl
Obsoletes: tmdns
Provides: tmdns
Obsoletes: mDNSResponder
Provides: mDNSResponder

%description
Avahi is a system which facilitates service discovery on a local
network -- this means that you can plug your laptop or computer into a
network and instantly be able to view other people who you can chat
with, find printers to print to or find files being shared. This kind
of technology is already found in MacOS X (branded 'Rendezvous',
'Bonjour' and sometimes 'ZeroConf') and is very convenient.

%package dnsconfd
Group: System/Servers
Summary: Avahi DNS configuration server
Requires: %{name} = %{version}
Requires(post): rpm-helper
Requires(preun): rpm-helper
%description dnsconfd
avahi-dnsconfd is a small daemon which may be used to configure
conventional DNS servers using mDNS in a DHCP-like fashion.
Especially useful on IPv6.

%package x11
Group: System/Servers
Summary: Graphical tools for Avahi
Requires: %{name} = %{version}
%description x11
Graphical tools for Avahi.
It includes avahi-discover-standalone.

%package python
Group: System/Libraries
Summary: Python bindings and utilities for Avahi
Requires: pygtk2.0-libglade python-twisted-core
Requires: python-twisted-web dbus-python avahi 
%description python
Python bindings and utilities for Avahi.
It includes avahi-bookmarks and avahi-discover.

%if %build_mono
%package sharp
Group: System/Libraries
Summary: Mono bindings for Avahi
BuildRequires: mono-devel mono-tools
Requires: %lib_client_name = %version
Requires: %lib_common_name = %version
Requires: %lib_glib_name = %version

%description sharp
Mono bindings for Avahi.

%package sharp-doc
Summary: Development documentation for avahi-sharp
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description sharp-doc
This package contains the API documentation for the avahi-sharp in
Monodoc format.
%endif

%package -n %{lib_client_name}
Group: System/Libraries
Summary: Library for avahi-client
Requires: %{name} = %{version}
%description -n %{lib_client_name}
Library for avahi-client.

%package -n %{lib_client_name}-devel
Group: Development/C
Summary: Devel library for avahi-client
Provides: %{client_name}-devel = %{version}-%{release}
Provides: lib%{client_name}-devel = %{version}-%{release}
Requires: %{lib_client_name} = %{version}
%description -n %{lib_client_name}-devel
Devel library for avahi-client.

%package -n %{lib_common_name}
Group: System/Libraries
Summary: Library for avahi-common
%description -n %{lib_common_name}
Library for avahi-common.

%package -n %{lib_common_name}-devel
Group: Development/C
Summary: Devel library for avahi-common
Provides: %{common_name}-devel = %{version}-%{release}
Provides: lib%{common_name}-devel = %{version}-%{release}
Requires: %{lib_common_name} = %{version}
%description -n %{lib_common_name}-devel
Devel library for avahi-common.

%package -n %{lib_core_name}
Group: System/Libraries
Summary: Library for avahi-core
%description -n %{lib_core_name}
Library for avahi-core.

%package -n %{lib_core_name}-devel
Group: Development/C
Summary: Devel library for avahi-core
Provides: %{core_name}-devel = %{version}-%{release}
Provides: lib%{core_name}-devel = %{version}-%{release}
Requires: %{lib_core_name} = %{version}
%description -n %{lib_core_name}-devel
Devel library for avahi-core.

%package -n %{lib_dns_sd_name}
Group: System/Libraries
Summary: Avahi compatibility library for libdns_sd
Obsoletes: %{lib_dns_sd_old_name}
Provides: %{lib_dns_sd_old_name}
%description -n %{lib_dns_sd_name}
Avahi compatibility library for libdns_sd

%package -n %{lib_dns_sd_name}-devel
Group: Development/C
Summary: Avahi devel compatibility library for libdns_sd
Provides: %{dns_sd_name}-devel = %{version}-%{release}
Provides: lib%{dns_sd_name}-devel = %{version}-%{release}
Requires: %{lib_dns_sd_name} = %{version}
Obsoletes: %{lib_dns_sd_old_name}-devel
Provides: %{lib_dns_sd_old_name}-devel
Provides: %{dns_sd_old_name}-devel = %{version}-%{release}
Provides: lib%{dns_sd_old_name}-devel = %{version}-%{release}
%description -n %{lib_dns_sd_name}-devel
Avahi devel compatibility library for libdns_sd.

%package -n %{lib_glib_name}
Group: System/Libraries
Summary: Library for avahi-glib
%description -n %{lib_glib_name}
Library for avahi-glib.

%package -n %{lib_glib_name}-devel
Group: Development/C
Summary: Devel library for avahi-glib
Provides: %{glib_name}-devel = %{version}-%{release}
Provides: lib%{glib_name}-devel = %{version}-%{release}
Requires: %{lib_glib_name} = %{version}
%description -n %{lib_glib_name}-devel
Devel library for avahi-glib.

%package -n %{lib_howl_name}
Group: System/Libraries
Summary: Avahi compatibility library for howl
Obsoletes: %{lib_howl_old_name}
Provides: %{lib_howl_old_name} = %{lib_howl_fake_EVR}
%description -n %{lib_howl_name}
Avahi compatibility library for howl.

%package -n %{lib_howl_name}-devel
Group: Development/C
Summary: Avahi devel compatibility library for libdns_sd for howl
Provides: %{howl_name}-devel = %{version}-%{release}
Provides: lib%{howl_name}-devel = %{version}-%{release}
Requires: %{lib_howl_name} = %{version}
Obsoletes: %{lib_howl_old_name}-devel
Provides: %{lib_howl_old_name}-devel = %{lib_howl_fake_EVR}
Provides: %{howl_old_name}-devel = %{version}-%{release}
Provides: lib%{howl_old_name}-devel = %{version}-%{release}
%description -n %{lib_howl_name}-devel
Avahi devel compatibility library for libdns_sd for howl.

%package -n %{lib_qt3_name}
Group: System/Libraries
Summary: Library for avahi-qt3
%description -n %{lib_qt3_name}
Library for avahi-qt3.

%package -n %{lib_qt3_name}-devel
Group: Development/C
Summary: Devel library for avahi-qt3
Provides: %{qt3_name}-devel = %{version}-%{release}
Provides: lib%{qt3_name}-devel = %{version}-%{release}
Requires: %{lib_qt3_name} = %{version}
%description -n %{lib_qt3_name}-devel
Devel library for avahi-qt3.

%if %build_qt4
%package -n %{lib_qt4_name}
Group: System/Libraries
Summary: Library for avahi-qt4
%description -n %{lib_qt4_name}
Library for avahi-qt4.

%package -n %{lib_qt4_name}-devel
Group: Development/C
Summary: Devel library for avahi-qt4
Provides: %{qt4_name}-devel = %{version}-%{release}
Provides: lib%{qt4_name}-devel = %{version}-%{release}
Requires: %{lib_qt4_name} = %{version}
%description -n %{lib_qt4_name}-devel
Devel library for avahi-qt4.
%endif

%prep
%setup -q

%build
export PKG_CONFIG_PATH=/usr/lib/qt4/%{_lib}/pkgconfig
%configure2_5x \
%if !%build_mono
    --disable-mono \
%endif
%if !%build_qt4
    --disable-qt4 \
%endif
  --localstatedir=%{_var} \
  --with-avahi-priv-access-group="avahi" \
  --with-dbus-system-address="unix:path=%{_var}/run/dbus/system_dbus_socket" \
  --enable-compat-libdns_sd \
  --enable-compat-howl
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/services/ssh.service
ln -s avahi-compat-howl.pc %buildroot%_libdir/pkgconfig/howl.pc
%if "%_lib" != "lib" && %build_mono
mkdir -p %buildroot%_prefix/lib
mv %buildroot%_libdir/mono %buildroot%_prefix/lib
perl -pi -e "s/%_lib/lib/" %buildroot%_libdir/pkgconfig/avahi-sharp.pc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%_pre_useradd %{name} %{_var}/%{name} /bin/false

%postun
%_postun_userdel %{name}

%post
%_post_service %{name}-daemon

%preun
%_preun_service %{name}-daemon

%post dnsconfd
%_post_service %{name}-dnsconfd

%preun dnsconfd
%_preun_service %{name}-dnsconfd

%post -n %{lib_client_name} -p /sbin/ldconfig
%postun -n %{lib_client_name} -p /sbin/ldconfig

%post -n %{lib_common_name} -p /sbin/ldconfig
%postun -n %{lib_common_name} -p /sbin/ldconfig

%post -n %{lib_core_name} -p /sbin/ldconfig
%postun -n %{lib_core_name} -p /sbin/ldconfig

%post -n %{lib_dns_sd_name} -p /sbin/ldconfig
%postun -n %{lib_dns_sd_name} -p /sbin/ldconfig

%post -n %{lib_glib_name} -p /sbin/ldconfig
%postun -n %{lib_glib_name} -p /sbin/ldconfig

%post -n %{lib_howl_name} -p /sbin/ldconfig
%postun -n %{lib_howl_name} -p /sbin/ldconfig

%post -n %{lib_qt3_name} -p /sbin/ldconfig
%postun -n %{lib_qt3_name} -p /sbin/ldconfig

%if %build_qt4
%post -n %{lib_qt4_name} -p /sbin/ldconfig
%postun -n %{lib_qt4_name} -p /sbin/ldconfig
%endif

%if %build_mono
%post sharp-doc
%_bindir/monodoc --make-index > /dev/null
%postun sharp-doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi
%endif

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/services/
%config(noreplace) %{_sysconfdir}/%{name}/hosts
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-daemon.conf
%config(noreplace) %{_sysconfdir}/%{name}/avahi-autoipd.action
%config(noreplace) %{_sysconfdir}/%{name}/services/sftp-ssh.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/%{name}-dbus.conf
%{_initrddir}/%{name}-daemon
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
%{_datadir}/%{name}/introspection/AddressResolver.introspect
%{_datadir}/%{name}/introspection/DomainBrowser.introspect
%{_datadir}/%{name}/introspection/EntryGroup.introspect
%{_datadir}/%{name}/introspection/HostNameResolver.introspect
%{_datadir}/%{name}/introspection/RecordBrowser.introspect
%{_datadir}/%{name}/introspection/Server.introspect
%{_datadir}/%{name}/introspection/ServiceBrowser.introspect
%{_datadir}/%{name}/introspection/ServiceResolver.introspect
%{_datadir}/%{name}/introspection/ServiceTypeBrowser.introspect
%{_datadir}/%{name}/service-types
%{_datadir}/%{name}/service-types.db
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

%files dnsconfd
%defattr(-,root,root)
%{_sysconfdir}/%{name}/%{name}-dnsconfd.action
%{_initrddir}/%{name}-dnsconfd
%{_sbindir}/%{name}-dnsconfd
%{_mandir}/man8/%{name}-dnsconfd.8*
%{_mandir}/man8/%{name}-dnsconfd.action.8*

%files x11
%defattr(-,root,root)
%{_bindir}/%{name}-discover-standalone

%files python
%defattr(-,root,root)
%{_bindir}/%{name}-bookmarks
%{_bindir}/%{name}-discover
%{py_puresitedir}/%{name}/*.py*
%{_datadir}/applications/%{name}-discover.desktop
%{_datadir}/%{name}/interfaces/%{name}-discover.glade
%{_mandir}/man1/%{name}-discover.1*
%{_mandir}/man1/%{name}-bookmarks.1*

%if %build_mono
%files sharp
%defattr(-,root,root)
%{_prefix}/lib/mono/%{name}-sharp/%{name}-sharp.dll
%{_prefix}/lib/mono/gac/%{name}-sharp/
%{_libdir}/pkgconfig/%{name}-sharp.pc

%files sharp-doc
%defattr(-,root,root)
%{_usr}/lib/monodoc/sources/%{name}-sharp-docs.source
%{_usr}/lib/monodoc/sources/%{name}-sharp-docs.tree
%{_usr}/lib/monodoc/sources/%{name}-sharp-docs.zip
%endif

%files -n %{lib_client_name}
%defattr(-,root,root)
%{_libdir}/lib%{name}-client.so.%{client_major}*

%files -n %{lib_common_name}
%defattr(-,root,root)
%{_libdir}/lib%{name}-common.so.%{common_major}*

%files -n %{lib_core_name}
%defattr(-,root,root)
%{_libdir}/lib%{name}-core.so.%{core_major}*

%files -n %{lib_dns_sd_name}
%defattr(-,root,root)
%{_libdir}/libdns_sd.so.%{dns_sd_major}*

%files -n %{lib_glib_name}
%defattr(-,root,root)
%{_libdir}/lib%{name}-glib.so.%{glib_major}*

%files -n %{lib_howl_name}
%defattr(-,root,root)
%{_libdir}/libhowl.so.%{howl_major}*

%files -n %{lib_qt3_name}
%defattr(-,root,root)
%{_libdir}/lib%{name}-qt3.so.%{qt3_major}*

%if %build_qt4
%files -n %{lib_qt4_name}
%defattr(-,root,root)
%{_libdir}/lib%{name}-qt4.so.%{qt4_major}*
%endif

%files -n %{lib_client_name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}-client
%{_libdir}/lib%{name}-client.a
%attr(644,root,root) %{_libdir}/lib%{name}-client.la
%{_libdir}/lib%{name}-client.so
%{_libdir}/pkgconfig/%{name}-client.pc

%files -n %{lib_common_name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}-common
%{_libdir}/lib%{name}-common.a
%attr(644,root,root) %{_libdir}/lib%{name}-common.la
%{_libdir}/lib%{name}-common.so

%files -n %{lib_core_name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}-core
%{_libdir}/lib%{name}-core.a
%attr(644,root,root) %{_libdir}/lib%{name}-core.la
%{_libdir}/lib%{name}-core.so
%{_libdir}/pkgconfig/%{name}-core.pc

%files -n %{lib_dns_sd_name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}-compat-libdns_sd
%{_libdir}/libdns_sd.a
%attr(644,root,root) %{_libdir}/libdns_sd.la
%{_libdir}/libdns_sd.so
%{_libdir}/pkgconfig/%{name}-compat-libdns_sd.pc

%files -n %{lib_glib_name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}-glib
%{_libdir}/lib%{name}-glib.a
%attr(644,root,root) %{_libdir}/lib%{name}-glib.la
%{_libdir}/lib%{name}-glib.so
%{_libdir}/pkgconfig/%{name}-glib.pc

%files -n %{lib_howl_name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}-compat-howl
%{_libdir}/libhowl.a
%attr(644,root,root) %{_libdir}/libhowl.la
%{_libdir}/libhowl.so
%{_libdir}/pkgconfig/%{name}-compat-howl.pc
%{_libdir}/pkgconfig/howl.pc

%files -n %{lib_qt3_name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}-qt3
%{_libdir}/lib%{name}-qt3.a
%attr(644,root,root) %{_libdir}/lib%{name}-qt3.la
%{_libdir}/lib%{name}-qt3.so
%{_libdir}/pkgconfig/%{name}-qt3.pc

%if %build_qt4
%files -n %{lib_qt4_name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}-qt4
%{_libdir}/lib%{name}-qt4.a
%attr(644,root,root) %{_libdir}/lib%{name}-qt4.la
%{_libdir}/lib%{name}-qt4.so
%{_libdir}/pkgconfig/%{name}-qt4.pc
%endif


