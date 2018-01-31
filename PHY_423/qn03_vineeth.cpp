#include<iostream>

int main()
{
  long long inp;
  std::cout<<"Enter the number of seconds : ";
  std::cin>>inp;

  std::cout<<inp<<" seconds = ";
  int days,hrs,mins,secs;
  days = inp/86400;
  inp -= days*86400;
  hrs = inp/3600;
  inp -= hrs*3600;
  mins = inp/60;
  inp -= mins*60;
  secs = inp;

  std::cout<<days<<" days, "<<hrs<<" hours, "<<mins<<" minutes, "<<secs<<" seconds\n";

  return (0);
}

