################################################ New Born Baby to Six Months ##################################################################################################################
# 0 = Normal
# 1 = Short (Fast) Breathing
# 2 = Hyperventilating
# 3 = Long Breathing
# 4 = Very Long Breathing



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
