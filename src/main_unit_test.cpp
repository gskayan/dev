#include "main_unit_test.h"

using namespace std;


TEST (Practice, TestGtest)
{
	bool success(true);
	ASSERT_TRUE(success);
};

int main(int argc, char* argv[])
{
	my_test_utils::printMessage("Hello World");
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
};
