# String Symphony

## Category
Forensics - Medium

## Description
Look through this symphonic ensemble for the flag and let the music string you along.   
(Note: You will find 10 parts of the flag. Encase the flag in texsaw{} and put an underscore between each part.  
Ex. texsaw{p0_p1_p2_p3_p4_p5_p6_p7_p8_p9})  

https://drive.google.com/file/d/1KNLyub1cHwR6TJ2O_5FftQXEE18RdDdJ/view?usp=sharing  

## Solution
The user is expected to use Volatility 2 for memory analysis. There are multiple processes running (violin1.exe, violin2.exe, viola.exe, cello.exe), each of which contain base64-encoded strings with the name of a Registry key/subkey and a series of notes. The user is expected to find these processes using pslist/pstree and get the strings using the strings tool. The note strings from each process can be stacked to create a series of 10 4-note chords. These 4-char strings indicate the location of 10 flag parts within the indicated Registry subkey, which can be pieced together to get the flag.

## Flag
texsaw{I_I6_IV_V_vi_ii6_I64_V_V7_I}

## Downloadable
symphony.tar (on Google Drive)

## Building Binaries
Run gcc/clang on the provided .c files on Windows.