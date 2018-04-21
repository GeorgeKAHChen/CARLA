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
#The number of segmentation
SegVar = 3
#1 means auto(With Gap Statistic)
#in N*