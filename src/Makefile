report : report.tex
	pdflatex report.tex
	bibtex report
	pdflatex report.tex
	pdflatex report.tex
	-mkdir ../pdf
	mv report.pdf ../pdf/
	-mkdir out
	-mv *.aux *.log *.bbl *.blg *.dvi ./out/
	okular ../pdf/report.pdf

clear :
	-rm -rf ./out/ ../pdf/
	-rm *.aux *.log *.bbl *.blg *.dvi *.out *.pdf

