#include<iostream>
#include<vector>
#include<numeric>

using namespace std;

float dot_product( vector<float> V1, vector<float> V2 )
{
  float inp,dotp;
  cout<<"Enter the components of first vector : \n";
  while ( cin>>inp && inp != 9999)
    V1.push_back(inp);
  cout<<"Enter the components of second vector : \n";
  while ( cin>>inp && inp != 9999)
    V2.push_back(inp);
  dotp = inner_product(V1.begin(),V1.end(),V2.begin(),0.0);
  return ( dotp );
}

int main()
{
  vector<float> V1,V2;
  float dotp;
  dotp = dot_product(V1,V2);
  cout<<"The Dot Product of the vectors is : "<<dotp<<"\n";
  return (0);
}

