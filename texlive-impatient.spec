Name:		texlive-impatient
Version:	20180303
Release:	2
Summary:	Free edition of the book "TeX for the Impatient"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/impatient
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This directory mirrors the canonical source of the project
which is maintaining the book "TeX for the Impatient", which is
now out of print. The book is also available in French
translation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/impatient

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
