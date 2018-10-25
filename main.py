from re import match
from parser import parse,BadCommand,printHelp
from threading import Thread
from communicate import communicate,statusPoll,turnPoll,gameStartedPoll

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

Thread(target=statusPoll, args=(username, APP_URL), kwargs={"sleepTime":0.75}).start()
Thread(target=turnPoll, args=(username, APP_URL), kwargs={"sleepTime":0.75}).start()
Thread(target=gameStartedPoll, args=(username, APP_URL), kwargs={"sleepTime":0.75}).start()

print(" --- WELCOME TO BATTLESHIP ---")

while True:

    commandLine = input()
    if commandLine == "help":
        printHelp()
        continue
    try:
        obj = parse(commandLine,urlRoot=APP_URL)
        obj["url"] += username
        Thread(target=communicate,args=(obj["method"],obj["url"])).start()
    except BadCommand as err:
        print("Bad Command : {}".format(err))

