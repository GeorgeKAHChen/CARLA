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
const int InteSize = 200;
double Cost(int var, double Parameter[var]);
int sb;								//For test

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


/*
Here is a struct using for quick sort
*/
typedef struct _Range {
	int start, end;
} Range;
Range new_Range(int s, int e) {
	Range r;
	r.start = s;
	r.end = e;
	return r;
}
void swap(double *x, double *y) {
	double t = *x;
	*x = *y;
	*y = t;
}


double quick_sort(const int len, double arr[len]) {
/*	
	//Function Instruction:
	This function will satisfied the quick sort algorithm.

	//Parameter Instruction:
	const int len = Length of the sort array
	double arr[len] = Array you want to sort

	return medium value of all array;
*/
	Range r[len];
	int p = 0;
	r[p++] = new_Range(0, len - 1);
	while (p) {
		Range range = r[--p];
		if (range.start >= range.end)
			continue;
		double mid = arr[range.end];
		int left = range.start, right = range.end - 1;
		while (left < right) {
			while (arr[left] < mid && left < right)
				left ++;
			while (arr[right] >= mid && left < right)
				right --;
			swap(&arr[left], &arr[right]);
		}
		if (arr[left] >= arr[range.end])
			swap(&arr[left], &arr[range.end]);
		else
			left++;
		r[p++] = new_Range(range.start, left - 1);
		r[p++] = new_Range(left + 1, range.end);
	}

	return arr[(int)(len/2)];
}


void Algorithm(const int var, const int ttl, const double gw, const double gh, const char command, double Interval[var][2]){
/*	
	//Function Instruction:
	This function is main function of CARLA Method.

	//Parameter Instruction:
	const int var = Total parameter will learning;
	const int ttl = Total iterator loop during the learning ;
	const double gw = Parameter gw of CARLA method;
	const double gh = Parameter gh of CARLA method;
	const char command = 
		"p" means this algorithm is using for presentation, it will calculate all PDF value
		"t" means this algorithm is using for test, it will print some test parameter
		"w" means this algorithm is using for working, it will output only main result
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
	int i;
	for(i = 0; i < var; i ++){
		lambda[i] = gw / (Interval[i][1] - Interval[i][0]);
		sigma[i] = gh * (Interval[i][1] - Interval[i][0]); 
	}


	//Main Loop
	int kase;
	for(kase = 0; kase < ttl; kase ++){
		int par;
		for(par = 0; par < var; par ++){
		/*
			==========Get the random number z, which is the PDF integral value==========
		*/
			//STILL HAVE SOME ERROR
			//I will recovery this bug latter, with the Mersenne Twister algorithm
			z = Random(seed);
			seed = (int)(z * 1000000);

		/*
			========================Newton's Method, get x========================
		*/

			//Definition and Initialization
			double delta = (Interval[par][0] + Interval[par][1]) / 2;
			double Remdelta = 0;

			//Main Loop
			int loop;
			for(loop = 0; loop < 1000; loop ++){
				//Integral function(Original function) integral
				double Fx = (delta - Interval[par][0]) / (Interval[par][1] - Interval[par][0]);
				int k;
				for(k = 1; k <= kase; k ++){
					tem = erf( (delta - x[par][k-1]) / (sqrt(2) * sigma[par]) ) - erf( (Interval[par][0] - x[par][k-1]) / (sqrt(2) * sigma[par]) );
					tem = beta[par][k] * lambda[par] * sigma[par] * sqrt(2 * pi) / 2 * tem;
					Fx = alpha[par][k] * (Fx + tem);
				}

				//Normal function(Partial function) integral
				double dFx = 1 / (Interval[par][1] - Interval[par][0]);
				int k;
				for(k = 1; k <= kase; k ++){
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
			int loop;
			for(loop = 0; loop < var; loop ++){
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
			double TemJ[kase + 1];
			memcpy(TemJ, J[par], sizeof(TemJ));

			Jmed[par] = quick_sort(kase + 1, TemJ);


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
			

		/*
			===============Tem output and confident if the algorithm is right our not===============
		*/

			if (command == 't')
				printf("%0.16f\t%0.16f\t%0.16f\t%0.16f\t%0.16f\t%0.16f\t%0.16f\t\n", z, x[par][kase], J[par][kase], Jmed[par], Jmin[par], alpha[par][kase + 1], beta[par][kase + 1]);

			if (command == 'p'){
				printf("sb:\t%0.16f\t%0.16f\t%0.16f\t%0.16f\t%0.16f\t%0.16f\t%0.16f\t\n", z, x[par][kase], J[par][kase], Jmed[par], Jmin[par], alpha[par][kase + 1], beta[par][kase + 1]);

				double Output = 0;
				double LenIntervar = (double)1 / InteSize * (Interval[par][1] - Interval[par][0]);

				int ima;
				for(ima = 0; ima < InteSize; ima ++){
					double delta = (double)ima / InteSize * (Interval[par][1] - Interval[par][0]) + Interval[par][0];				
					double total = (double)1 / (Interval[par][1] - Interval[par][0]);
					int k;
					for(k = 0; k <= kase; k ++){
						tem = beta[par][k + 1] * lambda[par] * exp( - pow((delta - x[par][k]), 2) / (2 * sigma[par] * sigma[par])  );
						total = alpha[par][k + 1] * (total + tem);
					}
					Output = (double)total;
					printf("%0.16f\t", Output);
					Output = 0;
				}
				printf("\n");

			}

		}
	}

	//Judgement, calculate the exception of PDF, and make a decision
	//freopen("After", "w", stdout);
	int par;
	for(par = 0; par < var; par ++){
		double Output = 0;
		double LenIntervar = (double)1 / InteSize * (Interval[par][1] - Interval[par][0]);
		int kase;
		for(kase = 0; kase < InteSize; kase ++){
			double delta = (double)kase / InteSize * (Interval[par][1] - Interval[par][0]) + Interval[par][0];				
			double total = (double)1 / (Interval[par][1] - Interval[par][0]);
			int k;
			for(k = 0; k <= ttl; k ++){
				tem = beta[par][k] * lambda[par] * exp( - pow((delta - x[par][k-1]), 2) / (2 * sigma[par] * sigma[par])  );
				total = alpha[par][k] * (total + tem);
			}
			Output += (double)delta * total * LenIntervar;
		}
		printf("%0.16f\n", Output);

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
	//Interval definition
	freopen("SaveArr", "w", stdout);

	double Interval[1][2];
	Interval[0][0] = 0;
	Interval[0][1] = 2;

	Algorithm(1, 10000, 0.01, 0.03, 'w', Interval);
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














