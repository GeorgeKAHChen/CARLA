############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		CARLA.py
#
############################################################

def ka_CARLA(ttl, loop, gw, gh, mode, Interval, FileLocal):
	from ctypes import *  
	libc = cdll.LoadLibrary("CARLA.so")  
	return libc.Algorithm(ttl, loop, gw, gh, mode, Interval, FileLocal)

