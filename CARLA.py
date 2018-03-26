############################################################
#
#		CARLA - Equation Solve
#		Copyright(c) KazukiAmakawa, all right reserved.
#		EquSolve.py
#
############################################################

class CARLA:
	def __init__(self, ParaSize, Boundary, TTLkase):
		self.ParaSize = ParaSize
		self.Boundary = Boundary
		self.TTLkase = TTLkase


	def F(delta, i, Loop):
		#This function will calculate the value of f(delta, i)


	def dF(delta, i, Loop):
		#This function will calculate the value of F'_x(delta, i)


	def GetX(z, i, xinit = (Constant.xmax + Constant.xmin) / 2):
		#This function will get the value x in the integral with variable upper


	def GetBeta(i):
		#This function will get the parameter beta in the next loop


	def GetAlpha(i):
		#This function will get the parameter alpha in the next loop


	def GetJmed(i):
		#This function will get the J_med


	def fx(tau, i, Loop):
		#This function will calculate the value of fx(tau, i)


	def Algorithm():
		import random

		e = math.e
		pi = math.pi
		#Constants

		x = [[] for n in range(self.ParaSize)]
		#Study parameter(Here is the solution of function)
		
		Jmed = 0.00
		Jmin = 999999999999.00
		#Statistic of cost
		
		J = [[] for n in range(self.ParaSize)]
		#Saving cost
		
		z = 0.00
		#Monte Carlo Integral value
		
		alpha = [[0] for n in range(self.ParaSize)]
		#Parameter to make integral equal to 1
		
		beta = [[0] for n in range(self.ParaSize)]
		#Reinforcement learning parameter
		
		Lambda = Constant.gw * (Constant.xmax - Constant.xmin)
		sigma = Constant.gh / (Constant.xmax - Constant.xmin)
		#Parameter actually used in integral

		for kase in range(0, )
			for Para in range(0, self.ParaSize):












