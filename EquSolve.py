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
#import matplotlib.pyplot as plt
from copy import deepcopy


#import files
import Init
import Constant


def Algorithm():
	Init.StaClear()
	
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
	
	Lambda = Constant.gw * (Constant.xmax - Constant.xmin)
	sigma = Constant.gh / (Constant.xmax - Constant.xmin)
	#Parameter actually used in integral

	SavStr = ""
	#For test output


	def F(delta, i, Loop):
		#This function will calculate the value of f(delta, i)
		if Loop == Constant.LoopMax or i == 0:
			return (delta - Constant.xmin) / (Constant.xmax - Constant.xmin)
		else:
			tem = math.erf((delta - x[i-1]) / sigma) - math.erf((Constant.xmin - x[i-1]) / sigma)
			return alpha[i] * F(delta, i-1, Loop + 1) + math.sqrt(2 * pi) / 2 * alpha[i] * beta[i] * Lambda * sigma * tem  


	def dF(delta, i, Loop):
		#This function will calculate the value of F'_x(delta, i)
		if Loop == Constant.LoopMax or i == 0:
			return 1 / (Constant.xmax - Constant.xmin)
		else:
			return alpha[i] * dF(delta, i-1, Loop + 1) + math.sqrt(2) * alpha[i] * beta[i] * Lambda * sigma * math.exp(- pow((delta - x[i-1]) / sigma, 2 ))


	def GetX(z, i, xinit = (Constant.xmax + Constant.xmin) / 2):
		#This function will get the value x in the integral with variable upper
		if i == 0:
			return Constant.xmin + z * (Constant.xmax - Constant.xmin)
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
		if abs(Jmed - Jmin) < 0.00001 or Jmed - J[i] < 0: 
			return 0
		else:
			return min(max(0, ((Jmed - J[i]) / (Jmed - Jmin)) ), 1)


	def GetAlpha(i):
		#This function will get the parameter alpha in the next loop
		tem = math.erf((Constant.xmax - x[i]) / (sigma * math.sqrt(2))) - math.erf((Constant.xmin - x[i]) / (sigma * math.sqrt(2)))
		TTL = 1 / (1 + beta[i+1] * math.sqrt(2 * pi) / 2 * Lambda * sigma * tem)
		#print(tem, TTL)
		return TTL


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
		if Loop == Constant.LoopMax or i == 0:
			return 1/(Constant.xmax - Constant.xmin)
		else:
			return alpha[i] * (fx(tau, i-1, Loop + 1) + Lambda * beta[i] * math.exp(-pow((tau - x[i-1]), 2) / (2 * sigma * sigma)))


	#Main Loop
	for kase in range(0, Constant.TTLkase):
		if Constant.MODEL == "PRE" or Constant.MODEL == "TEST":
			pass
			#print(str(kase) + "/"  + str(Constant.TTLkase), end = "\r")
		
		#Order: z_i, x_i, J_i(J_{med}, J_{min}), \beta_{i+1}, \alpha_{i+1}, f(\tau, i+1)
		z = random.random()
		#print(z)
		x.append(GetX(z, kase))
		J.append(Constant.Consume(x[kase]))
		Jmed = GetJmed(kase)
		Jmin = min(Jmin, J[kase])
		beta.append(GetBeta(kase))
		alpha.append(GetAlpha(kase))

		#print(z, Jmin, Jmed)
		if kase >= 2:
			x1 = np.linspace(Constant.xmin, Constant.xmax, 2000)
			FinIntegral = 0
			maxx = 0
			maxy = 0
			y1 = np.array([0.00 for n in range(2000)])
			for i in range(0, len(y1)):
				y1[i] = fx(x1[i], kase - 1, 0)
				if y1[i] > maxy:
					maxx = x1[i]
					maxy = y1[i]
			print(str(maxx))

			"""
			fig1 = plt.figure()
			ax = fig1.add_subplot(111)
			plt.xlim(Constant.xmin-0.1, Constant.xmax+0.1)
			plt.ylim(0, 5)

			ax.plot(x1, y1, label = "black")

			fig1.show()
			input("Press any key to continue")
			"""

	return None
	


#for i in range(0, 100):
Algorithm()










