#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:03:25 2017

@author: root
"""

import datetime
from crontab import CronTab
 
my_crons = CronTab(user='root')
for job in my_crons:
    sch = job.schedule(date_from=datetime.datetime.now())
    print (sch.get_next())