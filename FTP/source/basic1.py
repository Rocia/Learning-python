from ftplib import FTP
import sys

ftp = FTP('172.1.254.125')
ftp.login('opmstools','$opms$123')

ftp.cwd("/Rocia") #changing to /Rocia

def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print "Error"
 
 
ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "ftplib-example-1")
 
ftp.cwd('/pub/')         # change directory to /pub/
getFile(ftp,'README.nluug')
 
ftp.quit()