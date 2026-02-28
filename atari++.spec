Summary:	Versatile extended emulator of Atari 8-bit machines
Summary(pl.UTF-8):	Wszechstronny, rozszerzony emulator 8-bitowych komputerów Atari
Name:		atari++
Version:	1.83
Release:	2
License:	THOR Public Licence (MPL-like) or GPL
Group:		Applications/Emulators
Source0:	http://www.xl-project.com/download/%{name}_%{version}.tar.gz
# Source0-md5:	bc357e90d9a2d42471c58d77bccc20d5
Patch0:		%{name}-make.patch
URL:		http://www.xl-project.com/
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
atari++ is an emulator for (now rather aged) Atari 8 bit computers. It
emulates the Atari 800, Atari 400, the 800XL and 600XL, the 65XE and
130XE and the Atari 5200 Game Console. The emulation is cycle-precise,
that is "on the fly" modifications of chip registers will be visible
on the screen immediately, emulating even programs using horizontal
kernel tricks correctly.

%description -l pl.UTF-8
atari++ to emulator (już dosyć leciwych) 8-bitowych komputerów Atari.
Emuluje modele Atari 800, Atari 400, 800XL i 600XL, 65XE i 130XE oraz
konsole Atari 5200. Emulacja jest dokładna co do cyklu, co oznacza, że
modyfikowanie "w locie" rejestrów układów będzie widoczne od razu na
ekranie, dzięki czemu emulacja działa poprawnie nawet w programach
wykorzystujących sztuczki ze zmianami w środku linii.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/atari++

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CREDITS README.History README.LEGAL README.licence manual/*.{html,png}
%attr(755,root,root) %{_bindir}/atari++
%{_mandir}/man6/atari++.6*
