############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Pretreatment.py
#
############################################################
"""
		FUNCTION INSTRUCTION
		
This is the main function of all the program.

Histogram(img)
	This function will statistic the probability of all grey level
	
	img = Array of the figure 
	
	return Histogram array based on probability 

DerHis(HisArr)
	This function will get the second order derivative of the 
	histogram array

	HisArr = The histogram array of the image

	return 2nd order derivative array

Sta2Der(DerArr)
	This function will find the zero crossing of the histogram array

	DerArr = The second derivative array
	
	return Array of Pair of zero crossing as [[minvalue, maxvalur]...]

"""

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
import random


#import Files
import Init

def Histogram(img):
	Statistic = [0 for n in range(260)]
	Probability = [0.00 for n in range(260)]
	TTL = 0

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			Statistic[img[i][j]] += 1
			TTL += 1

	for i in range(0, len(Statistic)):
		Probability[i] = Statistic[i] / TTL

	return Probability


def DerHis(HisArr):
	Der1 = [0.00 for n in range(259)]
	for i in range(0, len(Der1)):
		Der1[i] = HisArr[i+1] - HisArr[i]

	Der2 = [0.00 for n in range(258)]
	for i in range(0, len(Der2)):
		Der2[i] = Der1[i+1] - Der1[i]

	return Der2


def Sta2Der(DerArr):
	ZeroCross = []
	ZeroSwich = False
	HaveSign = False
	Sign = False
	#False = Negative
	#True = Positive
	Tem = 0

	for i in range(0, len(DerArr)):
		if i < (len(DerArr)-1) and DerArr[i] * DerArr[i+1] < 0:
				if DerArr[i] > DerArr[i+1]:
					ZeroCross.append(i)
				else:
					ZeroCross.append(i + 1)
		else:
			if DerArr[i] == 0:
				if i != 0 and HaveSign == False:
					if DerArr[i - 1] > 0:
						Sign = True
						Tem = i
					else:
						Sign = False
						Tem = i
					HaveSign = True

			else:
				if HaveSign == True:
					if DerArr[i] > 0 and Sign == False:
						ZeroCross.append(int((i + Tem) / 2))
					if DerArr[i] < 0 and Sign == True:
						ZeroCross.append(int((i + Tem) / 2))

					HaveSign = False

	PairZero = []
	for i in range(0, len(ZeroCross) // 2):
		if ZeroCross[2 * i] != ZeroCross[2 * i + 1]:
			PairZero.append([ZeroCross[2 * i], ZeroCross[2 * i + 1]])

	return len(PairZero)


def ZCAnalysis(img, GausData):
	img1 = [[0.00 for n in range(len(img[0]))] for n in range(len(img))]
	for kase in range(0, len(GausData) - 1):
		if GausData[kase][2] < (1/(kase+1)):
			continue

		print([kase, len(GausData)], end = "\r")
		img2 = deepcopy(img)
		for i in range(0, len(img2)):
			for j in range(0, len(img2[i])):
				if img2[i][j] <= GausData[kase][0]:
					img2[i][j] = 0
				else:
					img2[i][j] = 255

		img2 = cv2.Canny(img2, 100, 200)

		for i in range(0, len(img2)):
			for j in range(0, len(img2[i])):
				img1[i][j] = max(img1[i][j], img2[i][j])
		Pretreatment.FigurePrint(img1, 2)
	print([len(GausData), len(GausData)], end = "\n")
	#img1 = cv2.Canny(img1, 100, 200)
	return img1



