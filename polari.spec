Summary:	IRC client for GNOME 3
Name:		polari
Version:	3.12.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/polari/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	284659630698500150bc6dda1ce612a1
URL:		https://wiki.gnome.org/Apps/Polari
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	telepathy-glib-devel
Requires(post,postun):  glib-gio-gsettings
Requires:	gjs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polari is an Internet Relay Chat (IRC) client designed for GNOME 3.

%prep
%setup -q

%build
%configure \
	GJS_CONSOLE=/usr/bin/gjs-console \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/polari/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/polari
%dir %{_libdir}/polari
%attr(755,root,root) %{_libdir}/polari/libpolari-1.0.so
%dir %{_libdir}/polari/girepository-1.0
%{_libdir}/polari/girepository-1.0/Polari-1.0.typelib
%{_datadir}/polari
%{_datadir}/dbus-1/services/org.gnome.Polari.service
%{_datadir}/glib-2.0/schemas/org.gnome.polari.gschema.xml
%{_desktopdir}/org.gnome.Polari.desktop
%{_iconsdir}/hicolor/*/apps/polari.*

