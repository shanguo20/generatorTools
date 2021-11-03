# coding=utf-8
import json
import os
from copy import copy

treeType = {
    "橡树": "minecraft:oak_tree_feature",
    "云杉树": "minecraft:spruce_tree_feature",
    "白桦树": "minecraft:birch_tree_feature",
    "金合欢树": "minecraft:savanna_tree_feature",
    "丛林树": "minecraft:jungle_tree_feature",
    "深色橡树": "minecraft:roofed_tree_feature",
}
fruitTreeJson = {
    "format_version": "1.14.0",
    "minecraft:aggregate_feature": {
        "description": {
            "identifier": ""
        },
        "early_out": "first_failure",
        "features": [
            "",
            ""
        ]
    }
}
fruitBlockJson = {
    "format_version": "1.14.0",
    "minecraft:single_block_feature": {
        "description": {
            "identifier": ""
        },
        "places_block": {
            "name": ""
        },
        "enforce_survivability_rules": True,
        "enforce_placement_rules": True,
        "may_attach_to": {
            "auto_rotate": False,
            "min_sides_must_attach": 2,
            "top": [
                {
                    "name": "minecraft:leaves",
                    "states": {
                        "old_leaf_type": "oak"
                    }
                },
                {
                    "name": "minecraft:leaves",
                    "states": {
                        "old_leaf_type": "birch"
                    }
                },
                {
                    "name": "minecraft:leaves2",
                    "states": {
                        "new_leaf_type": "dark_oak"
                    }
                },
                {
                    "name": "minecraft:leaves",
                    "states": {
                        "old_leaf_type": "jungle"
                    }
                },
                {
                    "name": "minecraft:leaves2",
                    "states": {
                        "new_leaf_type": "acacia"
                    }
                },
                {
                    "name": "minecraft:leaves",
                    "states": {
                        "old_leaf_type": "spruce"
                    }
                }
            ]
        }
    }
}
scatterFruitBlockJson = {
    "format_version": "1.14.0",
    "minecraft:scatter_feature": {
        "description": {
            "identifier": ""
        },
        "iterations": 5,
        "places_feature": "",
        "x": {
            "distribution": "uniform",
            "extent": [
                -2,
                2
            ]
        },
        "y": 0,
        "z": {
            "distribution": "uniform",
            "extent": [
                -2,
                2
            ]
        },
        "project_input_to_floor": False
    }
}
searchFruitBlockJson = {
    "format_version": "1.14.0",
    "minecraft:search_feature": {
        "description": {
            "identifier": ""
        },
        "places_feature": "",
        "search_volume": {
            "min": [0, 0, 0],
            "max": [0, 6, 0]
        },
        "search_axis": "+y",
        "required_successes": 1
    }
}
tree_biome = {
    "橡树": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "forest"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "mutated"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "birch"
        }
    ],
    "云杉树": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "forest"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "mutated"
        },
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "taiga"
        }
    ],
    "白桦树": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "forest"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "mutated"
        },
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "birch"
        }
    ],
    "金合欢树": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "savanna"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "mutated"
        }
    ],
    "丛林树": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "jungle"
        }
    ],
    "深色橡树": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "roofed"
        }
    ]
}
ruleJson = {
    "format_version": "1.13.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "",
            "places_feature": ""
        },
        "conditions": {
            "placement_pass": "sky_pass",
            "minecraft:biome_filter": None
        },
        "distribution": {
            "iterations": 1,
            "scatter_chance": 10,
            "coordinate_eval_order": "xzy",
            "x": {
                "distribution": "uniform",
                "extent": [
                    0,
                    15
                ]
            },
            "y": "query.get_height_at(variable.worldx, variable.worldz)",
            "z": {
                "distribution": "uniform",
                "extent": [
                    0,
                    15
                ]
            }
        }
    }
}
lootJson = {
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
itemText = "item.%s.name=%s\n"
blockText = "tile.%s.name=%s\n"
textList = []
fruitJson = {
    "format_version": "1.10",
    "minecraft:item": {
        "description": {"identifier": "",
                        "register_to_create_menu": True,
                        "category": "Nature"}, "components": {"minecraft:use_duration": 32, "minecraft:food": {"nutrition": 1, "saturation_modifier": "poor"}}}}
fruitResJson = {
    "format_version": "1.10",
    "minecraft:item": {
        "components": {
            "minecraft:icon": "",
            "minecraft:use_animation": "eat"
        },
        "description": {
            "identifier": ""
        }
    }
}
saplingJson = {
    "format_version": "1.10.0",
    "minecraft:block": {
        "description": {
            "identifier": "",
            "category": "Nature",
            "register_to_creative_menu": True
        },
        "components": {
            "minecraft:block_light_emission": {
                "emission": 0.0
            },
            "minecraft:block_light_absorption": {
                "value": 0
            },
            "netease:render_layer": {
                "value": "alpha"
            },
            "minecraft:map_color": {
                "color": "#555500"
            },
            "minecraft:destroy_time": {
                "value": 0.2
            },
            "netease:tier": {
                "digger": "hatchet",
                "destroy_special": False,
                "level": 0
            },
            "minecraft:explosion_resistance": {
                "value": 0.2
            },
            "netease:solid": {
                "value": False
            },
            "netease:pathable": {
                "value": True
            },
            "netease:face_directional": {
                "type": "direction"
            },
            "netease:aabb": {
                "collision": {
                    "min": [
                        0.0,
                        0.0,
                        0.0
                    ],
                    "max": [
                        0,
                        0,
                        0
                    ]
                },
                "clip": {
                    "min": [
                        0.1,
                        0.0,
                        0.1
                    ],
                    "max": [
                        0.9,
                        0.9,
                        0.9
                    ]
                }
            },
            "netease:block_entity": {
                "movable": True,
                "tick": True
            }
        }
    }
}
blocks = {}
terrain_texture = {}
item_texture = {}
textures_list = []
modelJson = {
    "format_version": "1.13.0",
    "netease:block_geometry":
        {
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
                            "origin": [-16, 0, 8],
                            "size": [16, 16, 4],
                            "pivot": [-8, 0, 8],
                            "rotation": [0, -45, 0],
                            "uv": {
                                "north": {"uv": [0, 0], "uv_size": [16, 16]}
                            }
                        },
                        {
                            "origin": [-16, 0, 8],
                            "size": [16, 16, 4],
                            "pivot": [-8, 0, 8],
                            "rotation": [0, 45, 0],
                            "uv": {
                                "north": {"uv": [0, 0], "uv_size": [16, 16]}
                            }
                        }
                    ]
                }
            ]
        }
}

