# CometTS
Final Proyect CMSC6950

This proyect consists in utilizing the Project CometTS through automizing a file reproducing the work.
 
Installation

Python 2.7 or 3.6 are the base requirements plus several packages. 
CometTS can be installed in multiple ways including conda, pip, docker, and cloning this repository.

USE

pip install CometTS 

#If this does not work 

    git clone https://github.com/CosmiQ/CometTS.git
    cd CometTS
    conda env create -f environment.yml
    source activate CometTS
    pip install CometTS

How to download VIIIRS Files
Enter https://eogdata.mines.edu/download_dnb_composites.html
Select area and download both files from desired month
Store Data as with the same structure

VIIRSData/

└ Lat075N_Long060W

    ├ SVDNB_npp_20120401-20120430_75N060W_vcmcfg_v10_c201605121456

    │   ├ SVDNB_npp_20120401-20120430_75N060W_vcmcfg_v10_c201605121456.avg_rade9

    │   ├ SVDNB_npp_20120401-20120430_75N060W_vcmcfg_v10_c201605121456.cf_cvg

    ├ SVDNB_npp_20120501-20120531_75N060W_vcmcfg_v10_c201605121458

    │   ├ SVDNB_npp_20120501-20120531_75N060W_vcmcfg_v10_c201605121458.avg_rade9

    │   ├ SVDNB_npp_20120501-20120531_75N060W_vcmcfg_v10_c201605121458.cf_cvg.tif

    ├ SVDNB_npp_20120601-20120630_75N060W_vcmcfg_v10_c201605121459

get in folder, and extract the files using the code tar -xzvf "Filename with extension .tgz"

go like that in every file to get selected file

Select area of interest and monthly data 

Select Area of study with https://geojson.io/ selecting it as a poligon. See Demo to see Malaga Example

Save as Shapefile and extract inside VIIRSData

execute make file, this should create a Raster_List, Create a FullSTAT file, Create 
a ANOVA FILE and Create a pdf Report. (make File not working when tested. Partially worked in Conda Python 3.7.8)

Had To Edit Original Coding in Plotting, given that the code did not let me Store png file given the order of operations in matplotlib show function and savefigure.


License

License use from Apache License 2004 ©
