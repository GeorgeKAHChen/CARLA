############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Constant.py
#
############################################################

gw = 0.02
gh = 0.3
Loop = 2000


mode = "w"
#w = work
#p = presentation, will output all data
#t = test, will output key data


FigSize = 256


DEBUG = True


Tsukaikata = "F"
#F = factory image processing(don't need pixel choose)
#M = medicine image processing(need pixel choose and just get boundary of that block)


GauKernel = [0.06136, 0.24477, 0.38774, 0.24477, 0.06136]
#This is a group sample Gaussian kernel with sigma = 1.00