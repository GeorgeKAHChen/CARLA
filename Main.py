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
DEBUG = Constant.DEBUG


def Main(ImageName):
	#Image input 
	img = np.array(Image.open(ImageName).convert("L"))

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
		String += str(0.0) + " " + str(1) + "\n"
		String += str(0) + " " + str(255) + "\n"
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
		os.system("gcc CARLA.c -lm -o CARLA")
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
	
	Treasholding = [0]

	for i in range(0, int(((len(DataOutput)) - 1) / 3)):
		Treasholding.append((DataOutput[i * 3 + 2] + DataOutput[i * 3 + 5]) / 2)

	Treasholding.append(255)

	#Figure Segmentation
	OutImg = [[0.00 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len(Treasholding) - 1):
		TemImg = Pretreatment.Treasholding(img, Treasholding[i], Treasholding[i + 1])
		for p in range(0, len(OutImg)):
			for q in range(0, len(OutImg[p])):
				OutImg[p][q] = max(TemImg[p][q], OutImg[p][q])

	for p in range(0, len(OutImg)):
		for q in range(0, len(OutImg[p])):
			OutImg[p][q] = 255 - OutImg[p][q]

	if Constant.mode == "p":
		plt.imshow(OutImg, cmap="gray")
		plt.axis("off")
		plt.show()
		InpStr = input("Save the figure?[Y/ n]")
	return OutImg


"""
def Main1(ImageName):
	#Image input 
	img = np.array(Image.open(ImageName).convert("L"))

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
	
	if Constant.mode == "p":	
		plt.imshow(OutImg, cmap="gray")
		plt.axis("off")
		plt.show()
		InpStr = input("Save the figure?[Y/ n]")

	return OutImg	
"""



def Main2(ImageName):
	import pandas as pd
	from gap_statistic import OptimalK
	from sklearn.datasets.samples_generator import make_blobs
	from sklearn.cluster import KMeans

	#==============================================================================
	#Pretreatments	
	#Image input 
	img = np.array(Image.open(ImageName).convert("L"))

	#Smoothing(with FFT based convolution)
	InpK = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])/25
	img1 = signal.fftconvolve(img, InpK[::-1], mode='full')
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = int(img1[i][j])

	#Get Histogram
	Histogram = Pretreatment.Histogram(img)
	#Histogram = Pretreatment.HistSmooth(Histogram)
	


	#==============================================================================
	#Gap statistic and judgement	
	N_Cluster = 0
	if Constant.SegVar == 1:
		optimalK = OptimalK(parallel_backend = 'joblib')
		ClusterSet = []
		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				ClusterSet.append([float(img[i][j])])
		ClusterSet = np.array(ClusterSet)
		N_Cluster = optimalK(ClusterSet, cluster_array = np.arange(1, 50))
		if N_Cluster < 3:
			N_Cluster = 3
		elif N_Cluster > 6:
			N_Cluster = 6
	else:
		N_Cluster = Constant.SegVar
	

	
	if DEBUG:
		print("Cluster = " + str(N_Cluster))

	
	
	#==============================================================================
	#Getting treasholding peak with wavelet based method and Bilter method
	PeaksFinal = []
	size = [2, 256, 128]
	peaks = [len(signal.find_peaks_cwt(Histogram, np.arange(1,2))), len(signal.find_peaks_cwt(Histogram, np.arange(1,256))), 0]

	while 1:
		if peaks[0] > N_Cluster and peaks[1] < N_Cluster:
			PeaksFinal = signal.find_peaks_cwt(Histogram, np.arange(1, size[2]))
			peaks[2] = len(PeaksFinal)
		
		if size[1] - size[0] <= 1 or peaks[2] == N_Cluster or peaks[0] < N_Cluster or peaks[1] > N_Cluster:
			break

		if peaks[0] > N_Cluster and peaks[2] < N_Cluster:
			size[1] = size[2]
			size[2] = int((size[0] + size[1]) / 2)
			peaks[1] = peaks[2]
			continue
		
		if peaks[1] < N_Cluster and peaks[2] > N_Cluster:
			size[0] = size[2]
			size[2] = int((size[0] + size[1]) / 2)
			peaks[0] = peaks[2]
			continue

	if PeaksFinal[0] == 0:
		PeaksFinal[0] = 1
	if PeaksFinal[len(PeaksFinal)-1] == 255:
		PeaksFinal[len(PeaksFinal)-1] = 254
	if DEBUG:
		print("Pretreatment finished")
		print(PeaksFinal)
	


	#==============================================================================
	#Getting treasholding value with iteration and learning method

	PairOfZC = []
	for i in range(0, len(PeaksFinal)):
		PairOfZC.append([PeaksFinal[i] - 1, PeaksFinal[i]])

	PairOfZC = Pretreatment.ProbLearn(Histogram, PairOfZC)
	
	PairOfZC = [[0, 255], [0, 255], [0, 255], [0, 255], [0, 255], [0, 255]]

	
	#==============================================================================
	#MAIN ALGORIHTM
	#==============================================================================
	#Learning Automaton : Continuous Action Reinforcement Learning Automaton 
	

	#==============================================================================
	#Parameter Saving and output - writing string
	String = ""
	for i in range(0, 256):
		String += str(Histogram[i])
		String += "\n"
	String += str(len(PairOfZC) * 3) + " " + str(Constant.Loop) + " " + str(Constant.gw) + " " + str(Constant.gh) + " " + Constant.mode + "\n"
	for i in range(0, len(PairOfZC)):
		String += str(0.0) + " " + str(1.0) + "\n"
		String += str(0) + " " + str(255) + "\n"
		String += str(PairOfZC[i][0]) + " " + str(PairOfZC[i][1]) + "\n"
	

	#==============================================================================
	#Parameter Saving and output - File writing
	FileName = "Input.out"
	os.system("rm " + FileName)
	Init.BuildFile(FileName)
	File = open(FileName, "a")
	File.write(String)
	File.close()


	#==============================================================================
	#Compile C files
	if Init.SystemJudge() == 0:		
		os.system("rm CARLA")
		os.system("gcc CARLA.c -lm -o CARLA")
	else:
		os.system("rm CARLA.exe")
		os.system("gcc CARLA.c")

	print("Input.out writing finished, main algorithm loop begin.")


	#==============================================================================
	#Main Algorithm in C
	if Init.SystemJudge() == 0:
		os.system("./CARLA")
	else:
		os.system(".\CARLA.exe")
	
	print("Main algorithm iteration finished. Analysis and output.")
	

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
	
	"""
	DataOutput = []
	for i in range(0, int(len(Data) / 3 + 0.1)):
		tem = [Data[3 * i + 2], Data[3 * i], Data[3 * i + 1]]
		DataOutput.append(tem)
	DataOutput.sort()
	

	
	#==============================================================================
	#Treasholding pretreatment
	#Just Final step treasholding getting
	Values = [[0.00 for n in range(255)] for n in range(len(DataOutput))]
	for i in range(0, len(DataOutput)):
		Pr = DataOutput[i][1]
		Sigma = DataOutput[i][2]
		Mu = DataOutput[i][0]
		for j in range(0, 255):
			Values[i][j] = Pr / (math.sqrt(2 * math.pi) * Sigma * Sigma) * math.exp(- pow(j - Mu, 2) / (2 * Sigma * Sigma))
	
	#Init.ArrOutput(Values, 1)


	#==============================================================================
	#Get the treasholding valus
	Treasholding = [0]
	j = 0
	for i in range(1, 255):
		print(j)
		if Values[j + 1][i] > Values[j][i]:
			if len(Treasholding) != 1:
				if j - Treasholding[len(Treasholding) - 1] < 3:
					pass
				else:
					Treasholding.append(i - 0.5)
			else:
				Treasholding.append(i - 0.5)

			if j != len(DataOutput) - 2:	
				j += 1
				continue
			else:
				break
	Treasholding.append(255)
	
	if DEBUG:
		print(Treasholding)
	

	#==============================================================================
	#Another Ths method
	Treasholding = [0]
	for i in range(0, len(DataOutput) - 1):
		Val = (DataOutput[i][0] + DataOutput[i+1][0]) / 2
		if DEBUG:
			Treasholding.append(Val)
			continue

		if len(Treasholding) > 1:
			if Val - Treasholding[i] < 5:
				continue
			else:
				Treasholding.append(Val)
		else:
			Treasholding.append(Val)

	Treasholding.append(255)

	if DEBUG:
		print(Treasholding)
	"""
	#==============================================================================
	#Get Ths
	Treasholding = []
	for i in range(0, int(len(Data) / 3 + 0.1)):
		Treasholding.append(Data[3 * i + 2])


	#==============================================================================
	#Figure Segmentation
	OutImg = [[0.00 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len(Treasholding) - 1):
		TemImg = Pretreatment.Treasholding(img, Treasholding[i], Treasholding[i + 1])
		for p in range(0, len(OutImg)):
			for q in range(0, len(OutImg[p])):
				OutImg[p][q] = max(TemImg[p][q], OutImg[p][q])

	for p in range(0, len(OutImg)):
		for q in range(0, len(OutImg[p])):
			OutImg[p][q] = 255 - OutImg[p][q]


	#==============================================================================
	#Output and Print
	if Constant.mode == "p":
		plt.imshow(OutImg, cmap="gray")
		plt.axis("off")
		plt.show()
		input("Press Enter to continue")


	#==============================================================================
	#Factory output
	if Constant.Tsukaikata == "F":
		return OutImg
	#==============================================================================
	#==============================================================================



	#==============================================================================
	#Output and Print
	if Constant.Tsukaikata == "M":
		#==============================================================================
		#Location choose
		plt.imshow(img, cmap="gray")
		plt.axis("off")
		plt.show()
		input("Press Enter to continue")

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
		for p in range(0, len(OutImg)):
			for q in range(0, len(OutImg[p])):
				if AnoImg[p][q] == 255:
					img[p][q] = 255

		if DEBUG:
			plt.imshow(AnoImg, cmap="gray")
			plt.axis("off")
			plt.show()
			input("Press Enter to continue")


		#==============================================================================
		#Output the figure
		plt.imshow(img, cmap="gray")
		plt.axis("off")
		plt.show()
		input("Press Enter to continue")

		return OutImg

	#==============================================================================
	#==============================================================================



if __name__ == "__main__":
	os.system("rm -r Output")
	ImageName = Constant.ImageName
	img = np.array(Image.open(ImageName).convert("L"))
	BlockInfo = Pretreatment.Partial(img)
	os.system("cp -r Output Output1")
	
	if DEBUG:
		print("Block Infomation: " + str(BlockInfo))
	
	for i in range(1, len(BlockInfo)):
		Subimg = np.array(Main2("Output/Block_" + str(i) + ".png"))
		os.system("rm Output/Block_" + str(i) + ".png")
		for p in range(0, len(Subimg)):
			for q in range(0, len(Subimg[p])):
				Subimg[p][q] = min(max(int(Subimg[p][q]), 0), 255)
		
		#circles1 = cv2.HoughCircles(Subimg, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=200, maxRadius=300)
		#circles = circles1[0, :, :]
		#for i in circles[:]: 
		#	cv2.circle(img, (i[0], i[1]), i[2], 128, 5)
		
		Pretreatment.Output(Subimg, "Block_" + str(i) + ".png", 1) 
	Pretreatment.Recovery(len(BlockInfo), BlockInfo, "Out.jpg")


#ImageName = Constant.ImageName
#Pretreatment.Output(Main2(ImageName), "Block_" + str(1) + ".png", 1) 

