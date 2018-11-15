# Mobin Anandwala
# 05/06/2016
# Breathing Log
# This script will log when each brething code is called from the breathing2 functions

from NewBorn import NewBorn
import os
import datetime
import time
from time import sleep

name = "C:\Users\JSSARPLH0031\Documents\BlogTest"
today = datetime.date.today()
log = name + "-" + str(today) + ".csv"
file = open(log,"wb")


# Add readings to the file
if os.stat(log).st_size == 0:
	file.write(str(now),"BreathingRate, TypeofBreathing\n")

for i in range(20,71):
    now = datetime.datetime.now()
    Test = NewBorn(i)
    file.write(str(now) + "," + str(i) + "," + Test + "," +  "\n")
    file.flush()
    time.sleep(5)

file.close()
