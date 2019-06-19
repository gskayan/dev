#include<iostream>
#include<fstream>
#include<unistd.h>

using namespace std;

int main()
{
  int loops(3);
  int i(0);
  bool doMore(true);
  ofstream of( "test_docker.out" );
  while(doMore)
    {
      i = loops;
      do
	{
	  cout << "Testing Docker container run : " << loops - i + 1 << endl;
	  of << loops -i << endl;
	  sleep(1);
	}
      while( --i );
      char y('y');
      cout << "Again? (y/n)"; cin >> y;
      doMore = ('y' == y );
    }

  return i;
}
