//###########################################################
//
//		CARLA
//		Copyright(c) KazukiAmakawa, all right reserved.
//		CARLA.cpp
//
//###########################################################
#include <math.h>
#include <stdio.h>
#include <string.h>
		
const double pi = 3.141592653589793;
const double e = 2.718281828459045;

class CARLA{
	private:
		char MODEL;

		int TTLkase;

		double gw;
		double gh;

		int NumVar;
		double Interval;
		
		double F(int i, int var, double delta);
		double dF(int i, int var, double delta);
		double Getx(int i, int var);

		double GetJmed(int i, int var);

		double GetBeta(int i, int var);
		double GetAlpha(int i, int var);
		
		double fx(int i, int var, double tau);		


	public:	
		CARLA(int NumVar, double Interval, char MODEL, int TTLkase, double gw, double gh);
		double Consume(double ImaGroup);
		double Algorithm();

};

CARLA::CARLA(int InpNumVar, double InpInterval[InpNumVar][2], char InpMODEL, int InpTTLkase, double Inpgw, double Inpgh){
	MODEL = InpMODEL;
	TTLkase = InpTTLkase;
	gw = Inpgw;
	gh = Inpgh;
	Interval = InpInterval;
	NumVar = InpNumVar;

}















int main(){
	

	return 0;
}












