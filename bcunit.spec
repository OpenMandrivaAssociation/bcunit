%define oname BCUnit
%define name %(echo %oname | tr [:upper:] {:lower:])

%define major	1
%define libname	%mklibname %{name}
%define devname	%mklibname %{name} -d

# exclude unwanted cmake requires
%global __provides_exclude_from ^%{_datadir}/cmake/.*/Find.*cmake$

%bcond_without curses
%bcond_with example
%bcond_with test

Name:		bcunit
Version:	5.4.118
Release:	1
License:	GPLv2+
Summary:	A Unit Testing Framework for C, based on (abandoned) CUnit
Group:		System/Libraries
URL:		https://github.com/BelledonneCommunications/bcunit
Source0:	https://gitlab.linphone.org/BC/public/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	ninja
%if %{with curses}
BuildRequires:	pkgconfig(ncurses)
%endif

BuildSystem:	cmake
BuildOption:	-DENABLE_BCUNIT_CURSES:BOOL=%{?with_nurses:ON}%{?!with_curses:OFF}
BuildOption:	-DENABLE_BCUNIT_EXAMPLE:BOOL=%{?with_example:ON}%{?!with_example:OFF}
BuildOption:	-DENABLE_BCUNIT_TEST:BOOL=%{?with_test:ON}%{?!with_test:OFF}

%patchlist
bcunit-5.3.5-cmake-fix_cmake_path.patch
bcunit-5.4.42-cmake-include_headers_path.patch

%description
This is BCUnit, a fork of the defunct project CUnit (see below), with several
fixes and patches applied.

BCUnit is platform/version independent and should be portable to all platforms.
BCUnit provides various interfaces to the framework, some of which are platform
dependent (e.g. curses on *nix).  Building other interfaces should be
straightforward with the facilities provided in the framework.

BCUnit is built as shared library which provides framework support when linkedù
into user testing code.  The framework complies with the conventional structure
of test cases bundled into suites which are registered with the framework for
running.  See the documentation for more about the structure and use of the
framework.

  * Automated: Non-interactive output to xml file
  * Basic: Non-interactive flexible programming interface
  * Console: Interactive console interface (ansi C)
  * Curses: Interactive graphical interface (Unix)

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	C testing framework
Group:		System/Libraries

%description -n %{libname}
This is BCUnit, a fork of the defunct project CUnit (see below), with several
fixes and patches applied.

BCUnit is platform/version independent and should be portable to all platforms.
BCUnit provides various interfaces to the framework, some of which are platform
dependent (e.g. curses on *nix).  Building other interfaces should be
straightforward with the facilities provided in the framework.

BCUnit is built as shared library which provides framework support when linkedù
into user testing code.  The framework complies with the conventional structure
of test cases bundled into suites which are registered with the framework for
running.  See the documentation for more about the structure and use of the
framework.

  * Automated: Non-interactive output to xml file
  * Basic: Non-interactive flexible programming interface
  * Console: Interactive console interface (ansi C)
  * Curses: Interactive graphical interface (Unix)

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
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{oname}
%{_datadir}/%{oname}
%{_datadir}/cmake/%{oname}

#---------------------------------------------------------------------------

