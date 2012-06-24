Summary:	GTK+ chess board interface for ICS and chess engines
Summary(pl):	Interfejs GTK+ do szachowych program�w i serwer�w
Name:		eboard
Version:	1.0.3
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	833e656549d9fd9191e51b08005633e3
URL:		http://eboard.sourceforge.net/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
Requires:	gnuchess
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eboard is a chess interface for Unix-like systems (GNU/Linux, FreeBSD,
Solaris, etc.) based on the GTK+ GUI toolkit. It provides a chess
board interface to ICS (Internet Chess Servers) like FICS and to chess
engines like GNU Chess, Sjeng and Crafty.

%description -l pl
eboard jest interfejsem do program�w szachowych dla system�w
uniksowych opartym na bibliotece GTK+. Umo�liwia wsp�prac� zar�wno z
internetowymi serwerami szachowymi (ICS) jak r�wnie� z programami
szachowymi jak GNUchess, Sjeng czy Crafty.

%prep
%setup -q

#I think it can be do better
%build
./configure \
	--prefix="%{_prefix}" \
	--compiler="%{__cxx}" \
	--man-prefix="%{_mandir}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man[16]/*
