%include common.spec

Name:		vbcc-target-%{target_cpu}-%{target_os}
Version:	daily%{today}
Release:	1%{?dist}
Summary:	VBCC target for %{target_cpu} %{target_os}.

Group:		Development/Languages
License:	vbcc license - non-commerical usage only, redistribution not allowed
URL:		http://sun.hasenbraten.de/vbcc/
Source0:	vbcc_target_%{target_cpu}-%{target_os}.lha
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#Requires:

%description
VBCC target for %{target_cpu} %{target_os}.

%prep
mkdir -p %{_builddir}/vbcc-target
cd %{_builddir}/vbcc-target
lha x %{SOURCE0}
cd %{_builddir}/vbcc-target/vbcc_target_%{target_cpu}-%{target_os}
%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/vbcc/targets/
rsync -a vbcc-target/vbcc_target_%{target_cpu}-%{target_os}/targets/%{target_cpu}-%{target_os} %{buildroot}/opt/vbcc/targets/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%include vbcc-target-%{target_cpu}-%{target_os}.files

%changelog

