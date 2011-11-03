# revision 21214
# category Package
# catalog-ctan /info/impatient
# catalog-date 2009-06-03 15:47:29 +0200
# catalog-license fdl
# catalog-version undef
Name:		texlive-impatient
Version:	20090603
Release:	1
Summary:	Free edition of the book "TeX for the Impatient"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/impatient
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This directory mirrors the canonical source of the project
which is maintaining the book "TeX for the Impatient", which is
now out of print. The book is also available in French
translation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/impatient/Makefile
%doc %{_texmfdistdir}/doc/plain/impatient/README
%doc %{_texmfdistdir}/doc/plain/impatient/backm.tex
%doc %{_texmfdistdir}/doc/plain/impatient/book.pdf
%doc %{_texmfdistdir}/doc/plain/impatient/book.tex
%doc %{_texmfdistdir}/doc/plain/impatient/capsule.tex
%doc %{_texmfdistdir}/doc/plain/impatient/concepts.tex
%doc %{_texmfdistdir}/doc/plain/impatient/config.tex
%doc %{_texmfdistdir}/doc/plain/impatient/copyrght.tex
%doc %{_texmfdistdir}/doc/plain/impatient/eplain.tex
%doc %{_texmfdistdir}/doc/plain/impatient/errata.future
%doc %{_texmfdistdir}/doc/plain/impatient/errors.tex
%doc %{_texmfdistdir}/doc/plain/impatient/examples.tex
%doc %{_texmfdistdir}/doc/plain/impatient/fdl.tex
%doc %{_texmfdistdir}/doc/plain/impatient/fonts.tex
%doc %{_texmfdistdir}/doc/plain/impatient/frontm.tex
%doc %{_texmfdistdir}/doc/plain/impatient/genops.tex
%doc %{_texmfdistdir}/doc/plain/impatient/index.tex
%doc %{_texmfdistdir}/doc/plain/impatient/index1.icn
%doc %{_texmfdistdir}/doc/plain/impatient/index2.icn
%doc %{_texmfdistdir}/doc/plain/impatient/macros.tex
%doc %{_texmfdistdir}/doc/plain/impatient/math.tex
%doc %{_texmfdistdir}/doc/plain/impatient/modes.tex
%doc %{_texmfdistdir}/doc/plain/impatient/pages.tex
%doc %{_texmfdistdir}/doc/plain/impatient/paras.tex
%doc %{_texmfdistdir}/doc/plain/impatient/preface.tex
%doc %{_texmfdistdir}/doc/plain/impatient/read1st.tex
%doc %{_texmfdistdir}/doc/plain/impatient/tips.tex
%doc %{_texmfdistdir}/doc/plain/impatient/usebook.tex
%doc %{_texmfdistdir}/doc/plain/impatient/usermacs.tex
%doc %{_texmfdistdir}/doc/plain/impatient/usingtex.tex
%doc %{_texmfdistdir}/doc/plain/impatient/xmptext.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
