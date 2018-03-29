############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		CARLA.py
#
############################################################

class CARLA(object):
	def __init__(self, Interval, MODEL = "-t", TTLkase = 1000, gw = 0.002, gh = 0.03):
		self.MODEL = MODEL

		self.TTLkase = TTLkase
		self.LoopMax = 500

		self.gw = gw
		self.gh = gh

		self.Interval = Interval
		self.NumVar = len(Interval)


	def Consume(self, ImaGourp):
		return None


	def Algorithm(self):
		import math
		import random
		from copy import deepcopy

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


		def GetBeta(i, var):
			if abs(Jmed[var] - Jmin[var]) < 0.00001 or Jmed[var] - J[var][i] < 0: 
				return 0
			else:
				return min(max(0, ((Jmed[var] - J[var][i]) / (Jmed[var] - Jmin[var])) ), 1)


		def GetAlpha(i, var):
			tem = math.erf((self.Interval[var][0] - x[var][i]) / (sigma[var] * math.sqrt(2))) - math.erf((self.Interval[var][1] - x[var][i]) / (sigma[var] * math.sqrt(2)))
			return 1 / (1 + beta[var][i+1] * math.sqrt(2 * pi) / 2 * Lambda[var] * sigma[var] * tem)


		def GetJmed(i, var):
			Arr = deepcopy(J[var])
			Arr.sort()
			if i % 2 == 0:
				return Arr[i//2]
			else:
				return (Arr[i//2] + Arr[(i+1)//2]) / 2


		def fx(tau, i, Loop, var):
			if Loop == self.LoopMax or i == 0:
				return 1/(self.Interval[var][0] - self.Interval[var][1])
			else:
				return alpha[var][i] * ( fx(tau, i-1, Loop + 1, var) + Lambda[var] * beta[var][i] * math.exp(-pow((tau - x[var][i-1]), 2) / (2 * sigma[var] * sigma[var])))


		for kase in range(0, self.TTLkase):
			if self.MODEL == "-p" or self.MODEL == "-t":
				print(str(kase) + "/"  + str(self.TTLkase), end = "\r")
			for var in range(0, self.NumVar):
				x[var].append(random.random())
				ImaCons = [0.00 for n in range(self.NumVar)]
				for ttl in range(0, len(ImaCons)):
					ImaCons[ttl] = x[ttl][len(x[ttl]) - 1]
				J[var].append(self.Consume(ImaCons))
				Jmed[var] = GetJmed(kase, var)
				Jmin[var] = min(Jmin[var], J[var][kase])
				beta[var].append(GetBeta(kase, var))
				alpha[var].append(GetAlpha(kase, var))

		RetVar = []
		for var in range(0, self.NumVar):
			import numpy as np
			x1 = np.linspace(self.Interval[0][0], self.Interval[0][1], 2000)
			FinIntegral = 0
			maxx = 0
			maxy = 0
			y1 = np.array([0.00 for n in range(2000)])
			for i in range(0, len(y1)):
				y1[i] = fx(x1[i], kase - 1, 0, var)
				if y1[i] > maxy:
					maxx = x1[i]
					maxy = y1[i]
			RetVar.append(maxx)

			if self.MODEL == "-p":
				import matplotlib.pyplot as plt
				fig1 = plt.figure()
				ax = fig1.add_subplot(111)
				plt.xlim(self.Interval[var][1]-0.1, self.Interval[var][0]+0.1)
				plt.ylim(0, 5)

				ax.plot(x1, y1, label = "black")

				fig1.show()
				input("Press any key to continue")
		
		if self.MODEL == "-t":
			print (RetVar)

		return RetVar
		