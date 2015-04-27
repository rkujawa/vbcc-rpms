%define vasm_cpu m68k
%define vasm_syntax mot

%define today %(date '+%%y%%m%%d')

Name:		vasm-%{vasm_cpu}_%{vasm_syntax}
Version:	daily%{today}	
Release:	1%{?dist}
Summary:	Retargetable and portable assembler.

Group:		Development/Languages
License:	vasm license - non-commerical usage only, redistribution not allowed
URL:		http://sun.hasenbraten.de/vasm/
Source0:	vasm.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc glibc-devel make gzip tar
Requires:	glibc

%description
vasm is a portable and retargetable assembler to create linkable objects in various formats or absolute code. Multiple CPU-, syntax and output-modules can be selected.

%prep
%setup -n vasm -q

%build
export CPU=%{vasm_cpu}
export SYNTAX=%{vasm_syntax}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/vbcc/bin
install -m 755 vasm%{vasm_cpu}_%{vasm_syntax} %{buildroot}/opt/vbcc/bin/
install -m 755 vobjdump %{buildroot}/opt/vbcc/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/vbcc/bin/vasm%{vasm_cpu}_%{vasm_syntax}
/opt/vbcc/bin/vobjdump
%doc

%changelog

