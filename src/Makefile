report : texReport title
	pdflatex report.tex
	bibtex report
	pdflatex report.tex
	pdflatex report.tex
	-mkdir ../pdf
	mv report.pdf ../pdf/
	-mkdir out
	-mv *.aux *.log *.bbl *.blg *.dvi *.out ./out/
	okular ../pdf/report.pdf

texReport : report.tex
	pdflatex report.tex

clear :
	-rm -rf ./out/ ../pdf/
	-rm *.aux *.log *.bbl *.blg *.dvi *.out *.pdf