recipeJson = {
    "format_version": "1.12",
    "minecraft:recipe_shapeless": {
        "description": {
            "identifier": ""
        },
        "tags": ["crafting_table"],
        "ingredients": [
        ],
        "result": {
            "item": "",
            "count": 1
        }
    }
}

item_texture_json = {
}


def create_fruitTree(item):
    name = str.lower(item["物品名"]).replace(" ", "_").replace("-", "_")
    identifier = "mwh_pam:" + name

    fruitBlock = fruitBlockJson.copy()
    fruitBlock["minecraft:single_block_feature"]["description"]["identifier"] = name + "_fruitBlock"
    fruitBlock["minecraft:single_block_feature"]["places_block"]["name"] = identifier + "_stage_0"

    food = copy(fruitJson)
    food["minecraft:item"]["description"]["identifier"] = identifier

    if not os.path.exists("tree/netease_items_beh/"):
        os.makedirs("tree/netease_items_beh/")
    f = open("tree/netease_items_beh/" + name + ".json", "w")
    f.write(json.dumps(food).replace("'", "\""))
    f.close()

    res = copy(fruitJson)
    res["minecraft:item"]["components"]["minecraft:use_animation"] = "eat"
    res["minecraft:item"]["components"]["minecraft:icon"] = identifier
    res["minecraft:item"]["description"]["identifier"] = identifier

    if not os.path.exists("tree/netease_items_res/"):
        os.makedirs("tree/netease_items_res/")
    f = open("tree/netease_items_res/" + name + ".json", "w")
    f.write(json.dumps(res).replace("'", "\""))
    f.close()

    item_texture_json[identifier] = {"textures": "textures/items/" + name + "item"}

    if not os.path.exists("tree/textures/"):
        os.makedirs("tree/textures/")
    f = open("tree/textures/item_texture.json", "w")
    f.write(json.dumps(item_texture_json).replace("'", "\""))
    f.close()

    textList.append(itemText % (identifier, item["中文名"].replace("树苗", "")))

    if not os.path.exists("tree/netease_features/"):
        os.makedirs("tree/netease_features/")
    f = open("tree/netease_features/" + name + "_fruitBlock.json", "w")
    f.write(json.dumps(fruitBlock).replace("'", "\""))
    f.close()

    scatterFruitBlock = scatterFruitBlockJson.copy()
    scatterFruitBlock["minecraft:scatter_feature"]["description"]["identifier"] = name + "_scatterFruitBlock"
    scatterFruitBlock["minecraft:scatter_feature"]["places_feature"] = name + "_fruitBlock"

    if not os.path.exists("tree/netease_features/"):
        os.makedirs("tree/netease_features/")
    f = open("tree/netease_features/" + name + "_scatterFruitBlock.json", "w")
    f.write(json.dumps(scatterFruitBlock).replace("'", "\""))
    f.close()

    searchFruitBlock = searchFruitBlockJson.copy()
    searchFruitBlock["minecraft:search_feature"]["description"]["identifier"] = name + "_searchFruitBlock"
    searchFruitBlock["minecraft:search_feature"]["places_feature"] = name + "_scatterFruitBlock"

    if not os.path.exists("tree/netease_features/"):
        os.makedirs("tree/netease_features/")
    f = open("tree/netease_features/" + name + "_searchFruitBlock.json", "w")
    f.write(json.dumps(searchFruitBlock).replace("'", "\""))
    f.close()

    fruitTree = fruitTreeJson.copy()
    fruitTree["minecraft:aggregate_feature"]["description"]["identifier"] = name + "_tree"
    fruitTree["minecraft:aggregate_feature"]["features"][0] = treeType.get(item["树类型"], "minecraft:oak_tree_feature")
    fruitTree["minecraft:aggregate_feature"]["features"][1] = name + "_searchFruitBlock"

    if not os.path.exists("tree/netease_features/"):
        os.makedirs("tree/netease_features/")
    f = open("tree/netease_features/" + name + "_tree.json", "w")
    f.write(json.dumps(fruitTree).replace("'", "\""))
    f.close()

    rule = ruleJson.copy()
    rule["minecraft:feature_rules"]["description"]["identifier"] = name + "_tree"
    rule["minecraft:feature_rules"]["description"]["places_feature"] = name + "_tree"
    rule["minecraft:feature_rules"]["conditions"]["minecraft:biome_filter"] = tree_biome.get(item["树类型"], tree_biome["橡树"])

    if not os.path.exists("tree/netease_feature_rules/"):
        os.makedirs("tree/netease_feature_rules/")
    f = open("tree/netease_feature_rules/" + name + "_tree.json", "w")
    f.write(json.dumps(rule).replace("'", "\""))
    f.close()

    saplingBlock = saplingJson.copy()
    saplingBlock["minecraft:block"]["description"]["identifier"] = identifier + "_sapling"

    if not os.path.exists("tree/netease_blocks/"):
        os.makedirs("tree/netease_blocks/")
    f = open("tree/netease_blocks/" + name + "_sapling.json", "w")
    f.write(json.dumps(saplingBlock).replace("'", "\""))
    f.close()

    blocks[identifier + "_sapling"] = {"netease_model": identifier + "_sapling", "sound": "grass"}
    if not os.path.exists("tree/"):
        os.makedirs("tree/")
    f = open("tree/blocks.json", "w")
    f.write(json.dumps(blocks).replace("'", "\""))
    f.close()

    model = modelJson.copy()
    model["netease:block_geometry"]["description"]["identifier"] = identifier + "_sapling"
    model["netease:block_geometry"]["description"]["textures"] = [identifier + "_sapling"]
    model["netease:block_geometry"]["description"]["item_texture"] = identifier + "_sapling"
    if not os.path.exists("tree/models/netease_block/"):
        os.makedirs("tree/models/netease_block/")
    f = open("tree/models/netease_block/" + name + "_sapling.json", "w")
    f.write(json.dumps(model).replace("'", "\""))
    f.close()

    item_texture[identifier + "_sapling"] = {"textures": "textures/blocks/" + name + "_sapling"}
    terrain_texture[identifier + "_sapling"] = {"textures": "textures/blocks/" + name + "_sapling"}
    textures_list.append("textures/blocks/" + name + "_sapling")

    textList.append(blockText % (identifier + "_sapling", item["中文名"]))

    item_texture[identifier] = {"textures": "textures/blocks/" + name}
    textures_list.append("textures/blocks/" + name)

    for i in range(3):
        if i != 2:
            fruitBlock = saplingJson.copy()
            fruitBlock["minecraft:block"]["description"]["identifier"] = identifier + "_stage_" + str(i)
            fruitBlock["minecraft:block"]["components"]["minecraft:destroy_time"]["value"] = 3.0
            fruitBlock["minecraft:block"]["components"]["minecraft:loot"] = {"table": "null"}
        else:
            fruitBlock = saplingJson.copy()
            fruitBlock["minecraft:block"]["description"]["identifier"] = identifier + "_stage_" + str(i)
            fruitBlock["minecraft:block"]["components"]["minecraft:destroy_time"]["value"] = 3.0
            fruitBlock["minecraft:block"]["components"]["minecraft:loot"] = {"table": "loot_tables/fruit/" + name + ".json"}
        if not os.path.exists("tree/netease_blocks/"):
            os.makedirs("tree/netease_blocks/")
        f = open("tree/netease_blocks/" + name + "_stage_" + str(i) + ".json", "w")
        f.write(json.dumps(fruitBlock).replace("'", "\""))
        f.close()

        model = modelJson.copy()
        model["netease:block_geometry"]["description"]["identifier"] = identifier + "_stage_" + str(i)
        model["netease:block_geometry"]["description"]["textures"] = [identifier + "_stage_" + str(i)]
        model["netease:block_geometry"]["description"]["item_texture"] = identifier + "_stage_" + str(i)
        if not os.path.exists("tree/models/netease_block/"):
            os.makedirs("tree/models/netease_block/")
        f = open("tree/models/netease_block/" + name + "_stage_" + str(i) + ".json", "w")
        f.write(json.dumps(model).replace("'", "\""))
        f.close()

        loot = lootJson.copy()
        loot["pools"][0]["entries"][0]["name"] = identifier
        if not os.path.exists("tree/loot_tables/fruit/"):
            os.makedirs("tree/loot_tables/fruit/")
        f = open("tree/loot_tables/fruit/" + name + ".json", "w")
        f.write(json.dumps(loot).replace("'", "\""))
        f.close()

        item_texture[identifier + "_stage_" + str(i)] = {"textures": "textures/blocks/" + name + "_stage_" + str(i)}
        terrain_texture[identifier + "_stage_" + str(i)] = {"textures": "textures/blocks/" + name + "_stage_" + str(i)}

        textures_list.append("textures/blocks/" + name + "_stage_" + str(i))

        textList.append(blockText % (identifier + "_stage_" + str(i), item["中文名"].replace("树苗", "") + "果实"))

        blocks[identifier + "_stage_" + str(i)] = {"netease_model": identifier + "_stage_" + str(i), "sound": "grass"}

    if not os.path.exists("tree/textures/"):
        os.makedirs("tree/textures/")
    f = open("tree/textures/item_texture.json", "w")
    f.write(json.dumps(item_texture).replace("'", "\""))
    f.close()

    if not os.path.exists("tree/textures/"):
        os.makedirs("tree/textures/")
    f = open("tree/textures/terrain_texture.json", "w")
    f.write(json.dumps(terrain_texture).replace("'", "\""))
    f.close()

    if not os.path.exists("tree/textures/"):
        os.makedirs("tree/textures/")
    f = open("tree/textures/textures_list.json", "w")
    f.write(json.dumps(textures_list).replace("'", "\""))
    f.close()

    f = open("tree/blocks.json", "w")
    f.write(json.dumps(blocks).replace("'", "\""))
    f.close()

    if not os.path.exists("tree/texts/"):
        os.makedirs("tree/texts/")
    f = open("tree/texts/zh_CN.lang", "w")
    f.write("".join(textList))
    f.close()

    recipe = recipeJson.copy()
    recipe["minecraft:recipe_shapeless"]["description"]["identifier"] = identifier + "_sapling"
    recipe["minecraft:recipe_shapeless"]["result"]["item"] = identifier + "_sapling"
    recipe["minecraft:recipe_shapeless"]["ingredients"] = [
        {
            "item": item["合成配方列表"][0]["key"]["A"]["id"] if ":" in item["合成配方列表"][0]["key"]["A"]["id"] else "mwh_pam:" + item["合成配方列表"][0]["key"]["A"]["id"],
            "data": 0
        },
        {
            "item": item["合成配方列表"][0]["key"]["B"]["id"] if ":" in item["合成配方列表"][0]["key"]["B"]["id"] else "mwh_pam:" + item["合成配方列表"][0]["key"]["B"]["id"],
            "data": 0
        }
    ]

    if not os.path.exists("tree/netease_recipes/"):
        os.makedirs("tree/netease_recipes/")
    f = open("tree/netease_recipes/" + name + "_sapling.json", "w")
    f.write(json.dumps(recipe).replace("'", "\""))
    f.close()
