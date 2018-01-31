#include<iostream>
#include<iomanip>

using namespace std;

int main()
{
    float f,c;
    cout<<" Farenheit to Celsius convertion table \n";
    cout<<" +----------+-------+\n";
    cout<<" |Farenheit |Celsius|\n";
    cout<<" +----------+-------+\n";
    for ( f = 0; f <= 100; f+=10 )
    {
      c = (5.0/9)*f - 32;
      cout<<" |"<<setw(10)<<setprecision(4)<<f<<"|"<<setw(7)<<setprecision(4)<<c<<"|\n";
      cout<<" +----------+-------+\n";
    }
    return (0);

}
