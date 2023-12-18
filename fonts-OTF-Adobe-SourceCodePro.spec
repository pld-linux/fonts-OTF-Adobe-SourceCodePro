# NOTE: there are also TTF fonts in tarball
%define		version_roman	2.030
%define		version_italic	1.050

Summary:	Adobe Source Code Pro - A set of OpenType fonts for coders
Summary(pl.UTF-8):	Adobe Source Code Pro - zbiór fontów OpenType dla programistów
Name:		fonts-OTF-Adobe-SourceCodePro
Version:	%{version_roman}.%{version_italic}
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	https://github.com/adobe-fonts/source-code-pro/archive/%{version_roman}R-ro%2f%{version_italic}R-it.tar.gz?/SourceCodePro-%{version_roman}R-ro-%{version_italic}R-it.tar.gz
# Source0-md5:	8120607f75da3b25cb8e34b64f02af9c
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
%setup -q -n source-code-pro-%{version_roman}R-ro-%{version_italic}R-it

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
%doc LICENSE.txt README.md
%{otffontsdir}/SourceCodePro-*.otf
%{_sysconfdir}/fonts/conf.d/%{name}.conf
%{_datadir}/fontconfig/conf.avail/%{name}.conf
