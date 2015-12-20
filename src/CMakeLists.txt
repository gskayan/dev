cmake_minimum_required(VERSION 2.6)

project(Practice)

include_directories("../include"
						"../googletest/googletest/include")

link_directories("./gtestbuild")

add_executable(testcode main_unit_test.cpp)

target_link_libraries(testcode "gtest")
