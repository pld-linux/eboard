Summary:	GTK chess board interface for ICS and chess engines
Summary(pl):	Interfejs gtk do szachowych programow i serwerów
Name:		eboard
Version:	0.9.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	2ef8e080aebde8d8de270f5335fcb8be
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
URL:		http://eboard.sourceforge.net/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
Requires:	gnuchess
Requires:	gtk+
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eboard is a chess interface for Unix-like systems (GNU/Linux, FreeBSD,
Solaris, etc.) based on the GTK+ GUI toolkit. It provides a chess
board interface to ICS (Internet Chess Servers) like FICS and to chess
engines like GNU Chess, Sjeng and Crafty.

%description -l pl
eboard jest interfejsem do programow szachowych dla systemów unixowych
opartym na bibliotece gtk+ . Umo¿liwia wspó³prace zarówno z
internetowymi serwerami szachowymi (ICS) jak równie¿ z programami
szachowymi jak GNUchess, Sjeng czy Crafty

%prep
%setup -q
#%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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
%attr(755,root,root) %{_datadir}/%{name}
%attr(644,root,root) %{_datadir}/%{name}/*
