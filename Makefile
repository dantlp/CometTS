#Executable to create a ARIMA model
report.pdf: report.tex ARIMA.png
	latexmk -pdf $<

create.0= create_csv.py 
	gcc -c create_csv.py

plot_result.0: plot_result.py
	gcc -c plot_result.py 

clean:
	rm -f ARIMA*.png



