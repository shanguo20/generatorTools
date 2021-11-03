# coding=utf-8
import json
import os
from copy import copy

seed_json = {"format_version": "1.10", "minecraft:item": {"description": {"identifier": "", "register_to_create_menu": True,
                                                                          "category": "Nature"}, "components": {"minecraft:seed": {"crop_result": "", "plant_at": "minecraft:farmland"}}}}
food_json = {"format_version": "1.10",
             "minecraft:item": {"description": {"identifier": "", "register_to_create_menu": True,
                                                "category": "Nature"}, "components": {"minecraft:use_duration": 32, "minecraft:food": {"nutrition": 1, "saturation_modifier": "poor"}}}}
food_seed_json = {
    "format_version": "1.10",
    "minecraft:item": {
        "description": {
            "identifier": "",
            "register_to_create_menu": True,
            "category": "Nature"
        },

        "components": {
            "minecraft:use_duration": 32,

            "minecraft:food": {
                "nutrition": 1,
                "saturation_modifier": "poor"
            },
            "minecraft:seed": {
                "crop_result": "",
                "plant_at": "minecraft:farmland"
            }
        }
    }
}
crop_json2 = {
    "format_version": "1.10.0",
    "minecraft:block": {
        "description": {
            "identifier": "",
            "register_to_creative_menu": False,
            "is_experimental": False,
            "base_block": "custom_crop_block"
        },
        "components": {

            "netease:may_place_on": {
                "block": ["minecraft:farmland"],
                "spawn_resources": True
            },
            "minecraft:block_light_absorption": {
                "value": 0
            },
            "netease:render_layer": {
                "value": "alpha"
            },
            "netease:aabb": {
                "collision": {
                    "min": [
                        0.0,
                        0.0,
                        0.0
                    ],
                    "max": [
                        0.0,
                        0.0,
                        0.0
                    ]
                },
                "clip": {
                    "min": [
                        0.0,
                        0.0,
                        0.0
                    ],
                    "max": []
                }
            },
            "netease:random_tick": {
                "enable": True,
                "tick_to_script": False
            },
            "netease:redstone_property": {
                "value": "break_on_push"
            },
            "minecraft:loot": {
                "table": ""
            },
            "netease:transform": {
                "conditions": {
                    "brightness": {
                        "max": 15,
                        "min": 9
                    },
                    "random_tick_count": {
                        "value": 380
                    },
                    "surrouding": {
                        "value": "minecraft:farmland",
                        "radius": 1
                    }
                },
                "result": ""
            }
        }
    }
}
crop_json = {
    "format_version": "1.10.0",
    "minecraft:block": {
        "description": {
            "identifier": "",
            "register_to_creative_menu": False,
            "is_experimental": False,
            "base_block": "custom_crop_block"
        },
        "components": {
            "netease:may_place_on": {
                "block": ["minecraft:farmland"],
                "spawn_resources": True
            },
            "minecraft:block_light_absorption": {
                "value": 0
            },
            "minecraft:loot": {
                "table": ""
            },
            "netease:render_layer": {
                "value": "alpha"
            },
            "netease:aabb": {
                "collision": {
                    "min": [
                        0.0,
                        0.0,
                        0.0
                    ],
                    "max": [
                        0.0,
                        0.0,
                        0.0
                    ]
                },
                "clip": {
                    "min": [
                        0.0,
                        0.0,
                        0.0
                    ],
                    "max": [
                        1.0,
                        1,
                        1.0
                    ]
                }
            }
        }
    }
}

item_res_json = {
    "format_version": "1.10",
    "minecraft:item": {
        "components": {
            "minecraft:icon": ""
        },
        "description": {
            "identifier": ""
        }
    }
}
itemText = "item.%s.name=%s\n"
blockText = "tile.%s.name=%s\n"
textList = []
blockJson = {
    "format_version": [1, 1, 0]
}

crop_model = {
    "format_version": "1.13.0",
    "netease:block_geometry": {
        "description": {
            "identifier": "",
            "textures": [],
            "item_texture": ""
        },
        "bones": [
            {
                "name": "unknown_bone",
                "pivot": [0, 0, 0],
                "cubes": [
                    {
                        "origin": [-12, 0, 0],
                        "size": [8, 16, 16],
                        "uv": {
                            "east": {"uv": [0, 0], "uv_size": [16, 16]},
                            "west": {"uv": [0, 0], "uv_size": [16, 16]}
                        }
                    },
                    {
                        "origin": [-16, 0, 4],
                        "size": [16, 16, 8],
                        "uv": {
                            "north": {"uv": [0, 0], "uv_size": [16, 16]},
                            "south": {"uv": [0, 0], "uv_size": [16, 16]}
                        }
                    }
                ]
            }
        ]
    }
}

