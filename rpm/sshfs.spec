Name:       sshfs
Version:    2.6
Release:    1
Summary:    Fuse sshfs client.

License:    GPLv2
Group:      Applications/Internet
URL:        https://github.com/libfuse/sshfs
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  automake
BuildRequires:  pkgconfig(fuse) >= 2.2
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
Requires:       openssh-clients

%description
Sshfs is a filesystem client based on the SSH File Transfer Protocol. Since most SSH servers already support this protocol it is very easy to set up: i.e. on the server side there's nothing to do. On the client side mounting the filesystem is as easy as logging into the server with ssh.

The idea of sshfs was taken from the SSHFS filesystem distributed with LUFS, which I found very useful. There were some limitations of that codebase, so I rewrote it. Features of this implementation are:

 - Based on FUSE (the best userspace filesystem framework for Linux ;)
 - Multithreading: more than one request can be on it's way to the server
 - Allowing large reads (max 64k)
 - Caching directory contents
 - Reconnect on failure


%prep
%setup -q -n %{name}-%{version}/%{name}

%build
autoreconf -v -f -i
%configure --disable-sshnodelay
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README.md AUTHORS COPYING ChangeLog
%{_bindir}/sshfs
%{_mandir}/man1/sshfs.1.gz
