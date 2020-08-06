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
input_path=os.path.join(input_path.split("Notebooks"0)[],"CometTS/VIIRS_Sample")