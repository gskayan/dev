#include "main_unit_test.h"

using namespace std;

TEST (Practice, TestGtest)
{
	bool success(true);
	ASSERT_TRUE(success);
};
TEST(Practice, PrintMessage_DoesNotThrow)
{
	EXPECT_NO_THROW(my_test_utils::printMessage("printMessage No Exception"));
}
TEST(Practice, ThrowException)
{
	std::exception e;
	std::runtime_error rte("I am std::runtime_error");
	ASSERT_THROW(my_test_utils::throwException(e), std::exception);
	ASSERT_THROW(my_test_utils::throwException(rte), std::exception);
	ASSERT_THROW(my_test_utils::throwException(rte), std::runtime_error);
}

int main(int argc, char* argv[])
{
	my_test_utils::printMessage("Hello This World");
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
};
