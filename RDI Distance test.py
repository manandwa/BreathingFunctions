# Mobin Anandawala
# 06/17/2016
# This code will use a desired deflection rate and try to calculate maximum distance
# Maximum resolution is 640 by 480
# Use lens equation as given in cnet forum answer as basis for starting

from math import *

## Convert mm into inches
def mmtoinch(mm):
    inch = mm/(25.4)
    return inch

def fttoin(ft):
    inch2 = ft*12.0
    return inch2


flogitech = mmtoinch(3.67) # focal length in mm (converted to inches)
min_focus = 10.0 # in cm
min_focus_mm = min_focus/10.0

d_o = fttoin(20.0) # object distance in ft (converted to inches)

finv = 1/(flogitech)
d_image = 1/(finv*(1 - (flogitech/d_o)))
