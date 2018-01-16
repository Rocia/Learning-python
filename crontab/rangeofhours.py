#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:47:12 2017

@author: rocia
"""

import crontab
 
tab = crontab.CronTab(user=True)
cmd = 'python /home/rocia/Desktop/a.py'
cron_job = tab.new(command=cmd)
cron_job.minute().on(1)
cron_job.hour().during(9,18)
#writes content to crontab
tab.write()
print (tab.render())