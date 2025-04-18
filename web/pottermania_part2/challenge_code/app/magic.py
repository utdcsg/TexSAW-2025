from flask import Flask, render_template, request, make_response, session, jsonify, render_template_string
import jwt
from datetime import datetime, timedelta, timezone
import random
import redis
import os
from flask_session import Session


app = Flask(__name__)

my_spells=["Expelliarmus", "Stupefy", "Protego", "Protego Maxima", "Petrificus Totalus",  
 "Reducto", "Confringo", "Bombarda", "Diffindo", "Impedimenta", "Rictusempra",  
 "Levicorpus", "Incarcerous", "Relashio", "Oppugno", "Finite Incantatem",  
 "Lumos Maxima", "Homenum Revelio", "Salvio Hexia", "Cave Inimicum", "Muffliato",  
 "Glisseo", "Everte Statum", "Expecto Patronum", "Langlock"]

secret_key="SlccjCzySpcxtzyp"

app.config['SESSION_TYPE'] = 'redis'
app.config['SECRET_KEY'] = 'appsecretkey'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
#password = 'texsaw{sO459@}'
redis_password = os.getenv("REDIS_PASS")
#app.config['SESSION_REDIS'] = redis.from_url(f'redis://:{redis_password}@127.0.0.1:6379')
app.config['SESSION_REDIS'] = redis.from_url(f'redis://:{redis_password}@pottermaina_part2_redis:6379')
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = False  # Only works with HTTPS
#TODO: set password for redis cache

app.config.from_object(__name__)  # <-- added
Session(app)

redis_client = redis.StrictRedis(host='pottermaina_part2_redis', port=6379, db=0, password=redis_password, decode_responses=True)

def generate_token(spell, date):
	claims = {'date': date,
			  'spell': spell,
			  'loc': 'battle of hogwarts'}
	return jwt.encode(claims, secret_key, algorithm='HS256')	

@app.route('/', methods=['GET'])
def home():
    #random.choice(my_spells)
	new_token = generate_token(my_spells[3], datetime.now(timezone.utc).isoformat())
    # Store the token in an HTTP-only cookie
	session['message_to_user'] = "Welcome to the battle of the century!"
	#generate session_id, set the flag in one place please
	#session_id= str(random.randint(100000, 999999))
	#tok = generate_token(random.choice(my_spells),'1998-05-02T09:45:00.000000+00:00')
	#redis_client.setex(session_id, timedelta(hours=2),tok )
	#print('set FLAG:',new_token)

	
	flask_resp = make_response(render_template_string(f"""
    <script>												   							   
        fetch('/magic', {{
            method: 'GET',
			credentials: "include",
            headers: {{
                'X-Magic-Token': '{new_token}'
            }}
        }})
        .then(response => response.text())
        .then(data => {{
            document.write(data);  // Render the response
        }});
    </script>
    """))
	#flask_resp.set_cookie('session_id', session_id, samesite='Lax', httponly=False)
	
	return flask_resp

@app.route('/magic', methods=['GET'])
def magic():
	#they would need to find a list of spells first to even get a token
	session_id = request.cookies.get('session')
	#session_id = request.cookies.get('session_id')
	if not session_id: return make_response(jsonify({"error":"session is nonetype"}),400)
	test_token = request.headers.get('X-Magic-Token')
	if not test_token: return make_response(jsonify({"error":"Invalid Request"}),400)

	magic_token = redis_client.get(session_id)
	if not magic_token: #regenerate token
		#print("CATCH")
		tok = generate_token(random.choice(my_spells),'1998-05-02T09:45:00.000000+00:00')
		redis_client.setex(session_id, timedelta(hours=2),tok)
		#print('set FLAG to:',tok)	
	#print("FLAG: ",magic_token)
	# Extract specific fields
	message_to_user = "© 2025 TexSAW. All rights reserved."
	cloud_image = "new_background_1.jpg"
	if test_token == magic_token:
			message_to_user = "yay you did it! here's the flag: texsaw{jWt_ch4LL5_4R3_34sY!}"
			cloud_image = "background_2.jpg"

	session['message_to_user'] = message_to_user
	resp = make_response(render_template('magic.html', cloud_image=cloud_image))
	return resp
	
@app.route('/spells')
def spells():
	return render_template('spells.html')

@app.route('/date')
def date():
	return render_template('date.html')

# Catch-all route for anything else
@app.route('/<path:invalid_path>')
def catch_all(invalid_path):
    # Option 1: Render a custom error page
    return make_response(jsonify({"error":"Invalid Request"}),400)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=1337, debug=True)
