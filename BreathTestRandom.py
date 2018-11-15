# Mobin Anandawala
# 06/14/2016
# This function will randomly generate a set of breathing rates to test against
# the breathing rate functions

import os
import time
from time import sleep
import random
import datetime

name = "Randomly Generated Breathing Rates"
today = datetime.date.today()
log_file = name + "-" + str(today)  + ".csv"
file = open(log_file,"wb")

if os.stat(log_file).st_size == 0:
    file.write("Breathing Rate\n")

data = []
n = 10000
for i in range((n+1)):
    r = random.randrange(20,41)
    data.append(r)
    file.write(str(data[i]) + "," +  "\n")
file.flush()
file.close()
