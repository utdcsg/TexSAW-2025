cmake_minimum_required(VERSION 3.10)
set(CMAKE_CXX_STANDARD 17)

project(generator)
add_executable(generator generator.cpp)

target_include_directories(generator PRIVATE "C:/Program Files/OpenSSL-Win64/include")
target_link_directories(generator PRIVATE "C:/Program Files/OpenSSL-Win64/lib/VC/x64/MD")
target_link_libraries(generator openssl libcrypto)