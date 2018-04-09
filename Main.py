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

#import files
import Init
import Pretreatment
import Constant


def Main():
	#Image input 
	img = np.array(Image.open("Figure/11.png").convert("L"))

	#Get Histogram
	Histogram = Pretreatment.Histogram(img)

	#Get 2-dim differential
	Differential = Pretreatment.DerHis(Histogram)

	#Get ZeroCrossing Pair
	ZCNumber = Pretreatment.Sta2Der(Differential)
	
	#Determint the ZeroCrossing Pair are not too small
	PairOfZC = []

	for i in range(0, len(ZCNumber)):
		if ZCNumber[i][1] - ZCNumber[i][0] < 4:
			continue
		else:
			PairOfZC.append(ZCNumber[i])
	
	#ZeroCrossing Learning
	if len(PairOfZC) >= 2:
		PairOfZC = Pretreatment.ProbLearn(Histogram, PairOfZC)
	elif len(PairOfZC) == 1:
		pass
	else:
		PairOfZC.append([0, 127])
		PairOfZC.append([128, 255])
	
	print("Pretreatment finished")
	
	#Parameter Saving and output - writing string
	String = ""
	for i in range(0, 256):
		String += str(Histogram[i])
		String += "\n"
	String += str(len(PairOfZC) * 3) + " " + str(Constant.Loop) + " " + str(Constant.gw) + " " + str(Constant.gh) + " " + Constant.mode + "\n"
	for i in range(0, len(PairOfZC)):
		String += str(0.0) + " " + str(0.5) + "\n"
		String += str(0) + " " + str(128) + "\n"
		String += str(PairOfZC[i][0]) + " " + str(PairOfZC[i][1]) + "\n"
	
	#Parameter Saving and output - File writing
	FileName = "Input.out"
	os.system("rm " + FileName)
	Init.BuildFile(FileName)
	File = open(FileName, "a")
	File.write(String)
	File.close()

	#Compile C files
	if Init.SystemJudge() == 0:		
		os.system("rm CARLA")
		os.system("gcc CARLA.c -o CARLA")
	else:
		os.system("rm CARLA.exe")
		os.system("gcc CARLA.c")

	print("Input.out writing finished, main algorithm loop begin.")

	#Main Algorithm in C
	if Init.SystemJudge() == 0:
		os.system("./CARLA")
	else:
		os.system(".\CARLA.exe")
	
	print("Main algorithm iteration finished. Analysis and output.")
	
	#Read the output file
	FileName = "Output.out"
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
			DataOutput.append(float(TemStr))
	
	Treasholding = []

	for i in range(0, int(((len(DataOutput)) - 1) / 3)):
			Treasholding.append((DataOutput[i * 3 + 2] + DataOutput[i * 3 + 5]) / 2)

	#Figure Segmentation
	OutImg = [[0.00 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len(Treasholding)):
		TemImg = Pretreatment.Treasholding(img, Treasholding[i])
		for p in range(0, len(OutImg)):
			for q in range(0, len(OutImg[p])):
				OutImg[p][q] = max(TemImg[p][q], OutImg[p][q])

	for p in range(0, len(OutImg)):
		for q in range(0, len(OutImg[p])):
			OutImg[p][q] = 255 - OutImg[p][q]

	plt.imshow(OutImg, cmap="gray")
	plt.axis("off")
	plt.show()
	InpStr = input("Save the figure?[Y/ n]")
	if InpStr == "Y" or InpStr == "y":
		Name = "Figure_"
		Name += str(TimeCal.GetTime())
		Name += ".png"
		os.system("cp null " + Name)
		misc.imsave(Name, img)
		if not os.path.exists("Output"):
			os.system("mkdir Output")
		os.system("mv " + Name + " Output/" + Name)
	


def Main1():
	#Image input 
	img = np.array(Image.open("Figure/06.png").convert("L"))

	#Get Histogram
	Histogram = Pretreatment.Histogram(img)

	#Get 2-dim differential
	Differential = Pretreatment.DerHis(Histogram)

	#Get ZeroCrossing Pair
	ZCNumber = Pretreatment.Sta2Der(Differential)
	
	#Determint the ZeroCrossing Pair are not too small
	PairOfZC = []
	for i in range(0, len(ZCNumber)):
		if ZCNumber[i][1] - ZCNumber[i][0] < 3:
			continue
		else:
			PairOfZC.append(ZCNumber[i])
	
	#ZeroCrossing Learning
	PairOfZC = Pretreatment.ProbLearn(Histogram, PairOfZC)
	
	print("Pretreatment finished")
	
	DataOutput = []
	for i in range(0, len(PairOfZC)):
		DataOutput.append(0)
		DataOutput.append(0)
		DataOutput.append((PairOfZC[i][0] + PairOfZC[i][1]) / 2)

	#Figure Segmentation
	OutImg = [[0.00 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len(DataOutput)):
		if i % 3 == 2:
			TemImg = Pretreatment.Treasholding(img, DataOutput[i])
			for p in range(0, len(OutImg)):
				for q in range(0, len(OutImg[p])):
					OutImg[p][q] = max(TemImg[p][q], OutImg[p][q])

	#InpK = np.array([[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]])
	#OutImg = signal.fftconvolve(OutImg, InpK[::-1], mode='full')
	#OutImg = cv2.Canny(np.uint8(OutImg), 85, 170)

	for p in range(0, len(OutImg)):
		for q in range(0, len(OutImg[p])):
			OutImg[p][q] = 255 - OutImg[p][q]
	
	plt.imshow(OutImg, cmap="gray")
	plt.axis("off")
	plt.show()
	InpStr = input("Save the figure?[Y/ n]")
	if InpStr == "Y" or InpStr == "y":
		Name = "Figure_"
		Name += str(TimeCal.GetTime())
		Name += ".png"
		os.system("cp null " + Name)
		misc.imsave(Name, img)
		if not os.path.exists("Output"):
			os.system("mkdir Output")
		os.system("mv " + Name + " Output/" + Name)
	




def Main2():
	import pandas as pd
	from gap_statistic import OptimalK
	from sklearn.datasets.samples_generator import make_blobs
	from sklearn.cluster import KMeans
	
	#Image input 
	img = np.array(Image.open("Figure/04.png").convert("L"))

	#Get Histogram
	Histogram = Pretreatment.Histogram(img)

	#Gap statistic
	optimalK = OptimalK(parallel_backend = 'joblib')
	ClusterSet = []
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			ClusterSet.append([i, j, img[i, j]])
	ClusterSet = np.array(ClusterSet)

	print(len(ClusterSet))
	print(ClusterSet)
	#DEBUG!!!!!!!!
	N_Cluster = optimalK(ClusterSet, cluster_array = np.arange(1, 50))

	print(N_Cluster)
	if N_Cluster < 2:
		N_Cluster = 2
	
	#Getting treasholding with Probability
	Treasholding = Pretreatment.AutoTH(Histogram, N_Cluster)

	print("Pretreatment finished")

	DataOutput = np.array([])
	for i in range(0, len(Treasholding)):
		DataOutput.append(0)
		DataOutput.append(0)
		DataOutput.append(Treasholding[i])

	#Figure Segmentation
	OutImg = [[0.00 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len(DataOutput)):
		if i % 3 == 2:
			TemImg = Pretreatment.Treasholding(img, DataOutput[i])
			for p in range(0, len(OutImg)):
				for q in range(0, len(OutImg[p])):
					OutImg[p][q] = max(TemImg[p][q], OutImg[p][q])

	#InpK = np.array([[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]])
	#OutImg = signal.fftconvolve(OutImg, InpK[::-1], mode='full')
	#OutImg = cv2.Canny(np.uint8(OutImg), 85, 170)

	for p in range(0, len(OutImg)):
		for q in range(0, len(OutImg[p])):
			OutImg[p][q] = 255 - OutImg[p][q]
	
	
	plt.imshow(OutImg, cmap="gray")
	plt.axis("off")
	plt.show()
	InpStr = input("Save the figure?[Y/ n]")
	if InpStr == "Y" or InpStr == "y":
		Name = "Figure_"
		Name += str(Init.GetTime())
		Name += ".png"
		os.system("cp null " + Name)
		misc.imsave(Name, img)
		if not os.path.exists("Output"):
			os.system("mkdir Output")
		os.system("mv " + Name + " Output/" + Name)





if __name__ == "__main__":
	#Main()
	Main2()











