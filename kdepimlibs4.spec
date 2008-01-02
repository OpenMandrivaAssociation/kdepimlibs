%define revision 751976

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

Name: kdepimlibs4
Summary: Libraries of the KDE-PIM project
Version: 3.97.1
Release: %mkrel 0.%revision.1
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepimlibs-%version.%revision.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepimlibs-%version.tar.bz2
%endif
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel
BuildRequires: openldap-devel
BuildRequires: boost-devel
BuildRequires: gpgme-devel

%description 
This module includes libraries that are central to the development and
execution of a KDE-PIM application.

The KDE-PIM project aims to bring together those who wish to help design,
implement, test, etc. anything that's to do with personal information
management.

This rather broad scope encompasses mail clients, addressbooks, usenet news,
scheduling and even sticky notes.

#--------------------------------------------------------------------------------

%package core
Group: Development/KDE and Qt
Summary: Config file and icons file for %name
Obsoletes: kdepimlibs4-common < 3.93.0-0.714098.1
Obsoletes: kdepim4-ioslaves < 3.93.0-0.714098.1
Provides: kio4-imap
Provides: kio4-ldap
Provides: kio4-pop3

%description core
This packages contains all icons, config file etc...

%files core
%defattr(-,root,root,-)
%_kde_libdir/kde4/*
%_kde_datadir/apps/*
%_kde_datadir/kde4/*
%_datadir/dbus-1/interfaces/*
%exclude %_kde_datadir/apps/cmake

#------------------------------------------------	

%define libkabc %mklibname kabc 4

%package -n %libkabc
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kabc5 < 3.93.0-0.714098.1

%description -n %libkabc
KDE 4 core library.

%post -n %libkabc -p /sbin/ldconfig
%postun -n %libkabc -p /sbin/ldconfig

%files -n %libkabc
%defattr(-,root,root)
%_kde_libdir/libkabc.so.*

#------------------------------------------------	

%define libkblog %mklibname kblog 4

%package -n %libkblog
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kblog5 < 3.93.0-0.714098.1

%description -n %libkblog
KDE 4 core library.

%post -n %libkblog -p /sbin/ldconfig
%postun -n %libkblog -p /sbin/ldconfig

%files -n %libkblog
%defattr(-,root,root)
%_kde_libdir/libkblog.so.*

#------------------------------------------------	

%define libkabc_file_core %mklibname kabc_file_core 4

%package -n %libkabc_file_core
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kabc_file_core5 < 3.93.0-0.714098.1

%description -n %libkabc_file_core
KDE 4 core library.

%post -n %libkabc_file_core -p /sbin/ldconfig
%postun -n %libkabc_file_core -p /sbin/ldconfig

%files -n %libkabc_file_core
%defattr(-,root,root)
%_kde_libdir/libkabc_file_core.so.*

#------------------------------------------------	

%define libkcal %mklibname kcal 4

%package -n %libkcal
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kcal5 < 3.93.0-0.714098.1

%description -n %libkcal
KDE 4 core library.

%post -n %libkcal -p /sbin/ldconfig
%postun -n %libkcal -p /sbin/ldconfig

%files -n %libkcal
%defattr(-,root,root)
%_kde_libdir/libkcal.so.*

#------------------------------------------------	

%define libkimap %mklibname kimap 4

%package -n %libkimap
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kimap5 < 3.93.0-0.714098.1

%description -n %libkimap
KDE 4 core library.

%post -n %libkimap -p /sbin/ldconfig
%postun -n %libkimap -p /sbin/ldconfig

%files -n %libkimap
%defattr(-,root,root)
%_kde_libdir/libkimap.so.*

#------------------------------------------------	

%define libkldap %mklibname kldap 4

%package -n %libkldap
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kldap5 < 3.93.0-0.714098.1

%description -n %libkldap
KDE 4 core library.

%post -n %libkldap -p /sbin/ldconfig
%postun -n %libkldap -p /sbin/ldconfig

%files -n %libkldap
%defattr(-,root,root)
%_kde_libdir/libkldap.so.*

#------------------------------------------------	

%define libkmime %mklibname kmime 4

%package -n %libkmime
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kmime5 < 3.93.0-0.714098.1

%description -n %libkmime
KDE 4 core library.

%post -n %libkmime -p /sbin/ldconfig
%postun -n %libkmime -p /sbin/ldconfig

%files -n %libkmime
%defattr(-,root,root)
%_kde_libdir/libkmime.so.*

#------------------------------------------------	

%define libkpimutils %mklibname kpimutils 4

%package -n %libkpimutils
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kpimutils5 < 3.93.0-0.714098.1

%description -n %libkpimutils
KDE 4 core library.

%post -n %libkpimutils -p /sbin/ldconfig
%postun -n %libkpimutils -p /sbin/ldconfig

%files -n %libkpimutils
%defattr(-,root,root)
%_kde_libdir/libkpimutils.so.*

#------------------------------------------------	

%define libkresources %mklibname kresources 4

%package -n %libkresources
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kresources5 < 3.93.0-0.714098.1

%description -n %libkresources
KDE 4 core library.

%post -n %libkresources -p /sbin/ldconfig
%postun -n %libkresources -p /sbin/ldconfig

%files -n %libkresources
%defattr(-,root,root)
%_kde_libdir/libkresources.so.*

#------------------------------------------------	

%define libktnef %mklibname ktnef 4

%package -n %libktnef
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}ktnef5 < 3.93.0-0.714098.1

%description -n %libktnef
KDE 4 core library.

%post -n %libktnef -p /sbin/ldconfig
%postun -n %libktnef -p /sbin/ldconfig

%files -n %libktnef
%defattr(-,root,root)
%_kde_libdir/libktnef.so.*

#------------------------------------------------	

%define libkxmlrpcclient %mklibname kxmlrpcclient 4

%package -n %libkxmlrpcclient
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kxmlrpcclient5 < 3.93.0-0.714098.1

%description -n %libkxmlrpcclient
KDE 4 core library.

%post -n %libkxmlrpcclient -p /sbin/ldconfig
%postun -n %libkxmlrpcclient -p /sbin/ldconfig

%files -n %libkxmlrpcclient
%defattr(-,root,root)
%_kde_libdir/libkxmlrpcclient.so.*

#------------------------------------------------	

%define libmailtransport %mklibname mailtransport 4

%package -n %libmailtransport
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}mailtransport5 < 3.93.0-0.714098.1

%description -n %libmailtransport
KDE 4 core library.

%post -n %libmailtransport -p /sbin/ldconfig
%postun -n %libmailtransport -p /sbin/ldconfig

%files -n %libmailtransport
%defattr(-,root,root)
%_kde_libdir/libmailtransport.so.*

#------------------------------------------------	

%define libsyndication %mklibname syndication 4

%package -n %libsyndication
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}syndication5 < 3.93.0-0.714098.1

%description -n %libsyndication
KDE 4 core library.

%post -n %libsyndication -p /sbin/ldconfig
%postun -n %libsyndication -p /sbin/ldconfig

%files -n %libsyndication
%defattr(-,root,root)
%_kde_libdir/libsyndication.so.*

#--------------------------------------------------------------------------------

%define libqgpgme %mklibname qgpgme 4

%package -n %libqgpgme
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}qgpgme5 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kleo4 < 3.93.0-0.714098.1

%description -n %libqgpgme
KDE 4 core library.

%post -n %libqgpgme -p /sbin/ldconfig
%postun -n %libqgpgme -p /sbin/ldconfig

%files -n %libqgpgme
%defattr(-,root,root)
%_kde_libdir/libqgpgme.so.*

#--------------------------------------------------------------------------------

%define libgpgmepp %mklibname gpgme++ 4

%package -n %libgpgmepp
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}gpgmepp5 < 3.93.0-0.714098.1
Obsoletes: %{_lib}gpgmepp4 < 3.93.0-0.714098.1

%description -n %libgpgmepp
KDE 4 core library.

%post -n %libgpgmepp -p /sbin/ldconfig
%postun -n %libgpgmepp -p /sbin/ldconfig

%files -n %libgpgmepp
%defattr(-,root,root)
%_kde_libdir/libgpgme+*.so.*

#--------------------------------------------------------------------------------

%define libkpimidentities %mklibname kpimidentities 4

%package -n %libkpimidentities
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kpimidentities5 < 3.93.0-0.714098.1

%description -n %libkpimidentities
KDE 4 core library.

%post -n %libkpimidentities -p /sbin/ldconfig
%postun -n %libkpimidentities -p /sbin/ldconfig

%files -n %libkpimidentities
%defattr(-,root,root)
%_kde_libdir/libkpimidentities.so.*

#--------------------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KDE applications
Requires: kdelibs4-devel
Provides: libkdepimlibs4-devel
Requires: %libkabc = %version
Requires: %libkblog = %version
Requires: %libkabc_file_core = %version
Requires: %libkcal = %version
Requires: %libkimap = %version
Requires: %libkldap = %version
Requires: %libkmime = %version
Requires: %libkpimutils = %version
Requires: %libkresources = %version
Requires: %libktnef = %version
Requires: %libkxmlrpcclient = %version
Requires: %libmailtransport = %version
Requires: %libsyndication = %version
Requires: %libqgpgme = %version
Requires: %libgpgmepp = %version
Requires: %libkpimidentities = %version

%description devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.

%files devel
%defattr(-,root,root,-)
%_kde_prefix/include/*
%_kde_libdir/*.so
%_kde_datadir/apps/cmake/*/*
%_kde_libdir/gpgmepp/*.cmake
%_kde_datadir/config.kcfg/*

#--------------------------------------------------------------------------------

%prep
%setup -q -n kdepimlibs-%version

%build
%cmake_kde4 

%make


%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install
rm -f %buildroot/%{_kde_libdir}/Gpgmepp/GpgmeppConfig.cmake
rm -f %buildroot/%{_kde_libdir}/Gpgmepp/GpgmeppLibraryDepends.cmake

%clean
rm -fr %buildroot

