############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		CARLA.py
#
############################################################

class CARLA(object):
	def __init__(self, Interval, MODEL = "-t", TTLkase = 1000, gw = 0.002, gh = 0.03, Other = []):
		self.MODEL = MODEL

		self.TTLkase = TTLkase

		self.gw = gw
		self.gh = gh

		self.Interval = Interval
		self.NumVar = len(Interval)

		self.Other = Other

	def Consume(self, ImaGroup):
		return None


	def Algorithm(self):
		import math
		import random
		from copy import deepcopy

		import Init

		e = math.e
		pi = math.pi
		x = [[] for n in range (self.NumVar)]	
		J = [[] for n in range (self.NumVar)]
		Jmed = [0.00 for n in range (self.NumVar)]
		Jmin = [999999999999.00 for n in range(self.NumVar)]
		alpha = [[0] for n in range (self.NumVar)]
		beta = [[0] for n in range (self.NumVar)]
		
		Lambda = []
		sigma = []


		for var in range(0, self.NumVar):
			Lambda.append(self.gw * (self.Interval[var][0] - self.Interval[var][1]))
			sigma.append(self.gh / (self.Interval[var][0] - self.Interval[var][1]))

		SavStr = ""


		def fx(tau, i, var):
			TTL = 0
			for Loop in range(0, i):
				if Loop == 0:
					TTL = 1 / (self.Interval[var][0] - self.Interval[var][1])
				else:
					tem = math.exp( - (pow((tau - x[var][Loop-1]), 2) / (2 * sigma[var] * sigma[var]) ) )
					#print(tem)
					TTL = alpha[var][Loop] * ( TTL + beta[var][Loop] * Lambda[var] * tem )

			return TTL


		def F(delta, i, var):
			#This function will calculate the value of f(delta, i)
			TTL = 0
			for Loop in range(0, i + 1):
				if Loop == 0:
					TTL = (delta - self.Interval[var][1]) / (self.Interval[var][0] - self.Interval[var][1])
				else:
					tem = math.erf((delta - x[var][Loop-1]) / (math.sqrt(2) * sigma[var])) - math.erf((self.Interval[var][1] - x[var][Loop-1]) / (math.sqrt(2) * sigma[var]))
					if delta == 2:
						print(tem)
					TTL += alpha[var][Loop] * ( TTL + math.sqrt(2 * pi) / 2 * beta[var][Loop] * Lambda[var] * sigma[var] * tem )
			if delta == 2:
				print(TTL)
			return TTL


		def dF(delta, i, var):
			#This function will calculate the value of F'_x(delta, i)
			TTL = 0
			for Loop in range(0, i + 1):
				if Loop == 0:
					TTL = 1 / (self.Interval[var][0] - self.Interval[var][1])
				else:
					TTL += alpha[var][Loop] * ( TTL + math.sqrt(pi) / 2 * beta[var][Loop] * Lambda[var] * sigma[var] * math.exp(- pow((delta - x[var][Loop-1]), 2 ) / (2 * sigma[var] * sigma[var]) ) )
			return TTL


		def GetX(z, i, var, xinit = (self.Interval[var][1] + self.Interval[var][0]) / 2):
			#This function will get the value x in the integral with variable upper
			if i == 0:
				return self.Interval[var][1] + z * (self.Interval[var][0] - self.Interval[var][1])
			else:
				#Use Newton's method to iterator
				RemDelta = 0.00
				delta = xinit
				for NTKase in range(0, 1000):
					FX = F(delta, i, var)
					dFX = dF(delta, i, var)
					delta = delta - (FX - z) / dFX
					print(delta)
					#print(RemDelta, delta, FX, dFX, end = "")
					#input()
					if abs(RemDelta - delta) < 0.000000001:
						break

					RemDelta = delta
				#print(delta, end = "\t")
				
				return delta
		

		def GetBeta(i, var):
			if abs(Jmed[var] - Jmin[var]) < 0.00001 or Jmed[var] - J[var][i] < 0: 
				return 0
			else:
				return min(max(0, ((Jmed[var] - J[var][i]) / (Jmed[var] - Jmin[var])) ), 1)


		def GetAlpha(i, var):
			tem = math.erf( (self.Interval[var][0] - x[var][i]) / (sigma[var] * math.sqrt(2)) ) - math.erf( (self.Interval[var][1] - x[var][i]) / (sigma[var] * math.sqrt(2)) )
			return 1 / (1 + beta[var][i+1] * math.sqrt(2 * pi) / 2 * Lambda[var] * sigma[var] * tem)


		def GetJmed(i, var):
			Arr = deepcopy(J[var])
			Arr.sort()
			if i % 2 == 0:
				return Arr[i//2]
			else:
				return (Arr[i//2] + Arr[(i+1)//2]) / 2

		
		for kase in range(0, self.TTLkase):
			if self.MODEL == "-p" or self.MODEL == "-t":
				pass
				#print(str(kase) + "/"  + str(self.TTLkase), end = "\r")
			for var in range(0, self.NumVar):
				z = random.random()
				x[var].append(GetX(z, kase, var))

				ImaCons = [0.00 for n in range(self.NumVar)]
				
				for ttl in range(0, len(ImaCons)):
					if len(x[ttl]) == 0:
						ImaCons[ttl] = (self.Interval[ttl][1] + self.Interval[ttl][0]) / 2
					else:
						ImaCons[ttl] = x[ttl][len(x[ttl]) - 1]

				J[var].append(self.Consume(ImaCons))
				Jmed[var] = GetJmed(kase, var)
				Jmin[var] = min(Jmin[var], J[var][kase])
				beta[var].append(GetBeta(kase, var))
				alpha[var].append(GetAlpha(kase, var))
				
				F(2, kase, var)
				#print(z, x[var][kase], J[var][kase], Jmed[var], Jmin[var], beta[var][kase], alpha[var][kase])
				#print(z)
				print(Jmed[var], Jmin[var], J[var][kase], beta[var][kase+1])
				input()
			#begin of output============================================
			RetVar = []
			for var in range(0, self.NumVar):
				import numpy as np
				x1 = np.linspace(self.Interval[0][0], self.Interval[0][1], 2000)
				FinIntegral = 0
				maxx = 0
				maxy = 0
				y1 = np.array([1/2 for n in range(2000)])
				if kase >= 1:
					for i in range(0, len(y1)):
						y1[i] = fx(x1[i], kase - 1, var)
						if y1[i] > maxy:
							maxx = x1[i]
							maxy = y1[i]
				RetVar.append(maxx)

				if self.MODEL == "-p" and (kase % 50 == 0 or kase <= 10):
					import matplotlib.pyplot as plt
					fig1 = plt.figure()
					ax = fig1.add_subplot(111)
					plt.xlim(self.Interval[var][1]-0.1, self.Interval[var][0]+0.1)
					plt.ylim(0, 3)

					ax.plot(x1, y1, label = "black")

					#fig1.show()
					#input("Press any key to continue")
					plt.savefig('Saving/Figure' + str(Init.GetTime()) + '.png')

			if self.MODEL == "-t":
				print (RetVar)
			#end of output============================================


		return RetVar
	

class Equation(CARLA):
	def Consume(self, ImaGourp):
		import math
		return abs(pow(math.e, ImaGourp[0])- 2)


Equ = Equation([[2, 0]], "-p", 500, 0.2, 0.3)
Solution = Equ.Algorithm()
print(Solution)	