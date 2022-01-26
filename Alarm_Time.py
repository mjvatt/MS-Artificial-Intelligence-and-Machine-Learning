# -*- coding: utf-8 -*-
"""
Created on Mon May 24 7:45:08 2021

@author: mjvat
"""

def alarm(current_time, alarm_wait):
    
    global alarm_time
    if ((current_time + alarm_wait) < 24):
        alarm_time = current_time + alarm_wait
        return alarm_time
    else: 
        hours_remaining_today = (24 - current_time)
        if ((alarm_wait - hours_remaining_today) < 24):
            alarm_time = alarm_wait - hours_remaining_today
            return alarm_time
        else:
            alarm_time = ((alarm_wait - hours_remaining_today) % 24)
            return alarm_time

def main():
    current_time = int(input('What time is it currently rounded to the nearest hour (0-23):\n'))
    alarm_wait = int(input('In how many hours would you like the alarm to start?\n'))
    alarm(current_time, alarm_wait)
    print('\nThe alarm will go off at {} which is in {} hours'.format(alarm_time, alarm_wait))
    
if __name__ == '__main__':
    main()