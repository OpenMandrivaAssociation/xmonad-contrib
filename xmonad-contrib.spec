%define ghc_version 6.10.4
%define X11_version 1.4.6.1
%define cabal_setup Setup.lhs

# ghc does not emit debug information
%define debug_package %{nil}

Name:           xmonad-contrib
Version:        0.9
Release:        %mkrel 1
Summary:        Third party extensions for xmonad
Group:          Development/Other
License:        BSD
URL:            http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:       %{name}-devel = %{version}-%{release}
BuildRequires: xmonad = %{version}
BuildRequires: haskell(X11) >= 1.4.6.1
BuildRequires: haskell(utf8-string)
BuildRequires: ghc >= %{ghc_version}
BuildRequires: libxinerama-devel, libx11-devel, libxext-devel
BuildRequires: haddock, haskell-macros, haskell-utf8-string
Requires: xmonad = %{version}
Requires:       ghc = %{ghc_version}
Requires(post): ghc
Requires(preun): ghc

%description
Haskell xmonad-contrib library for ghc-%{ghc_version}.

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

%check
%_cabal_check

%install
rm -rf $RPM_BUILD_ROOT
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/%{name}-%{version}/ghc-%{ghc_version}/*
%{_datadir}/doc/%{name}-%{version}
%_cabal_rpm_files
