#Executable to create a ARIMA model
report.pdf: report.tex 
	latexmk -pdf $<

plot_result.0: plot_result.py San_Juan_FullStats.csv 
	gcc -c plot_result.py San_Juan_FullStats.csv


clean:
	rm -f *.o
