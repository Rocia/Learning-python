#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:42:40 2017

@author: root
"""

from ftplib import FTP
ftp = FTP('172.1.254.125')
ftp.login('opmstools','$opms$123')
listoffiles = ftp.nlst()
'''
['172.29.6.31', 'CSS_ePub', 'Depository_Source', 'EXE_FILES', 'home', 'Nikhil_Upload', 'Ravi', 'Rocia', 'ssss', 'test', 'WK_CCH_CSS', 'WMS', 'WMSTEST']
'''
print( ftp.getwelcome())
'''
220 FTP SERVER,UNAUTHORIZED ACCESS RESTRICTED
'''
print( ftp.pwd())
'''/Rocia'''
ftp.voidcmd('ls')
ftp.cwd('Rocia')
#ftp.retrbinary('RETR 1000.txt', open('1000.txt', 'wb').write)
