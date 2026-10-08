Name:           ooaudit
Version:        0.2.0
Release:        1%{?dist}
Summary:        Immutable audit recorder logging system calls, IO streams, and agent decisions.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooaudit
Source0:        ooaudit-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooaudit is a sovereign, capability-bounded ACTION LEDGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooaudit
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooaudit-uninstall

%files
/usr/bin/ooaudit
/usr/bin/ooaudit-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign action ledger and cryptographic hash-chain auditor
