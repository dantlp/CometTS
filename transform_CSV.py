#Imports
import os
from CometTS.CometTS import run_comet
from Plotting import run_plot, run_plot_arima
from CometTS.ARIMA import run_arima, timeseries_trend
import ipywidgets as widgets
from IPython.display import Javascript, display, clear_output
from ipywidgets import interact, interactive, fixed, interact_manual
import matplotlib.pyplot as plt
import seaborn as sns
import shapely
import pandas as pd
import geopandas as gpd
sns.set(color_codes=True)

## Define default paths for sample data
input_path=os.path.abspath('')
input_path=os.path.join(input_path.split("CometTS")[0],"CometTS\VIIRSData")

directory_csv = os.path.join(input_path,'Raster_List.csv')
zonalpoly = os.path.join(input_path,'POLYGON.shp')
NoDataValue = '-1'
mask_value ='0'

#create CSV file with analisis
print(directory_csv)
I = run_comet(
    directory_csv,
    zonalpoly,
    NoDataValue,
    mask_value,
    maskit=True)
run_plot(I,figname='First_plot.png')




