# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.4

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CMake.app/Contents/bin/cmake

# The command to remove a file.
RM = /Applications/CMake.app/Contents/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/familycomputer/dev/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/familycomputer/dev

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake cache editor..."
	/Applications/CMake.app/Contents/bin/cmake-gui -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/Applications/CMake.app/Contents/bin/cmake -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /Users/familycomputer/dev/CMakeFiles /Users/familycomputer/dev/CMakeFiles/progress.marks
	$(MAKE) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /Users/familycomputer/dev/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named testcode

# Build rule for target.
testcode: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 testcode
.PHONY : testcode

# fast build rule for target.
testcode/fast:
	$(MAKE) -f CMakeFiles/testcode.dir/build.make CMakeFiles/testcode.dir/build
.PHONY : testcode/fast

#=============================================================================
# Target rules for targets named testx

# Build rule for target.
testx: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 testx
.PHONY : testx

# fast build rule for target.
testx/fast:
	$(MAKE) -f CMakeFiles/testx.dir/build.make CMakeFiles/testx.dir/build
.PHONY : testx/fast

main_unit_test.o: main_unit_test.cpp.o

.PHONY : main_unit_test.o

# target to build an object file
main_unit_test.cpp.o:
	$(MAKE) -f CMakeFiles/testcode.dir/build.make CMakeFiles/testcode.dir/main_unit_test.cpp.o
.PHONY : main_unit_test.cpp.o

main_unit_test.i: main_unit_test.cpp.i

.PHONY : main_unit_test.i

# target to preprocess a source file
main_unit_test.cpp.i:
	$(MAKE) -f CMakeFiles/testcode.dir/build.make CMakeFiles/testcode.dir/main_unit_test.cpp.i
.PHONY : main_unit_test.cpp.i

main_unit_test.s: main_unit_test.cpp.s

.PHONY : main_unit_test.s

# target to generate assembly for a file
main_unit_test.cpp.s:
	$(MAKE) -f CMakeFiles/testcode.dir/build.make CMakeFiles/testcode.dir/main_unit_test.cpp.s
.PHONY : main_unit_test.cpp.s

try_auto.o: try_auto.cpp.o

.PHONY : try_auto.o

# target to build an object file
try_auto.cpp.o:
	$(MAKE) -f CMakeFiles/testx.dir/build.make CMakeFiles/testx.dir/try_auto.cpp.o
.PHONY : try_auto.cpp.o

try_auto.i: try_auto.cpp.i

.PHONY : try_auto.i

# target to preprocess a source file
try_auto.cpp.i:
	$(MAKE) -f CMakeFiles/testx.dir/build.make CMakeFiles/testx.dir/try_auto.cpp.i
.PHONY : try_auto.cpp.i

try_auto.s: try_auto.cpp.s

.PHONY : try_auto.s

# target to generate assembly for a file
try_auto.cpp.s:
	$(MAKE) -f CMakeFiles/testx.dir/build.make CMakeFiles/testx.dir/try_auto.cpp.s
.PHONY : try_auto.cpp.s

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... testcode"
	@echo "... edit_cache"
	@echo "... rebuild_cache"
	@echo "... testx"
	@echo "... main_unit_test.o"
	@echo "... main_unit_test.i"
	@echo "... main_unit_test.s"
	@echo "... try_auto.o"
	@echo "... try_auto.i"
	@echo "... try_auto.s"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system

