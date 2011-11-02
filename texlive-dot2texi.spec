Name:		texlive-dot2texi
Version:	3.0
Release:	1
Summary:	Create graphs within LaTeX using the dot2tex tool
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dot2texi
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dot2texi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dot2texi.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The dot2texi package allows you to embed graphs in the DOT
graph description language in your LaTeX documents. The dot2tex
tool is used to invoke Graphviz for graph layout, and to
transform the output from Graphviz to LaTeX code. The generated
code relies on the TikZ and PGF package or the PSTricks
package. The process is automated if shell escape is enabled.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dot2texi/dot2texi.sty
%doc %{_texmfdistdir}/doc/latex/dot2texi/README
%doc %{_texmfdistdir}/doc/latex/dot2texi/dot2texi.pdf
%doc %{_texmfdistdir}/doc/latex/dot2texi/dot2texi.tex
%doc %{_texmfdistdir}/doc/latex/dot2texi/examples/d2tpstexamples.pdf
%doc %{_texmfdistdir}/doc/latex/dot2texi/examples/d2tpstexamples.tex
%doc %{_texmfdistdir}/doc/latex/dot2texi/examples/d2ttikzexamples.pdf
%doc %{_texmfdistdir}/doc/latex/dot2texi/examples/d2ttikzexamples.tex
%doc %{_texmfdistdir}/doc/latex/dot2texi/examples/docgraphs.pdf
%doc %{_texmfdistdir}/doc/latex/dot2texi/examples/docgraphs.tex
%doc %{_texmfdistdir}/doc/latex/dot2texi/examples/docgraphsorig.pdf
%doc %{_texmfdistdir}/doc/latex/dot2texi/gpl.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
