# Deleted Evidence

## Category
Forensics - Medium-Hard

## Description
Someone used this computer to generate the flag, but it has since been deleted. We weren’t able to image the computer, but we did acquire this memory dump and this executable.  
(Note: Find the last flag generated, from the last seed created, and append the timestamp for the creation of the last seed in YYYY-MM-DD_Hr:Min:Sec.  
Ex. texsaw{0fffabcd01234567_2025-04-01_08:00:00})  

Memory File: https://drive.google.com/file/d/12R4lO-t0PdEsH7zFL8X6HVeNjehrbMAg/view?usp=sharing  

## Solution
The user is expected to use Volatility 2 for memory analysis. There are a suspicious number of Notepad.exe processes running. The user can find out that generator.exe was run recently through cmdline/userassist, and is expected to look at MFT timestamps to find that the last created seed file was seed_89.txt. The user can dump the memory of the latest Notepad.exe instance (corresponding with this seed) and find the seed as a string. Then, the user creates a .txt file with this seed, inputs it to generator.exe, and receives the flag.

## Flag
texsaw{0f59ede3e09e5a4d18b480be9e56f3c2aa1ed0b67287f0bc60ca0b2bce62ac28_2025-03-26_02:08:23}

## Downloadable
evidence.tar (on Google Drive)
generator.tar

## Building Binaries
Shouldn't need to build any binaries (generator.exe) because challenge is self-contained in memory dump and executable. Running the executable requires having Visual Studio 2022 and Visual C++ Redistributable installed.  

Building generator requires Visual Studio 2022, CMake, and the OpenSSL library.  
- Download Visual C++ Redistributable  
- Download Visual Studio 2022  
- Install OpenSSL using a supported package manager on Windows (I used Chocolatey https://community.chocolatey.org/packages/openssl)  
- Place CMakeLists and generator.cpp in the same directory (/generator)  
- Create a "Build" directory and cd into it (/generator/Build)  
- Run "cmake .."  
- Run "cmake --build ."  
- The "generator.exe" executable should be in (/generator/Build/Debug)  

