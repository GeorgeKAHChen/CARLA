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
	N_Cluster = 20



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

	if DEBUG:
		AnaLine += "tem = "
		AnaLine += str(DataLast)
		AnaLine += ";\n"



	"""
	#==============================================================================
	#Thresholding solution with distance matirx
	#==============================================================================
	"""
	TrueGap = int(len(DataLast) / 3 + 0.1)
	Thresholding = Pretreatment.GMM_THS(Histogram, DataLast)

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
		
		if DEBUG:
			if i == 0:
				os.system("rm -r CARLA-test/Data")
				os.system("mkdir CARLA-test/Data")
			OutArr = "sjb = "
			OutArr += str(SizeSet)
			OutArr += "\n"
			FileName = "CARLA-test/Data/ArrFile" + str(i) + ".py"
			File = open(FileName, "w")
			File.write(OutArr)
			File.close()




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
	misc.imsave("Saving/result.png", OutImg)
	return OutImg
	#==============================================================================
	#==============================================================================




Main2(Constant.ImageName)

