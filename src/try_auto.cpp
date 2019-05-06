#include <iostream>
#include <vector>

int main (int argc, char const *argv[])
{

  auto v = {1,2,3,4,5,6,7};
	for(int x:v) std::cout << x+40 << std::endl;
	return 0;
}


