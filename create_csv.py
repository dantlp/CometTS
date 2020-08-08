## Import your packages
import os
from CometTS.CSV_It import csv_it

input_path=os.path.abspath('')
input_path=os.path.join(input_path.split("CometTS")[0],"CometTS/VIIRSData")

#The input directory for the data. Specify directory directly for another directory.
input_dir = input_path
# The naming pattern for your time-series data, if not necessary, just set at "*"
TSdata = "S*rade9*.tif"
# The number of observations that were aggregated per date-somewhat useful is working with monthly composite data
Observations = "S*cvg*.tif"
# The naming pattern for your masked data
Mask = "S*cvg*.tif"
# The location of the date within your filename.  Note python indexing of string here
DateLoc = "10:18"

gdf_out = csv_it(input_dir, TSdata, Observations, Mask, DateLoc)
output = os.path.join(input_dir, 'Raster_List.csv')
gdf_out.to_csv(output)