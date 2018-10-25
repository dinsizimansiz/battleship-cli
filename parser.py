def parse(line,urlRoot = "localhost:5050/"):
    try:
        objProperties = {"url" : urlRoot}
        words = line.split()
        if words[0] == "get":
            objProperties["method"] = "get"

            if words[1] == "playertable":
                objProperties["url"] += "playertable?username="
            elif words[1] == "enemytable":
                objProperties["url"] += "enemytable?username="
            elif words[1] == "status":
                objProperties["url"] += "status?username="
            elif words[1] == "freeships":
                objProperties["url"] += "freeships?username="
            elif words[1] == "placedships":
                objProperties["url"] += "placedships?username="
            elif words[1] == "enemytable":
                objProperties["url"] += "playertable?username="
            elif words[1] == "opponent":
                objProperties["url"] += "opponentguesses?username="
            elif words[1] == "turn":
                objProperties["url"] += "isturn?username="
            elif words[1] == "started":
                objProperties["url"] += "started?username="

        else:
            objProperties["method"] = "post"
            if words[0] == "makemove":
                objProperties["url"] += "makemove?x={}&y={}&username=".format(words[1],words[2])
            elif words[0] == "placeship":
                objProperties["url"] += "placeship?shipname={}&x={}&y={}&direction={}&username=".\
                    format(words[1],words[2],words[3],words[4])
            elif words[0] == "ready":
                objProperties["url"] += "ready?username="
            elif words[0] == "unready":
                objProperties["url"] += "unready?username="
            elif words[0] == "removeship":
                objProperties["url"] += "removeship?shipname={}&username=".format(words[1])
            elif words[0] == "enqueue":
                objProperties["url"] += "enqueue?username="
            elif words[0] == "dequeue":
                objProperties["url"] += "dequeue?username="

        return objProperties

    except IndexError:

        raise BadCommand(line)

class BadCommand(Exception):
    pass