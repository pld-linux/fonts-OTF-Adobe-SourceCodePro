# NOTE: there are also TTF fonts in tarball
%define		version_upright		2.042
%define		version_italic		1.062
%define		version_variable	1.026

Summary:	Adobe Source Code Pro - A set of OpenType fonts for coders
Summary(pl.UTF-8):	Adobe Source Code Pro - zbiór fontów OpenType dla programistów
Name:		fonts-OTF-Adobe-SourceCodePro
Version:	%{version_upright}.%{version_italic}
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	https://github.com/adobe-fonts/source-code-pro/archive/%{version_upright}R-u%2f%{version_italic}R-i%2f%{version_variable}R-vf.tar.gz?/SourceCodePro-%{version_upright}R-u-%{version_italic}R-i-%{version_variable}R-vf.tar.gz
# Source0-md5:	91fcd818b22d26b4401058f3c4244936
Source1:	%{name}-fontconfig.conf
URL:		http://adobe-fonts.github.io/source-code-pro/
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         otffontsdir     %{_fontsdir}/OTF

%description
Source Sans is a set of monospaced OpenType fonts that have been
designed to work well coding environments.

%description -l pl.UTF-8
Source Sans to zbiór fontów OpenType o stałej szerokości znaku,
zaprojektowany z myślą o środowiskach programistycznych.

%prep
%setup -q -n source-code-pro-%{version_upright}R-u-%{version_italic}R-i-%{version_variable}R-vf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{otffontsdir},%{_datadir}/fontconfig/conf.avail,%{_sysconfdir}/fonts/conf.d}

install -p OTF/*.otf $RPM_BUILD_ROOT%{otffontsdir}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/%{name}.conf
ln -s %{_datadir}/fontconfig/conf.avail/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{otffontsdir}/SourceCodePro-*.otf
%{_sysconfdir}/fonts/conf.d/%{name}.conf
%{_datadir}/fontconfig/conf.avail/%{name}.conf
