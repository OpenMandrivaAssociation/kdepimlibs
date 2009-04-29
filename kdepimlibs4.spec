%define svnrevision svn954171

Name: kdepimlibs4
Summary: Libraries of the KDE-PIM project
Version: 4.2.70
Release: %mkrel 0.%svnrevision.1
Epoch:   2
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepimlibs-%version.%svnrevision.tar.bz2
BuildRequires: kdelibs4-devel >= 2:4.1.73
BuildRequires: openldap-devel
BuildRequires: boost-devel
BuildRequires: gpgme-devel
BuildRequires: akonadi-devel >= 0.80.0-3.808261.4
BuildRequires: xft2-devel
BuildRequires: xpm-devel
BuildRequires: libical-devel >= 0.41

%description 
This module includes libraries that are central to the development and
execution of a KDE-PIM application.

The KDE-PIM project aims to bring together those who wish to help design,
implement, test, etc. anything that's to do with personal information
management.

This rather broad scope encompasses mail clients, addressbooks, usenet news,
scheduling and even sticky notes.

#--------------------------------------------------------------------------------

%package   core
Group:     Development/KDE and Qt
Summary:   Config file and icons file for %name
Obsoletes: kdepimlibs4-common < 3.93.0-0.714098.1
Obsoletes: kdepim4-ioslaves < 3.93.0-0.714098.1
Provides:  kio4-imap
Provides:  kio4-ldap
Provides:  kio4-pop3

%description core
This packages contains all icons, config file etc... of kdepimlibs4.

