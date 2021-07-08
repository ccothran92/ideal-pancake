#!/bin/bash
ps axf | grep my_thing.py | grep -v grep | awk '{print "kill -9 " $1}' | sh
python3 /home/pi/Documents/v2/ideal-pancake/ideal-pancake/v2/my_thing.py