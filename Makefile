#Executable to create a ARIMA model
ARIMA: main.o output.o 
	gcc -o ARIMA main.o output.o 

main.0: main.c function.h
	gcc -c main.c

output.0: output.c function.h
	gcc -c output.c 

clean:
	rm -f ARIMA *.o

report.pdf: report.tex ARIMA.png
	latexmk -pdf $<

