Summary:	A Panel Applet for the GNOME GUI desktop environment.
Name:		gnotes_applet
Version:	1.64
Release:	2
License:	GPL
Group:		Applications/Productivity
Source:		http://www.netcom.com/~spoon/gnotes/%{name}-%{version}.tar.bz2
URL:		http://www.netcom.com/~spoon/gnotes/
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

%description
GNotes is a GNOME Panel Applet that allows you to place cool little yellow
sticky notes all over your desktop. The notes are similar to those little
yellow paper sticky notes that are plastered around the edges of your
monitor.

GNotes are a GREEN (environmentally friendly) alternative to those paper
sticky notes. GNotes are 100% virtual, 100% paper free, and constructed of
100% recycled pixels.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
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
