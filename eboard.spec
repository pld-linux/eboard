# TODO:
# - check why it fails with ccache turned on
Summary:	GTK+ chess board interface for ICS and chess engines
Summary(pl.UTF-8):	Interfejs GTK+ do szachowych programów i serwerów
Name:		eboard
Version:	1.1.1
Release:	4
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/eboard/%{name}-%{version}.tar.bz2
# Source0-md5:	03dcdaa2bc85218b1b18c4bee276fea7
Source1:	%{name}.desktop
Patch0:		%{name}-const.patch
URL:		http://www.bergo.eng.br/eboard/
BuildRequires:	gtk+2-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
Suggests:	Sjeng-Free
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
%patch0 -p1

# This way is needed, because package contains non-standard configure file
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
