%define Name BCUnit
%define	major 1
%define	libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		bcunit
Version:	3.0.2
Release:	2
License:	GPLv2+
Summary:	A Unit Testing Framework for C, based on (abandoned) CUnit
Group:		System/Libraries
URL:		https://github.com/BelledonneCommunications/bcunit
Source0:	https://github.com/BelledonneCommunications/bcunit/archive/%{version}.tar.gz
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	cmake ninja

%description
BCUnit is a lightweight system for writing, administering, and running unit
tests in C.  It provides C programmers a basic testing functionality with a
flexible variety of user interfaces.

BCUnit is built as a static library which is linked with the user's testing
code.  It uses a simple framework for building test structures, and provides a
rich set of assertions for testing common data types. In addition, several
different interfaces are provided for running tests and reporting results.
These interfaces currently include:

- Automated: Non-interactive output to xml file
- Basic: Non-interactive flexible programming interface
- Console: Interactive console interface (ansi C)
- Curses: Interactive graphical interface (Unix)

It is based on the abandoned CUnit.

%package -n %{libname}
Summary:	C testing framework
Group:		System/Libraries

%description -n %{libname}
BCUnit is a lightweight system for writing, administering, and running unit
tests in C.  It provides C programmers a basic testing functionality with a
flexible variety of user interfaces.

BCUnit is built as a static library which is linked with the user's testing
code.  It uses a simple framework for building test structures, and provides a
rich set of assertions for testing common data types. In addition, several
different interfaces are provided for running tests and reporting results.
These interfaces currently include:

- Automated: Non-interactive output to xml file
- Basic: Non-interactive flexible programming interface
- Console: Interactive console interface (ansi C)
- Curses: Interactive graphical interface (Unix)

It is based on the abandoned CUnit.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname %{name} 1 -d

%description -n	%{develname}
This package contains development files for %{name}.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{Name}
%{_datadir}/%{Name}
%{_datadir}/BCunit
