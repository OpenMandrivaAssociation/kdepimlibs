%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kde_snapshot svn1198704
%endif

Name: kdepimlibs4
Summary: Libraries of the KDE-PIM project
Version: 4.6.4
%if %branch
Release: 0.%kde_snapshot.1
%else
Release: 1
%endif
Epoch: 2
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepimlibs-%version%{kde_snapshot}.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepimlibs-%version.tar.bz2
%endif
BuildRequires: kdelibs4-devel >= 2:4.5.0
BuildRequires: openldap-devel
BuildRequires: boost-devel
BuildRequires: gpgme-devel
BuildRequires: akonadi-devel >= 1:1.4.54
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

%package core
Group: Development/KDE and Qt
Summary: Config file and icons file for %name
Obsoletes: kdepimlibs4-common
Obsoletes: kdepim4-ioslaves
Obsoletes: %{mklibname kdepimlibs 4} < 2:4.3.1
Conflicts: %{mklibname kholidays 4} < 2:4.3.1-1
Conflicts: kontact < 2:4.3.73
Conflicts: %{name}-devel < 2.4.5.71

%description core
This packages contains all icons, config file etc... of kdepimlibs4.

%files core
%defattr(-,root,root,-)
%_kde_libdir/kde4/kabc_directory.so
%_kde_libdir/kde4/kabc_file.so
%_kde_libdir/kde4/kabc_net.so
%_kde_libdir/kde4/kabcformat_binary.so
%_kde_libdir/kde4/kcal_local.so
%_kde_libdir/kde4/kcal_localdir.so
%_kde_libdir/kde4/kcm_akonadicontact_actions.so
%_kde_libdir/kde4/kcm_kresources.so
%_kde_libdir/kde4/kcm_mailtransport.so
%_kde_datadir/config.kcfg/*
%_kde_appsdir/akonadi
%_kde_appsdir/akonadi-kde
%_kde_appsdir/kabc
%_kde_appsdir/kconf_update/mailtransports.upd
%_kde_appsdir/kconf_update/migrate-transports.pl
%_kde_appsdir/libkholidays
%_kde_services/akonadi/contact
%_kde_services/akonadicontact_actions.desktop
%_kde_services/kcm_mailtransport.desktop
%dir %_kde_services/kresources
%_kde_services/kresources.desktop
%dir %_kde_services/kresources/kabc
%_kde_services/kresources/kabc/dir.desktop
%_kde_services/kresources/kabc/file.desktop
%_kde_services/kresources/kabc/net.desktop
%_kde_services/kresources/kabc_manager.desktop
%_kde_services/kresources/kcal
%_kde_services/kresources/kcal_manager.desktop
%_kde_servicetypes/*.desktop
%_datadir/dbus-1/interfaces/*
%_kde_datadir/mime/packages/kdepimlibs-mime.xml
%_kde_docdir/HTML/en/kcontrol/kresources
%dir %_kde_docdir/HTML/en/kioslave

#------------------------------------------------	

%package -n kio4-imap
Summary: KDE 4 imap module
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n kio4-imap
KDE 4 imap module.

%files -n kio4-imap
%defattr(-,root,root)
%_kde_docdir/HTML/en/kioslave/imap
%_kde_libdir/kde4/kio_imap4.so
%_kde_datadir/kde4/services/imap*

#------------------------------------------------	

%package -n kio4-pop3
Summary: KDE 4 pop3 module
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n kio4-pop3
KDE 4 pop3 module.

%files -n kio4-pop3
%defattr(-,root,root)
%_kde_docdir/HTML/en/kioslave/pop3
%_kde_libdir/kde4/kio_pop3.so
%_kde_datadir/kde4/services/pop*

#------------------------------------------------	

%package -n kio4-ldap
Summary: KDE 4 ldap module
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n kio4-ldap
KDE 4 ldap module.

%files -n kio4-ldap
%defattr(-,root,root)
%_kde_docdir/HTML/en/kioslave/ldap
%_kde_libdir/kde4/kio_ldap.so
%_kde_datadir/kde4/services/ldap*
%_kde_libdir/kde4/kabc_ldapkio.so
%_kde_datadir/kde4/services/kresources/kabc/ldapkio.desktop

#------------------------------------------------	

%package -n kio4-sieve
Summary: KDE 4 sieve module
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n kio4-sieve
KDE 4 sieve module.

%files -n kio4-sieve
%defattr(-,root,root)
%_kde_libdir/kde4/kio_sieve.so
%_kde_datadir/kde4/services/sieve*
%doc %_kde_docdir/HTML/en/kioslave/sieve

#------------------------------------------------	

%package -n kio4-mbox
Summary: KDE 4 mbox module
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n kio4-mbox
KDE 4 mbox module.

%files -n kio4-mbox
%defattr(-,root,root)
%_kde_libdir/kde4/kio_mbox.so
%_kde_datadir/kde4/services/mbox*
%doc %_kde_docdir/HTML/en/kioslave/mbox

#------------------------------------------------	

%package -n kio4-smtp
Summary: KDE 4 smtp module
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n kio4-smtp
KDE 4 smtp module.

%files -n kio4-smtp
%defattr(-,root,root)
%_kde_docdir/HTML/en/kioslave/smtp
%_kde_libdir/kde4/kio_smtp.so
%_kde_datadir/kde4/services/smtp*

#------------------------------------------------	

%package -n kio4-nntp
Summary: KDE 4 nntp module
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n kio4-nntp
KDE 4 nntp module.

%files -n kio4-nntp
%defattr(-,root,root)
%_kde_docdir/HTML/en/kioslave/nntp
%_kde_libdir/kde4/kio_nntp.so
%_kde_datadir/kde4/services/nntp*

#------------------------------------------------	

%define kabc_major 4
%define libkabc %mklibname kabc %kabc_major

%package -n %libkabc
Summary: KDE 4 core library
Group:  System/Libraries
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

%description -n %libkldap
KDE 4 core library.

%files -n %libkldap
%defattr(-,root,root)
%_kde_libdir/libkldap.so.%{kldap_major}*

#------------------------------------------------

%define kmbox_major 4
%define libkmbox %mklibname kmbox %{kmbox_major}

%package -n %libkmbox
Summary: KDE 4 core library
Group: System/Libraries
Requires: %{name}-core = %epoch:%version
Obsoletes: %{_lib}mbox4 < 2:4.5.71

%description -n %libkmbox
KDE 4 core library.

%files -n %libkmbox
%defattr(-,root,root)
%_kde_libdir/libkmbox.so.%{kmbox_major}*

#------------------------------------------------	

%define kmime_major 4
%define libkmime %mklibname kmime %{kmime_major}

%package -n %libkmime
Summary: KDE 4 core library
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

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
Requires: %{name}-core = %epoch:%version

%description -n %libmicroblog
KDE 4 core library.

%files -n %libmicroblog
%defattr(-,root,root)
%_kde_libdir/libmicroblog.so.%{microblog_major}*

#------------------------------------------------

%define akonadi_contact_major 4
%define libakonadi_contact %mklibname akonadi-contact %{akonadi_contact_major}

%package -n %libakonadi_contact
Summary: KDE 4 core library
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n %libakonadi_contact
KDE 4 core library.

%files -n %libakonadi_contact
%defattr(-,root,root)
%_kde_libdir/libakonadi-contact.so.%{akonadi_contact_major}*

#------------------------------------------------

%define akonadi_kcal_major 4
%define libakonadi_kcal %mklibname akonadi-kcal %{akonadi_kcal_major}

%package -n %libakonadi_kcal
Summary: KDE 4 core library
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n %libakonadi_kcal
KDE 4 core library.

%files -n %libakonadi_kcal
%defattr(-,root,root)
%_kde_libdir/libakonadi-kcal.so.%{akonadi_kcal_major}*

#------------------------------------------------

%define kontactinterface_major 4
%define libkontactinterface %mklibname kontactinterface %{kontactinterface_major}

%package -n %libkontactinterface
Summary: KDE 4 core library
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n %libkontactinterface
KDE 4 core library.

%files -n %libkontactinterface
%defattr(-,root,root)
%_kde_libdir/libkontactinterface.so.%{kontactinterface_major}*

#------------------------------------------------

%define akonadi_calendar_major 4
%define libakonadi_calendar %mklibname akonadi-calendar %{akonadi_calendar_major}

%package -n %libakonadi_calendar
Summary: KDE 4 core library
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n %libakonadi_calendar
KDE 4 core library.

%files -n %libakonadi_calendar
%defattr(-,root,root)
%_kde_libdir/libakonadi-calendar.so.%{akonadi_calendar_major}*

#------------------------------------------------

%define kcalcore_major 4
%define libkcalcore %mklibname kcalcore %{kcalcore_major}

%package -n %libkcalcore
Summary: KDE 4 core library
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n %libkcalcore
KDE 4 core library.

%files -n %libkcalcore
%defattr(-,root,root)
%_kde_libdir/libkcalcore.so.%{kcalcore_major}*

#------------------------------------------------

%define kcalutils_major 4
%define libkcalutils %mklibname kcalutils %{kcalutils_major}

%package -n %libkcalutils
Summary: KDE 4 core library
Group: System/Libraries
Requires: %{name}-core = %epoch:%version

%description -n %libkcalutils
KDE 4 core library.

%files -n %libkcalutils
%defattr(-,root,root)
%_kde_libdir/libkcalutils.so.%{kcalutils_major}*

#------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KDE applications
Requires: kdelibs4-devel >= 2:4.5.0
Requires: %name-core = %epoch:%version
Requires: %libakonadi_calendar = %epoch:%version
Requires: %libakonadi_contact = %epoch:%version
Requires: %libakonadi_kabc = %epoch:%version
Requires: %libakonadi_kcal = %epoch:%version
Requires: %libakonadi_kde = %epoch:%version
Requires: %libakonadi_kmime = %epoch:%version
Requires: %libgpgmepp = %epoch:%version
Requires: %libkabc = %epoch:%version
Requires: %libkabc_file_core = %epoch:%version
Requires: %libkblog = %epoch:%version
Requires: %libkcal = %epoch:%version
Requires: %libkcalcore = %epoch:%version
Requires: %libkcalutils = %epoch:%version
Requires: %libkholidays = %epoch:%version
Requires: %libkimap = %epoch:%version
Requires: %libkldap = %epoch:%version
Requires: %libkmbox = %epoch:%version
Requires: %libkmime = %epoch:%version
Requires: %libkontactinterface = %epoch:%version
Requires: %libkpimidentities = %epoch:%version
Requires: %libkpimtextedit = %epoch:%version
Requires: %libkpimutils = %epoch:%version
Requires: %libkresources = %epoch:%version
Requires: %libktnef = %epoch:%version
Requires: %libkxmlrpcclient = %epoch:%version
Requires: %libmailtransport = %epoch:%version
Requires: %libmicroblog = %epoch:%version
Requires: %libqgpgme = %epoch:%version
Requires: %libsyndication = %epoch:%version
Requires: boost-devel
Conflicts: kdepim4-devel < 2:4.3.90

%description devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.

%files devel
%defattr(-,root,root,-)
%_kde_includedir/*
%_kde_libdir/*.so
%_kde_datadir/apps/cmake/*/*
%_kde_libdir/gpgmepp/*.cmake
%_kde_libdir/kde4/plugins/designer/*.so
%_kde_libdir/cmake/KdepimLibs

#--------------------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdepimlibs-%version%{kde_snapshot}
%else
%setup -q -n kdepimlibs-%version
%endif

%build
%cmake_kde4 
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -fr %buildroot

