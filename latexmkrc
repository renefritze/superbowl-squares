@default_files = ('superbowl_squares.tex');

$latex = 'latex -interaction=nonstopmode -recorder -synctex=1 --src-specials -shell-escape %O %S';

$lualatex= 'lualatex -interaction=nonstopmode -recorder -synctex=1 -shell-escape %O %S';

# this is for old (<=4.45) latexmk versions
$pdf_mode = 1;
$pdflatex = $lualatex;
# newer version would just set
# $pdf_mode = 4

$postscript_mode = $dvi_mode = 0;

# Use bibtex if a .bib file exists
$bibtex_use = 1;

$pdf_previewer = 'xdg-open';

# Also remove pdfsync files on clean
$clean_ext = 'pdfsync synctex.gz';
