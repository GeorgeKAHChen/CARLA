############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		RWPart.py
#
############################################################
"""
		FUNCTION INSTRUCTION
		
This is the file with the function from CRIEA program.
The main goal of these functions is adding the space infomation to the segmentation algorithm


Toboggan(img)
	Toboggan algorithm function, a image differential function.

	img = [input image array]

	return [the image array coding with Toboggan], [The infomation of all block, include[Code, Grey, LocX, LocY, Size]]


WeightFunc(Point1, Point2)
	This function will calculate the weight between two node

	Point1 = [BlockCode1, Grey1, LocX1, LocY1]
	Point2 = [BlockCode2, Grey2, LocX2, LocY2]

	return The probability between two node

Laplacian(NodeInfo, VarL)
	This function will return normalization laplacian matrix 

	NodeInfo = [array of all node after Toboggan]
	VarL = 

"""




#import head
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import math
from scipy import misc
import cv2
from copy import deepcopy
import random


#import files
import Init
import Constant
DEBUG = Constant.DEBUG




def Toboggan(img):
	SavArr = [[-1 for n in range(len(img[0]))] for n in range(len(img))]
	Gradient = [[0 for n in range(len(img[0]))] for n in range(len(img))]

	#Get Gradient
	img1 = cv2.Sobel(img, cv2.CV_16S, 1, 0)
	img2 = cv2.Sobel(img, cv2.CV_16S, 0, 1)

	for i in range(0, len(img1)):
		for j in range(0, len(img1[i])):
			Gradient[i][j] = math.sqrt(pow(img1[i][j], 2)+pow(img2[i][j], 2))

	Label = 0
	TobBlock = [[-1, 0, 0, 0, 0]]
	#MainLoop
	for i in range(0, len(SavArr)):
		for j in range(0, len(SavArr[i])):
			print("TobBlock = " + str(Label), end = "\r")
			
			if SavArr[i][j] != -1:
				continue

			Stack = [[i, j]]
			s = i
			t = j
			ImaLabel = 0
			#print(Stack)
			while 1:
				s = Stack[len(Stack) - 1][0]
				t = Stack[len(Stack) - 1][1]

				Neigh = []
				
				for p in range(-1, 2):
					for q in range(-1, 2):
						if p == 0 and q == 0:
							continue
						LocX = s + p
						LocY = t + q
						if LocX < 0 or LocY < 0 or LocX > len(SavArr) - 1 or LocY > len(SavArr[0]) - 1:
							continue
						else:
							Neigh.append([Gradient[LocX][LocY], LocX, LocY])
							

				#print(Stack)
				#input()
				Neigh.sort()
				
				if Gradient[Neigh[0][1]][Neigh[0][2]] > Gradient[s][t]:
					if SavArr[s][t] == -1 or SavArr[s][t] == -2:
						TobBlock.append([-1, 0, 0, 0, 0])
						Label += 1
						ImaLabel = Label
						break
					else:
						ImaLabel = SavArr[s][t]
						break
				else:
					if SavArr[Neigh[0][1]][Neigh[0][2]] == -1:
						Stack.append([Neigh[0][1], Neigh[0][2]])
						SavArr[Neigh[0][1]][Neigh[0][2]] = -2
						continue
					elif SavArr[Neigh[0][1]][Neigh[0][2]] == -2:
						TobBlock.append([-1, 0, 0, 0, 0])
						Label += 1
						ImaLabel = Label
						break
					else:
						ImaLabel = SavArr[Neigh[0][1]][Neigh[0][2]]
						break

			while len(Stack) != 0:
				LocX = Stack[len(Stack) - 1][0]
				LocY = Stack[len(Stack) - 1][1]
				Grey = img[LocX][LocY]
				Stack.pop()
				if SavArr[LocX][LocY] != -2 and SavArr[LocX][LocY] != -1:
					continue
				SavArr[LocX][LocY] = ImaLabel
				TobBlock[ImaLabel][1] += Grey
				TobBlock[ImaLabel][2] += LocX
				TobBlock[ImaLabel][3] += LocY
				TobBlock[ImaLabel][4] += 1
	
	#Init.ArrOutput(SavArr)
	print("TobBlock = " + str(Label), end = "\n")
	#print(str([len(img) - 1, len(img[0]) - 1]))
	for i in range(1, len(TobBlock)):
		TobBlock[i][1] /= TobBlock[i][4]
		TobBlock[i][2] /= TobBlock[i][4]
		TobBlock[i][3] /= TobBlock[i][4]


	return [SavArr, TobBlock]




def TobBoundary(TobImage, TobBlock, BlockArea):
	for i in range(0, len(TobImage)):
		for j in range(0, len(TobImage[i])):
			if TobImage[i][j] == -1:
				continue

			TobImage[i][j] = TobBlock[TobImage[i][j]][0]
	
	OutImg = [[255 for n in range(len(TobImage[1]))] for i in range(len(TobImage))]
	
	for i in range(0, BlockArea):
		BlankImg = [[0 for n in range(len(TobImage[1]))] for i in range(len(TobImage))]
		for p in range(0, len(TobImage)):
			for q in range(0, len(TobImage[p])):
				if TobImage[p][q] == i:
					BlankImg[p][q] = 255

		BlankImg = cv2.Canny(np.uint8(BlankImg), 85, 170)
		for p in range(0, len(BlankImg)):
			for q in range(0, len(BlankImg[p])):
				if BlankImg[p][q] > 200:
					OutImg[p][q] = 0

	return OutImg



















