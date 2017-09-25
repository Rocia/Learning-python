#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:38:23 2017

@author: root
"""

from crontab import CronTab
 
my_cron = CronTab(user='root')
for job in my_cron:
    if job.comment == 'test':
        my_cron.remove(job)
        my_cron.write()
		
for job in my_cron:
	print(job)
	
	
#alternate
	
	'''
	my_cron.remove(comment='dateinfo')
	
	'''