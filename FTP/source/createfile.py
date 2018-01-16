#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:10:22 2017

@author: root
"""

from ftplib import FTP
import os

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
		
ftp = FTP('172.1.254.125')
ftp.login('opmstools','$opms$123')

ftp.cwd("/Rocia") #changing to /Rocia
 
 
upload(ftp, "1000.txt")