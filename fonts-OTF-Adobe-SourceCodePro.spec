%define		_name	SourceCodePro
Summary:	Adobe Source Code Pro - A set of OpenType fonts for coders
Name:		fonts-OTF-Adobe-%{_name}
Version:	1.009
Release:	1
License:	OFL
Group:		Fonts
Source0:	http://downloads.sourceforge.net/sourcecodepro.adobe/SourceCodePro_FontsOnly-%{version}.zip
# Source0-md5:	dfc882152ec1ed85dc1178529c54b7a5
Source1:	%{name}-fontconfig.conf
URL:		http://sourceforge.net/projects/sourcecodepro.adobe/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         otffontsdir     %{_fontsdir}/OTF

%description
Source Sans is a set of monospaced OpenType fonts that have been
designed to work well coding environments.

%prep
%setup -q -n SourceCodePro_FontsOnly-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{otffontsdir},%{_datadir}/fontconfig/conf.avail,%{_sysconfdir}/fonts/conf.d}

install -p *.otf $RPM_BUILD_ROOT%{otffontsdir}
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
%{otffontsdir}/*.otf
%{_sysconfdir}/fonts/conf.d/%{name}.conf
%{_datadir}/fontconfig/conf.avail/%{name}.conf
