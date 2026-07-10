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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

