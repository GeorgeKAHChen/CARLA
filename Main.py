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


def MainFunction():
	#Image input 
	img = np.array(Image.open("Figure/01.png").convert("L"))

	#Get histogram and Zero crossing total
	Histogram = Pretreatment.Histogram(img)
	Differential = Pretreatment.DerHis(Histogram)
	ZCNumber = Pretreatment.Sta2Der(Differential)

	#print(ZCNumber)
	class CARLA_Image(CARLA.CARLA):
		def Consume(self, ImaGroup):
			import math
			Omega = 1

			Array = [0.00 for n in range(256)]
			Prob = 0
			for i in range(0, len(ImaGroup) // 3):
				for j in range(0, len(Array)):
					Array[j] += ImaGroup[3 * i] / (math.sqrt(2 * math.pi) * ImaGroup[3 * i + 1]) * math.exp( - pow(j - ImaGroup[3 * i + 2], 2) / (2 * ImaGroup[3 * i + 1]* ImaGroup[3 * i + 1]) )
					Prob += ImaGroup[3 * i]
			TTL = 0
			for i in range(0, len(Array)):
				TTL += pow(Array[i] - self.Other[i], 2)
			TTL /= 256
			TTL += Omega * pow((1 - Prob), 2)
			return TTL
			

	Interval = []
	for i in range(0, ZCNumber):
		Interval.append([1/ZCNumber, 0])
		Interval.append([128, 0]) 
		Interval.append([255, 0])
	print(Interval)

	CARLA_Image_Learning = CARLA_Image(Interval, "-p", 200, 0.2, 0.03, Histogram)

	Solution = CARLA_Image_Learning.Algorithm()

	print(Solution)
	return

















MainFunction()