item_texture_json = {
    "resource_pack_name": "vanilla",
    "texture_name": "atlas.items",
    "texture_data": {
    }
}
block_texture_json = {
    "resource_pack_name": "vanilla",
    "texture_name": "atlas.terrain",
    "texture_data": {
    }
}
textureList = []

crop_loot_json = {
    "pools": [
        {
            "entries": [
                {
                    "name": "",
                    "type": "item",
                    "weight": 1
                }
            ],
            "rolls": 1
        }
    ]
}

crop_loot_json2 = {
    "pools": [
        {
            "entries": [
                {
                    "name": "",
                    "type": "item",
                    "weight": 1
                }
            ],
            "rolls": 1
        },
        {
            "entries": [
                {
                    "name": "",
                    "type": "item",
                    "weight": 1
                }
            ],
            "rolls": 1
        }
    ]
}


def create_crop(item):
    item["name"] = str.lower(item["关键词"]).replace(" ", "_").replace("-", "_")
    item["identifier"] = "mwh_pam:" + item["name"]
    if item["是否有种子"]:
        seed = copy(seed_json)
        seed["minecraft:item"]["description"]["identifier"] = item["identifier"] + "seed"
        seed["minecraft:item"]["components"]["minecraft:seed"]["crop_result"] = item["identifier"] + "_stage_0"

        if not os.path.exists("crop/netease_items_beh/"):
            os.makedirs("crop/netease_items_beh/")
        f = open("crop/netease_items_beh/" + item["name"] + "seed.json", "w")
        f.write(json.dumps(seed).replace("'", "\""))
        f.close()

        food = copy(food_json)
        food["minecraft:item"]["description"]["identifier"] = item["identifier"]

        if not os.path.exists("crop/netease_items_beh/"):
            os.makedirs("crop/netease_items_beh/")
        f = open("crop/netease_items_beh/" + item["name"] + ".json", "w")
        f.write(json.dumps(food).replace("'", "\""))
        f.close()

        seeditem_res = copy(item_res_json)
        seeditem_res["minecraft:item"]["components"]["minecraft:use_animation"] = "eat"
        seeditem_res["minecraft:item"]["components"]["minecraft:icon"] = item["identifier"] + "seed"
        seeditem_res["minecraft:item"]["description"]["identifier"] = item["identifier"] + "seed"

        if not os.path.exists("crop/netease_items_res/"):
            os.makedirs("crop/netease_items_res/")
        f = open("crop/netease_items_res/" + item["name"] + "seed.json", "w")
        f.write(json.dumps(seeditem_res).replace("'", "\""))
        f.close()

        fooditem_res = copy(item_res_json)
        fooditem_res["minecraft:item"]["components"]["minecraft:icon"] = item["identifier"]
        fooditem_res["minecraft:item"]["description"]["identifier"] = item["identifier"]

        if not os.path.exists("crop/netease_items_res/"):
            os.makedirs("crop/netease_items_res/")
        f = open("crop/netease_items_res/" + item["name"] + ".json", "w")
        f.write(json.dumps(fooditem_res).replace("'", "\""))
        f.close()

        item_texture_json["texture_data"][item["identifier"]] = {}
        item_texture_json["texture_data"][item["identifier"]]["textures"] = "textures/items/" + item["name"] + "item"

        item_texture_json["texture_data"][item["identifier"] + "seed"] = {}
        item_texture_json["texture_data"][item["identifier"] + "seed"]["textures"] = "textures/items/" + item["name"] + "seeditem"

        textList.append(itemText % (item["identifier"] + "seed", item["中文名"] + "种子"))
        textList.append(itemText % (item["identifier"], item["中文名"]))

    else:
        food_seed = copy(food_seed_json)
        food_seed["minecraft:item"]["description"]["identifier"] = item["identifier"] + "seed"
        food_seed["minecraft:item"]["components"]["minecraft:seed"]["crop_result"] = item["identifier"] + "_stage_0"

        if not os.path.exists("crop/netease_items_beh/"):
            os.makedirs("crop/netease_items_beh/")
        f = open("crop/netease_items_beh/" + item["name"] + "seed.json", "w")
        f.write(json.dumps(food_seed).replace("'", "\""))
        f.close()

        fooditem_res = copy(item_res_json)
        fooditem_res["minecraft:item"]["components"]["minecraft:icon"] = item["identifier"] + "seed"
        fooditem_res["minecraft:item"]["description"]["identifier"] = item["identifier"] + "seed"

        if not os.path.exists("crop/netease_items_res/"):
            os.makedirs("crop/netease_items_res/")
        f = open("crop/netease_items_res/" + item["name"] + "seed.json", "w")
        f.write(json.dumps(fooditem_res).replace("'", "\""))
        f.close()

        item_texture_json["texture_data"][item["identifier"] + "seed"] = {}
        item_texture_json["texture_data"][item["identifier"] + "seed"]["textures"] = "textures/items/" + item["name"] + "seeditem"
        textureList.append("textures/items/" + item["name"] + "seeditem")
        textList.append(itemText % (item["identifier"] + "seed", item["中文名"] + "种子"))

    for i in range(4):
        if i != 3:
            crop = copy(crop_json2)
            crop["minecraft:block"]["description"]["identifier"] = item["identifier"] + "_stage_" + str(i)
            crop["minecraft:block"]["components"]["netease:aabb"]["clip"]["max"] = [1, 1 / 16.0 * ((i + 1) * 4), 1]
            crop["minecraft:block"]["components"]["netease:transform"]["result"] = item["identifier"] + "_stage_" + str(i + 1)
            crop["minecraft:block"]["components"]["minecraft:loot"]["table"] = "loot_tables/crop/" + item["name"] + "_seed.json"
        else:
            crop = copy(crop_json)
            crop["minecraft:block"]["description"]["identifier"] = item["identifier"] + "_stage_" + str(i)
            crop["minecraft:block"]["components"]["minecraft:loot"]["table"] = "loot_tables/crop/" + item["name"] + ".json"

        if not os.path.exists("netease_blocks/"):
            os.makedirs("netease_blocks/")
        f = open("crop/netease_blocks/" + item["name"] + "_stage_" + str(i) + ".json", "w")
        f.write(json.dumps(crop).replace("'", "\n"))
        f.close()

        item_texture_json["texture_data"][item["identifier"] + "_stage_" + str(i)] = {}
        item_texture_json["texture_data"][item["identifier"] + "_stage_" + str(i)]["textures"] = "textures/blocks/" + item["name"] + "_stage_" + str(i + 1)
        textureList.append("textures/blocks/" + item["name"] + "_stage_" + str(i + 1))
        block_texture_json["texture_data"][item["identifier"] + "_stage_" + str(i)] = {}
        block_texture_json["texture_data"][item["identifier"] + "_stage_" + str(i)]["textures"] = "textures/blocks/" + item["name"] + "_stage_" + str(i + 1)
        textList.append(blockText % (item["identifier"] + "_stage_" + str(i + 1), item["中文名"]))

        model = copy(crop_model)
        model["netease:block_geometry"]["description"]["identifier"] = item["identifier"] + "_stage_" + str(i)
        model["netease:block_geometry"]["description"]["textures"] = [item["identifier"] + "_stage_" + str(i)]
        model["netease:block_geometry"]["description"]["item_texture"] = item["identifier"] + "_stage_" + str(i)

        if not os.path.exists("models/netease_block/"):
            os.makedirs("models/netease_block/")
        print item["identifier"] + "_stage_" + str(i) + ".json"
        f = open("crop/models/netease_block/" + item["name"] + "_stage_" + str(i) + ".json", "w")
        f.write(json.dumps(model).replace("'", "\n"))
        f.close()

        blockJson[item["identifier"] + "_stage_" + str(i)] = {
            "netease_model": item["identifier"] + "_stage_" + str(i),
            "sound": "grass"
        }

    loot = copy(crop_loot_json)
    loot["pools"][0]["entries"][0]["name"] = item["identifier"] + "seed"

    loot2 = copy(crop_loot_json2)
    loot2["pools"][0]["entries"][0]["name"] = item["identifier"] + "seed"
    loot2["pools"][1]["entries"][0]["name"] = item["identifier"]

    if not os.path.exists("loot_tables/crop/"):
        os.makedirs("loot_tables/crop/")
    f = open("loot_tables/crop/" + item["name"] + "_seed.json", "w")
    f.write(json.dumps(loot).replace("'", "\""))
    f.close()

    if not os.path.exists("loot_tables/crop/"):
        os.makedirs("loot_tables/crop/")
    f = open("loot_tables/crop/" + item["name"] + ".json", "w")
    f.write(json.dumps(loot2).replace("'", "\""))
    f.close()

    f = open("crop/blocks.json", "w")
    f.write(json.dumps(blockJson).replace("'", "\""))
    f.close()

    if not os.path.exists("crop/texts/"):
        os.makedirs("crop/texts/")
    f = open("crop/texts/zh_CN.lang", "w")
    f.write("".join(textList))
    f.close()

    if not os.path.exists("crop/textures/"):
        os.makedirs("crop/textures/")
    f = open("crop/textures/item_texture.json", "w")
    f.write(json.dumps(item_texture_json).replace("'", "\""))
    f.close()
    if not os.path.exists("crop/textures/"):
        os.makedirs("crop/textures/")
    f = open("crop/textures/terrain_texture.json", "w")
    f.write(json.dumps(block_texture_json).replace("'", "\""))
    f.close()
    if not os.path.exists("crop/textures/"):
        os.makedirs("crop/textures/")
    f = open("crop/textures/textures_list.json", "w")
    f.write(json.dumps(textureList).replace("'", "\""))
    f.close()
