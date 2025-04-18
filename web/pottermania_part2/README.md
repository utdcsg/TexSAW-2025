# pottermania_part2

## Category

Web

## Points

Medium (200 points)

## Authors

Shreya Soman, Zarish Mehboob

## Description

Can you **direct(ory)** Harry to **go** down the right **path** to defeat You-Know-Who?
P.S. You might want to check out pottermaina_part1, it's **key**

## Solution

# Part 1: Finding the JWT token
Users can look at the Request header once they've loaded the challenge page and view the "X-Magic-Token" which contains three fields, spells, data, and location.

# Part 2: Dirbust to find fields
Directory traversal to find two pages : /spells and /date

# Part 3: Put it all together
Use the secret key (SlccjCzySpcxtzyp) to sign the new JWT tokens and brute force to get the flag. Note: users will need to send the session cookie over as well (if they're using curl).

## Flag
texsaw{jWt_ch4LL5_4R3_34sY!}

## To Run
install requirements and run through venv




