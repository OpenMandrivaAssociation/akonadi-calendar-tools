%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Command line interface to KDE calendars
Name:		akonadi-calendar-tools
Version:	23.08.5
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KPim5CalendarSupport)
BuildRequires:	cmake(KPim5Akonadi)
BuildRequires:	cmake(KPim5AkonadiCalendar)
BuildRequires:	cmake(KPim5Libkdepim)
BuildRequires:	cmake(KPim5CalendarUtils)
BuildRequires:	boost-devel
Requires:	kdepim-runtime
Conflicts:	korganizer < 3:16.12

%description
A command line interface to KDE calendars. It lets you view, insert, remove,
or modify calendar events by way of the command line or from a scripting
language. Additionally, konsolekalendar can create a new KDE calendar, export
a KDE calendar to a variety of other formats, and import another KDE calendar.

%files -f all.lang
%{_kde5_applicationsdir}/konsolekalendar.desktop
%{_bindir}/calendarjanitor
%{_bindir}/konsolekalendar
%{_docdir}/*/*/konsolekalendar
%{_iconsdir}/hicolor/*/apps/konsolekalendar.*
%{_datadir}/qlogging-categories5/console.categories
%{_datadir}/qlogging-categories5/console.renamecategories

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang calendarjanitor
%find_lang konsolekalendar

cat *.lang >all.lang
