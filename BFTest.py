# Mobin Anandwala
# 05/12/2016
# Testing breathing functions to determine at what point they activate

import BreathFunctions
from BreathFunctions import NewBorn, SixMonths
import csv

with open("Generated Breathing Rates-2016-05-12.csv") as datalog:
    reader = csv.reader(datalog)
    for row in reader:
        print(row)
