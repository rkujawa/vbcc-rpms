%include common.spec

Name:		vlink
Version:	daily%{today}	
Release:	1%{?dist}
Summary:	Portable linker.

Group:		Development/Languages
License:	vlink license - non-commerical usage only, redistribution not allowed
URL:		http://sun.hasenbraten.de/vlink/
Source0:	vlink.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	gcc glibc-devel make gzip tar
Requires:	glibc

%description
vlink is a portable linker, written in ANSI-C, that can read and write a wide range of object- and executable file formats. It can be used to link a specific target format from several different input file formats, or for converting, stripping and manipulating files.

%prep
%setup -n vlink -q

%build
mkdir objects
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/vbcc/bin
install -m 755 vlink %{buildroot}/opt/vbcc/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/vbcc/bin/vlink
%doc

%changelog

