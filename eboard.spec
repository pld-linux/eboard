Summary:	GTK+ chess board interface for ICS and chess engines
Summary(pl):	Interfejs GTK+ do szachowych programów i serwerów
Name:		eboard
Version:	0.9.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	2ef8e080aebde8d8de270f5335fcb8be
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
eboard jest interfejsem do programów szachowych dla systemów
uniksowych opartym na bibliotece GTK+. Umo¿liwia wspó³pracê zarówno z
internetowymi serwerami szachowymi (ICS) jak równie¿ z programami
szachowymi jak GNUchess, Sjeng czy Crafty.

%prep
%setup -q

# it_IT.po is just a copy of it.po
sed -e 's/^C\(XX\)\?FLAGS=.*//;s/it it_IT/it/' configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man[16]/*
