%global debug_package %{nil}
%define _cabal_setup Setup.lhs
%define _no_haddock 1
%define module  xmonad-contrib
Name:           %{module}
Version:        0.10
Release:        2
Summary:        Third party extensions for xmonad
Group:          Development/Other
License:        BSD
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc
buildrequires:  ghc-devel
buildrequires:  haskell-macros
buildrequires:  cabal-install
buildrequires:  haskell(xmonad)
buildrequires:  X11-devel

%description
Third party tiling algorithms, configurations and scripts to xmonad, a tiling
window manager for X.
For an introduction to building, configuring and using xmonad extensions, see
"XMonad.Doc". In particular:
"XMonad.Doc.Configuring", a guide to configuring xmonad
"XMonad.Doc.Extending", using the contributed extensions library
"XMonad.Doc.Developing", introduction to xmonad internals and writing your own
extensions.

%prep
%setup -q -n %{module}-%{version}

%build
cabal update
cabal install
cabal configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-executable-stripping
cabal build
%_cabal_genscripts

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files


