import sys
import requests
import json
from flask import Flask, request, abort

URL = 'https://young-robust-angolatitan.glitch.me/olark'

PARAMS =  {
           "email": "test@olark.com",
           "phone": "7038671223",
           "pizza-size": "small",
           "topping": "cheese"
        }
r = requests.get(url = URL, params = PARAMS)
# That one will only pull from local server not our URL
# r = requests.post(polark_url, data=json.dumps(data ), headers={"Content-Type": 'application/json'})
data = r.json()
print(PARAMS)


nypizza = Flask(__name__)
# Intitiates the listener
@nypizza.route('/', methods=['POST'])
def pizzafun():
    return 'PIZZA TIME'

# THIS IS THE LISTENER
@nypizza.route('/custom', methods=['POST'])
def webhook():
    print("\n\nReceived")
    sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return 'NEW WEBHOOK WORKS', 200
    else:
        abort(400)

@nypizza.route('/notny', methods=['POST'])
def notny():
    print("\n\nReceived")
    sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return"CUSTOMER NOT IN NEW YORK AREA"
    else:
        abort(400)

@nypizza.route('/saladlover', methods=['POST'])
def saladlover():
    print("\n\nReceived")
    sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return "CUSTOMER NEVER MENTIONED A PIZZA"
    else:
        abort(400)

if __name__ == '__main__':
    nypizza.run(debug=True)
