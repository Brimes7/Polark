import sys
import json
import requests
from flask import Flask, request, abort
#URL
URL = 'https://young-robust-angolatitan.glitch.me/olark'
#dummy data
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

    r = requests.post(URL, data=json.dumps(params), headers={"Content-Type": 'application/json'})
    print(f"SENT PIZZA REQUEST FOR {email}")

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "HELLO NEW YORK CITY!"

#Checks the body
#Cannot get pizza function to run proper
def check_msg_body(body):
    # for z in range(len(body)):
    #     body[z] = body[z].lower()
    return "pizza" in body.lower()

#Checks the kind
def check_msg_kind(kind):
    return kind == "MessageToOperator"

def pizza_lover():
    print("\n\nReceived")
    sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return "CUSTOMER DID MENTION A PIZZA"
    else:
        abort(400)

def salad_lover():
    print("\n\nReceived")
    sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return "CUSTOMER DID NOT MENTION A PIZZA"
    else:
        abort(400)
#Checks the main messages
def check_main_msgs(msgs, emailAddress, phoneNumber):
    for msg in msgs:

        body = msg["body"]
        kind = msg["kind"]
        #Why is this not reading skips and goes to else
        if check_msg_kind(kind) and check_msg_body(body):
            print("Pizza mentioned")
            send_pizza_req(emailAddress, phoneNumber)
        else:
            print("Customer May live in NY but did not mention Pizza")
            return salad_lover()

        return pizza_lover()


#Check if even in NY
def check_ny(city):
    return "new york" in city.lower()


def notny():
    print("\n\nReceived")
    sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return"CUSTOMER NOT IN NEW YORK AREA. INELLIGBLE FOR PIZZA ROLLOUT."
    else:
        abort(400)


# Intitiates the listener
@app.route('/', methods=['POST'])
def pizzafun():

    items = request.json["items"]
    visitor = request.json["visitor"]
    city = visitor["city"]


    #implementing objects to call them
    # if check_ny(city) and items == check_msg_body:
    if check_ny(city):
        check_main_msgs(items, visitor["emailAddress"], visitor["phoneNumber"])
    else:
        return notny()

    return check_main_msgs(items, visitor["emailAddress"], visitor["phoneNumber"])

if __name__ == '__main__':
    app.run(debug=True)
