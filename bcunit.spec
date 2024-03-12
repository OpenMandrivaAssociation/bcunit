%define oname BCUnit
%define name %(echo %oname | tr [:upper:] {:lower:])

%define major	1
%define libname	%mklibname %{name}
%define devname	%mklibname %{name} -d

# exclude unwanted cmake requires
%global __provides_exclude_from ^%{_datadir}/cmake/.*/Find.*cmake$

%bcond_without	ncurses
%bcond_with	static
%bcond_without	strict

Name:		bcunit
Version:	5.3.34
Release:	1
License:	GPLv2+
Summary:	A Unit Testing Framework for C, based on (abandoned) CUnit
Group:		System/Libraries
URL:		https://github.com/BelledonneCommunications/bcunit
Source0:	https://gitlab.linphone.org/BC/public/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch0:		bcunit-5.3.5-cmake-fix_cmake_path.patch
BuildRequires:	cmake
BuildRequires:	ninja
%if %{with ncurses}
BuildRequires:	pkgconfig(ncurses)
%endif

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

#---------------------------------------------------------------------------

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

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains development files for %{name}.

%files -n %{devname}
%{_libdir}/*.so
%if %{with static}
%{_libdir}/*.a
%endif
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{oname}
%{_datadir}/%{oname}
%{_datadir}/cmake/%{oname}

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?commit:%{commit}}%{!?commit:%{version}}

%build
%cmake \
	-DENABLE_STATIC:BOOL=%{?with_static:ON}%{?!with_static:OFF} \
	-DENABLE_STRICT:BOOL=%{?with_strict:ON}%{?!with_strict:OFF} \
	-DENABLE_CURSES:BOOL=%{?with_ncurses:ON}%{?!with_ncurses:OFF} \
	-G Ninja

%ninja_build #-C build

%install
%ninja_install -C build

