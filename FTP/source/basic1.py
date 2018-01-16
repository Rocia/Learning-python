from ftplib import FTP

ftp = FTP('172.1.254.125')
ftp.login('opmstools','$opms$123')

print ("File List: ")

files = ftp.dir()

print (files)

ftp.cwd("/Rocia") #changing to /Rocia