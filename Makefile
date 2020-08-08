#Executable to create a ARIMA model
report.pdf:  Brightness.png
	latexmk -pdf $<

Brightness.png: ./VIIRSData/POLYGON_FullStats.csv graph.py
	python3 .\graph.py 

./VIIRSData/POLYGON_FullStats.csv: ./VIIRSData/Raster_List.csv ./VIIRSData/POLYGON.shp transform_CSV.py
	python transform_CSV.py 

./VIIRSData/Raster_List.csv: create_csv.py
	python3 create_csv.py


.PHONY: clean almost_clean
clean: almost_clean
	rm report.pdf
	rm ./VIIRSData/Raster_List.csv
	rm ./VIIRSData/POLYGON_FullStats.csv
	rm Brightness.png 
	rm First_plot.png
