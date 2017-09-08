#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:15:41 2017

@author: root
"""

from ftplib import FTP
#import sys

ftp = FTP('172.1.254.125')
ftp.login('opmstools','$opms$123')

ftp.cwd("/Rocia") #changing to /Rocia

def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print ("Error")
 
 

 
ftp.cwd('/Rocia')         # change directory to /pub/
getFile(ftp,'1000.txt')
 
ftp.quit()