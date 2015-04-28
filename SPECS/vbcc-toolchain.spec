%include common.spec

Name:		vbcc-toolchain-%{target_cpu}_%{target_os}
Version:	daily%{today}	
Release:	1%{?dist}
Summary:	VBCC based toolchain for %{target_os} (%{target_cpu}).

Group:		Development/Languages
License:	vbcc/vasm/vlink licenses - non-commerical usage only, redistribution not allowed
URL:		http://sun.hasenbraten.de/vbcc/

Requires:	vasm-%{target_cpu}_%{target_asm_syntax} vlink vbcc-%{target_cpu} vbcc-target-%{target_cpu}-%{target_os} 

%description
Package agregating vbcc, vlink, vasm for %{target_cpu}-%{target_os}.

%prep

%build

%install

%clean

%files

%changelog

