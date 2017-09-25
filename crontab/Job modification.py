#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:35:31 2017

@author: root
"""

from crontab import CronTab
 
my_cron = CronTab(user='root')
for job in my_cron:
    if job.comment == 'test':
	    job.hour.every(10)
	    my_cron.write()
print ('Cron job modified successfully')
print(job)