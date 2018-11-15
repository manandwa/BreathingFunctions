from math import *


outfile = open('sinebreathwave.csv','w')

Fs = 8000
f = 500
sample = 200
Amp = 20
a = [0]*sample

for n in range(sample):
    a[n] = Amp*sin(2*pi*f*n/Fs)
    outfile.write(str(a[n]) + "," + "\n")
outfile.close()
