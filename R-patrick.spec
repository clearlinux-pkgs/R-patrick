#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-patrick
Version  : 0.2.0
Release  : 2
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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689806465

%install
export SOURCE_DATE_EPOCH=1689806465
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
