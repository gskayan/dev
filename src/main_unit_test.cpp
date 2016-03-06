#include "main_unit_test.h"
#include <thread>

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
	ASSERT_THROW(my_test_utils::throwRTException(rte), std::runtime_error) << "This test expected to fail a test message";
}

int main(int argc, char* argv[])
{
	std::thread t1(my_test_utils::printMessage, "This is message from thread");
	my_test_utils::printMessage("Hello This World");
	::testing::InitGoogleTest(&argc, argv);
	t1.join();
	return RUN_ALL_TESTS();
};