%files core
%defattr(-,root,root,-)
%_kde_libdir/kde4/*
%_kde_datadir/apps/*
%_kde_datadir/kde4/*
%_kde_datadir/dbus-1/interfaces/*
%_kde_docdir/HTML/en/kcontrol/kresources
%_kde_docdir/HTML/en/kioslave/imap
%_kde_docdir/HTML/en/kioslave/ldap
%_kde_docdir/HTML/en/kioslave/nntp
%_kde_docdir/HTML/en/kioslave/pop3
%_kde_docdir/HTML/en/kioslave/smtp
%exclude %_kde_datadir/apps/cmake

#------------------------------------------------	

%define kabc_major 4
%define libkabc %mklibname kabc %kabc_major

%package -n %libkabc
Summary:    KDE 4 core library
Group:      System/Libraries
Obsoletes:  %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes:  %{_lib}kabc5 < 3.93.0-0.714098.1

%description -n %libkabc
KDE 4 core library.

%files -n %libkabc
%defattr(-,root,root)
%_kde_libdir/libkabc.so.%{kabc_major}*

#------------------------------------------------	

%define kblog_major 4
%define libkblog %mklibname kblog %{kblog_major}

%package -n %libkblog
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kblog5 < 3.93.0-0.714098.1

%description -n %libkblog
KDE 4 core library.

%files -n %libkblog
%defattr(-,root,root)
%_kde_libdir/libkblog.so.%{kblog_major}*

#------------------------------------------------	

%define kabc_file_core_major 4
%define libkabc_file_core %mklibname kabc_file_core %{kabc_file_core_major}

%package -n %libkabc_file_core
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kabc_file_core5 < 3.93.0-0.714098.1

%description -n %libkabc_file_core
KDE 4 core library.

%files -n %libkabc_file_core
%defattr(-,root,root)
%_kde_libdir/libkabc_file_core.so.%{kabc_file_core_major}*

#------------------------------------------------	

%define kcal_major 4
%define libkcal %mklibname kcal %{kcal_major}

%package -n %libkcal
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kcal5 < 3.93.0-0.714098.1

%description -n %libkcal
KDE 4 core library.

%files -n %libkcal
%defattr(-,root,root)
%_kde_libdir/libkcal.so.%{kcal_major}*

#------------------------------------------------	

%define kimap_major 4
%define libkimap %mklibname kimap %{kimap_major}

%package -n %libkimap
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kimap5 < 3.93.0-0.714098.1

%description -n %libkimap
KDE 4 core library.

%files -n %libkimap
%defattr(-,root,root)
%_kde_libdir/libkimap.so.%{kimap_major}*

#------------------------------------------------	

%define kldap_major 4
%define libkldap %mklibname kldap %{kldap_major}

%package -n %libkldap
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kldap5 < 3.93.0-0.714098.1

%description -n %libkldap
KDE 4 core library.

%files -n %libkldap
%defattr(-,root,root)
%_kde_libdir/libkldap.so.%{kldap_major}*

#------------------------------------------------	

%define kmime_major 4
%define libkmime %mklibname kmime %{kmime_major}

%package -n %libkmime
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kmime5 < 3.93.0-0.714098.1

%description -n %libkmime
KDE 4 core library.

%files -n %libkmime
%defattr(-,root,root)
%_kde_libdir/libkmime.so.%{kmime_major}*

#------------------------------------------------	

%define kpimutils_major 4
%define libkpimutils %mklibname kpimutils %{kpimutils_major}

%package -n %libkpimutils
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kpimutils5 < 3.93.0-0.714098.1

%description -n %libkpimutils
KDE 4 core library.

%files -n %libkpimutils
%defattr(-,root,root)
%_kde_libdir/libkpimutils.so.%{kpimutils_major}*

#------------------------------------------------	

%define kresources_major 4
%define libkresources %mklibname kresources %{kresources_major}

%package -n %libkresources
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kresources5 < 3.93.0-0.714098.1

%description -n %libkresources
KDE 4 core library.

%files -n %libkresources
%defattr(-,root,root)
%_kde_libdir/libkresources.so.%{kresources_major}*

#------------------------------------------------	

%define ktnef_major 4
%define libktnef %mklibname ktnef %{ktnef_major}

%package -n %libktnef
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}ktnef5 < 3.93.0-0.714098.1

%description -n %libktnef
KDE 4 core library.

%files -n %libktnef
%defattr(-,root,root)
%_kde_libdir/libktnef.so.%{ktnef_major}*

#------------------------------------------------	

%define kxmlrpcclient_major 4
%define libkxmlrpcclient %mklibname kxmlrpcclient %{kxmlrpcclient_major}

%package -n %libkxmlrpcclient
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kxmlrpcclient5 < 3.93.0-0.714098.1

%description -n %libkxmlrpcclient
KDE 4 core library.

%files -n %libkxmlrpcclient
%defattr(-,root,root)
%_kde_libdir/libkxmlrpcclient.so.%{kxmlrpcclient_major}*

#------------------------------------------------	

%define mailtransport_major 4
%define libmailtransport %mklibname mailtransport %{mailtransport_major}

%package -n %libmailtransport
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}mailtransport5 < 3.93.0-0.714098.1

%description -n %libmailtransport
KDE 4 core library.

%files -n %libmailtransport
%defattr(-,root,root)
%_kde_libdir/libmailtransport.so.%{mailtransport_major}*

#------------------------------------------------	

%define syndication_major 4
%define libsyndication %mklibname syndication %{syndication_major}

%package -n %libsyndication
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}syndication5 < 3.93.0-0.714098.1

%description -n %libsyndication
KDE 4 core library.

%files -n %libsyndication
%defattr(-,root,root)
%_kde_libdir/libsyndication.so.%{syndication_major}*

#--------------------------------------------------------------------------------

%define qgpgme_major 1
%define libqgpgme %mklibname qgpgme %{qgpgme_major}

%package -n %libqgpgme
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}qgpgme5 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kleo4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}qgpgme4

%description -n %libqgpgme
KDE 4 core library.

%files -n %libqgpgme
%defattr(-,root,root)
%_kde_libdir/libqgpgme.so.%{qgpgme_major}*

#--------------------------------------------------------------------------------

%define gpgmepp_major 2
%define libgpgmepp %mklibname gpgme++ %{gpgmepp_major}

%package -n %libgpgmepp
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}gpgmepp5 < 3.93.0-0.714098.1
Obsoletes: %{_lib}gpgmepp4
Obsoletes: %{_lib}gpgme++4

%description -n %libgpgmepp
KDE 4 core library.

%files -n %libgpgmepp
%defattr(-,root,root)
%_kde_libdir/libgpgme+*.so.%{gpgmepp_major}*

#--------------------------------------------------------------------------------

%define kpimidentities_major 4
%define libkpimidentities %mklibname kpimidentities %{kpimidentities_major}

%package -n %libkpimidentities
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdepimlibs4 < 3.93.0-0.714098.1
Obsoletes: %{_lib}kpimidentities5 < 3.93.0-0.714098.1

%description -n %libkpimidentities
KDE 4 core library.

%files -n %libkpimidentities
%defattr(-,root,root)
%_kde_libdir/libkpimidentities.so.%{kpimidentities_major}*

#------------------------------------------------	

%define akonadi_kde_major 4
%define libakonadi_kde %mklibname akonadi-kde %{akonadi_kde_major}

%package -n %libakonadi_kde
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libakonadi_kde
KDE 4 core library.

%files -n %libakonadi_kde
%defattr(-,root,root)
%_kde_libdir/libakonadi-kde.so.%{akonadi_kde_major}*


#------------------------------------------------

%define akonadi_kabc_major 4
%define libakonadi_kabc %mklibname akonadi-kabc %{akonadi_kabc_major}

%package -n %libakonadi_kabc
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libakonadi_kabc
KDE 4 core library.

%files -n %libakonadi_kabc
%defattr(-,root,root)
%_kde_libdir/libakonadi-kabc.so.%{akonadi_kabc_major}*

#------------------------------------------------	

%define akonadi_kmime_major 4
%define libakonadi_kmime %mklibname akonadi-kmime %{akonadi_kmime_major}

%package -n %libakonadi_kmime
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libakonadi_kmime
KDE 4 core library.

%files -n %libakonadi_kmime
%defattr(-,root,root)
%_kde_libdir/libakonadi-kmime.so.%{akonadi_kmime_major}*

#------------------------------------------------

%define kholidays_major 4
%define libkholidays %mklibname kholidays %{kholidays_major}

%package -n %libkholidays
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkholidays
KDE 4 core library.

%files -n %libkholidays
%defattr(-,root,root)
%_kde_libdir/libkholidays.so.%{kholidays_major}*

#------------------------------------------------	

%define kpimtextedit_major 4
%define libkpimtextedit %mklibname kpimtextedit %{kpimtextedit_major}

%package -n %libkpimtextedit
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkpimtextedit
KDE 4 core library.

%files -n %libkpimtextedit
%defattr(-,root,root)
%_kde_libdir/libkpimtextedit.so.%{kpimtextedit_major}*

#------------------------------------------------

%define microblog_major 4
%define libmicroblog %mklibname microblog %{microblog_major}

%package -n %libmicroblog
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libmicroblog
KDE 4 core library.

%files -n %libmicroblog
%defattr(-,root,root)
%_kde_libdir/libmicroblog.so.%{microblog_major}*

#------------------------------------------------


%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KDE applications
Requires: kdelibs4-devel
Provides: libkdepimlibs4-devel
Requires: %name-core = %epoch:%version
Requires: %libkabc = %epoch:%version
Requires: %libkblog = %epoch:%version
Requires: %libkabc_file_core = %epoch:%version
Requires: %libkcal = %epoch:%version
Requires: %libkimap = %epoch:%version
Requires: %libkldap = %epoch:%version
Requires: %libkmime = %epoch:%version
Requires: %libkpimutils = %epoch:%version
Requires: %libkresources = %epoch:%version
Requires: %libktnef = %epoch:%version
Requires: %libkxmlrpcclient = %epoch:%version
Requires: %libmailtransport = %epoch:%version
Requires: %libsyndication = %epoch:%version
Requires: %libqgpgme = %epoch:%version
Requires: %libgpgmepp = %epoch:%version
Requires: %libkpimidentities = %epoch:%version
Requires: %libakonadi_kmime = %epoch:%version
Requires: %libakonadi_kabc = %epoch:%version
Requires: %libakonadi_kde = %epoch:%version
Requires: %libkholidays = %epoch:%version
Requires: %libkpimtextedit = %epoch:%version
Requires: %libmicroblog = %epoch:%version

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
%_kde_libdir/cmake/

#--------------------------------------------------------------------------------

%prep
%setup -q -n kdepimlibs-%version.%svnrevision

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



