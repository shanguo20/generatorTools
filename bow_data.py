def bow_data(itemList):
    bow_data = {}
    Json = "bow_data = %s"
    for item in itemList:
        if item["type"] == "bow":
            bow_data[item["identifier"]] = {"use_duration": item["use_duration"],
                                            "attack_damage": item["attack_damage"]}

    f = open("bow_datas.py", "w")
    f.write(Json % bow_data)
    f.close()
