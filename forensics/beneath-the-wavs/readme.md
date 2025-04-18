# Hidden beneath the wavs

Author: Timothy Sweet

## Category
Forensics (moderate)

## Description
We've found the burglary suspect's voice notes. But oh no! One of them has been zipped up with a password. After throwing hashcat at it for a whole week, it's clear he covered his tracks by using a super secure password. But this format was made long before Bernstein freed us all... so perhaps you can find a back way in?

## Flag
```
texsaw{Th3_s1l3nce_SH4ll_l3ad_TH3_W4y}
```
## Downloadable
secret.zip

## Solution
1. `bkcrack -L secret_note.zip`: Note that it is "ZipCrypto (store)
1. `bkcrack -C secret_note.zip -c aaaac.wav -p /dev/zero -o 0x70 -t 32` execute the known-plaintext attack with the known plantext of zeros (conveniently sourced from /dev/zero) with offset into the wav file of 0x70 and 32 bytes of them (minimum 12 needed for attack, but it's faster with more). This provides us the pkzip master key of `3ec5bc1b c7a05f7b 9d70bba5`
1. `bkcrack -C secret_note.zip -c aaaac.wav -d testout.wav -k 3ec5bc1b c7a05f7b 9d70bba5` decrypt and write out the wav file
1. `ffprobe testout.wav` or `mediainfo testout.wav` - use any media program (cli or gui) that can read tags to view the flag in the comment field


## Instructions for generation
1. `echo "who needs lockpicks when the window is already broken" | espeak-ng --stdout | ffmpeg -f wav -i pipe: -ar 32880 -fflags +bitexact -metadata COMMENT="texsaw{Th3_s1l3nce_SH4ll_l3ad_TH3_W4y}" -y aaaac.wav`
1. `zip -Z store -e -P "$(dd if=/dev/urandom bs=64 count=1 2>/dev/null | base64 -w0)" secret_note.zip aaaac.wav`

## Rationale
The flag is embedded in the wav metadata. The wav is stripped of all metadata except the flag. It is resampled to an unusual sample rate to make the challenge harder by having a less typical header. The intended solution is to take advantage of the file having many contiguous null bytes after the header (as most uncompressed audio files beginning with a tiny bit of silence would). The password is not bruteforceable; instead, the known-plaintext vulnerability in the extremely weak stream cipher of PKZIP encryption is intended to be exploited, such as via the `bkcrack` utility.

## Author
SuperMarioFan