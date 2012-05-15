%define name    gift-openft
%define version 0.2.1.6
%define rel	5

Summary:        OpenFT plugin for giFT
Name:           %{name}
Version:        %{version}
Release:        %mkrel %{rel}
License:        GPL
Group:          Networking/File transfer
URL:            http://gift.sf.net/
Source0:        http://download.sourceforge.net/gift/%{name}-%{version}.tar.bz2
Requires:	gift
BuildRequires:	db-devel
BuildRequires:	gift-devel
BuildRequires:	zlib-devel
BuildRequires:	magic-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
This is the OpenFT plugin for giFT.

%prep
%setup -q
perl -pi -e 's,\${prefix}/lib,%{_libdir},' m4/gift-prefix.m4 configure*

%build
%configure2_5x 
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README INSTALL NEWS TODO
%{_datadir}/*
%{_libdir}/giFT/*

