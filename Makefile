#Executable to create a ARIMA model
report.pdf: report.tex ARIMA1.png
	latexmk -pdf $<

ARIMA1.png: plot_result.py  
	plot_result.py 

clean:
	rm -f *.o
