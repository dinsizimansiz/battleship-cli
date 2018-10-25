import requests
from termcolor import colored
from time import sleep


def communicate(method:str,url:str) -> None:

    resp = requests.request(method,url)
    try :
        _json = resp.json()
        if _json.get("err",None) is not None:
            print(colored(str(_json["err"]),"red"),flush=True)

        if _json.get("payload",None) is not None:
            print(colored(str(_json["payload"]),"cyan"),flush=True)

        if _json.get("success",None) is not None:
            print(colored(str(_json["success"]),"yellow"),flush=True)
    except Exception:
        # In undefined request express sends an html. That causes an error.
        print("CANNOT {} {}".format(method.upper(),url))

def statusPoll(username, urlRoot="http://127.0.0.1:5050/", sleepTime = 0.25) :

    resp = requests.get("{}status?username={}".format(urlRoot,username))
    status = resp.json().get("payload",0)

    def _poll(status):
        sleep(sleepTime)
        resp = requests.get("{}status?username={}".format(urlRoot, username))
        newStatus = resp.json().get("payload", None)

        if status == 2 and newStatus == 0:
            print(colored("Game ended.", "yellow"), flush=True)
        elif status == 1 and newStatus == 2:
            print(colored("Game started.", "yellow"), flush=True)

        status = newStatus
        return status

    try:

        while True:
            status = _poll(status)

    except Exception:
        pass
    finally:

        while True:
            status = _poll(status)

def turnPoll(username, urlRoot="http://127.0.0.1:5050/", sleepTime = 0.25):

    resp = requests.get("{}isturn?username={}".format(urlRoot,username))
    isTurn = resp.json().get("payload",False)

    def _poll(isTurn):
        sleep(sleepTime)
        resp = requests.get("{}isturn?username={}".format(urlRoot, username))
        updatedTurn = resp.json().get("payload", None)

        if not isTurn and updatedTurn:
            print(colored("Your turn", "turqoise"), flush=True)

        isTurn = updatedTurn
        return isTurn

    try:
        while True:
            isTurn = _poll(isTurn)

    except Exception:
        pass
    finally:

        while True:
            isTurn = _poll(isTurn)

def gameStartedPoll(username, urlRoot="http://127.0.0.1:5050/", sleepTime = 0.25):

    resp = requests.get("{}isturn?username={}".format(urlRoot, username))
    gameStarted = resp.json().get("payload", False)

    def _poll(gameStarted):
        sleep(sleepTime)
        resp = requests.get("{}isturn?username={}".format(urlRoot, username))
        updatedGameStarted = resp.json().get("payload", None)

        if not gameStarted and updatedGameStarted:
            print(colored("All ships are set . Now you can make moves.", "turqoise"), flush=True)

        gameStarted = updatedGameStarted
        return gameStarted


    try:
        while True :
            gameStarted = _poll(gameStarted)
    except Exception:
        pass
    finally :

        while True:

            gameStarted = _poll(gameStarted)
