import pandas as pd
import os
import geopandas as gpd
import shapely.wkt
import seaborn as sns
from CometTS.Plotting import run_plot, run_plot_arima
sns.set(color_codes=True)
import matplotlib.pyplot as pl
## Define default paths for sample data
Pic_Path=os.path.abspath('')
Pic_Path=os.path.join(Pic_Path.split("CometTS")[0],"CometTS/VIIRSData")
input_path=os.path.abspath('')
input_path=os.path.join(input_path.split("CometTS")[0],"CometTS/VIIRSData")

def gen_plots(input_csv):
    df = pd.read_csv(input_csv)
    df = df.loc[df['count'] != 0]
    df = df.sort_values(['date'])
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
    ## Specific flags can be passed to the function to modify the plots, ses CometTS.Plotting code for full listing
    # run_plot(df, y_label="NDVI", title_label= "NDVI over time - ID: ")
    run_plot(df, ymax=100)
    
    
def gen_plots_arima(input_csv):
    df = pd.read_csv(input_csv)
    df = df.loc[df['count'] != 0]
    df = df.sort_values(['date'])
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
    ## Specific flags can be passed to the function to modify the plots, ses CometTS.Plotting code for full listing
    # run_plot(df, y_label="NDVI", title_label= "NDVI over time - ID: ")
    run_plot_arima(df, title_label= "Brightness Over Time, with ARIMA Analysis", ymax=100)

input_CSV = os.path.join(input_path, "San_Juan_FullStats.csv")
gen_plots(input_CSV)
Pic_Path
pl.savefig('ARIMA1.png')