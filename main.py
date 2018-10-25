from re import match
from parser import parse
from threading import Thread
from communicate import communicate

ADDRESS = "127.0.0.1"
APP_URL = "http://{}:5050/".format(ADDRESS)

username = None
usernamePattern = r"[A-Za-z0-9]{6,20}"
while True:

    _username = str(input("Enter username : "))
    _match = match(usernamePattern,_username)
    if _match:
        username = _match.group()
        break


while True:

    commandLine = input("<battleship>  ")
    obj = parse(commandLine,urlRoot=APP_URL)
    obj["url"].format(username)
    Thread(target=communicate,args=(obj["method"],obj["url"])).start()
