#include <iostream>
#include <string>
#include <exception>
#include "gtest/gtest.h"

namespace my_test_utils
{
	void printMessage(std::string msg)
	{	
		std::cout << msg << std::endl;
	};
	
	void throwException( std::exception& e)
	{
		throw e;
	}
};