# Note that this is NOT a relocatable package
%define ver      1.64
%define rel      1
%define prefix   /usr

Summary: A Panel Applet for the GNOME GUI desktop environment.
Name: gnotes_applet
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/Productivity
Source: http://www.netcom.com/~spoon/gnotes/gnotes_applet-%{ver}.tar.gz
BuildRoot: /var/tmp/gnotes_applet-root
# Obsoletes: 

URL: http://www.netcom.com/~spoon/gnotes/
Prereq: /sbin/install-info
Docdir: %{prefix}/doc

Requires: gnome-libs >= 1.0.0
Requires: ORBit >= 0.4.0

%description
GNotes 

%changelog

%prep
%setup

%build
# Needed for snapshot releases.
%ifarch alpha
  MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif
MYCFLAGS="$RPM_OPT_FLAGS"

if [ ! -f configure ]; then
  CFLAGS="$MYCFLAGS" ./autogen.sh $MYARCH_FLAGS --prefix=%prefix --sysconfdir=/etc --localstatedir=/var/lib
else
  CFLAGS="$MYCFLAGS" ./configure $MYARCH_FLAGS --prefix=%prefix --sysconfdir=/etc --localstatedir=/var/lib
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%config /etc
%{prefix}/bin
%{prefix}/share
