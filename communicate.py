import requests
from termcolor import colored

def communicate(method,url):

    resp = requests.request(method,url)
    _json = resp.json()
    if _json.get("err",None) is not None:
        print(colored(str(_json["err"]),"red"))

    if _json.get("payload",None) is not None:
        print(colored(str(_json["payload"]),"cyan"))

    if _json.get("success",None) is not None:
        print(colored(str(_json["success"]),"yellow"))