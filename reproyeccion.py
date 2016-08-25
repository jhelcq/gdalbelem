from osgeo import gdal
import numpy as np
from gdalconst import *

# Read the input raster into a Numpy array
infile = "clasificacion_deforestacion.tif"
data   = gdal.Open(infile, GA_Update)

print(data.GetGeoTransform())
data.SetGeoTransform([60,0,546585,0,-60,8040955])
print(data.GetGeoTransform())

# metadata = data.GetMetadata()
# print(data)
# print(metadata)