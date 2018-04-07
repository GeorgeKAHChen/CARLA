############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Main.py
#
############################################################

#import head
import numpy as np
import os
from PIL import Image

#import files
import Init
import Pretreatment
import Constant


def MainFunction():
	#Image input 
	img = np.array(Image.open("Figure/03.jpg").convert("L"))

	#Get histogram and Zero crossing total
	Histogram = Pretreatment.Histogram(img)
	Differential = Pretreatment.DerHis(Histogram)
	ZCNumber = Pretreatment.Sta2Der(Differential)

	

	PairOfZC = []
	for i in range(0, len(ZCNumber)):
		if ZCNumber[i][1] - ZCNumber[i][0] < 3:
			continue
		else:
			PairOfZC.append(ZCNumber[i])
	PairOfZC = Pretreatment.ProbLearn(Histogram, PairOfZC)
	
	#Init.ArrOutput([Histogram, Differential, ZCNumber, PairOfZC], 1)
	print("Pretreatment finished")
	String = ""
	for i in range(0, 256):
		String += str(Histogram[i])
		String += "\n"
	String += str(len(PairOfZC) * 3) + " " + str(Constant.Loop) + " " + str(Constant.gw) + " " + str(Constant.gh) + " " + Constant.mode + "\n"
	for i in range(0, len(PairOfZC)):
		String += str(0.0) + " " + str(0.5) + "\n"
		String += str(0) + " " + str(128) + "\n"
		String += str(PairOfZC[i][0]) + " " + str(PairOfZC[i][1]) + "\n"

	if Init.SystemJudge() == 0:		
		os.system("gcc CARLA.c -o CARLA")
	else:
		os.system("gcc CARLA.c")

	FileName = "Input.out"
	os.system("rm " + FileName)
	Init.BuildFile(FileName)
	File = open(FileName, "a")
	File.write(String)
	File.close()

	print("Input.out writing finished, main algorithm loop begin.")
	if Init.SystemJudge() == 0:
		os.system("./CARLA")
	else:
		os.system(".\CARLA.exe")
	
	print("Main algorithm iteration finished. Analysis and output.")
	"""
	FileName = "Output"
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
			DataOutput.append(float(FileLine))

	"""
	return

















MainFunction()


