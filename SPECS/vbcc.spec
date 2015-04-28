%include common.spec

Name:		vbcc-%{target_cpu}
Version:	daily%{today}
Release:	1%{?dist}
Summary:	Optimizing, retargetable and portable ISO C compiler.

Group:		Development/Languages
License:	vbcc license - non-commerical usage only, redistribution not allowed
URL:		http://sun.hasenbraten.de/vbcc/
Source0:	vbcc.tar.gz
Patch0:		vbcc-dtgen-defaults.diff
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	glibc

%description
vbcc is a highly optimizing portable and retargetable ISO C compiler. It supports ISO C according to ISO/IEC 9899:1989 and a subset of the new standard ISO/IEC 9899:1999 (C99).

%prep
%setup -n vbcc -q
%patch0 -p1

%build
mkdir bin
export TARGET=%{target_cpu}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/vbcc/bin
install -m 755 bin/vbcc%{target_cpu} %{buildroot}/opt/vbcc/bin/
install -m 755 bin/vc %{buildroot}/opt/vbcc/bin/
install -m 755 bin/vprof %{buildroot}/opt/vbcc/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/vbcc/bin/vbcc%{target_cpu}
/opt/vbcc/bin/vc
/opt/vbcc/bin/vprof
%doc

%changelog

