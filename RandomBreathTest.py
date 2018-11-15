# Mobin Anandawala
# 06/14/2016
# This function will randomly generate a set of breathing rates to test against
# the breathing rate functions

import os
import time
from time import sleep
import random
import datetime

NBLowerBound = 30
NBUpperBound = 60
delta = 10

def NewBorn(BreathingRate):
	global NBLowerBound
	global NBUpperBound
	global delta
	if int(BreathingRate)  >= NBLowerBound and int(BreathingRate) <= NBUpperBound:
		outstring =  "Normal Breathing Rate"
	elif int (BreathingRate) > NBUpperBound and int(BreathingRate) <= (NBUpperBound + delta):
		outstring =  "Short (Fast) Breathing Rate"
	elif (BreathingRate) > (NBUpperBound + delta):
		outstring =  "Hyperventilating"
	elif int(BreathingRate) < NBLowerBound and int(BreathingRate) >= (NBLowerBound - delta):
		outstring =  "Long (slow) Breathing Rate"
	elif int(BreathingRate) < (NBLowerBound - delta):
		print "Very Long (very slow) Breathing Rate"

	return outstring


name = "Randomly Generated Breathing Rates Results"
today = datetime.date.today()
log_file = name + "-" + str(today)  + ".csv"
file = open(log_file,"wb")

if os.stat(log_file).st_size == 0:
    file.write("Breathing Rate,Result\n")

data = []
n = 10000
for i in range((n+1)):
    r = random.randrange(20,41)
    data.append(r)
    reading = NewBorn(data[i])
    file.write(str(data[i]) + "," +  reading + "," + "\n")
file.flush()
file.close()
