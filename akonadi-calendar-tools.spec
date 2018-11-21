Summary:	Command line interface to KDE calendars
Name:		akonadi-calendar-tools
Version:	 18.08.3
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5AkonadiCalendar)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5CalendarSupport)
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
%{_sysconfdir}/xdg/console.categories
%{_sysconfdir}/xdg/console.renamecategories

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
