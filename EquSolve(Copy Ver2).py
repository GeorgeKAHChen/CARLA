############################################################
#
#		CARLA - Equation Solve
#		Copyright(c) KazukiAmakawa, all right reserved.
#		EquSolve.py
#
############################################################

#This file will use CARLA method to solve the problem of equation solve.
#import packages
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


#import files
import Init
import Constant


def Algorithm():
	Init.StaClear()
	#=======================================================
	#Parameters and functions followed are the learning object you can change
	xmin = 0.00
	xmax = 2.00
	#Interval min and max
	def Consume(x):
		#This function is used as consume function for every action
		#You can change your parameter if you want to learn other things
		return abs(pow(e, x) - 2)
	
	#=======================================================
	#Parameters and functions followed are the learning parameter you can change
	TTLkase = 2000
	#Loop total case
	gw = 0.02
	gh = 0.3
	#Parameter about the converge speed in H(x, x_i)
	LoopMax = 500
	#Parameter which can change the iteration times to uniform distribution in Newton' method


	#=======================================================
	#DO NOT CHANGE ANYTHING BELOW!!
	e = math.e
	pi = math.pi
	#Constants

	x = []
	#Study parameter(Here is the solution of function)
	
	Jmed = 0.00
	Jmin = 999999999999.00
	#Statistic of cost
	
	J = []
	#Saving cost
	
	z = 0.00
	#Monte Carlo Integral value
	
	alpha = [0]
	#Parameter to make integral equal to 1
	
	beta = [0]
	#Reinforcement learning parameter
	
	Lambda = gw * (xmax - xmin)
	sigma = gh / (xmax - xmin)
	#Parameter actually used in integral

	SavStr = ""
	#For test output


	def F(delta, i, Loop):
		#This function will calculate the value of f(delta, i)
		if Loop == LoopMax or i == 0:
			return (delta - xmin) / (xmax - xmin)
		else:
			tem = math.erf((delta - x[i-1]) / sigma) - math.erf((xmin - x[i-1]) / sigma)
			return alpha[i] * F(delta, i-1, Loop + 1) + math.sqrt(2 * pi) / 2 * alpha[i] * beta[i] * Lambda * sigma * tem  


	def dF(delta, i, Loop):
		#This function will calculate the value of F'_x(delta, i)
		if Loop == LoopMax or i == 0:
			return 1 / (xmax - xmin)
		else:
			return alpha[i] * dF(delta, i-1, Loop + 1) + math.sqrt(2) * alpha[i] * beta[i] * Lambda * sigma * math.exp((delta - x[i-1]) / sigma)  


	def GetX(z, i, xinit = (xmax + xmin) / 2):
		#This function will get the value x in the integral with variable upper
		if i == 0:
			return xmin + z * (xmax - xmin)
		else:
			#Use Newton's method to iterator
			RemDelta = 0.00
			delta = xinit
			for NTKase in range(0, 1000):
				FX = F(delta, i, 0)
				dFX = dF(delta, i, 0)
				delta = delta - (FX - z) / dFX
				
				if abs(RemDelta - delta) < 0.01:
					break

				RemDelta = delta
			return delta


	def GetBeta(i):
		#This function will get the parameter beta in the next loop
		if abs(Jmed - Jmin) < 0.00001:
			return 0
		else:
			return max(0, ((Jmed - J[i]) / (Jmed - Jmin)) )


	def GetAlpha(i):
		#This function will get the parameter alpha in the next loop
		tem = math.erf((xmax - x[i]) / sigma) - math.erf((xmin - x[i]) / sigma)
		return 1 / (1 + beta[i+1] * math.sqrt(2 * pi) / 2 * Lambda * sigma * tem)


	def GetJmed(i):
		#This function will get the J_med
		Arr = deepcopy(J)
		Arr.sort()
		if i % 2 == 0:
			return Arr[i//2]
		else:
			return (Arr[i//2] + Arr[(i+1)//2]) / 2


	def fx(tau, i, Loop):
		#This function will calculate the value of fx(tau, i)
		if Loop == LoopMax or i == 0:
			return 1/(xmax - xmin)
		else:
			return alpha[i] * (fx(tau, i-1, Loop + 1) + Lambda * beta[i] * math.exp(-pow((tau - x[i-1]), 2) / (2 * sigma * sigma)))


	#Main Loop
	for kase in range(0, TTLkase):
		if Constant.MODEL == "PRE" or Constant.MODEL == "TEST":
			print(str(kase) + "/"  + str(TTLkase), end = "\r")
		
		#Order: z_i, x_i, J_i(J_{med}, J_{min}), \beta_{i+1}, \alpha_{i+1}, f(\tau, i+1)
		z = random.random()
		x.append(GetX(z, kase))
		J.append(Consume(x[kase]))
		Jmed = GetJmed(kase)
		Jmin = min(Jmin, J[kase])
		if (Jmed - J[kase]) <= 0:
			beta.append(0)
		else:
			beta.append(GetBeta(kase))
		alpha.append(GetAlpha(kase))
		
		if Constant.MODEL == "TEST":
			x1 = np.linspace(xmin, xmax, 500)
			FinIntegral = 0
			maxx = 0
			maxy = 0
			if kase != 0:
				for i in range(1, len(x1)):
					y1 = fx(x1[i], kase - 1, 0)
					if y1 > maxy:
						maxx = x1[i]
						maxy = y1

			SavStr += (str(Jmed) + "\t" + str(maxx) + "\n")
			print(SavStr, end = "\r")

	#Get the maxinum of PDF
	x1 = np.linspace(xmin, xmax, 500)
	FinIntegral = 0
	maxx = 0
	maxy = 0
	for i in range(1, len(x1)):
		y1 = fx(x1[i], TTLkase - 1, 0)
		if y1 > maxy:
			maxx = x1[i]
			maxy = y1
	print(str(maxx))

	#Output and Print
	#You can change the model of output in the file named Constant.py
	if Constant.MODEL == "PRE" :
		pass
	
	elif Constant.MODEL == "VPS":
		pass

	elif Constant.MODEL == "TEST":
		FileName = "SavingJmed"
		Init.BuildFile(FileName)
		File = open(FileName, "a")
		File.write(SavStr)
		File.close()

		"""
		Init.ArrOutput([alpha, beta, x])
		fig1 = plt.figure()
		ax = fig1.add_subplot(111)
		plt.xlim(xmin, xmax)
		plt.ylim(0, 5)

		print(str(maxx))

		y1 = np.array([0.00 for n in range(500)])
		for i in range(0, len(y1)):
			y1[i] = fx(x1[i], TTLkase - 1, 0)
		ax.plot(x1, y1, label = "black")

		fig1.show()
		input("Press any key to continue")
		"""

	return None
	


#for i in range(0, 100):
Algorithm()










