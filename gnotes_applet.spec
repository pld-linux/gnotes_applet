Summary:	GNotes - a Panel Applet for the GNOME GUI desktop environment
Summary(pl.UTF-8):   GNotes - aplet dla panelu GNOME
Name:		gnotes_applet
Version:	1.64
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.netcom.com/~spoon/gnotes/%{name}-%{version}.tar.bz2
# Source0-md5:	53e841f47836e3f554b10c996844a14d
URL:		http://www.netcom.com/~spoon/gnotes/
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-core-devel >= 1.0.0
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
GNotes is a GNOME Panel Applet that allows you to place cool little
yellow sticky notes all over your desktop. The notes are similar to
those little yellow paper sticky notes that are plastered around the
edges of your monitor.

GNotes are a GREEN (environmentally friendly) alternative to those
paper sticky notes. GNotes are 100% virtual, 100% paper free, and
constructed of 100% recycled pixels.

%description -l pl.UTF-8
GNotes to aplet panelu GNOME pozwalający umieszczać małe żółte notatki
na całym desktopie. Te notatki są podobne do żółtych karteczek
przyklejanych naokoło monitora.

GNotes są zieloną (przyjazną dla środowiska) alternatywą dla
papierowych notatek. Są w 100% wirtualne, w 100% wolne od papieru i
składają się w 100% ze zdatnych do ponownego użycia pikseli.

%prep
%setup -q

sed -i -e '/AM_CONDITIONAL(FALSE/d' configure.in

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
# empty LINGUAS - no translations in any *.po (just empty msgstrs)
%configure \
	LINGUAS=""
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/gnotes_applet.gnorba
%{_datadir}/applets/Utility/*
