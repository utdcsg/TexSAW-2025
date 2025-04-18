# Scrambled Packets

## Category
Forensics (Easy)

## Description
I accidentally broke my message and it got all mixed up with everything else. Can you help me get it back? 
Flag format: TexSAW{example_flag}

## Solution
There’s a bunch of scrambled packets that should all be ignored other than the ICMP packets. There’s some decoy ICMP packets with junk data that should also all be ignored. They can identify some packets that only contain one byte of data, being a character of the flag. Filtering for those packets lets you reconstruct the flag according to the ICMP sequence numbers. 

## Flag
TexSAW{thanks_for_fixing_it}

## Downloadable
cap.pcap

