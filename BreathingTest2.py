# Mobin Anandwala
# 05/05/2016
# Breathing Test
# This script will create indicators based on different breathing rates of a newborn up to 1 year

################################################ New Born Baby to Six Months ##################################################################################################################
NBLowerBound = 30
NBUpperBound = 60
delta = 10


def NewBorn(BreathingRate):
	global NBLowerBound
	global NBUpperBound
	global delta
	if int(BreathingRate)  >= NBLowerBound and int(BreathingRate) <= NBUpperBound:
		print "Normal Breathing Rate"
	elif int (BreathingRate) > NBUpperBound and int(BreathingRate) <= (NBUpperBound + delta):
		print "Short (Fast) Breathing Rate"
	elif (BreathingRate) > (NBUpperBound + delta):
		print "Hyperventilating"
	elif int(BreathingRate) < NBLowerBound and int(BreathingRate) >= (NBLowerBound - delta):
		print "Long (slow) Breathing Rate"
	elif int(BreathingRate) < (NBLowerBound - delta):
		print "Very Long (very slow) Breathing Rate"
			
	
	
############################################## Six Months to One Year #########################################################################################################################
SMLowerBound = 24
SMUpperBound = 30

def SixMonth(BreathingRate):
	global SMLowerBound
	global SMUpperBound
	if int(BreathingRate)  >= SMLowerBound and int(BreathingRate) <= SMUpperBound:
		print "Normal Breathing Rate"
	elif int (BreathingRate) > SMUpperBound and int(BreathingRate) <= (SMUpperBound + delta):
		print "Short (Fast) Breathing Rate"
	elif (BreathingRate) > (SMUpperBound + delta):
		print "Hyperventilating"
	elif int(BreathingRate) < SMLowerBound and int(BreathingRate) >= (SMLowerBound - delta):
		print "Long (slow) Breathing Rate"
	elif int(BreathingRate) < (SMLowerBound - delta):
		print "Very Long (very slow) Breathing Rate"

# while True:
	# BreathTest = raw_input("Enter breaths per minute: ")
	# if int(BreathTest) >= SMLowerBound and int(BreathTest) <= SMUpperBound:
		# print "Normal Breathing Rate"
	# elif int(BreathTest) > SMUpperBound and int(BreathTest) <= (SMUpperBound + delta):
			# print "Short (Fast) Breathing Rate"
	# elif int(BreathTest) > (SMUpperBound + delta):
		# print "Hyperventilating"
	# elif int(BreathTest) < SMLowerBound and int(BreathTest) >= (SMLowerBound - delta):
		# print "Long (slow) Breathing Rate"
	# elif int(BreathTest) < (SMLowerBound - delta):
		# print "Very Long (very slow) Breathing Rate"	


