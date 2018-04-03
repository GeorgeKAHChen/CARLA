//###########################################################
//
//		CARLA
//		Copyright(c) KazukiAmakawa, all right reserved.
//		CARLA.c
//
//###########################################################

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>


const double pi = 3.141592653589793;
const double e = 2.718281828459045;


double Random(int seed){
/*	
	//Function Instruction:
	This function will return a random number with seed

	//Parameter Instruction:
	int seed = Random number getting seed;

	return A random number;
*/

	//Definition and Initialization
	double num;
	srand(seed);

	//Main Loop, get random number
	for(int i = 0; i < 10; i ++)
		num = (double)rand()/RAND_MAX;
	
	//Output and return
	return num;
}




double Algorithm(int var, int kase, double gw, double gh, double Interval[var][2]){
/*	
	//Function Instruction:
	This function is main function of CARLA Method.

	//Parameter Instruction:
	int var = Total parameter will learning;
	int kase = Total iterator loop during the learning ;
	double gw = Parameter gw of CARLA method;
	double gh = Parameter gh of CARLA method;
	Interval[var][2] = [[X1Min, X1Max], ... ,[XnMin, XnMax]] where n = var;

	return Learning result;
*/


	//Saving Definition
	double x[var][kase];				//To save all decision point
	double J[var][kase];				//To save all cost value
	double Jmed[var];					//To save medium value of all J
	double Jmin[var];					//To save minumum value of all J
	double alpha[var][kase + 1];		//To save all PDF parameter
	double beta[var][kase + 1];			//To save all reinforcement parameter
	double lambda[var];					//To save all lambda parameter
	double sigma[var];					//To save all sigma parameter

	int seed = time(NULL);				//For random number getting
	double z;							//A random number which is the PDF integral value


	//Pretreatment, Calculate lambda and sigma
	for(int i = 0; i < var; i ++){
		lambda[i] = gw / (Interval[i][1] - Interval[i][0]);
		sigma[i] = gh * (Interval[i][1] - Interval[i][0]); 
	}


	//Main Loop
	for(int ttl = 0; ttl < kase; ttl ++){
		for(int par = 0; par < var; par ++){
			//Get the random number z, which is the PDF integral value
			z = Random(seed);
			seed = (int)(z * 100);

			/*
				Newton's Method, get x
			*/

			//Definition and Initialization
			double delta = (Interval[par][0] + Interval[par][1]) / 2;
			double Remdelta = 0;

			//Main Loop
			for(int loop = 0; loop < 1000; loop ++){
				//Integral function(Original function) integral
				double Fx = (delta - Interval[par][0]) / (Interval[par][1] - Interval[par][0]);
				for(int k = 1; k <= kase; k ++){
					tem = erf( (delta - x[par][k-1]) / (sqrt(2) * sigma[par]) ) - erf( (Interval[par][0] - x[par][k-1]) / (sqrt(2) * sigma[par]) );
					tem = beta[par][k] * lambda[par] * sigma[par] * sqrt(2 * pi) / 2 * tem;
					Fx = alpha[par][k] * (Fx + tem);
				}

				//Normal function(Partial function) integral
				double dFx = 1 / (Interval[par][1] - Interval[par][0]);
				for(int k = 1; k <= kase; k ++){
					tem = exp( pow((delta - x[par][k-1]), 2) / (2 * sigma[par] * sigma[par]) );
					tem = beta[par][k] * sigma[par] * lambda[par] * sqrt(2 * pi) / 2 * tem;
					dFx = alpha[par][k](dFx + tem);
				}

				//Newton's iterator
				Remdelta = delta;
				delta = delta - (Fx - z) / dFx;
				
				//Condition judgement
				if (delta - Remdelta < 0.000001) && (delta - Remdelta < 0.000001):
					break;
			}

			x[par][kase] = delta;


			//Calculate the cost J
			double Parameter[var];
			for(int loop = 0; loop < var; loop ++){
				if (loop <= par){

				}
				else{

				}
			}

			//Reflesh the medium and minimum cost


			//Calculate the reinforcement value beta


			//Calculate the PDF parameter alpha and get the PDF of next koop
			
		}
	}

	//Judgement, calculate the exception of PDF, and make a decision
	double Decision = 0;



	//Output and return
	return 0;
}




int main(){
/*	
	//Function Instruction:
	Main function, where is the begining of all program

	//Parameter Instruction:
	void;

	return 0;
*/

	//Interval definition
	double Interval[1][2];
	Interval[0] = {0, 2}


	Algorithm(1, 1000, 0.02, 0.3, );
	return 0;
}















