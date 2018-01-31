#include<iostream>
#include<iomanip>

using namespace std;

int main()
{
  float u = 10.0, g = 9.8,y;
  cout<<"+------------+------------+\n";
  cout<<"|      t     |     y(t)   |\n";
  cout<<"+------------+------------+\n";
  for ( float t = 0; t < 2*u/g; t+= u/(10*g))
  {
    y = u*t - (1/2)*g*t*t;
    cout<<"|"<<setw(12)<<setprecision(6)<<t<<"|"<<setw(12)<<setprecision(6)<<y<<"|\n";
    cout<<"+------------+------------+\n";
  }
  return (0);
}


