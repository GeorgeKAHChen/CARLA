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
import Constant




def Histogram(img):
	Statistic = [0 for n in range(258)]
	Probability = [0.00 for n in range(258)]
	TTL = 0

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			Statistic[img[i][j]] += 1
			TTL += 1

	for i in range(0, len(Statistic)):
		Probability[i] = Statistic[i] / TTL

	return Probability


def DerHis(HisArr):
	Der1 = [0.00 for n in range(257)]
	for i in range(0, len(Der1)):
		Der1[i] = HisArr[i+1] - HisArr[i]

	Der2 = [0.00 for n in range(256)]
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

	return PairZero


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



def FigurePrint(img, kind):
	plt.imshow(img, cmap="gray")
	plt.axis("off")
	plt.show()
	Init.LogWrite("Figure output succeed", "0")
	if kind == 1:
		InpStr = input("Save the figure?[Y/ n]")
		if InpStr == "Y" or InpStr == "y":
			Name = "Figure_"
			Name += str(Init.GetTime())
			Name += ".png"
			Output(img, Name, 2)
	elif kind == 1:
		pass
	elif kind == 3:
		Name = "Figure_"
		Name += str(Init.GetTime())
		Name += ".png"
		Output(img, Name, 2)
	return


def ProbLearn(HisArr, ZeroC):
	mu = []
	sigma = []
	for i in range(0, len(ZeroC)):
		mu.append(((ZeroC[i][1] - ZeroC[i][0]) / 2) + ZeroC[i][0])
		sigma.append((ZeroC[i][1] - ZeroC[i][0]) / 2)


	def SumProb():
		#This function can confident if the loop finish condition is establish
		Prob = 0.00
		for i in range(0, len(ZeroC)):
			for p in range(ZeroC[i][0], ZeroC[i][1]):
				Prob += HisArr[p]
		if Prob > 0.97:
			return True
		else:
			return False
	
	ZeroC[0][0] = 0
	ZeroC[len(ZeroC) - 1][1] = 255
	Loop = 0
	while 1:
		Loop += 1
		for i in range(0, len(ZeroC)):
			Interval = ZeroC[i][1] - ZeroC[i][0]
			if i != 0:
				ZeroC[i][0] = max(ZeroC[i - 1][1], ZeroC[i][0] - Interval)

			if i != len(ZeroC)-1:
				ZeroC[i][1] = min(ZeroC[i + 1][0], ZeroC[i][1] + Interval)
		
		if SumProb() == True:
			break
		else:
			continue

	return ZeroC


def Treasholding(img, TSH, TSH2):
	TemImg = [[0.00 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			if img[i][j] < TSH or img[i][j] > TSH2:
				TemImg[i][j] = 0
			else:
				TemImg[i][j] = 255

	return cv2.Canny(np.uint8(TemImg), 85, 170)


def Output(img, Name, kind):
	if Init.SystemJudge() == 0:
		os.system("cp null " + Name)
		misc.imsave(Name, img)
		if kind == 1:
			if not os.path.exists("Output"):
				os.system("mkdir Output")
			os.system("mv " + Name + " Output/" + Name)
		if kind == 2:
			if not os.path.exists("Saving"):
				os.system("mkdir Saving")
			os.system("mv " + Name + " Saving/" + Name)
	else:
		os.system("copy null " + Name)
		misc.imsave(Name, img)
		if kind == 1:
			if not os.path.exists("Output"):
				os.system("mkdir Output")
			os.system("move " + Name + " Output/" + Name)
		if kind == 2:
			if not os.path.exists("Saving"):
				os.system("mkdir Saving")
			os.system("move " + Name + " Saving/" + Name)		
	return


def AutoTH(Histogram, varTH):
	Prob = 1 / varTH
	Sum = 0
	Loc = []
	for i in range(0, len(Histogram)):
		Sum += Histogram[i]
		Tem = False
		while 1:
			if Sum >= Prob:
				Sum -= Prob
				if Tem == False:
					Loc.append(i)
					Tem = True
					continue
			else:
				break
	return Loc



def Partial(img):
	FigSize = Constant.FigSize
	
	BlockX = (len(img[0]) - 1) // FigSize
	BlockY = (len(img) - 1) // FigSize
	
	Tem = 0
	BlockInfo = [[0, 0, 0, 0]]
	for i in range(0, BlockY + 1):
		for j in range(0, BlockX + 1):
			Tem += 1
			SaveImg = []
			p = 0
			q = 0
			for p in range(0, FigSize):
				Line = []
				for q in range(0, FigSize):	
					try:
						Line.append(img[i * FigSize + p][j * FigSize + q])
					except:
						break
				if len(Line) != 0:
					SaveImg.append(Line)
				else:
					break
			#print([i, j, p, q])
			#print(img)
			BlockInfo.append([i, j, len(SaveImg), len(SaveImg[0])])
			Output(SaveImg, "Block_" + str(Tem) + ".png", 1)

	BlockInfo[0][2] = FigSize * BlockX  + BlockInfo[len(BlockInfo)-1][3]
	BlockInfo[0][3] = FigSize * BlockY  + BlockInfo[len(BlockInfo)-1][2]
	#print(BlockInfo[len(BlockInfo)-1][2], BlockInfo[len(BlockInfo)-1][3])
	return BlockInfo



def Recovery(BlockSize, BlockInfo, ImageName):
	FigSize = Constant.FigSize
	img = [[0 for n in range(BlockInfo[0][2] + 1)] for n in range(BlockInfo[0][3] + 1)]
	for kase in range(1, len(BlockInfo)):
		img1 = np.array(Image.open("Output/Block_" + str(kase) + ".png").convert("L"))
		for i in range(0, len(img1)):
			for j in range(0, len(img1[i])): 
				img[FigSize * BlockInfo[kase][0] + i][FigSize * BlockInfo[kase][1] + j] = img1[i][j]
	Output(img, ImageName, 2)

