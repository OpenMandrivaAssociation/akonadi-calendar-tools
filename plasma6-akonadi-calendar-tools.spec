#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Command line interface to KDE calendars
Name:		plasma6-akonadi-calendar-tools
Version:	24.08.3
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/akonadi-calendar-tools/-/archive/%{gitbranch}/akonadi-calendar-tools-%{gitbranchd}.tar.bz2#/akonadi-calendar-tools-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/akonadi-calendar-tools-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6CalendarSupport)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiCalendar)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	boost-devel

%description
A command line interface to KDE calendars. It lets you view, insert, remove,
or modify calendar events by way of the command line or from a scripting
language. Additionally, konsolekalendar can create a new KDE calendar, export
a KDE calendar to a variety of other formats, and import another KDE calendar.

%files -f all.lang
%{_datadir}/applications/konsolekalendar.desktop
%{_bindir}/calendarjanitor
%{_bindir}/konsolekalendar
%{_docdir}/*/*/konsolekalendar
%{_iconsdir}/hicolor/*/apps/konsolekalendar.*
%{_datadir}/qlogging-categories6/console.categories
%{_datadir}/qlogging-categories6/console.renamecategories

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n akonadi-calendar-tools-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang calendarjanitor
%find_lang konsolekalendar

cat *.lang >all.lang
