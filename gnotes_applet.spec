Summary:	GNotes - a Panel Applet for the GNOME GUI desktop environment
Summary(pl):	GNotes - aplet dla panelu Gnome
Name:		gnotes_applet
Version:	1.64
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	http://www.netcom.com/~spoon/gnotes/%{name}-%{version}.tar.bz2
URL:		http://www.netcom.com/~spoon/gnotes/
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

%description
GNotes is a GNOME Panel Applet that allows you to place cool little
yellow sticky notes all over your desktop. The notes are similar to
those little yellow paper sticky notes that are plastered around the
edges of your monitor.

GNotes are a GREEN (environmentally friendly) alternative to those
paper sticky notes. GNotes are 100% virtual, 100% paper free, and
constructed of 100% recycled pixels.

%description -l pl
GNotes to aplet panelu GNOME pozwalaj±cy umieszczaæ ma³e ¿ó³te notatki
na ca³ym desktopie. Te notatki s± podobne do ¿ó³tych karteczek
przyklejanych naoko³o monitora.

GNotes s± zielon± (przyjazn± dla ¶rodowiska) alternatyw± dla
papierowych notatek. S± w 100% wirtualne, w 100% wolne od papieru i
sk³adaj± siê w 100% ze zdatnych do ponownego u¿ycia pikseli.

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%config /etc
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applets/Utility/*
