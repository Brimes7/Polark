import sys
import json
from flask import Flask, request, abort

URL = 'https://young-robust-angolatitan.glitch.me/olark'

PARAMS =  {
           "email": "test@olark.com",
           "phone": "7038671223",
           "pizza-size": "small",
           "topping": "cheese"
        }
# r = requests.get(url = URL, params = PARAMS)
# That one will only pull from local server not our URL
# r = requests.post(URL, data=json.dumps(PARAMS), headers={"Content-Type": 'application/json'})
# data = r.json()
# print(PARAMS)

def send_pizza_req(email, phone):
    params = {
        "email": email,
        "phone": phone,
        "pizza-size": "small",
        "topping": "cheese"
    }

    r = request.post(URL, data=json.dumps(params), headers={"Content-Type": 'application/json'})
    print(f"SENT PIZZA REQUEST FOR {email}")

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "HELLO"


# Intitiates the listener
@app.route('/', methods=['POST'])
def pizzafun():

    items = request.json["items"]
    visitor = request.json["visitor"]
    for msg in items:
        print(msg)
        body = msg["body"]
        print(body)
        kind = msg["kind"]
        if kind == "MessageToOperator":
            if "pizza" in body:
                send_pizza_req(visitor["emailAddress"], visitor["phoneNumber"])



    return 'PIZZA TIME'
# THIS IS THE LISTENER
@app.route('/custom', methods=['POST'])
def webhook():
    print("\n\nReceived")
    sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return 'NEW WEBHOOK WORKS', 200
    else:
        abort(400)

@app.route('/notny', methods=['POST'])
def notny():
    print("\n\nReceived")
    sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return"CUSTOMER NOT IN NEW YORK AREA"
    else:
        abort(400)

@app.route('/saladlover', methods=['POST'])
def saladlover():
    print("\n\nReceived")
    sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return "CUSTOMER NEVER MENTIONED A PIZZA"
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)
