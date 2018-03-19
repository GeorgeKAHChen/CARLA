############################################################
#
#		CARLA - Equation Solve
#		Copyright(c) KazukiAmakawa, all right reserved.
#		EquSolve.py
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
	xmin = 0.00
	xmax = 2.00
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
	gh = 0.3
	#Parameter about the converge speed in H(x, x_i)
	LoopMax = 50
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
	
	alpha = [1]
	#Parameter to make integral equal to 1
	
	beta = [1]
	#Reinforcement learning parameter
	
	Lambda = gw * (xmax - xmin)
	sigma = gh / (xmax - xmin)
	#Parameter actually used in integral

	def F(delta, i, Loop):
		#This function will calculate the value of f(delta, i)
		if Loop == LoopMax or i == 0:
			return (delta - xmin) / (xmax - xmin)
		else:
			tem = math.erf((delta - x[i-1]) / sigma) - math.erf((xmin - x[i-1]) / sigma)
			TTL = F(delta, i-1, Loop + 1) + math.sqrt(2 * pi) / 2 * alpha[i] * beta[i] * Lambda * sigma * tem  
			return TTL

	def dF(delta, i, Loop):
		#This function will calculate the value of F'_x(delta, i)
		if Loop == LoopMax or i == 0:
			return 0
		else:
			TTL = dF(delta, i-1, Loop + 1) + math.sqrt(2) * alpha[i] * beta[i] * Lambda * sigma * math.exp((delta - x[i-1]) / sigma)  
			return TTL

	def GetX(z, i, xinit = (xmax + xmin) / 2):
		#This function will get the value x in the integral with variable upper
		if i == 0:
			return xmin + z * (xmax - xmin)
		else:
			#Use Newton's method to iterator
			RemDelta = 0.00
			delta = xinit
			while 1:
				delta = delta - (F(delta, i, 0) - z) / dF(delta, i, 0)
				
				if abs(RemDelta - delta) < 0.0001:
					break

				RemDelta = delta
			return 0

	def GetBeta(i):
		#This function will get the parameter beta in the next loop
		if Jmed - Jmin == 0:
			return 1
		else:
			return max(0, (Jmed - J[i]) / (Jmed - Jmin))

	def GetAlpha(i):
		#This function will get the parameter alpha in the next loop
		tem = math.erf((xmax - x[i]) / sigma) - math.erf((xmin - x[i]) / sigma)
		return 1 / (1 + beta[i+1] * math.sqrt(2 * pi) / 2 * Lambda * sigma * tem)

	#Main Loop
	for kase in range(0, TTLkase):
		#Order: z_i, x_i, J_i(J_{med}, J_{min}), \beta_{i+1}, \alpha_{i+1}, f(\tau, i+1)
		z = random.random()
		if len(x) == 0 :
			x.append(GetX(z, kase))
		else:
			x.append(GetX(z, kase, x[kase - 1]))
		J.append(Consume(x[kase]))
		Jmed = (Jmed * kase + J[kase]) / (kase + 1)
		Jmin = min(Jmin, J[kase])
		beta.append(GetBeta(kase))
		alpha.append(GetAlpha(kase))
		print(x)




Algorithm()









