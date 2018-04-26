############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Main.py
#
############################################################
import CARLA

def Cost(Parameter):
	import math
	var = Parameter[0]
	return abs(pow(math.e, var) - 2)
	
print(os.path.realpath(__file__))
CARLA.ka_CARLA(1, 2000, 0.2, 0.03, "t", [0, 2], os.path.realpath(__file__))
