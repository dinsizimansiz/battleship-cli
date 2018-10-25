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

def printHelp():

    print("get playertable")
    print("\tGets your current playertable.")
    print("get enemytable")
    print("\tGets your current enemytable.")
    print("get opponent")
    print("\tGets your opponents moves.")
    print("get status")
    print("\tGets current status.0 offline,1 in queue,2 in match.")
    print("get freeships")
    print("\tGets unplaced ships to board with name.")
    print("get placedships")
    print("\tGets placed ships to board with name.")
    print("get turn")
    print("\tGets whether your turn or not.")
    print("get started")
    print("\tGets whether game you're in started or not.")
    print("makemove <x:int> <y:int>")
    print("\tMakes move to your enemy table.")
    print("placeship <shipname:str> <x:int> <y:int> <direction:str>")
    print("\tPlaced ship to your playertable.")
    print("ready")
    print("\tSets you ready if you placed all ships.")
    print("unready")
    print("\tSets you unready")
    print("removeship <shipname:str>")
    print("\tRemoves ship you want from your playertable.")
    print("enqueue")
    print("\tAdds to you matchmaking queue.")
    print("dequeue")
    print("\tGets you out from matchmaking queue.",end="\n\n")
    print("Shipname   : CellCharacter : ShipSize")
    print("--------     -------------   --------")
    print("carrier    : 11111         : 5")
    print("battleship : 2222          : 4")
    print("submarine  : 333           : 3")
    print("cruiser    : 444           : 3")
    print("destroyer  : 55            : 2",end = "\n\n")
    print("DirectionName : Orientation")
    print("-------------   -----------")
    print("north         : UP")
    print("east          : RIGHT")
    print("south         : DOWN")
    print("west          : LEFT")