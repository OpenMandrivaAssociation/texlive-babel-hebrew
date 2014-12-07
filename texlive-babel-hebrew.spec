# revision 30273
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-hebrew
Version:	20131013
Release:	8
Summary:	TeXLive babel-hebrew package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-hebrew.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-hebrew.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-hebrew.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-hebrew package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-hebrew/8859-8.def
%{_texmfdistdir}/tex/generic/babel-hebrew/cp1255.def
%{_texmfdistdir}/tex/generic/babel-hebrew/cp862.def
%{_texmfdistdir}/tex/generic/babel-hebrew/he8OmegaHebrew.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8aharoni.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8cmr.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8cmss.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8cmtt.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8david.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8drugulin.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8enc.def
%{_texmfdistdir}/tex/generic/babel-hebrew/he8frankruehl.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8miriam.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8nachlieli.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8yad.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/hebcal.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/hebfont.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/hebrew.ldf
%{_texmfdistdir}/tex/generic/babel-hebrew/hebrew_newcode.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/hebrew_oldcode.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/hebrew_p.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/lheclas.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lhecmr.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lhecmss.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lhecmtt.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lhecrml.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheenc.def
%{_texmfdistdir}/tex/generic/babel-hebrew/lhefr.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheredis.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheshold.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheshscr.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheshstk.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/rlbabel.def
%{_texmfdistdir}/tex/generic/babel-hebrew/si960.def
%doc %{_texmfdistdir}/doc/generic/babel-hebrew/00readme.heb
%doc %{_texmfdistdir}/doc/generic/babel-hebrew/heb209.pdf
%doc %{_texmfdistdir}/doc/generic/babel-hebrew/hebinp.pdf
%doc %{_texmfdistdir}/doc/generic/babel-hebrew/hebrew.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-hebrew/heb209.dtx
%doc %{_texmfdistdir}/source/generic/babel-hebrew/hebinp.dtx
%doc %{_texmfdistdir}/source/generic/babel-hebrew/hebrew.dtx
%doc %{_texmfdistdir}/source/generic/babel-hebrew/hebrew.fdd
%doc %{_texmfdistdir}/source/generic/babel-hebrew/hebrew.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
