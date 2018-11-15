# Mobin Anandwala
# 05/09/2016
# Breathing functions
# This package will include all the breathing functions in a single package
# The desired age range can be imported using python's import commoand for testing

NBLowerBound = 25
NBUpperBound = 40
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

SMLowerBound = 20
SMUpperBound = 30

def SixMonths(BreathingRate):
	global SMLowerBound
	global SMUpperBound
	global delta
	if int(BreathingRate)  >= SMLowerBound and int(BreathingRate) <= SMUpperBound:
		outstring =  "Normal Breathing Rate"
	elif int (BreathingRate) > SMUpperBound and int(BreathingRate) <= (SMUpperBound + delta):
		outstring =  "Short (Fast) Breathing Rate"
	elif (BreathingRate) > (SMUpperBound + delta):
		outstring =  "Hyperventilating"
	elif int(BreathingRate) < SMLowerBound and int(BreathingRate) >= (SMLowerBound - delta):
		outstring =  "Long (slow) Breathing Rate"
	elif int(BreathingRate) < (SMLowerBound - delta):
		print "Very Long (very slow) Breathing Rate"

	return outstring
