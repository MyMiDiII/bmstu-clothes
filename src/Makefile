report : report.tex
	pdflatex report.tex
	bibtex report
	pdflatex report.tex
	pdflatex report.tex
	mkdir pdf
	mv report.pdf ../pdf/
	mkdir out
	mv *.aux *.log *.bbl *.blg *.dvi ./out/

clear :
	rm -rf ./out/ 
	rm *.aux *.log *.bbl *.blg *.dvi

