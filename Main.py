############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Main.py
#
############################################################

#import head
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches
from scipy import misc
from collections import deque
from PIL import ImageFilter
import cv2
from copy import deepcopy


#import files
import Init
import CARLA
import Pretreatment
import Constant

def MainFunction():
	#Image input 
	img = np.array(Image.open("Figure/01.png").convert("L"))

	#Get histogram and Zero crossing total
	Histogram = Pretreatment.Histogram(img)
	Differential = Pretreatment.DerHis(Histogram)
	ZCNumber = Pretreatment.Sta2Der(Differential)



	if Init.SystemJudge() == 0:
		if not os.path.exists("CARLA"):
			os.system("gcc CARLA.c -o CARLA")
	else:
		if not os.path.exists("CARLA.exe"):
			os.system("gcc CARLA.c")

	Str = "Reading data"
	FileName = "Input.out"
	os.system("rm " + FileName)
	Init.BuildFile(FileName)
	File = open(FileName, "a")
	File.write(Str)
	File.close()

	if Init.SystemJudge() == 0:
		os.system("./CARLA")
	else:
		os.system(".\CARLA.exe")
	

	FileName = "Output"
	File = open(FileName, "r")
	DataOutput = []
	while 1:
		FileLine = File.readline()
		if not FileLine:
			break
		
		if FileLine[0] == "o":
			TemStr = ""
			for i in range(1, len(FileLine)):
				TemStr += FileLine[i]
			DataOutput.append(float(FileLine))
		
	return

















MainFunction()


