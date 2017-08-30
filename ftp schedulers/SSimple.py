import sys
import platform
import imp
print "Importing arcpy... this may take a moment\n"
import arcpy
 
# Open a log file to write to
#
f = open(r'E:\schedule.log','w')
 
# Write date/time
#
f.write(time.strftime('%x %X'))
f.write('\n')
 
# Test receiving of arguments/parameters via arcpy
#
f.write("Parameter 0 : " + arcpy.GetParameterAsText(0) + "\n")
 
# Python info
#
f.write("Python EXE : " + sys.executable + "\n")
f.write("Architecture : " + platform.architecture()[0] + "\n")
f.write("Path to arcpy : " + imp.find_module("arcpy")[1] + "\n")
f.close()
