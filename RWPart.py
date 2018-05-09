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
import Pretreatment
DEBUG = Constant.DEBUG



def Toboggan(img):
	SavArr = [[-1 for n in range(len(img[0]))] for n in range(len(img))]
	Gradient = [[0 for n in range(len(img[0]))] for n in range(len(img))]

	#Get Gradient
	img1 = cv2.Sobel(img, cv2.CV_16S, 1, 0)
	img2 = cv2.Sobel(img, cv2.CV_16S, 0, 1)

	for i in range(0, len(img1)):
		for j in range(0, len(img1[i])):
			Gradient[i][j] = int(math.sqrt(pow(img1[i][j], 2)+pow(img2[i][j], 2)))

	Tem = 0
	Tem1 = -1
	Color = [[0, 0]]
	Loc = [[0, 0]]
	#MainLoop
	for i in range(1, len(SavArr)-1):
		for j in range(1, len(SavArr[i])-1):
			if SavArr[i][j] != -1:
				continue

			Stack = [[i, j]]
			Tem += 1
			Color.append([0, 0])
			Loc.append([0, 0])
			while 1:
				if len(Stack) == 0:
					break

				Block = []
				Vari = Stack[len(Stack)-1][0]
				Varj = Stack[len(Stack)-1][1]
				Stack.pop()
				if SavArr[Vari][Varj] == -1:
					SavArr[Vari][Varj] = Tem
					Color[len(Color)-1][0] += 1
					Color[len(Color)-1][1] += img[Vari][Varj]
					Loc[len(Color)-1][0] += Vari
					Loc[len(Color)-1][1] += Varj
				else:
					continue
			
				if Tem != Tem1:
					print("Block:\t" + str(Tem), end = "\r")
					Tem1 = Tem

				for p in range(-1, 2):
					for q in range(-1, 2):
						Poi = 0
						try:
							Poi = Gradient[Vari+p][Varj+q]
						except:
							continue
						Block.append([Gradient[Vari+p][Varj+q], Vari+p, Varj+q])

				Block.sort()
				for k in range(0, len(Block)):
					if SavArr[Block[k][1]][Block[k][2]] == -1 and Block[k][1] > 0 and Block[k][2] > 0:
						#This judgement may have some bug
						Stack.append([Block[k][1], Block[k][2]])
						break
					
	print("Block:\t" + str(Tem), end = "\n")
	BlockInfo = [[0, 0, 0, 0, 0]]

	for i in range(1, len(Color)):
		Tem = [-1]
		Tem.append(abs(int(Color[i][1]/Color[i][0])))
		Tem.append(abs(int(Loc[i][0]/Color[i][0])))
		Tem.append(abs(int(Loc[i][1]/Color[i][0])))
		Tem.append(0)
		BlockInfo.append(Tem)

	for i in range(0, len(SavArr)):
		for j in range(0, len(SavArr[i])):
			if SavArr[i][j] == -1:
				continue
			BlockInfo[SavArr[i][j]][4] += 1

	return [SavArr, BlockInfo]



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
















