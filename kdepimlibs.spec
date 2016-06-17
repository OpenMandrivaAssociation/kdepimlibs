%define major 5

Summary:	Libraries of the KDE-PIM project
Name:		kdepimlibs
Version:	16.04.2
Release:	1
Epoch:		3
Group:		Graphical desktop/KDE
License:	ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
Url:		https://projects.kde.org/projects/kde/kdepimlibs
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	openldap-devel
BuildRequires:	shared-mime-info
BuildRequires:	akonadi
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5Ldap)
BuildRequires:	cmake(KF5Mbox)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Ldap)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5Mbox)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Grantlee5)
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	xsltproc
# Needed because of /usr/include/KF5/AkonadiCore/std_exception.h
BuildRequires:	gcc-c++

%description
This module includes libraries that are central to the development and
execution of a KDE-PIM application.

The KDE-PIM project aims to bring together those who wish to help design,
implement, test, etc. anything that's to do with personal information
management.

This rather broad scope encompasses mail clients, addressbooks, usenet news,
scheduling and even sticky notes.

#----------------------------------------------------------------------------

%package core
Group:		Development/KDE and Qt
Summary:	Config file and icons file for %{name}
Conflicts:	%{name}-devel < 2.4.5.71
Conflicts:	akonadi-kde < 3:4.12.0

%description core
This packages contains all icons, config file etc... of kdepimlibs4.

%files core
%config %{_sysconfdir}/xdg/kdepimlibs-kioslave.categories
%{_bindir}/akonadi_benchmarker
%dir %{_datadir}/kservices5/akonadi
%dir %{_datadir}/akonadi
%dir %{_datadir}/akonadi/plugins
%dir %{_datadir}/akonadi/plugins/serializer
%doc %dir %{_docdir}/HTML/en/kioslave5
%{_datadir}/kf5/akonadi
%{_datadir}/config.kcfg/specialmailcollections.kcfg
%{_datadir}/mime/packages/x-vnd.kde.contactgroup.xml
%{_datadir}/mime/packages/x-vnd.akonadi5.socialfeeditem.xml

#----------------------------------------------------------------------------

%package -n kio-pop3
Summary:	KDE pop3 module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio-pop3
KDE pop3 module.

%files -n kio-pop3
%{_libdir}/qt5/plugins/kf5/kio/pop3.so
%{_datadir}/kservices5/pop3.protocol
%{_datadir}/kservices5/pop3s.protocol
%doc %{_docdir}/HTML/en/kioslave5/pop3

#----------------------------------------------------------------------------

%package -n kio-imap
Summary:	KDE imap module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio-imap
KDE imap module.

%files -n kio-imap
%doc %{_docdir}/HTML/en/kioslave5/imap

#----------------------------------------------------------------------------

%package -n kio-ldap
Summary:	KDE ldap module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio-ldap
KDE ldap module.

%files -n kio-ldap
%{_libdir}/qt5/plugins/kf5/kio/ldap.so
%{_datadir}/kservices5/ldap.protocol
%{_datadir}/kservices5/ldaps.protocol
%doc %{_docdir}/HTML/en/kioslave5/ldap

#----------------------------------------------------------------------------

%package -n kio-sieve
Summary:	KDE sieve module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio-sieve
KDE sieve module.

%files -n kio-sieve
%{_libdir}/qt5/plugins/kf5/kio/sieve.so
%{_datadir}/kservices5/sieve.protocol
%doc %{_docdir}/HTML/en/kioslave5/sieve

#----------------------------------------------------------------------------

%package -n kio-mbox
Summary:	KDE mbox module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio-mbox
KDE mbox module.

%files -n kio-mbox
%{_libdir}/qt5/plugins/kf5/kio/mbox.so
%{_datadir}/kservices5/mbox.protocol
%doc %{_docdir}/HTML/en/kioslave5/mbox

#----------------------------------------------------------------------------

%package -n kio-smtp
Summary:	KDE smtp module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio-smtp
KDE smtp module.

%files -n kio-smtp
%{_libdir}/qt5/plugins/kf5/kio/smtp.so
%{_datadir}/kservices5/smtp.protocol
%{_datadir}/kservices5/smtps.protocol
%doc %{_docdir}/HTML/en/kioslave5/smtp

#----------------------------------------------------------------------------

%package -n kio-nntp
Summary:	KDE nntp module
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n kio-nntp
KDE nntp module.

