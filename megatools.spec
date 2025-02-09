Name:		megatools
Version:	1.11.3.20250203
Release:	1
License:	GPLv2
Summary:	megatools - command line client application for Mega
Group:		File tools
URL:		https://xff.cz/megatools/
# See also: https://github.com/megous/megatools
Source:		https://xff.cz/megatools/builds/megatools-%{version}.tar.gz
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildSystem:	meson

%description
Megatools is a collection of programs for accessing Mega service from.
a command line of your desktop or server.

Megatools allow you to copy individual files as well as entire directory.
trees to and from the cloud. You can also perform streaming downloads for.
example to preview videos and audio files, without needing to download.
the entire file.

Megatools are robust and optimized for fast operation - as fast as Mega.
servers allow. Memory requirements and CPU utilization are kept at minimum.

You can register account using a 'megareg' tool, with the benefit of having.
true control of your encryption keys.

Mega website can be found at http://mega.co.nz.

%files
#docs attr(-,root,root) README HACKING HOWTO LICENSE
%defattr(-,root,root)
%{_bindir}/mega*
%{_mandir}/man1/mega*
%{_mandir}/man5/mega*
%{_docdir}/%{name}/*
