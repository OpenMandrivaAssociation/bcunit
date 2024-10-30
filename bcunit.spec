%define oname BCUnit
%define name %(echo %oname | tr [:upper:] {:lower:])

%define major	1
%define libname	%mklibname %{name}
%define devname	%mklibname %{name} -d

# exclude unwanted cmake requires
%global __provides_exclude_from ^%{_datadir}/cmake/.*/Find.*cmake$

%bcond curses	1

Name:		bcunit
Version:	5.3.93
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

%prep
%autosetup -p1 -n %{name}-%{?commit:%{commit}}%{!?commit:%{version}}

%build
%cmake \
	-DENABLE_CURSES:BOOL=%{?with_ncurses:ON}%{?!with_ncurses:OFF} \
	-DBUILD_TEST:BOOL=%{?with_test:ON}%{?!with_test:OFF} \
	-G Ninja

%ninja_build #-C build

%install
%ninja_install -C build

