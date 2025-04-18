from flask import Flask, request, make_response, send_from_directory, Response
import os
import jwt

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/")
def root():
    return send_from_directory('static', 'index.html')

@app.delete("/")
@app.delete("/<path:path>")
def delete_endpoint(path=None):
    return "Why would you delete my website :( here's a sad flag texsaw{why_d0_i_del3t3ed}"

if __name__ == "__main__":
    app.run(debug=True)