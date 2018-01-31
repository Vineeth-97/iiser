#include<iostream>
#include<cstring>

using namespace std;

int main()
{
  char line[100], *word;
  int ctr=0;
  cout<<"Enter words : \n";
  cin.getline(line,100,'\n');
  word = strtok ( line, ",. -");
  while ( word != NULL  )
  {
    if ( strcmp( word, "done" ) != 0 )
      ctr++;
    else break;
    word = strtok (NULL, " ,.-");
  }
  cout<<" You entered a total of "<<ctr<<" words.\n";
  return (0);
}

