# Restore old style debuginfo creation for rpm >= 4.14.
%undefine _debugsource_packages
%undefine _debuginfo_subpackages
%global debug_package %{nil}

# -*- rpm-spec -*-
Summary:        UBS atomic shared-memory primitives
Name:           ubs-atomic
ExclusiveArch:  aarch64
Version:        1.0.0
Release:        7
License:        Mulan PSL v2
URL:            https://atomgit.com/openeuler/ubs-atomic
Source0:        %{name}-%{version}.tar.gz
Group:          Development/Libraries
Vendor:         Huawei Technologies Co., Ltd.
Prefix: /usr

BuildRequires:  cmake >= 3.22 make >= 4.3 gcc-c++ >= 10.3 gcc >= 10.3
BuildRequires:  glibc-devel >= 2.34 libstdc++-devel >= 10.3
BuildRequires:  libboundscheck >= v1.1
BuildRequires:  ninja-build >= 1.10 bash bc coreutils
Requires:       glibc >= 2.34 libgcc >= 10.3 libstdc++ >= 10.3 libboundscheck >= v1.1

%define _rpmdir %_topdir/RPMS
%define _srcrpmdir %_topdir/SRPMS
%define _rpmfilename %{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}.rpm
%define _unpackaged_files_terminate_build 0

%define project_dir %{name}-%{version}
%define cmake_build_dir dist/release

%description
UBS atomic shared-memory primitives.

%prep
%setup -q -T -b 0 -c -n %{project_dir}

%build
cd %{_builddir}/%{project_dir}/
cmake -S . -B %{cmake_build_dir} -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DUBS_ATOMIC_VERSION=%{version} \
    -DUBS_ATOMIC_PACKAGE_RELEASE=%{release} \
    -DBUILD_TESTS=OFF \
    -DENABLE_COVERAGE=OFF \
    -DFORCE_COLORED_OUTPUT=ON
cmake --build %{cmake_build_dir} --target all -j %{?_smp_build_ncpus}

%install
cd %{_builddir}/%{project_dir}/
cmake --install %{cmake_build_dir} --prefix %{buildroot}/usr

%files
%defattr(755,root,root,-)
/usr/lib64/libubs-atomic.so
%defattr(644,root,root,-)
/usr/include/ub_dist_comm_queue.h
/usr/include/ub_dist_lock.h
/usr/include/ub_dist_tx_res.h

%changelog
* Tue Jul 14 2026 David Hwang <huangdewei@huawei.com> - 1.0.0-7
- fix: For B003 package, form PR40
* Mon June 15 2026 Sami <abudusaimikuerban@h-partners.com> - 1.0.0-6
- fix: For B026 package, form PR45
* Tue June 02 2026 Sami <abudusaimikuerban@h-partners.com> - 1.0.0-5
- fix: For B020 package, form PR39
* Tue May 26 2026 Sami <abudusaimikuerban@h-partners.com> - 1.0.0-4
- fix: For B017 package, form PR33
* Tue May 19 2026 Sami <abudusaimikuerban@h-partners.com> - 1.0.0-3
- fix: For B015 package, form PR25
* Tue May 12 2026 David Hwang <huangdewei@huawei.com> - 1.0.0-2
- fix: For B013 package, form PR19
* Tue May 12 2026 David Hwang <huangdewei@huawei.com> - 1.0.0-1
- Init ubs-atomic rpm.
