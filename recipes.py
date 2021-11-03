# coding=utf-8
import json
import os


def recipes(itemList):
    for item in itemList:

        if "recipes" in item and item["type"] != "fruitTree":
            recipesList = item["recipes"]
            for recipesIndex, recipes in enumerate(recipesList):
                recipesJson = {
                    "format_version": "1.12",
                    "minecraft:recipe_shaped": {
                        "description": {
                            "identifier": ""
                        },
                        "key": {},
                        "pattern": [],
                        "result": [],
                        "tags": [
                            "crafting_table"
                        ]
                    }
                }

                if "合成输出个数" in recipes:
                    recipes["count"] = recipes["合成输出个数"]
                else:
                    recipes["count"] = 1

                if "key" in recipes:
                    for k in recipes["key"]:
                        if "minecraft:" not in recipes["key"][k]["id"]:
                            recipes["key"][k]["item"] = "mwh_pam:" + str.lower(recipes["key"][k]["id"]).replace(" ", "_")
                            del recipes["key"][k]["id"]
                        else:
                            recipes["key"][k]["item"] = recipes["key"][k]["id"]
                            del recipes["key"][k]["id"]
                    if "返回物品" in recipes and recipes["返回物品"] != "":
                        if type(recipes["返回物品"]) == str:
                            recipesJson["minecraft:recipe_shaped"]["result"] = [
                                {
                                    "item": item["identifier"],
                                    "count": recipes["count"]
                                },
                                {
                                    "item": "mwh_pam:" + recipes["返回物品"],
                                    "count": 1
                                }
                            ]
                        elif type(recipes["返回物品"]) == list:
                            recipesJson["minecraft:recipe_shaped"]["result"] = [
                                {"item": item["identifier"], "count": recipes["count"]}
                            ]
                            for resultIndex in range(len(recipes["返回物品"])):
                                recipesJson["minecraft:recipe_shaped"]["result"].append({"item": "mwh_pam:" + recipes["返回物品"][resultIndex], "count": 1})
                    else:
                        recipesJson["minecraft:recipe_shaped"]["result"] = {"item": item["identifier"], "count": 1}
                    recipesJson["minecraft:recipe_shaped"]["description"]["identifier"] = item["identifier"] + "_" + str(recipesIndex)
                    recipesJson["minecraft:recipe_shaped"]["key"] = recipes["key"]
                    recipesJson["minecraft:recipe_shaped"]["pattern"] = recipes["pattern"]

                    if not os.path.exists("netease_recipes"):
                        os.makedirs("netease_recipes")
                    f = open("netease_recipes/" + "recipes_" + item["name"] + "_" + str(recipesIndex) + ".json", "w")
                    f.write(json.dumps(recipesJson).replace("\'", "\""))
                    f.close()
