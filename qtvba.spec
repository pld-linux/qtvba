Summary:	Qt based frontend to VisualBoyAdvance
Summary(pl.UTF-8):   Nakładka na VisualBoyAdvance napisana pod Qt
Name:		qtvba
Version:	0.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.apex.net.au/~twalker/qtvba/%{name}-%{version}.tar.gz
# Source0-md5:	16837d77d0f0e02c10fe60d509ed252f
URL:		http://www.apex.net.au/~twalker/qtvba/
BuildRequires:	qt-devel
Requires:	VisualBoyAdvance
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QTVBA is a Qt 3.x and C++-based graphical frontend to the
VisualBoyAdvance Nintendo Gameboy Advance Emulator. Features include
dual screenshot handling, save game information, number and last date
played recording, a built in ROM renamer, and compatibility with
GBA-Shell's screenshot formats and indexing.

%description -l pl.UTF-8
QTVBA to napisana w C++ i korzystająca z Qt graficzna nakładka na
emulator GameBoy Advance firmy Nintendo - VisualBoyAdvance. Aktualnie
obsługuje zapisywanie gry, zmiany nazw ROM-ów z poziomu apliakcji,
zapisywanie liczby i daty gier oraz format i indeksowanie zrzutów
ekranu z GBA.

%prep
%setup -q

%build
export QTDIR=%{_usr}
export QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++/
qmake qtvba.pro
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -pipe -Wall -D_REENTRANT  -DQT_NO_DEBUG -DQT_THREAD_SUPPORT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install qtvba $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtvba
