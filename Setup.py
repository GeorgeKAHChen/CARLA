############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Setup.py
#
############################################################


def SystemJudge():
	import platform  
	Str = platform.system() 
	if Str[0] == "w" or Str[0] == "W":
		return 1
	else:
		return 0


def CompileC():
	import os
	if SystemJudge() == 0:
		os.system("gcc -I/usr/include/python2.7/ -shared -o CARLA.so CARLA.c -L/usr/lib/ -lpython2.7")

	elif SystemJudge() == 1:
		print("Sorry, this code cannot work on Windows system")


