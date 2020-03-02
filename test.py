import requests
from flask import request
from flask import Flask


app = Flask(__name__)





def get_info(ip_address):
    try:
        api_request = "http://api.ipstack.com/"+ip_address+"?access_key=bd8c2772145066d381339aee65bbdeb4"
        resp = requests.get(api_request)
        data = resp.json()
        return data
    except Exception as e:
        return e


@app.route("/")
def home():
    ip_address = request.remote_addr
    location = get_info(ip_address)
    print (location)
    return "Hello World"

if __name__ == "__main__":
    app.run()