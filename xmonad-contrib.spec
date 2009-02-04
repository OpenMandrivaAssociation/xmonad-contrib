%define ghc_version 6.10.1
%define X11_version 1.4.5
%define cabal_setup Setup.lhs

#define pkg_libdir %{_libdir}/ghc-%{ghc_version}/%{pkg_name}-%{version}
#define pkg_docdir %{_docdir}/ghc/libraries/%{pkg_name}-%{version}

# ghc does not emit debug information
%define debug_package %{nil}

Name:           xmonad-contrib
Version:        0.8.1
Release:        %mkrel 1
Summary:        Haskell %{name} library - Third party extensions for xmonad

Group:          Development/Other
License:        BSD3
URL:            http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Provides:       %{name}-devel = %{version}-%{release}
BuildRequires: xmonad = %{version}
BuildRequires: haskell-X11 = %{X11_version}
BuildRequires: ghc = %{ghc_version}
BuildRequires: libxinerama-devel, libx11-devel, libxext-devel
BuildRequires: haddock, haskell-macros
Requires: xmonad = %{version}
Requires:       ghc = %{ghc_version}
Requires(post): ghc = %{ghc_version}
Requires(preun): ghc = %{ghc_version}

%description
Haskell %{pkg_name} library for ghc-%{ghc_version}.

Third party tiling algorithms, configurations and scripts to xmonad,
a tiling window manager for X.

For an introduction to building, configuring and using xmonad
extensions, see "XMonad.Doc". In particular:

"XMonad.Doc.Configuring", a guide to configuring xmonad

"XMonad.Doc.Extending", using the contributed extensions library

"XMonad.Doc.Developing", introduction to xmonad internals and writing
your own extensions.

%prep
%setup -q -n %{name}-%{version}

%build
%_cabal_build
%_cabal_genscripts


%install
rm -rf $RPM_BUILD_ROOT
%_cabal_install
%_cabal_rpm_gen_deps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/%{name}-%{version}/ghc-%{ghc_version}/*
%{_datadir}/doc/%{name}-%{version}/html/*
%{_datadir}/doc/%{name}-%{version}/LICENSE
%{_datadir}/haskell-deps/%{name}-%{version}-%{release}/*
