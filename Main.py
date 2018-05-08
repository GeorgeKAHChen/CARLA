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
from scipy import signal
from collections import deque
from PIL import ImageFilter
import cv2
from copy import deepcopy
import random
import pandas as pd
from gap_statistic import OptimalK
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans


#import files
import Init
import Pretreatment
import Constant
import RWPart
DEBUG = Constant.DEBUG



def Main2(ImageName):
	"""
	#==============================================================================
	#Pretreatments
	#==============================================================================
	"""
	#==============================================================================	
	#Parameter check and import package
	if Constant.ParameterDetermine() == False:
		return


	#==============================================================================
	#For output to matlab image statistic
	AnaLine = ""
	

	#==============================================================================
	#Image input
	img = np.array(Image.open(ImageName).convert("L"))


	#==============================================================================
	#Smoothing(with FFT based convolution)
	InpK = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])/25
	img1 = signal.fftconvolve(img, InpK[::-1], mode='full')
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = int(img1[i][j])


	#==============================================================================
	#Toboggan Algorithm
	TobImage, TobBlock = RWPart.Toboggan(img)
	#CAUTION: The block code of Toboggan is begin from 1 rather than 0!!
	

	#==============================================================================
	#Get the histogram
	Histogram = [0 for n in range(256)]
	TTL = 0
	for i in range(0, len(TobBlock)):
		Histogram[TobBlock[i][1]] += TobBlock[i][4]
		TTL += TobBlock[i][4]
	
	for i in range(0, len(Histogram)):
		Histogram[i] /= TTL



	#==============================================================================
	#Histogram Saving and output
	String = "Histogram = "
	String += str(Histogram)
	FileName = "tem.py"
	File = open(FileName, "w")
	File.write(String)
	File.close()


	#==============================================================================
	#Compile C files
	if Init.SystemJudge() == 0:		
		os.system("rm CARLA")
		if Constant.System == "L":
			os.system("gcc -Wall -lm -I/usr/include/python3.6m CARLA.c -o CARLA -L/usr/lib -lpython3.6m")
		if Constant.System == "M":
			os.system("gcc -Wall -lm -I/usr/include/python2.7 CARLA.c -o CARLA -L/usr/lib -lpython2.7")
	else:
		os.system("rm CARLA.exe")
		os.system("gcc CARLA.c")

	if DEBUG:
		AnaLine += "His = "
		AnaLine += str(Histogram)
		AnaLine += ";\n"
		print("Cluster Begin")


	"""
	#==============================================================================
	#Gap Statistic
	#==============================================================================
	"""
	N_Cluster = 0

	#==============================================================================
	#Gap statistic and judgement
	"""
	optimalK = OptimalK(parallel_backend = 'joblib')
	ClusterSet = []
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			ClusterSet.append([float(img[i][j])])
	ClusterSet = np.array(ClusterSet)
	N_Cluster = optimalK(ClusterSet, cluster_array = np.arange(1, 20))
	if N_Cluster < 3:
		N_Cluster = 3
	"""
	N_Cluster = 20
	if DEBUG:
		print("Cluster = " + str(N_Cluster))

	
	#==============================================================================
	#Final cost 
	FinalCost = [0.00 for n in range(N_Cluster)]
	TrueGap = N_Cluster
	DataLast = []



	"""
	#==============================================================================
	#Main CARLA Algorithm Loop
	#==============================================================================
	"""

	for Gap in range(N_Cluster, 0, -1):
		#==============================================================================
		#Pretreatment of CARLA, get the initial data
		PairOfZC = Pretreatment.GetPeak(Histogram, Gap)
		if len(PairOfZC) == 0:
			break
		if DEBUG:
			print(len(PairOfZC), Gap)
		PairOfZC = Pretreatment.ProbLearn(Histogram, PairOfZC)
		

		#==============================================================================
		#Data Saving
		String = ""
		String += str(len(PairOfZC) * 3) + " " + str(Constant.Loop) + " " + str(Constant.gw) + " " + str(Constant.gh) + " " + Constant.mode + "\n"
		for i in range(0, len(PairOfZC)):
			String += str(0.0) + " " + str(1.0) + "\n"
			String += str(0) + " " + str(255) + "\n"
			String += str(PairOfZC[i][0]) + " " + str(PairOfZC[i][1]) + "\n"
		FileName = "Input.out"
		os.system("rm " + FileName)
		Init.BuildFile(FileName)
		File = open(FileName, "a")
		File.write(String)
		File.close()

		

		"""		
		#==============================================================================
		#CARLA MAIN ALGORIHTM
		#==============================================================================
		#Learning Automaton : Continuous Action Reinforcement Learning Automaton 
		"""
		#==============================================================================
		#Main Algorithm in C
		if Init.SystemJudge() == 0:
			os.system("./CARLA")
		else:
			os.system("CARLA.exe")
		

		#==============================================================================
		#Read the output file
		FileName = "Output.out"
		File = open(FileName, "r")
		Data = []
		while 1:
			FileLine = File.readline()
			if not FileLine:
				break
			
			if FileLine[0] == "o":
				TemStr = ""
				for i in range(1, len(FileLine)):
					TemStr += FileLine[i]
				Data.append(float(TemStr))
		
		FinalCost[Gap - 1] = Constant.Cost(Data)
		if Gap != N_Cluster:
			if FinalCost[Gap - 1] > FinalCost[Gap]:
				break
		TrueGap = Gap
		DataLast = Data



	if DEBUG:
		AnaLine += "tem = "
		AnaLine += str(Data)
		AnaLine += ";\n"



	"""
	#==============================================================================
	#Thresholding solution with distance matirx
	#==============================================================================
	"""
	if DEBUG:
		print(TrueGap)

	Thresholding = [0]
	if TrueGap == 1:
		Sum = 0.00
		Tem = 0
		for i in range(0, len(Histogram)):
			Sum += Histogram[i]
			if Sum >= 0.5:
				Tem = i
				break
		if Tem != 0:
			Thresholding.append(Tem)
		else:
			Thresholding.append(1)

	else:
		Value = [[0.00 for n in range(256)] for n in range(TrueGap)]
		for p in range(0, TrueGap):
			Prob = DataLast[p * 3]
			Sigma = DataLast[p * 3 + 1]
			Mu = DataLast[p * 3 + 2]
			for q in range(0, 256):
				Value[p][q] = Prob * math.exp(- (pow(q - Mu, 2) / (2 * Sigma * Sigma))) / (math.sqrt(2 * math.pi) * Sigma)
		Init.ArrOutput(Value, 1)
		Group = 0
		for p in range(0, 256):
			if Value[Group + 1][p] > Value[Group][p]:
				Group += 1
				if Thresholding[len(Thresholding) - 1] - p >= 3:
					Thresholding.append(p)
				if Group == TrueGap - 1:
					break

	Thresholding.append(256)



	#==============================================================================
	#Segmentation with distance matrix
	OutImg = [[0.00 for n in range(len(img[0]))] for n in range(len(img))]

	for i in range(0, len(Thresholding) - 1):
		Interval = [Thresholding[i], Thresholding[i + 1]]
		BlockSet = []
		for j in range(1, len(TobBlock)):
			if TobBlock[j][1] < Interval[1] and TobBlock[j][1] >= Interval[0]:
				BlockSet.append(j)
		SubBlock = [[0.00 for n in range(len(BlockSet))] for n in range(len(BlockSet))]
		SizeSet = []
		for p in range(0, len(SubBlock)):
			for q in range(p + 1, len(SubBlock)):
				tem1 = BlockSet[p]
				tem2 = BlockSet[q]
				SubBlock[p][q] = math.sqrt( pow(TobBlock[tem1][2] - TobBlock[tem2][2], 2) + pow(TobBlock[tem1][3] - TobBlock[tem2][3], 2) )
				SubBlock[q][p] = SubBlock[p][q]
				SizeSet.append(SubBlock[p][q])
		AveDis = sum(SizeSet) / len(SizeSet)
		AnaLine += "sb" + str(i) + " = "
		AnaLine += str(SizeSet)
		AnaLine += ";\n"


	#NOT FINISHED
	if DEBUG:
		AnaLine += "ths = "
		AnaLine += str(Thresholding)
		AnaLine += ";\n"
		FileName = "SaveArrTem"
		File = open(FileName, "w")
		File.write(AnaLine)
		File.close()




	"""
	#==============================================================================
	#Output and Print
	#==============================================================================
	"""
	if Constant.mode == "p":
		plt.imshow(OutImg, cmap="gray")
		plt.axis("off")
		plt.show()
		input("Press Enter to continue")



	"""
	#==============================================================================
	#Factory output
	#==============================================================================
	"""
	if Constant.Tsukaikata == "F":
		OutImg = Pretreatment.CombineFigures(img, OutImg, 1)
		misc.imsave("Saving/result.png", OutImg)
		return OutImg
	#==============================================================================
	#==============================================================================




	"""
	#==============================================================================
	#Medicine output
	#==============================================================================
	"""
	#==============================================================================
	#Output and Print
	if Constant.Tsukaikata == "M":
		#==============================================================================
		#Location choose
		plt.imshow(img, cmap="gray")
		plt.axis("off")
		plt.show()

		PointY = Init.IntInput("Input location X = ", "0", "999999999", "int")
		PointX = Init.IntInput("Input location Y = ", "0", "999999999", "int")
		AnoImg = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	

		#==============================================================================
		#Get boundary (with BFS)
		Stack = [[PointX, PointY]]
		AnoImg[PointX][PointY] = 1
		while 1:
			tem1 = Stack.pop()
			LocX = tem1[0]
			LocY = tem1[1]
			if OutImg[LocX + 1][LocY] >= 5 and AnoImg[LocX + 1][LocY] == 0:
				Stack.append([LocX + 1, LocY])
				AnoImg[LocX + 1][LocY] = 1
			
			elif AnoImg[LocX + 1][LocY] != 1:
				AnoImg[LocX + 1][LocY] = 255


			if OutImg[LocX - 1][LocY] >= 5 and AnoImg[LocX - 1][LocY] == 0:
				Stack.append([LocX - 1, LocY])
				AnoImg[LocX - 1][LocY] = 1
		
			elif AnoImg[LocX - 1][LocY] != 1:
				AnoImg[LocX - 1][LocY] = 255


			if OutImg[LocX][LocY + 1] >= 5 and AnoImg[LocX][LocY + 1] == 0:
				Stack.append([LocX, LocY + 1])
				AnoImg[LocX][LocY + 1] = 1

			elif AnoImg[LocX][LocY + 1] != 1:
				AnoImg[LocX][LocY + 1] = 255


			if OutImg[LocX][LocY - 1] >= 5 and AnoImg[LocX][LocY - 1] == 0:
				Stack.append([LocX, LocY - 1])
				AnoImg[LocX][LocY - 1] = 1

			elif AnoImg[LocX][LocY - 1] != 1:
				AnoImg[LocX][LocY - 1] = 255

			if len(Stack) == 0:
				break
		

		#==============================================================================
		#Boundary Print
		OutImg = [[0 for n in range(len(img[1]))] for n in range(len(img))]
		for p in range(0, len(OutImg)):
			for q in range(0, len(OutImg[p])):
				if AnoImg[p][q] == 255:
					OutImg[p][q] = 0
				else:
					OutImg[p][q] = 255


		#==============================================================================
		#Output the figure
		OutImg = Pretreatment.CombineFigures(img, OutImg, 1)
		misc.imsave("Saving/result.png", OutImg)
		return OutImg


	#==============================================================================
	#==============================================================================



ImageName = Constant.ImageName
Main2(ImageName)

