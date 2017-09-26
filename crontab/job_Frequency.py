#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:47:29 2017

@author: root
"""
from crontab import CronTab
my_cron = CronTab(user='root')
my_cron.remove_all()
my_cron.write()
job = my_cron.new(command='python /home/rocia/Desktop/a.py', comment='hi')
my_cron.write()

for job in my_cron:
    print (job)	
    print (job.frequency())
    print (job.frequency_per_hour())