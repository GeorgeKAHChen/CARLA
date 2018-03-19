############################################################
#
#		CARLA - Equation Solve
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Init.py
#
############################################################

#This file will use CARLA method to solve the problem of equation solve.

import math
import numpy as np 
import os
import random


import Init



def Algorithm():
	#=======================================================
	#Parameters and functions followed are the learning object you can change
	xmin = 0
	xmax = 2
	#Interval min and max
	def Consume(x):
		#This function is used as consume function for every action
		#You can change your parameter if you want to learn other things
		return abs(pow(e, x) - 2)
	
	#=======================================================
	#Parameters and functions followed are the learning parameter you can change
	TTLkase = 1000
	#Loop total case
	gw = 0.2
	gh = 0.003
	#Parameter about the converge speed in H(x, x_i)


	#=======================================================
	#DO NOT CHANGE ANYTHING BELOW!!
	e = math.e
	pi = math.pi
	#Constants

	x = []
	#Study parameter(Here is the solution of function)
	
	Jmed = 0
	Jmin = 999999999999
	#Statistic of cost
	
	J = []
	#Saving cost
	
	z = 0
	#Monte Carlo Integral value
	
	alpha = [1]
	#Parameter to make integral equal to 1
	
	beta = [0]
	#Reinforcement learning parameter
	
	Lambda = gw * (xmax - xmin)
	sigma = gh / (xmax - xmin)
	#Parameter actually used in integral
	
	def GetX(z, n):
		#This function will get the value x in the integral with variable upper
		if n == 0:
			return xmin + z * (xmax - xmin)
		else:
			#I am not confident how to write this part of integral
			return 0

	def GetBeta(i):
		#This function will get the parameter beta in the next loop
		if Jmed - Jmin == 0:
			return 0
		else:
			return max(0, (Jmed - J[i]) / (Jmed - Jmin))

	def GetAlpha(i):
		#This function will get the parameter alpha in the next loop
		tem = math.erf((xmax - x[i]) / sigma) - math.erf((xmin - x[i]) / sigma)
		return 1 / (1 + beta[i+1] * math.sqrt(2 * pi) / 2 * Lambda * sigma * tem)

	#Main Loop
	for kase in range(0, len(TTLkase)):
		#Order: z_i, x_i, J_i(J_{med}, J_{min}), \beta_{i+1}, \alpha_{i+1}, f(\tau, i+1)
		z = random.ramdom()
		x.append(GetX(z, kase))
		J.append(Consume(x[kase]))
		Jmed = (Jmed * kase + J[kase]) / (kase + 1)
		Jmin = min(Jmin, J[kase])
		beta.append(GetBeta(kase))
		alpha.append(GetAlpha(kase))

	print(x[len(x) - 1])



Algorithm()









