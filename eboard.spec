# TODO:
# - check why it fails with ccache turned on
Summary:	GTK+ chess board interface for ICS and chess engines
Summary(pl.UTF-8):	Interfejs GTK+ do szachowych programów i serwerów
Name:		eboard
Version:	1.0.4
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	2bd2927a670ed23594cbf524bc5746ef
Source1:	%{name}.desktop
URL:		http://www.bergo.eng.br/eboard/
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
Suggests:	crafty
Suggests:	gnuchess
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eboard is a chess interface for Unix-like systems (GNU/Linux, FreeBSD,
Solaris, etc.) based on the GTK+ GUI toolkit. It provides a chess
board interface to ICS (Internet Chess Servers) like FICS and to chess
engines like GNU Chess, Sjeng and Crafty.

%description -l pl.UTF-8
eboard jest interfejsem do programów szachowych dla systemów
uniksowych opartym na bibliotece GTK+. Umożliwia współpracę zarówno z
internetowymi serwerami szachowymi (ICS) jak również z programami
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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install icon-eboard.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO Documentation/*.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man[16]/*
%{_pixmapsdir}/%{name}.xpm
