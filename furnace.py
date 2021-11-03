# coding=utf-8
def furnace(itemList):
    json = """{
            "format_version": "1.12",
            "minecraft:recipe_furnace": {
                "description": {
                    "identifier": "%s"
                },
                "input": {
                    "item": "%s",
                    "data": %s,
                    "count": %s
                },
                "output": {
                    "item": "%s",
                    "count": %s,
                    "data": %s
                },
                "tags": [
                    %s
                    "furnace"
                ]
            }
        }"""
    for item in itemList:
        try:
            if "furnace" in item:
                furnaceItem = item["furnace"]

                furnaceItem["input"]["id"] = furnaceItem["input"]["输入物品id"]
                del furnaceItem["input"]["输入物品id"]

                furnaceItem["input"]["data"] = furnaceItem["input"]["输入物品特殊值"]
                del furnaceItem["input"]["输入物品特殊值"]

                furnaceItem["input"]["count"] = furnaceItem["input"]["输入物品个数"]
                del furnaceItem["input"]["输入物品个数"]

                if "output" in furnaceItem:
                    if "输出物品特殊值" in furnaceItem["output"]:
                        furnaceItem["output"]["data"] = furnaceItem["output"]["输出物品特殊值"]
                        del furnaceItem["output"]["输出物品特殊值"]
                    else:
                        furnaceItem["output"]["data"] = 0

                    furnaceItem["output"]["count"] = furnaceItem["output"]["输出物品个数"]
                    del furnaceItem["output"]["输出物品个数"]
                else:
                    furnaceItem["output"] = {}
                    furnaceItem["output"]["data"] = 0
                    furnaceItem["output"]["count"] = 1

                furnaceJson = json % (
                    item["identifier"],
                    "mwh_pam:" + str.lower(furnaceItem["input"]["id"]).replace(" ",
                                                                               "_")
                    ,
                    furnaceItem["input"]["data"],
                    furnaceItem["input"]["count"],
                    item["identifier"],
                    furnaceItem["output"]["count"],
                    furnaceItem["output"]["data"],
                    """ "blast_furnace",""" if "food_" not in item["identifier"] else """ "smoker",
                "campfire","""
                )
                f = open("netease_recipes/" + "furnace_" + item["name"] + ".json", "w")
                f.write(furnaceJson)
                f.close()
        except Exception as exp:
            print exp, "\n", item["identifier"]