%files -n kio-nntp
%{_libdir}/qt5/plugins/kf5/kio/nntp.so
%{_datadir}/kservices5/nntp.protocol
%{_datadir}/kservices5/nntps.protocol
%doc %{_docdir}/HTML/en/kioslave5/nntp

#----------------------------------------------------------------------------

%define libakonadicontact %mklibname KF5AkonadiContact %{major}

%package -n %{libakonadicontact}
Summary:	Akonadi contact handling library
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}
Requires:	akonadi-contact-data = %{EVRD}

%description -n %{libakonadicontact}
Akonadi contact handling library

%files -n %{libakonadicontact}
%{_libdir}/libKF5AkonadiContact.so.%{major}*
%{_libdir}/qt5/plugins/kcm_akonadicontact_actions.so

#----------------------------------------------------------------------------
%package -n akonadi-contact-data
Summary:	Data files needed for Akonadi contact management
Group:		System/Libraries
Requires:	%{libakonadicontact} = %{EVRD}
BuildArch:	noarch

%description -n akonadi-contact-data
Data files needed for Akonadi contact management

%files -n akonadi-contact-data
%{_datadir}/kservicetypes5/kaddressbookimprotocol.desktop
%{_datadir}/kservices5/akonadicontact_actions.desktop
%{_datadir}/icons/*/*/*/*_protocol.*
%{_datadir}/kservices5/akonadi/contact/*protocol.desktop
%{_datadir}/akonadicontact

#----------------------------------------------------------------------------

%define libakonadimime %mklibname KF5AkonadiMime %{major}

%package -n %{libakonadimime}
Summary:	Akonadi MIME library
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n %{libakonadimime}
Akonadi MIME library

%files -n %{libakonadimime}
%{_libdir}/libKF5AkonadiMime.so.%{major}*

#----------------------------------------------------------------------------

%define libakonadinotes %mklibname KF5AkonadiNotes %{major}

%package -n %{libakonadinotes}
Summary:	Akonadi notes library
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}

%description -n %{libakonadinotes}
Akonadi notes library.

%files -n %{libakonadinotes}
%{_libdir}/libKF5AkonadiNotes.so.%{major}*

#----------------------------------------------------------------------------

%define libakonadisocialutils %mklibname KF5AkonadiSocialUtils %{major}

%package -n %{libakonadisocialutils}
Summary:	Akonadi social utilities library
Group:		System/Libraries
Requires:	%{name}-core = %{EVRD}
Requires:	akonadi-social-utils-data = %{EVRD}

%description -n %{libakonadisocialutils}
Akonadi social utilities library.

%files -n %{libakonadisocialutils}
%{_libdir}/libKF5AkonadiSocialUtils.so.%{major}*
%{_libdir}/qt5/plugins/akonadi_serializer_socialfeeditem.so

#----------------------------------------------------------------------------
%package -n akonadi-social-utils-data
Requires:	%{libakonadisocialutils} = %{EVRD}
Group:		System/Libraries
BuildArch:	noarch

%description -n akonadi-social-utils-data
Data files needed for Akonadi social utilities

%files -n akonadi-social-utils-data
%{_datadir}/akonadi/plugins/serializer/akonadi_serializer_socialfeeditem.desktop

#----------------------------------------------------------------------------

%package devel
Group:		Development/KDE and Qt
Summary:	Header files and documentation for compiling KDE applications
Requires:	%{name}-core = %{EVRD}
Requires:	%{libakonadicontact} = %{EVRD}
Requires:	%{libakonadimime} = %{EVRD}
Requires:	%{libakonadinotes} = %{EVRD}
Requires:	%{libakonadisocialutils} = %{EVRD}
Requires:	boost-devel
# To avoid file conflict (FindQtOAuth.cmake)
Conflicts:	choqok-devel < 1.3-3

%description devel
This package includes the header files you will need to compile applications
for KDE. Also included is the KDE API documentation in HTML format for easy
browsing.

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5AkonadiContact
%{_libdir}/cmake/KF5AkonadiMime
%{_libdir}/cmake/KF5AkonadiNotes
%{_libdir}/cmake/KF5AkonadiSocialUtils
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiContact.pri
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiMime.pri
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiNotes.pri
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiSocialUtils.pri

#----------------------------------------------------------------------------

%prep
%setup -q -n kdepimlibs-%{version}
%cmake_kde5 -DBUILD_TESTING=ON

%build
%ninja -C build

%install
%ninja_install -C build
