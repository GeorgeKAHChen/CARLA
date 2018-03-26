#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include "Parameter.h"

void Algorithm(){

	//Constants

	double x[1];
	//Study parameter(Here is the solution of function)
	
	double Jmed = 0.00;
	double Jmin = 999999999999.00;
	//Statistic of cost
	
	double J[1];
	//Saving cost
	
	double z = 0.00;
	//Monte Carlo Integral value
	
	double alpha[1] = {0};
	//Parameter to make integral equal to 1
	
	double beta[1] = {0};
	//Reinforcement learning parameter
	
	double Lambda = gw * (xmax - xmin);
	double sigma = gh / (xmax - xmin);
	//Parameter actually used in integral

	std::string SavStr = "";
	//For test output

	printf("%f\t%f\n", Lambda, sigma);


}


int main(){
	//Main Function
	Algorithm();

	return 0;
}