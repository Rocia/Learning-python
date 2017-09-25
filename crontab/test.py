#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:38:24 2017

@author: root
"""

def main(): 
    from crontab import CronTab

    cron = CronTab(user=True)

    job = cron.new(command='python /home/rocia/Desktop/a.py')
    job.minute.on(2)
    job.hour.on(12)

    cron.write()

if __name__ == "__main__":
  main()