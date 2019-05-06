#include <iostream>
#include <thread>
#include <typeinfo>
#include <chrono>

int main( int argc, char* argv[])
{
  using namespace std;

  thread t ([](){
      int i=5; 
      while(i--) {
	cout << "iter#="<<i<<" " << flush;
	this_thread::sleep_for(chrono::seconds(1));
      } 
      cout << endl;
    });

  t.join();
};


