#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:45:41 2017

@author: root
"""
from crontab import CronTab
 
my_cron = CronTab(user='root')
my_cron.remove_all()
for job in my_cron:
	print(job)