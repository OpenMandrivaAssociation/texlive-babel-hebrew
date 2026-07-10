%global tl_name babel-hebrew
%global tl_revision 77914

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	Babel support for Hebrew
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/hebrew
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-hebrew.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-hebrew.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-hebrew.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of Hebrew
in babel. Macros to control the use of text direction control of TeX--
XeT and e-TeX are provided (and may be used elsewhere). Some shortcuts
are defined, as well as translations to Hebrew of standard "LaTeX
names". For questions, bug reports, or support, please open an issue in
the repository. Note: the package is in maintenance mode. Bugs will be
fixed, but no new features will be added. The .ldf file is only
compatible with pdfLaTeX or LaTeX. Even then, for documents containing
more than a short text in Hebrew, it is strongly recommended to use
LuaTeX (with babel's .ini file or polyglossia). For short texts with
pdfTeX, use the .ini file. Consult the documentation of babel for better
settings for Hebrew.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-hebrew
%dir %{_datadir}/texmf-dist/source/generic/babel-hebrew
%dir %{_datadir}/texmf-dist/tex/generic/babel-hebrew
%doc %{_datadir}/texmf-dist/doc/generic/babel-hebrew/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-hebrew/hebrew.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-hebrew/hebrew.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-hebrew/hebrew.ins
%{_datadir}/texmf-dist/tex/generic/babel-hebrew/hebcal.sty
%{_datadir}/texmf-dist/tex/generic/babel-hebrew/hebrew.ldf
%{_datadir}/texmf-dist/tex/generic/babel-hebrew/hebrew_newcode.sty
%{_datadir}/texmf-dist/tex/generic/babel-hebrew/hebrew_oldcode.sty
%{_datadir}/texmf-dist/tex/generic/babel-hebrew/hebrew_p.sty
%{_datadir}/texmf-dist/tex/generic/babel-hebrew/rlbabel.def
