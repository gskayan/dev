cmake_minimum_required(VERSION 2.6)

project(Practice)

include_directories("../include")

link_directories("./lib/gtest" "./lib/gmock")

add_executable(testcode main_unit_test.cpp)

target_link_libraries(testcode "gtest")
