import arcpy
import os
from datetime import datetime
 
# Import the toolbox containing the model.  This toolbox
#  has an alias of "gpxtools"
#
arcpy.ImportToolbox(r"c:\importgpx\myGPXstuff.tbx")
 
# Run the model.  The model has two parameters, the input
#  .gpx file and the feature class to update
#
arcpy.ImportGPX_gpxtools(r"c:\ftp\inbox\datadrop.gpx",
                         r"c:\ftp\server.sde\gpx_tracks")
 
# Now that the input gpx file has been processed, rename it
#   to have the date and time.
#
os.rename(r"c:\ftp\inbox\datadrop.gpx",
          r"c:\ftp\inbox\datadrop{}.gpx".format(datetime.strftime(datetime.now(), "%Y%m%d"))
