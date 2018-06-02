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
	#Pretreatments and Definition
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
	#Initial CARLA
	Pretreatment.Pre_CARLA()

	#==============================================================================
	#Give Minimum number of GMM model
	N_Cluster = Constant.N_Cluster



	"""
	#==============================================================================
	#Pre-Processing Algorithm and Claculation
	#==============================================================================
	"""
	#==============================================================================
	#Toboggan Algorithm
	TobImage, TobBlock = RWPart.Toboggan(img)
	#CAUTION: The block code of Toboggan is begin from 1 rather than 0!!
	
	#==============================================================================
	#Get the histogram
	Histogram = Pretreatment.Histogram(TobBlock)
	
	if DEBUG:
		AnaLine += "His = "
		AnaLine += str(Histogram)
		AnaLine += ";\n"



	"""
	#==============================================================================
	#Main CARLA Algorithm Loop
	#==============================================================================
	"""
	#==============================================================================
	#Pretreatment of CARLA, get the initial data
	PairOfZC = Pretreatment.ProbLearn(Histogram, Pretreatment.GetPeak(Histogram, N_Cluster))
	
	#==============================================================================
	#GMM - CARLA
	DataLast = Pretreatment.CARLA(Histogram, PairOfZC)

	#==============================================================================
	#GMM - Ths
	Thresholding = Pretreatment.GMM_THS(Histogram, DataLast)
	

	if DEBUG:
		AnaLine += "tem = "
		AnaLine += str(DataLast)
		AnaLine += ";\n"



	"""
	#==============================================================================
	#Thresholding solution with distance matirx
	#==============================================================================
	"""
	#==============================================================================
	#Data classify
	for i in range(1, len(TobBlock)):
		KMeansData = [[] for n in range(len(Thresholding) - 1)]
		TobLoc = [[] for n in range(len(Thresholding) - 1)]
		for j in range(0, len(Thresholding)):
			if TobBlock[i][3] < Thresholding[j]:
				KMeansData[j - 1].append([TobBlock[i][0], TobBlock[i][1]])
				TobLoc[j - 1].append(i)
				break

	Init.ArrOutput(KMeansData)

	for i in range(0, len(KMeansData)):
		Data = KMeansData[i]

		#==============================================================================
		#Gap Statistic
		optimalK = OptimalK(parallel_backend = 'joblib')
		N_Cluster = optimalK(np.array(Data), cluster_array = np.arange(1, 50))

		if DEBUG:
			print(N_Cluster)

		#==============================================================================
		#Build K-means
		KMResult = KMeans(n_clusters = N_Cluster, random_state = 10).fit_predict(Data)

		Group = [[n] for n in range(N_Cluster)]
		TTL = len(Data)
		for j in range(0, len(KMResult)):
			Group[KMResult[j]] += 1

		Group.sort()
		SameGroup = []
		Summ = 0
		for j in range(0, len(Group)):
			Summ += Group[k][1]
			SameGroup.append(Group[k][0])
			if Summ / TTL > Constant.LenPar:
				break

		for j in range(0, len(SameGroup)):
			pass



		

	OutImg = np.array([[0.00 for n in range(len(img[0]))] for n in range(len(img))])

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
	# output
	#==============================================================================
	"""

	OutImg = Pretreatment.CombineFigures(img, OutImg, 1)
	misc.imsave("Saving/result" + str(Init.GetTime()) + ".png", OutImg)	
	return OutImg
	#==============================================================================
	#==============================================================================





def Main2333(ImageName):
	"""
	#==============================================================================
	#Pretreatments and Definition
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
	#Initial CARLA
	Pretreatment.Pre_CARLA()

	#==============================================================================
	#Give Minimum number of GMM model
	N_Cluster = Constant.N_Cluster



	"""
	#==============================================================================
	#Pre-Processing Algorithm and Claculation
	#==============================================================================
	"""

	#==============================================================================
	#Get the histogram
	Histogram = Pretreatment.Histogram(img)

	if DEBUG:
		AnaLine += "His = "
		AnaLine += str(Histogram)
		AnaLine += ";\n"

	"""
	#==============================================================================
	#Main CARLA Algorithm Loop
	#==============================================================================
	"""
	#==============================================================================
	#Pretreatment of CARLA, get the initial data
	PairOfZC = []
	IntLen = 256 / N_Cluster
	for i in range(0, N_Cluster):
		PairOfZC.append([int(i * IntLen), int((i + 1) * IntLen)])
	PairOfZC[N_Cluster - 1][1] = 256

	#==============================================================================
	#GMM - CARLA
	DataLast = Pretreatment.CARLA(Histogram, PairOfZC)

	#==============================================================================
	#GMM - Ths
	Thresholding = Pretreatment.GMM_THS(Histogram, DataLast)
	

	if DEBUG:
		AnaLine += "tem = "
		AnaLine += str(DataLast)
		AnaLine += ";\n"

	OutImg = np.array([[255 for n in range(len(img[1]))] for n in range(len(img))])
	
	for i in range(0, len(Thresholding) - 1):
		OutImg -= Pretreatment.Thresholding(img, Thresholding[i], Thresholding[i + 1])
	
	for i in range(0, len(OutImg)):
		for j in range(0, len(OutImg[i])):
			OutImg[i][j] = max(OutImg[i][j], 0)
	
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
	# output
	#==============================================================================
	"""

	OutImg = Pretreatment.CombineFigures(img, OutImg, 1)
	os.system("mkdir Saving")
	misc.imsave("Saving/result" + str(Init.GetTime()) + ".png", OutImg)	
	return OutImg
	#==============================================================================
	#==============================================================================






def Main4546(ImageName):
	"""
	#==============================================================================
	#Pretreatments and Definition
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
	#Initial CARLA
	Pretreatment.Pre_CARLA()

	#==============================================================================
	#Give Minimum number of GMM model
	N_Cluster = Constant.N_Cluster



	"""
	#==============================================================================
	#Pre-Processing Algorithm and Claculation
	#==============================================================================
	"""

	#==============================================================================
	#Get the histogram
	Histogram = Pretreatment.Histogram(img)

	if DEBUG:
		AnaLine += "His = "
		AnaLine += str(Histogram)
		AnaLine += ";\n"

	"""
	#==============================================================================
	#Main CARLA Algorithm Loop
	#==============================================================================
	"""
	#==============================================================================
	#Pretreatment of CARLA, get the initial data
	PairOfZC = []
	IntLen = 256 / N_Cluster
	for i in range(0, N_Cluster):
		PairOfZC.append([int(i * IntLen), int((i + 1) * IntLen)])
	PairOfZC[N_Cluster - 1][1] = 256

	#==============================================================================
	#GMM - CARLA
	DataLast = Pretreatment.CARLA(Histogram, PairOfZC)

	#==============================================================================
	#GMM - Ths
	Thresholding = Pretreatment.GMM_THS(Histogram, DataLast)
	

	if DEBUG:
		AnaLine += "tem = "
		AnaLine += str(DataLast)
		AnaLine += ";\n"

	KmeansData = [[] for n in range(len(Thresholding) - 1)]

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			for k in range(0, len(Thresholding)):
				if img[i][j] < Thresholding[k]:
					KmeansData[k - 1].append([float(i), float(j)])
					break

	OutImg = np.array([[-1 for n in range(len(img[1]))] for n in range(len(img))])
	sb = 0
	for i in range(0, len(KmeansData)):
		if DEBUG:
			print(str(i) + "/" + str(len(KmeansData)), end = "\r")
		#==============================================================================
		#K-means cluster
		Data = KmeansData[i]
		optimalK = OptimalK(parallel_backend = 'joblib')
		N_Cluster = optimalK(np.array(Data), cluster_array = np.arange(1, 50))
		KMResult = KMeans(n_clusters = N_Cluster, random_state = 10).fit_predict(Data)

		#==============================================================================
		#Analysis
		Group = [[0, n] for n in range(N_Cluster)]
		TTL = len(Data)
		for j in range(0, len(KMResult)):
			Group[KMResult[j]][0] += 1

		Group.sort()

		SameGroup = []
		Summ = 0
		for j in range(len(Group)):
			Summ += Group[j][0]
			SameGroup.append(Group[j][1])
			if Summ / TTL > Constant.LocPar:
				break

		for p in range(0, len(KMResult)):
			for q in range(0, len(SameGroup)):
				if KMResult[p] == SameGroup[q]:
					OutImg[int(Data[p][0] + 0.1)] [int(Data[p][1] + 0.1)] = i
					break
	if DEBUG:
		print( str(len(KmeansData)) + "/" +  str(len(KmeansData)))
	
	FinOut = np.array([[0 for n in range(len(img[1]))] for n in range(len(img))])
	
	for i in range(-1, len(KmeansData)):
		OutImg1 = np.array([[0 for n in range(len(img[1]))] for n in range(len(img))])
		for p in range(0, len(OutImg1)):
			for q in range(0, len(OutImg1[p])):
				if OutImg[p][q] == i:
					OutImg1[p][q] = 0
				else:
					OutImg1[p][q] = 255
		if i != -1:
			FinOut += np.array(cv2.Canny(np.uint8(OutImg1), 85, 170))
		else:
			misc.imsave("Saving/result" + str(Init.GetTime()) + ".png", FinOut)	

	
	OutImg = 255 - FinOut

	for i in range(0, len(OutImg)):
		for j in range(0, len(OutImg[i])):
			OutImg[i][j] = max(OutImg[i][j], 0)
	
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
	# output
	#==============================================================================
	"""

	OutImg = Pretreatment.CombineFigures(img, OutImg, 1)
	os.system("mkdir Saving")
	misc.imsave("Saving/result" + str(Init.GetTime()) + ".png", OutImg)	
	return OutImg
	#==============================================================================
	#==============================================================================




#Main4546("Figure/Aznyan.png")
#Main2333("Figure/Easy.png")
#Main2333("Figure/Aznyan.png")
#Main2333("Figure/Caman.bmp")
#Main2333("Figure/Difficult.png")
#Main2333("Figure/Factory.png")
#Main2333("Figure/Heart.png")

Main2333("Figure/Inp1.jpg")
Main2333("Figure/Inp3.jpg")
Main2333("Figure/Inp4.jpg")
Main2333("Figure/Inp5.jpg")
Main2333("Figure/Inp7.jpg")
Main2333("Figure/Inp8.jpg")
Main2333("Figure/Inp9.jpg")
