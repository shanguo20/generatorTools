def attack_speed(itemList):
    speed = {}
    Json = "sword_speed = %s"
    for item in itemList:
        if item["type"] == "sword":
            speed[item["identifier"]] = item["attack_speed"]

    f = open("attack_speeds.py", "w")
    f.write(Json % speed)
    f.close()
