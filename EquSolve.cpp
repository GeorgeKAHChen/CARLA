#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

class CARLA{
	public:
		//Definition public functions
		double ErrorFunction(ValueX);
		double Xmin, Xmax;
		double Algorithm();
		int 
		
	private:
		//Definition constants
		const double e = 2.718281828459045;
		const double pi = 3.141592653589793;

		//Definition variables
		double x = []
		#Study parameter(Here is the solution of function)
		
		Jmed = 0.00
		Jmin = 999999999999.00
		#Statistic of cost
		
		J = []
		#Saving cost
		
		z = 0.00
		#Monte Carlo Integral value
		
		alpha = [0]
		#Parameter to make integral equal to 1
		
		beta = [0]
		#Reinforcement learning parameter
		
		Lambda = Constant.gw * (Constant.xmax - Constant.xmin)
		sigma = Constant.gh / (Constant.xmax - Constant.xmin)
		#Parameter actually used in integral

		SavStr = ""
		#For test output
		//Definition private functions
		double Fx(double delta, int i, int Loop);
		double dFx(double delta, int i , int Loop);
		double GetX(double z, int i, double Xinit);
		double GetBeta(int i);
		double GetAlpha(int i);
		double GetJmed(int i);
		double fx(double tau, int i, int Loop);
}
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