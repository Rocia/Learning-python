#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:38:24 2017

@author: root
"""

def crony(): 
    from crontab import CronTab

    cron = CronTab(user=True)

    job = cron.new(command='cd /root python /home/rocia/Desktop/a.py', comment = 'test')

    #cron.write()
    for job in cron:
	    if job.comment == 'test':
	        print (job)
if __name__ == "__main__":
	cron = crony()
	print (cron)
	
  