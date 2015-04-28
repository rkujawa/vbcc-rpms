%define target_cpu m68k
%define target_asm_syntax mot
%define target_os amigaos

%define today %(date '+%%y%%m%%d')

Group:		Development/Languages
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc glibc-devel make gzip tar

