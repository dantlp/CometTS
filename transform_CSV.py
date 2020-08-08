#Imports
import os
from CometTS.CometTS import run_comet
from CometTS.Plotting import run_plot, run_plot_arima
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
input_path=os.path.join(input_path.split("CometTS")[0],"CometTS/VIIRSData")
I=run_comet(C:\Users\dante\Documents\Mun\CMSC6950\CometTS\CometTS/VIIRS_Sample\Raster_List.csv,C:\Users\dante\Documents\Mun\CMSC6950\CometTS\CometTS/VIIRS_Sample\San_Juan.shp,C:\Users\dante\Documents\Mun\CMSC6950\CometTS\CometTS/VIIRS_Sample\Malaga.csv,-1,0,maskit=FALSE)
plt.show(I)