Name:		qtvba
Summary:	QT based frontend to VisualBoyAdvance
Summary(pl):	Nak³adka na VisualBoyAdvance napisana pod QT
Version:	0.2
Release:	1
Source0:	http://www.apex.net.au/~twalker/qtvba/%{name}-%{version}.tar.gz
# Source0-md5:	9f61cb15f10c751f6215f5ab5b14e451
URL:		http://www.apex.net.au/~twalker/qtvba/
Group:		Applications
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
License:	GPL
BuildRequires:	qt-devel
Requires:	qt
Requires:	VisualBoyAdvance

%description
QTVBA is a Qt 3.x and C++-based graphical frontend to the
VisualBoyAdvance Nintendo Gameboy Advance Emulator. Features include
dual screenshot handling, save game information, number and last date
played recording, a built in ROM renamer, and compatibility with
GBA-Shell's screenshot formats and indexing.

%description -l pl
QTVBA to napisana w C++ i korzystaj±ca z QT graficzna nak³adka na 
emulator GameBoy Advance (C) Nintendo - VisualBoyAdvance. Aktualnie obs³uguje
zapisywanie gry, zmiany nazw ROMów z poziomu apliakcji, zapisywanie d³ugo¶æ i
daty gier oraz format i indeksowanie zrzutów ekranu z GBA.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q 

%build
export QTDIR=%{_usr}
export QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++/
qmake qtvba.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install qtvba  $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtvba
