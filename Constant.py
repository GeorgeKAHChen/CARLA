############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Constant.py
#
############################################################
#Here are all parameter you can change during all the CARLA processing
#CAUTION: DO NOT CHANGE THE PARAMETER CHECK FUNCTION


#==============================================================================
#Parameter of main CARLA processing
#Usually let gw = 0.02, gh = 0.3 and Loop = 2000 in paper
gw = 0.02
gh = 0.3
Loop = 1000


#==============================================================================
#Working method
mode = "w"
#w = work
#p = presentation, will output all data
#t = test, will output key data


#==============================================================================
#Block figure size
FigSize = 256


#==============================================================================
#Debug model, True means open, False means close
DEBUG = True


#==============================================================================
#File choosing
ImageName = "Figure/aznyan.jpg"
#This is the file you want the algorithm working on it.


#==============================================================================
#System parameter
System = "M"


#==============================================================================
#Distance between two thresholding
ThsDis = 5



#==============================================================================
#Distant parameter for toboggan block number
DisPar = 0.01



#==============================================================================
#Cost function, using in CARLA learning main algorithm
#C code will find this function automaton, so donot change the name of this fucntion
def Cost(Parameter):
	import math
	import tem
	Output = [0.00 for n in range(256)]
	for i in range(0, int(len(Parameter) / 3 + 0.1)):
		Pr = Parameter[3 * i]
		Sigma = Parameter[3 * i + 1]
		Mu = Parameter[3 * i + 2]
		for j in range(0, len(Output)):
			Output[j] += Pr * math.exp(- (pow(j - Mu, 2) / (2 * Sigma * Sigma))) / (math.sqrt(2 * math.pi) * Sigma)
	TTL = 0
	for i in range(0, len(Output)):
		TTL += pow(Output[i] - tem.Histogram[i], 2)

	return TTL / 256





#==============================================================================
#Parameter check function, DO NOT CHANGE THIS FUCNTION
#==============================================================================
def ParameterDetermine():
	#This function will determine all parameter is legal or not
	#Parameter of CARLA
	import os
	NoError = True
	if mode != "w" and mode and "p" and mode != "t":
		print("Working method error")
		NoError = False

	if DEBUG == True:
		print("CAUTION: DEBUG MODEL")

	if not os.path.exists(ImageName):
		print("File not exist")
		NoError = False

	return NoError
