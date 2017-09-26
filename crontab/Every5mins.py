#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:35:54 2017

@author: rocia
"""

'''
from crontab import CronTab
 
tab = CronTab(user='www',fake_tab='True')
cmd = '/var/www/pjr-env/bin/python /var/www/PRJ/job.py'
cron_job = tab.new(cmd)
cron_job.minute().every(5)
#writes content to crontab
tab.write()
print (tab.render())''' 
def main(): 
    from crontab import CronTab
    #from crontab import CronSlice

    cron = CronTab(user=True)

    job = cron.new(command='python /home/rocia/Desktop/a.py')
    job.minute.every(2)

    cron.write()
    print (cron.render()) 


if __name__ == "__main__":
  main()