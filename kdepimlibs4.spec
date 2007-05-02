%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070502

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}


%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif


%define lib_major 5
%define lib_name_orig libkdepimlibs4
%define lib_name %mklibname kdepimlibs4 %{lib_major}
%define libqt %mklibname qt 4



Name: 		kdepimlibs4
Summary: 	K Desktop Environment - Libraries
Version: 	3.80.3
Release:	%mkrel 0.%branch_date.3
Group: 		Graphical desktop/KDE
License: 	ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: 	%_tmppath/%name-%version-%release-root
URL: 		http://www.kde.org
Packager:       Mandriva Linux KDE Team <kde@mandriva.com>
%if %branch
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepimlibs-%version-%branch_date.tar.bz2
%else
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepimlibs-%version.tar.bz2
%endif
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires:	openldap-devel

%description 
This module includes libraries that are central to the development and
execution of a KDE-PIM application.

The KDE-PIM project aims to bring together those who wish to help design,
implement, test, etc. anything that's to do with personal information
management.

This rather broad scope encompasses mail clients, addressbooks, usenet news,
scheduling and even sticky notes.


%package    common
Group:      Development/KDE and Qt
Summary:    Config file and icons file for %name.
Requires:	%lib_name = %version-%release

%description common
This packages contains all icons, config file etc...

%package -n %lib_name
Group:      Development/KDE and Qt
Summary:    Core libraries for KDE
Requires:   kdelibs4 >= %version-%mini_release

%description -n %lib_name
Libraries for the K Desktop Environment.


%package -n %lib_name-devel
Group:		Development/KDE and Qt
Summary:	Header files and documentation for compiling KDE applications.
Requires:	%{lib_name}
Requires:	kdelibs4-devel >= %version-%mini_release
Provides:	kdepimlibs4-devel

%description -n %lib_name-devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.


%prep
%setup -q -nkdepimlibs-%version-%branch_date

%build
cd $RPM_BUILD_DIR/kdepimlibs-%version-%branch_date
mkdir build
cd build
#use when we use standard %%prefix
#export QTDIR=%qt4dir
export QTDIR=/usr/lib/qt4/

export PATH=$QTDIR/bin:$PATH
cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
	../

%make


%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdepimlibs-%version-%branch_date/build/

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig


%files common
%defattr(-,root,root,-)
#move into progs
%dir %_datadir/apps/kabc/
%_datadir/apps/kabc/countrytransl.map
%dir %_datadir/apps/kabc/formats/
%_datadir/apps/kabc/formats/binary.desktop

%dir %_datadir/apps/libical/zoneinfo/
%dir %_datadir/apps/libical/zoneinfo/Africa/
%_datadir/apps/libical/zoneinfo/Africa/*.ics
%dir %_datadir/apps/libical/zoneinfo/America
%_datadir/apps/libical/zoneinfo/America/*.ics
%dir %_datadir/apps/libical/zoneinfo/Antarctica/
%_datadir/apps/libical/zoneinfo/Antarctica/*.ics
%dir %_datadir/apps/libical/zoneinfo/Arctic/
%_datadir/apps/libical/zoneinfo/Arctic/*.ics
%dir %_datadir/apps/libical/zoneinfo/Asia/
%_datadir/apps/libical/zoneinfo/Asia/*.ics
%dir %_datadir/apps/libical/zoneinfo/Atlantic/
%_datadir/apps/libical/zoneinfo/Atlantic/*.ics
%dir %_datadir/apps/libical/zoneinfo/Australia/
%_datadir/apps/libical/zoneinfo/Australia/*.ics
%dir %_datadir/apps/libical/zoneinfo/Europe/
%_datadir/apps/libical/zoneinfo/Europe/*.ics
%dir %_datadir/apps/libical/zoneinfo/Indian/
%_datadir/apps/libical/zoneinfo/Indian/*.ics
%dir %_datadir/apps/libical/zoneinfo/Pacific/
%_datadir/apps/libical/zoneinfo/Pacific/*.ics
%dir %_datadir/apps/libical/zoneinfo/America/Indiana/
%_datadir/apps/libical/zoneinfo/America/Kentucky/
%_datadir/apps/libical/zoneinfo/zones.tab
%_datadir/apps/libical/zoneinfo/America/Indiana/*.ics
%dir %_datadir/apps/libical/zoneinfo/America/Kentucky/
%_datadir/apps/libical/zoneinfo/America/Kentucky/*.ics
%dir %_datadir/apps/libical/zoneinfo/America/Argentina/
%_datadir/apps/libical/zoneinfo/America/Argentina/*.ics

%_datadir/autostart/kab2kabc.desktop
#TODO: Laurent: add categorie
%_datadir/kde4/services/kresources.desktop
%_datadir/kde4/services/kresources/kabc/*.desktop
%_datadir/kde4/services/kresources/*.desktop

%_datadir/kde4/services/kresources/kcal/*.desktop

%_datadir/kde4/servicetypes/*.desktop
%_datadir/config.kcfg/pimemoticons.kcfg

%files -n %{lib_name}
%defattr(-,root,root,-)
%_libdir/kde4/*.so
%_libdir/*.so.*


%files -n %lib_name-devel
%defattr(-,root,root,-)
%_datadir/dbus-1/interfaces/org.kde.KResourcesManager.xml
%dir %_includedir/kabc/
%_includedir/kabc/*.h
%dir %_includedir/kcal/
%_includedir/kcal/*.h
%dir %_includedir/kldap/
%_includedir/kldap/*.h
%dir %_includedir/kmime/
%_includedir/kmime/*.h
%dir %_includedir/kresources/
%_includedir/kresources/*.h
%dir %_includedir/ktnef/
%_includedir/ktnef/*.h
%dir %_includedir/kxmlrpcclient/
%_includedir/kxmlrpcclient/*.h
%dir %_includedir/syndication/
%_includedir/syndication/*.h
%dir %_includedir/syndication/atom/
%_includedir/syndication/atom/*.h
%dir %_includedir/syndication/rdf/
%_includedir/syndication/rdf/*.h
%dir %_includedir/syndication/rss2/
%_includedir/syndication/rss2/*.h
%dir %_includedir/kblog/
%_includedir/kblog/*.h
%dir %_includedir/kimap/
%_includedir/kimap/*.h
%dir %_includedir/kpimutils/
%_includedir/kpimutils/*.h

%_libdir/*.so
%_datadir/apps/cmake/modules/*.cmake


