#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mlmRev
Version  : 1.0.8
Release  : 26
URL      : https://cran.r-project.org/src/contrib/mlmRev_1.0-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mlmRev_1.0-8.tar.gz
Summary  : Examples from Multilevel Modelling Software Review
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lme4
BuildRequires : R-lme4
BuildRequires : buildreq-R

%description
as well as other well-known data sets from the multilevel modelling
  literature.

%prep
%setup -q -c -n mlmRev
cd %{_builddir}/mlmRev

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589749619

%install
export SOURCE_DATE_EPOCH=1589749619
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlmRev
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlmRev
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlmRev
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mlmRev || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mlmRev/DESCRIPTION
/usr/lib64/R/library/mlmRev/INDEX
/usr/lib64/R/library/mlmRev/Meta/Rd.rds
/usr/lib64/R/library/mlmRev/Meta/data.rds
/usr/lib64/R/library/mlmRev/Meta/features.rds
/usr/lib64/R/library/mlmRev/Meta/hsearch.rds
/usr/lib64/R/library/mlmRev/Meta/links.rds
/usr/lib64/R/library/mlmRev/Meta/nsInfo.rds
/usr/lib64/R/library/mlmRev/Meta/package.rds
/usr/lib64/R/library/mlmRev/Meta/vignette.rds
/usr/lib64/R/library/mlmRev/NAMESPACE
/usr/lib64/R/library/mlmRev/data/Rdata.rdb
/usr/lib64/R/library/mlmRev/data/Rdata.rds
/usr/lib64/R/library/mlmRev/data/Rdata.rdx
/usr/lib64/R/library/mlmRev/doc/MlmSoftRev.R
/usr/lib64/R/library/mlmRev/doc/MlmSoftRev.Rnw
/usr/lib64/R/library/mlmRev/doc/MlmSoftRev.pdf
/usr/lib64/R/library/mlmRev/doc/StarData.R
/usr/lib64/R/library/mlmRev/doc/StarData.Rnw
/usr/lib64/R/library/mlmRev/doc/StarData.pdf
/usr/lib64/R/library/mlmRev/doc/index.html
/usr/lib64/R/library/mlmRev/help/AnIndex
/usr/lib64/R/library/mlmRev/help/aliases.rds
/usr/lib64/R/library/mlmRev/help/mlmRev.rdb
/usr/lib64/R/library/mlmRev/help/mlmRev.rdx
/usr/lib64/R/library/mlmRev/help/paths.rds
/usr/lib64/R/library/mlmRev/html/00Index.html
/usr/lib64/R/library/mlmRev/html/R.css
/usr/lib64/R/library/mlmRev/original/text-star.zip
/usr/lib64/R/library/mlmRev/tests/guImmun.R
/usr/lib64/R/library/mlmRev/tests/lmerTest.R
/usr/lib64/R/library/mlmRev/tests/versions.R
