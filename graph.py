import pandas as pd
import os
import geopandas as gpd
import shapely.wkt
import seaborn as sns
from Plotting import run_plot, run_plot_arima
sns.set(color_codes=True)
import matplotlib.pyplot as pl
## Define default paths for sample data
input_path=os.path.abspath('')
input_path=os.path.join(input_path.split("CometTS")[0],"CometTS/VIIRSData")

def gen_plots(input_csv):
    df = pd.read_csv(input_csv)
    df = df.loc[df['count'] != 0]
    df = df.sort_values(['date'])
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
    ## Specific flags can be passed to the function to modify the plots, ses CometTS.Plotting code for full listing
    # run_plot(df, y_label="NDVI", title_label= "NDVI over time - ID: ")
    run_plot(df, ymax=100,figname='Brightness')

input_CSV = os.path.join(input_path, "POLYGON_FullStats.csv")
gen_plots(input_CSV)
