#include<iostream>
#include<cmath>
#include<ctime>

using namespace std;

double energy(int * temp,int N)               // Function to calculate the energy of a config given by "temp"
{
  double E_s = 0;
  for ( int i = 0 ; i<(N-1); i++)
    E_s += temp[i]*temp[i+1];                 //Nearest neighbour interactions
  E_s += temp[N-1]*temp[0];                   //Periodic boundary condition
  return (E_s);
}

void calculate(int N, double B)
{
  int E_s,k;
  int* temp;                                 //temp is a temporary variable to store the generated configuration as a series of +1 and -1.
  temp = new int[N];                         //Dynamic array initialization
  double m_s,E,m,Z;
  E_s = 0;
  m_s = 0;
  for ( long i = 0; i<exp2(N); ++i)
  {
    k = i;
    for ( int j = 0; j<N; ++j)
    {
      temp[j] = (k%2)*2 - 1;                 // Generates all possible sequences containing +1 and -1 and of size N
      k/=2;
      m_s += temp[j];
    }
    E_s = energy(temp,N);
    m_s = 1.0*m_s/N;                         // Average magnetization is sum of each magnetic moment / number of sites

    E += E_s*1.0*exp(-1*B*E_s);              // Numerator of average energy expression
    Z += 1.0*exp(-1*B*E_s);                  // Partition function calculation
    m += abs(m_s)*1.0*exp(-1*B*E_s);         // Numerator of average absolute magnetization expression

    m_s = 0;
    E_s = 0;
  }
  E /= Z;
  m /= Z;
  cout<<" Average Energy = "<<E<<"\n";
  cout<<" Average Magnetization = "<<m<<"\n";
  delete temp;
}


int main()
{
  int N;
  double B;
  cout<<"Enter the lattice size : ";
  cin>>N;
  cout<<"Enter the value of beta : ";
  cin>>B;
  int start = clock();
  cout<<"Result : \n";
  cout<<"Total number of basis states = "<<exp2(N)<<"\n";
  calculate(N,B);
  int stop = clock();
  cout<<"\n Time taken to execute = "<<(stop-start)/double(CLOCKS_PER_SEC)*1000<<" ms\n";
  return (0);
}

