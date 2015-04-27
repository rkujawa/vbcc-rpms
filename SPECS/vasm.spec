Name:		vasm-m68k_mot
Version:	daily
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
export CPU=m68k
export SYNTAX=mot
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/vbcc/bin
install -m 755 vasmm68k_mot %{buildroot}/opt/vbcc/bin/
install -m 755 vobjdump %{buildroot}/opt/vbcc/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/vbcc/bin/vasmm68k_mot
/opt/vbcc/bin/vobjdump
%doc


%changelog

