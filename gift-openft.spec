%define name    gift-openft
%define version 0.2.1.6
%define rel	6

Summary:        OpenFT plugin for giFT
Name:           %{name}
Version:        %{version}
Release:        %{rel}
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



%changelog
* Tue May 15 2012 Crispin Boylan <crisb@mandriva.org> 0.2.1.6-6
+ Revision: 799077
- Drop mkrel
- Rebuild

* Fri Aug 12 2011 Andrey Bondrov <abondrov@mandriva.org> 0.2.1.6-4
+ Revision: 694182
- Fix BuildRequires
- Remove PLF reference
- imported package gift-openft

