//###########################################################
//
//		CARLA
//		Copyright(c) KazukiAmakawa, all right reserved.
//		CARLA.c
//
//###########################################################

struct CARLA{
	private:
		char MODEL;

		int TTLkase;
		int LoopMax = 500;

		double gw;
		double gh;

		double* Interval;
		int NumVar = len(Interval);

		double Other[1];

		double GetBeta(int i, int var);
		double GetAlpha(int i, int var);
		double GetJmed(int i, int var);
		double fx(double tau, int i, int Loop, int var);

	public:	
		CARLA(double* Interval, char MODEL, int TTLkase, double gw, double gh, double* Other);
		double Consume(ImaGroup);
		double Algorithm();
}

CARLA::CARLA(double* InpInterval, char InpMODEL, int InpTTLkase, double Inpgw, double Inpgh, double* InpOther){
	MODEL = InpMODEL;
	TTLkase = InpTTLkase;
	gw = Inpgw;
	gh = Inpgh;
	Interval = InpInterval;
	Other = InpOther;
}

double CARLA::Consume(ImaGroup){
	return 0
}

double CARLA::Algorithm(){
	#include<math.h>


}