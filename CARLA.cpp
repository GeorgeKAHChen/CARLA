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

class CARLA{
	private:
		char MODEL;

		int TTLkase;
		int LoopMax = 500;

		double gw;
		double gh;

		double* Interval;
		int NumVar = sizeof(Interval) / sizeof(double) / 2;

		double* Other;

		double GetBeta(int i, int var);
		double GetAlpha(int i, int var);
		double GetJmed(int i, int var);
		double fx(double tau, int i, int Loop, int var);

		const double pi = 3.141592653589793;
		const double e = 2.718281828459045;

	public:	
		CARLA(double* Interval, char MODEL, int TTLkase, double gw, double gh, double* Other);
		double Consume(double* ImaGroup);
		double* Algorithm();
};

CARLA::CARLA(double* InpInterval, char InpMODEL, int InpTTLkase, double Inpgw, double Inpgh, double* InpOther){
	MODEL = InpMODEL;
	TTLkase = InpTTLkase;
	gw = Inpgw;
	gh = Inpgh;
	Interval = InpInterval;
	Other = InpOther;
}

double CARLA::Consume(double* ImaGroup){
	return 0;
}

double* CARLA::Algorithm(){
	double x[NumVar][TTLkase];
	double J[NumVar][TTLkase];

	double Jmed[NumVar];
	double Jmin[NumVar];
	
	double alpha[NumVar][TTLkase];
	double beta[NumVar][TTLkase];

	double Lambda[NumVar];
	double sigma[NumVar];

	for(int i = 0; i < NumVar; i ++)
		memset(x[NumVar], (Interval[NumVar][1] + Interval[NumVar][0]) / 2, sizeof(x[NumVar]));
	memset(J, 0, sizeof(J));
	
	memset(Jmed, 0.00, sizeof(Jmed));
	memset(Jmed, 9999999999.00, sizeof(Jmed));

	memset(alpha, 0, sizeof(alpha));
	memset(beta, 0, sizeof(beta));

	for(int i = 0; i < NumVar; i ++){
		Lambda[i] = gw * (Interval[i][0] - Interval[i][1]);
		sigma[i] = gh / (Interval[i][0] - Interval[i][1]);
	}

}

int main(){
	printf("2333\n");
	return 0;
}







