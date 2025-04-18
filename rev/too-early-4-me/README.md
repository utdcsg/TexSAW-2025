# Too Early 4 Me
Ever since I got back from spring break, the semester's been getting pretty rough. I have an 8am class, and a commute - I'm waking up way too early for me! So, I wrote a program to survey everybody to see how THEY feel when their alarm clock goes off that early. We'll see...

### Downloadable files
 - `chall.out`: The challenge executable

### Build/Setup
 - Run included Makefile. Do not include `flag_encoder.out` in the challenge files. It's only for utility in generating the flag.

### Flag
 - `texsaw{how_signalicious_much_swag}`

# Solution
While the program is blocking for input, run `kill -SIGALRM <PID>` in another terminal. PID can be found with `ps aux | grep chall | grep -v grep | awk '{print $2}'`. The program prints the flag for you when the signal is received.
