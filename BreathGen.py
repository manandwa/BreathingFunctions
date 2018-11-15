# Mobin Anandwala
# Created on  05/11/2016
# Updated on 5/12/2016
# This code will generate a csv file to use for Breathing Tests
# New Born is 25 to 40 and 6-12 months is 20 to 30 so this will generate a range of breathing rates from new born to one year old

import os
import datetime

name = "Generated Breathing Rates"
today = datetime.date.today()
log_file = name + "-" + str(today)  + ".csv"
breathrange = range(20,41)
file = open(log_file,"wb")

if os.stat(log_file).st_size == 0:
    file.write("Breathing Rate\n")

for i in range(len(breathrange)):
    file.write(str(breathrange[i]) + "\n")
    if i > len(breathrange):
        break

file.flush()
file.close()

#
# while i in breathrange <= len(breathrange):
#     file.write(str(breathrange[i]))
# if i > len(breathrange):
#     file.flush()
