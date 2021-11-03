def crossbow_data(itemList):
    bow_data = {}
    Json = "crossbow_data = %s"
    for item in itemList:
        if item["type"] == "crossbow":
            bow_data[item["identifier"]] = {"use_duration": item["use_duration"],
                                            "attack_damage": item["attack_damage"]}

    f = open("crossbow_datas.py", "w")
    f.write(Json % bow_data)
    f.close()
