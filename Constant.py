############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Constant.py
#
############################################################

#==============================================================================
#Parameter of CARLA
gw = 0.02
gh = 0.3
Loop = 2000


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
#Problem method
Tsukaikata = "F"
#F = factory image processing(don't need pixel choose)
#M = medicine image processing(need pixel choose and just get boundary of that block)


#==============================================================================
#Histogram smoothing kernel
GauKernel = [0.06136, 0.24477, 0.38774, 0.24477, 0.06136]
#This is a group sample Gaussian kernel with sigma = 1.00


#==============================================================================
#File choosing
ImageName = "Figure/18.png"
#This is the file you want the algorithm working on it.


#==============================================================================
#The number of clusters
SegVar = 2
#1 means auto(With Gap Statistic)
#0 means auto(With Zero crossing)
#in N*


#==============================================================================
#Learning model
LearnModel = "all"
#"all" means learning all 3K parameter
#"part" means learning only 2K parameter




#==============================================================================
#Parameter check, DO NOT CHANGE THIS FUCNTION
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

	if Tsukaikata != "F" and Tsukaikata != "M":
		print("Problem method error")
		NoError = False

	if not os.path.exists(ImageName):
		print("File not exist")
		NoError = False

	try:
		tem = str(SegVar)
		int(tem)
	except:
		print("Cluster value error")
		NoError = False

	if SegVar < 0:
		print("Cluster value error")
		NoError = False

	if LearnModel == "all" and SegVar == 0:
		print("Cluster value error, Learning all parameter cannot have 0 cluster")
		NoError = False
	
	if LearnModel != "all" and LearnModel != "part":
		print("CARLA learning error")
		NoError = False

	return NoError