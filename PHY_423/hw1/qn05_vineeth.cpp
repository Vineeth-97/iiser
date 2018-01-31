#include<iostream>
#include<cmath>
#include<fstream>
#include<iomanip>

using namespace std;

double gauss( float x , float a, float m)
{
  return exp((-1/2)*(1/(a*a))*(x-m)*(x-m))/(2*4.0*atan(1.0)*a);
}

int main()
{
  ofstream gfile ("gaussian.txt");
  gfile<<"+------------+------------+\n";
  gfile<<"|      x     |    f(x)    |\n";
  gfile<<"+------------+------------+\n";
  float x,a = 2, m = 0;
  for ( x = -10; x <= 10; x += 0.01)
  {
    gfile<<"|"<<setw(12)<<setprecision(6)<<x<<"|"<<setw(12)<<setprecision(6)<<gauss(x,a,m)<<"|\n";
    gfile<<"+------------+------------+\n";
    }
  gfile.close();
  return (0);
}
