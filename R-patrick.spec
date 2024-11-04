#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: 750e50d
#
Name     : R-patrick
Version  : 0.2.0
Release  : 5
URL      : https://cran.r-project.org/src/contrib/patrick_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/patrick_0.2.0.tar.gz
Summary  : Parameterized Unit Testing
Group    : Development/Tools
License  : Apache-2.0
Requires: R-dplyr
Requires: R-purrr
Requires: R-rlang
Requires: R-testthat
Requires: R-tibble
BuildRequires : R-dplyr
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-testthat
BuildRequires : R-tibble
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
lets you add parameters to your unit tests. Parameterized unit tests
    are often easier to read and more reliable, since they follow the DNRY
    (do not repeat yourself) rule.

%prep
%setup -q -n patrick
pushd ..
cp -a patrick buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707102399

%install
export SOURCE_DATE_EPOCH=1707102399
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/patrick/DESCRIPTION
/usr/lib64/R/library/patrick/INDEX
/usr/lib64/R/library/patrick/Meta/Rd.rds
/usr/lib64/R/library/patrick/Meta/features.rds
/usr/lib64/R/library/patrick/Meta/hsearch.rds
/usr/lib64/R/library/patrick/Meta/links.rds
/usr/lib64/R/library/patrick/Meta/nsInfo.rds
/usr/lib64/R/library/patrick/Meta/package.rds
/usr/lib64/R/library/patrick/NAMESPACE
/usr/lib64/R/library/patrick/NEWS.md
/usr/lib64/R/library/patrick/R/patrick
/usr/lib64/R/library/patrick/R/patrick.rdb
/usr/lib64/R/library/patrick/R/patrick.rdx
/usr/lib64/R/library/patrick/help/AnIndex
/usr/lib64/R/library/patrick/help/aliases.rds
/usr/lib64/R/library/patrick/help/paths.rds
/usr/lib64/R/library/patrick/help/patrick.rdb
/usr/lib64/R/library/patrick/help/patrick.rdx
/usr/lib64/R/library/patrick/html/00Index.html
/usr/lib64/R/library/patrick/html/R.css
/usr/lib64/R/library/patrick/tests/testthat.R
/usr/lib64/R/library/patrick/tests/testthat/test-with_parameters.R
