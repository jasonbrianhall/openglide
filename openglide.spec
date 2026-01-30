Name:           openglide
Version:        0.09
Release:        1%{?dist}
Summary:        Glide 2.x to OpenGL wrapper

License:        GPL-2.0-or-later
URL:            https://github.com/openglide/openglide
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel

# Disable automatic debug package generation
%global debug_package %{nil}

%description
OpenGLide is a Glide 2.x wrapper that translates Glide API calls into OpenGL.
It allows legacy 3dfx Glide applications to run on modern systems using OpenGL
as the rendering backend.

%package devel
Summary:        Development files for building Glide applications using OpenGLide
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and development libraries for building applications that use
the Glide 2.x API implemented by OpenGLide.

# -------------------------------------------------------------
# PREP: create source tarball from current working directory
# -------------------------------------------------------------
%prep
%setup -q

# -------------------------------------------------------------
# BUILD
# -------------------------------------------------------------
%build
./bootstrap
./configure --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --datadir=%{_datadir}
%make_build

# -------------------------------------------------------------
# INSTALL
# -------------------------------------------------------------
%install
rm -rf %{buildroot}
%make_install DESTDIR=%{buildroot}

# Install SDK headers
install -m 644 sdk2_*.h %{buildroot}%{_includedir}/

# Remove static libs if any
find %{buildroot} -name "*.a" -delete

# -------------------------------------------------------------
# FILE LISTS
# -------------------------------------------------------------
%files
%license LICENSE
%doc README.md
%{_libdir}/libglide2x.so*
%{_libdir}/libglide.so.2

%files devel
%{_includedir}/glide.h
%{_includedir}/openglide/
%{_includedir}/sdk2_*.h

%changelog
* Fri Jan 30 2026 Jason Hall <jbhall@example.com> - 0.09-1
- Initial RPM packaging from local source tree
