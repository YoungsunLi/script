#!user/bin/env python
# -*- coding: utf-8 -*-
from os import system
from time import sleep

try:
    while True:
        temp_file = open('/sys/class/thermal/thermal_zone0/temp')
        temp = float(temp_file.read()) / 1000
        temp_file.close()

        system('clear')
        print('temp = %2.2f\'C' %temp)

        sleep(1)
except(KeyboardInterrupt, SystemExit):
    pass
