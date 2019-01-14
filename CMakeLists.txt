cmake_minimum_required(VERSION 2.6)

project(main CXX)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

set(SOURCES_LIST "./A/main.cpp")


add_executable(main ${SOURCES_LIST}) 

add_custom_target(generating
	WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/B"
	COMMAND python3 ./gen.py)

add_dependencies(main generating)

target_include_directories(main PUBLIC "./")
