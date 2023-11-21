%define         openssl_version 1.1.1g
Name:           penglai-ssl
Version:        2.10
Release:        1
Summary:        Penglai SSL
ExclusiveArch:	riscv64
License:        OpenSSL and BSD-3-Clause
URL:            https://gitee.com/nicolas-cage/penglai-ssl
Source0:        https://github.com/intel/intel-sgx-ssl/archive/intel-sgx-ssl-lin_%{version}_%{openssl_version}.zip
Source1:        https://www.openssl.org/source/old/1.1.1/openssl-%{openssl_version}.tar.gz


BuildRequires:  cmake

Requires:       glibc

%description
The penglai SSL library is intended to 
provide cryptographic services for pengali enclave applications.
The Penglai library is based on the underlying OpenSSL* 
Open Source project, providing a full-strength general purpose
cryptography library. Supported OpenSSL version is 1.1.1g.


%package devel
Summary:        Development files for pengali sgx ssl
Requires:       %{name} = %{version}-%{release}

%description devel
%{summary}.


%package_help
%define debug_package %{nil}

%prep

%setup -q -n intel-sgx-ssl-lin_2.10_1.1.1g
# %patch0 -p2
# %patch1 -p2
# %patch2 -p2
%build
cp %{SOURCE1} openssl_source/
cd Linux
make sgxssl_no_mitigation

%install
cd Linux
make install DESTDIR=$RPM_BUILD_ROOT/opt/pengali/openssl
cp -r package/docs $RPM_BUILD_ROOT/opt/pengali/openssl/
cp   ../README.md $RPM_BUILD_ROOT/opt/pengali/openssl/docs/
cp   License.txt $RPM_BUILD_ROOT/opt/pengali/openssl/docs/

%files
/opt/pengali/openssl/lib64/*
/opt/pengali/openssl/docs/*

%files devel
/opt/pengali/openssl/include/*

#%changelog
# * Sat Mar 20 2021 zhangguangzhi <zhangguangzhi3@huawei.com> - 2.10-6
# - modify for sp
# * Mon Feb 22 2021 chenmaodong <chenmaodong@huawei.com> - 2.10-5
# - add ocall file operation and getenv
# * Tue Jan 26 2021 yanlu <yanlu14@huawei.com> - 2.10-4
# - add ocall file operation and getenv
# * Mon Jan 18 2021 yanlu <yanlu14@huawei.com> - 2.10-3
# - add ocall read and write
# * Mon Jan 18 2021 chenmaodong <chenmaodong@huawei.com> - 2.10-2
# - init
# * Tue Dec 29 2020 chenmaodong <chenmaodong@huawei.com> - 2.10-1
# - init

# Patch0:         0001-add-ocall-read-write.patch
# Patch1:         0002-add-ocall-file-operation-and-getenv.patch 
# Patch2:         0003-modify-for-sp.patch