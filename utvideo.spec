Summary:	Ut Video codec suite
Summary(pl.UTF-8):	Kodek Ut Video
Name:		utvideo
Version:	18.2.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://umezawa.dyndns.info/archive/utvideo/%{name}-%{version}-src.zip
# Source0-md5:	1ede3a39a737b89557f251e42945e2dc
Source1:	%{name}-makefile
Patch0:		%{name}-shared.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-linux.patch
URL:		http://umezawa.dyndns.info/wordpress/?cat=28
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ut Video Codec Suite is a multi-platform and multi-interface lossless
video codec.

%description -l pl.UTF-8
Ut Video to wieloplatformowy, mający wiele interfejsów bezstratny
kodek obrazu.

%package devel
Summary:	Header files for Ut Video library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ut Video
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for Ut Video library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ut Video.

%package static
Summary:	Static Ut Video library
Summary(pl.UTF-8):	Statyczna biblioteka Ut Video
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Ut Video library.

%description static -l pl.UTF-8
Statyczna biblioteka Ut Video.

%prep
%setup -q

cp %{SOURCE1} GNUmakefile

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__make} \
%ifarch i586 i686 pentium2 pentium3 pentium4
	ARCH=i386 \
%endif
%ifarch %{x8664}
	ARCH=x86_86 \
%endif
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags} %{rpmcppflags} -std=c++11" \
	V=1 \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.en.html
%lang(ja) %doc readme.ja.html
%attr(755,root,root) %{_libdir}/libutvideo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libutvideo.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libutvideo.so
%{_libdir}/libutvideo.la
%{_includedir}/utvideo

%files static
%defattr(644,root,root,755)
%{_libdir}/libutvideo.a
