Summary:	Gwibber - an open source microblogging client for GNOME
Name:		gwibber
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	09aa0722927c069fc70243b2e10d5bbe
URL:		https://launchpad.net/gwibber
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	python-devel >= 1:2.5.0
BuildRequires:	python-distutils-extra
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	desktop-file-utils
%pyrequires_eq	python-modules
Requires:	python-PIL >= 1.1.6
Requires:	python-dbus >= 0.80.2
Requires:	python-feedparser >= 4.1
Requires:	python-gnome-gconf >= 2.18.0
Requires:	python-mx-DateTime >= 3.0.0
Requires:	python-pygtk-gtk >= 2.10.4
Requires:	python-pynotify >= 0.1.1
Requires:	python-pywebkitgtk >= 1.0.1
Requires:	python-pyxdg >= 0.15
Requires:	python-simplejson >= 1.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gwibber is an open source microblogging client for GNOME.

It supports Twitter, Jaiku, Identi.ca, Facebook, Flickr, Digg and RSS.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \
	--prefix=%{_prefix}

%find_lang %{name} --with-gnome
%py_postclean $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/gwibber
%{py_sitescriptdir}/gwibber-%{version}-py*.egg-info
%dir %{py_sitescriptdir}/gwibber
%dir %{py_sitescriptdir}/gwibber/microblog
%dir %{py_sitescriptdir}/gwibber/microblog/support
%{py_sitescriptdir}/gwibber/*.py[co]
%{py_sitescriptdir}/gwibber/microblog/*.py[co]
%{py_sitescriptdir}/gwibber/microblog/support/*.py[co]
%{_desktopdir}/gwibber.desktop
%{_pixmapsdir}/gwibber.svg
%{_datadir}/%{name}
