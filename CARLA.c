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
const int InteSize = 2000;
double Cost(int var, double Parameter[var]);


/*===================DO NOT CHANGE ANYTHING BELOW===================*/


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


int compare(const void *a, const void *b){  
   return *(double *)a - *(double *)b;   
}  




void Algorithm(int var, int ttl, double gw, double gh, double Interval[var][2]){
/*	
	//Function Instruction:
	This function is main function of CARLA Method.

	//Parameter Instruction:
	int var = Total parameter will learning;
	int ttl = Total iterator loop during the learning ;
	double gw = Parameter gw of CARLA method;
	double gh = Parameter gh of CARLA method;
	Interval[var][2] = [[X1Min, X1Max], ... ,[XnMin, XnMax]] where n = var;

	return Learning result array;
*/


	//Saving Definition
	double x[var][ttl];					//To save all decision point
	double J[var][ttl];					//To save all cost value
	double Jmed[var];					//To save medium value of all J
	double Jmin[var];					//To save minumum value of all J
	double alpha[var][ttl + 1];			//To save all PDF parameter
	double beta[var][ttl + 1];			//To save all reinforcement parameter
	double lambda[var];					//To save all lambda parameter
	double sigma[var];					//To save all sigma parameter


	int seed = time(NULL);				//For random number getting
	double z;							//A random number which is the PDF integral value
	double tem;							//A temple tank for saving calculation value


	//Pretreatment, Calculate lambda and sigma
	for(int i = 0; i < var; i ++){
		lambda[i] = gw / (Interval[i][1] - Interval[i][0]);
		sigma[i] = gh * (Interval[i][1] - Interval[i][0]); 
	}


	//Main Loop
	for(int kase = 0; kase < ttl; kase ++){
		for(int par = 0; par < var; par ++){
		/*
			==========Get the random number z, which is the PDF integral value==========
		*/
			//STILL HAVE SOME ERROR
			z = Random(seed);
			seed = (int)(z * 100);

		/*
			========================Newton's Method, get x========================
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
					tem = exp(- pow((delta - x[par][k-1]), 2) / (2 * sigma[par] * sigma[par]) );
					tem = beta[par][k] * lambda[par] * sqrt(pi) / 2 * tem;
					dFx = alpha[par][k] * (dFx + tem);
				}

				//Newton's iterator
				Remdelta = delta;
				delta = delta - (Fx - z) / dFx;
				
				//Condition judgement
				if ((delta - Remdelta < 0.000001) && (delta - Remdelta > -0.000001))
					break;
			}

			x[par][kase] = delta;

		/*
			=========================Calculate the cost J=========================
		*/

			//Get the parameter group at present.
			double Parameter[var];
			for(int loop = 0; loop < var; loop ++){
				if (loop <= par){
					Parameter[loop] = x[loop][kase];
				}
				else{
					Parameter[loop] = x[loop][kase - 1];
				}
			}

			//Calculate the cost
			J[par][kase] = Cost(var, Parameter);

		/*
			====================Reflesh the medium and minimum cost====================
		*/
			//Calculation of Jmed
			//Definition and Initialization
			double TemJ[kase];
			memcpy(TemJ, J[par], sizeof(TemJ));
			
			//STILL HAVE SOME ERROR
			qsort(TemJ , kase, sizeof(double), compare);  
			Jmed[par] = TemJ[(int)(kase / 2)];


			//Calculation of Jmin
			if (kase == 0)		
				Jmin[par] = J[par][kase];
			else				
				Jmin[par] = (Jmin[par] < J[par][kase])? Jmin[par] : J[par][kase];


		/*
			====================Calculate the reinforcement value beta====================
		*/
			if ((Jmed[par] - Jmin[par]) < 0.000001 && (Jmed[par] - Jmin[par]) > -0.000001)
				beta[par][kase + 1] = 0;
			else{
				tem = (Jmed[par] - J[par][kase]) / (Jmed[par] - Jmin[par]);
				beta[par][kase + 1] = (tem > 0)? tem : 0;
			}


		/*
			==========Calculate the PDF parameter alpha and get the PDF of next koop==========
		*/
			tem = erf( (Interval[par][1] - x[par][kase]) / (sqrt(2) * sigma[par]) ) - erf( (Interval[par][0] - x[par][kase]) / (sqrt(2) * sigma[par]) );
			tem = beta[par][kase + 1] * lambda[par] * sigma[par] * sqrt(2 * pi) / 2 * tem;
			alpha[par][kase + 1] = 1 / (1 + tem);
			
			printf("%f\t%f\t%f\t%f\t%f\t%f\t%f\t\n", z, x[par][kase], J[par][kase], Jmed[par], Jmin[par], alpha[par][kase + 1], beta[par][kase + 1]);
		}
	}

	//Judgement, calculate the exception of PDF, and make a decision
	//freopen("After", "w", stdout);
	
	for(int par = 0; par < var; par ++){
		double Output = 0;
		double LenIntervar = 1 / InteSize * (Interval[par][1] - Interval[par][0]);
		
		for(int kase = 0; kase < InteSize; kase ++){
			double delta = kase / InteSize * (Interval[par][1] - Interval[par][0]) + Interval[par][0];	
			double total = 1 / (Interval[par][1] - Interval[par][0]);
			for(int k = 1; k < ttl; k ++){
				tem = beta[par][k] * lambda[par] * exp( - pow((delta - x[par][k-1]), 2) / (2 * sigma[par] * sigma[par])  );
				total = alpha[par][k] * (total + tem);
			}
			Output += total * LenIntervar;
			printf("%f\t%f\t\t", total, Output);
		}
		
		printf("%f\n", Output);
	}


	return ;
}


/*===================DO NOT CHANGE ANYTHING ABOVE===================*/


int main(int argc, char const *argv[]){
/*	
	//Function Instruction:
	Main function, where is the begining of all program

	//Parameter Instruction:
	void;

	return 0;
*/
	freopen("SaveArr", "w", stdout);
	//Interval definition
	double Interval[1][2];
	Interval[0][0] = 0;
	Interval[0][1] = 2;


	Algorithm(1, 1000, 0.2, 0.3, Interval);
	return 0;
}


double Cost(int var, double Parameter[var]){
/*	
	//Function Instruction:
	This function will return cost in different situation, which you can change it.

	//Parameter Instruction:
	double cost valut;

	return 0;
*/	
	double tem = pow(e, Parameter[0]) - 2;
	return (tem > 0)? tem : -tem;
}














