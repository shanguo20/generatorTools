# coding=utf-8
from create_crop import create_crop


def createItem(itemList):
    fenceConnectList = []
    fenceConnectItem = """ "%s"
    """
    for i in itemList:
        if i["type"] == "fence":
            fenceConnectList.append(fenceConnectItem % i["identifier"])
    for item in itemList:
        if item["type"] == "item":
            json = """
            {
                "format_version": "1.10",
                "minecraft:item": {
                    "components": {
                        "minecraft:foil": false,
                        "minecraft:max_stack_size": %s
                    },
                    "description": {
                        "category": "Items",
                        "identifier": "%s",
                        "register_to_create_menu": true
                    }
                }
            }
            """ % (item["max_stack_size"], item["identifier"])
            f = open("netease_items_beh/" + item["name"] + ".json", "w")
            f.write(json)
            f.close()
        elif item["type"] in ["sword", "hoe", "hatchet", "pickaxe", "shovel"]:
            itemType = item["type"]
            if itemType == "axe":
                itemType = "hatchet"
            try:
                json = """
                {
                  "format_version": "1.10",
                  "minecraft:item": {
                    "components": {
                      "minecraft:max_damage": %s,
                      "minecraft:max_stack_size": %s,
                      "netease:weapon": {
                        "attack_damage": %s,
                        "enchantment": %s,
                        "level": %s,
                        "speed": %s,
                        "type": "%s"                     
                      }
                    },
                    "description": {
                      "category": "Equipment",
                      "identifier": "%s",
                      "register_to_create_menu": true
                    }
                  }
                }
            """ % (
                    item["max_damage"],
                    item["max_stack_size"],
                    item["attack_damage"],
                    item["enchantment"],
                    item["level"],
                    item["speed"],
                    itemType,
                    item["identifier"]
                )
            except Exception as exc:
                print exc, "\n", item["identifier"]
            f = open("netease_items_beh/" + item["name"] + ".json", "w")
            f.write(json)
            f.close()
        elif item["type"] == "food":
            if "nutrition" not in item:
                print item["identifier"]
            if item["saturation_modifier"] <= 1:
                item["saturation_modifier"] = "poor"
            elif item["saturation_modifier"] <= 3:
                item["saturation_modifier"] = "low"
            elif item["saturation_modifier"] <= 6:
                item["saturation_modifier"] = "normal"
            elif item["saturation_modifier"] <= 8:
                item["saturation_modifier"] = "good"
            elif item["saturation_modifier"] <= 10:
                item["saturation_modifier"] = "max"
            elif item["saturation_modifier"] > 10:
                item["saturation_modifier"] = "supernatural"
            json = """{
  "format_version": "1.10",
  "minecraft:item": {
    "description": {
      "identifier": "%s",
      "register_to_create_menu":true,
      "category":"Equipment"
    },
    "components": {
      "minecraft:use_duration": 32,
      "minecraft:max_stack_size": %s,
      "minecraft:food": {
        %s
        "nutrition": %s,
        "saturation_modifier": "%s",
        "can_always_eat":%s
      }
    }
  }
}"""
            components = ""
            if "using_converts_to" in item:
                components += """
                "using_converts_to":"%s",""" % item["using_converts_to"]
            if "cooldown_type" in item:
                components += """
                "cooldown_type":"%s",""" % (item["cooldown_type"])
                components += """
                "cooldown_time":%s,""" % (item["cooldown_time"])
            json = json % (
                item["identifier"],
                item["max_stack_size"],
                components,
                item["nutrition"],
                item["saturation_modifier"],
                "true" if item["can_always_eat"] else "false"
            )
            print item["name"]
            f = open("netease_items_beh/" + item["name"] + ".json", "w")
            f.write(json)
            f.close()
        elif item["type"] in ["helmet", "chestplate", "leggings", "boots"]:
            armor = ["helmet", "chestplate", "leggings", "boots"]
            json = \
                """{
                    "format_version": "1.10",
                    "minecraft:item": {
                        "components": {
                            "minecraft:max_damage": %s,
                            "minecraft:max_stack_size": %s,
                            "netease:armor": {
                                "armor_slot": %s,
                                "defense": %s,
                                "enchantment": %s
                            }
                        },
                        "description": {
                            "category": "Equipment",
                            "identifier": "%s",
                            "register_to_create_menu": true
                        }
                    }
                }""" % (
                    item["max_damage"],
                    item["max_stack_size"],
                    armor.index(item["type"]),
                    item["defense"],
                    item["enchantment"],
                    item["identifier"]
                )
            f = open("netease_items_beh/" + item["name"] + ".json", "w")
            f.write(json)
            f.close()
        elif item["type"] in ["block", "typex", "carpet", "halfbrick", "staircase", "fence", "banner", "normal", "flag"]:
            json = """
                {
                    "format_version": "1.10.0",
                    "minecraft:block": {
                        "description": {
                            "identifier": "%s",
                            "category": "%s",
                            "register_to_creative_menu": true
                        },
                        "components": {
                            "minecraft:block_light_emission": {
                                "emission": %s
                            },
                            "minecraft:block_light_absorption": {
                                "value": %s
                            },
                            "netease:render_layer": {
                                "value": "%s"
                            },
                            "minecraft:map_color": {
                                "color": "%s"
                            },
                            "minecraft:destroy_time": {
                                "value": %s
                            },
                            "netease:tier": {
                                "digger": "%s",
                                "destroy_special": %s,
                                "level": %s
                            },
                            "minecraft:explosion_resistance": {
                                "value": %s
                            },
                            "netease:solid": {
                                "value": %s
                            },
                            "netease:pathable": {
                                "value": %s
                            },
                            "netease:face_directional": {
                                "type": "%s"
                            },
                            "netease:aabb": {
                                "collision": {
                                    "min": [
                                        0.0,
                                        0.0,
                                        0.0
                                    ],
                                    "max": [
                                        %s,
                                        %s,
                                        %s
                                    ]
                                },
                                "clip": {
                                    "min": [
                                        0.0,
                                        0.0,
                                        0.0
                                    ],
                                    "max": [
                                        %s,
                                        %s,
                                        %s
                                    ]
                                }
                            }
                            %s
                            %s
                        }
                    }
                }
                            """
            blockJson = \
                """
                    ,
                    "netease:block_entity": {
                        "movable": %s,
                        "tick": %s
                    }
                """
            loot_tablesItem = \
                """
                ,
                    "minecraft:loot": {
                        "table": "loot_tables/netease/%s.json"
                    }
                """
            collision = [0, 0, 0]
            if "collision" not in item:
                if item["type"] in ["block", "normal"]:
                    collision = [1, 1, 1]
                elif item["type"] == "typex":
                    collision = [0, 0, 0]
                elif item["type"] == "carpet":
                    collision = [1, 0.0625, 1]
                elif item["type"] in ["banner", "flag"]:
                    collision = [0, 0, 0]
            else:
                collision = item["collision"]
            clip = [1, 1, 1]
            if item["type"] == "block":
                clip = [1, 1, 1]
            elif item["type"] == "typex":
                clip = [1, 1, 1]
            elif item["type"] == "carpet":
                clip = [1, 0.0625, 1]

            if item["type"] in ["block", "typex", "carpet", "normal"]:
                block = json % (
                    item["identifier"],
                    "Nature",
                    0.0 if "block_light_emission" not in item else item["block_light_emission"],
                    0.0 if "block_light_absorption" not in item else item["block_light_absorption"],
                    "opaque" if "render_layer" not in item else item["render_layer"],
                    "#FFFFFF" if "map_color" not in item else item["map_color"],
                    item["destroy_time"],
                    item["digger"],
                    item["destroy_special"],
                    0 if "level" not in item else item["level"],
                    item["explosion_resistance"],
                    "true" if "solid" not in item else item["solid"],
                    "true" if "pathable" not in item else item["pathable"],
                    "direction" if "face_directional" not in item else item["face_directional"],
                    collision[0], collision[1], collision[2],
                    clip[0], clip[1], clip[2],
                    loot_tablesItem % (item["name"]) if "loot_tables" in item and
                                                        item[
                                                            "loot_tables"][
                                                            "name"] != "" else "",
                    blockJson % (item["movable"], item["tick"]) if "block_entity" in item and item[
                        "block_entity"] == "true" else ""
                )

                f = open("netease_blocks/" + item["name"] + ".json", "w")
                if "goldpile" in item["name"]:
                    print item["name"]
                f.write(block)
                f.close()
            elif item["type"] == "halfbrick":
                item["loot_tables"] = {
                    "max": 1,
                    "min": 1,
                    "data": 0,
                    "name": item["identifier"]
                }
                downJson = """
                {
                    "format_version": "1.10.0",
                    "minecraft:block": {
                        "description": {
                            "identifier": "%s",
                            "category": "Construction",
                            "register_to_creative_menu": true
                        },
                        "components": {
                            "minecraft:block_light_emission": {
                                "emission": %s
                            },
                            "minecraft:block_light_absorption": {
                                "value": %s
                            },
                            "netease:render_layer": {
                                "value": "%s"
                            },
                            "minecraft:map_color": {
                                "color": "%s"
                            },
                            "minecraft:destroy_time": {
                                "value": %s
                            },
                            "netease:tier": {
                                "digger": "%s",
                                "destroy_special": %s,
                                "level": %s
                            },
                            "minecraft:explosion_resistance": {
                                "value": %s
                            },
                            "netease:solid": {
                                "value": %s
                            },
                            "netease:pathable": {
                                "value": %s
                            },
                            "netease:face_directional": {
                                "type": "%s"
                            },
                            "netease:aabb": {
                                "collision": {
                                    "min": [
                                        0.0,
                                        0.0,
                                        0.0
                                    ],
                                    "max": [
                                        %s,
                                        %s,
                                        %s
                                    ]
                                },
                                "clip": {
                                    "min": [
                                        0.0,
                                        0.0,
                                        0.0
                                    ],
                                    "max": [
                                        %s,
                                        %s,
                                        %s
                                    ]
                                }
                            }
                            %s
                            %s
                        }
                    }
                }
                            """
                down = downJson % (
                    item["identifier"],
                    0.0 if "block_light_emission" not in item else item["block_light_emission"],
                    0.0 if "block_light_absorption" not in item else item["block_light_absorption"],
                    "opaque" if "render_layer" not in item else item["render_layer"],
                    "#FFFFFF" if "map_color" not in item else item["map_color"],
                    item["destroy_time"],
                    item["digger"],
                    item["destroy_special"],
                    0 if "level" not in item else item["level"],
                    item["explosion_resistance"],
                    "true" if "solid" not in item else item["solid"],
                    "true" if "pathable" not in item else item["pathable"],
                    "direction" if "face_directional" not in item else item["face_directional"],
                    1, 0.5, 1,
                    1, 0.5, 1,
                    loot_tablesItem % (item["name"]) if "loot_tables" in item and
                                                        item[
                                                            "loot_tables"][
                                                            "name"] != "" else "",
                    blockJson % (item["movable"], item["tick"]) if "block_entity" in item and item[
                        "block_entity"] == "true" else ""
                )

                f = open("netease_blocks/" + item["name"] + ".json", "w")
                f.write(down)
                f.close()

                upJson = """
{
    "format_version": "1.10.0",
    "minecraft:block": {
        "description": {
            "identifier": "%s",
            "category": "Construction",
            "register_to_creative_menu": false
        },
        "components": {
            "minecraft:block_light_emission": {
                "emission": %s
            },
            "minecraft:block_light_absorption": {
                "value": %s
            },
            "netease:render_layer": {
                "value": "%s"
            },
            "minecraft:map_color": {
                "color": "%s"
            },
            "minecraft:destroy_time": {
                "value": %s
            },
            "netease:tier": {
                "digger": "%s",
                "destroy_special": %s,
                "level": %s
            },
            "minecraft:explosion_resistance": {
                "value": %s
            },
            "netease:solid": {
                "value": %s
            },
            "netease:pathable": {
                "value": %s
            },
            "netease:face_directional": {
                "type": "%s"
            },
            "netease:aabb": {
                "collision": {
                    "min": [
                        0.0,
                        0.5,
                        0.0
                    ],
                    "max": [
                        %s,
                        %s,
                        %s
                    ]
                },
                "clip": {
                    "min": [
                        0.0,
                        0.5,
                        0.0
                    ],
                    "max": [
                        %s,
                        %s,
                        %s
                    ]
                }
            }
            %s
            %s
        }
    }
}
            """
                up = upJson % (
                    item["identifier"] + "_top",
                    0.0 if "block_light_emission" not in item else item["block_light_emission"],
                    0.0 if "block_light_absorption" not in item else item["block_light_absorption"],
                    "opaque" if "render_layer" not in item else item["render_layer"],
                    "#FFFFFF" if "map_color" not in item else item["map_color"],
                    item["destroy_time"],
                    item["digger"],
                    item["destroy_special"],
                    0 if "level" not in item else item["level"],
                    item["explosion_resistance"],
                    "true" if "solid" not in item else item["solid"],
                    "true" if "pathable" not in item else item["pathable"],
                    "direction" if "face_directional" not in item else item["face_directional"],
                    1, 1, 1,
                    1, 1, 1,
                    loot_tablesItem % (item["name"]) if "loot_tables" in item and
                                                        item[
                                                            "loot_tables"][
                                                            "name"] != "" else "",
                    blockJson % (item["movable"], item["tick"]) if "block_entity" in item and item[
                        "block_entity"] == "true" else ""
                )

                f = open("netease_blocks/" + item["name"] + "_top.json", "w")
                f.write(up)
                f.close()
            elif item["type"] in ["banner", "flag"]:
                item["loot_tables"] = {
                    "max": 1,
                    "min": 1,
                    "data": 0,
                    "name": item["identifier"]
                }
                Json = """
                {
                    "format_version": "1.10.0",
                    "minecraft:block": {
                        "description": {
                            "identifier": "%s",
                            "category": "Construction",
                            "register_to_creative_menu": true
                        },
                        "components": {
                            "minecraft:block_light_emission": {
                                "emission": %s
                            },
                            "minecraft:block_light_absorption": {
                                "value": %s
                            },
                            "netease:render_layer": {
                                "value": "%s"
                            },
                            "minecraft:map_color": {
                                "color": "%s"
                            },
                            "minecraft:destroy_time": {
                                "value": %s
                            },
                            "netease:tier": {
                                "digger": "%s",
                                "destroy_special": %s,
                                "level": %s
                            },
                            "minecraft:explosion_resistance": {
                                "value": %s
                            },
                            "netease:solid": {
                                "value": %s
                            },
                            "netease:pathable": {
                                "value": %s
                            },
                            "netease:face_directional": {
                                "type": "%s"
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
                                        1.0,
                                        1.0
                                    ]
                                }
                            }
                            %s
                            %s
                        }
                    }
                }
                            """
                down = Json % (
                    item["identifier"],
                    0.0 if "block_light_emission" not in item else item["block_light_emission"],
                    0.0 if "block_light_absorption" not in item else item["block_light_absorption"],
                    "opaque" if "render_layer" not in item else item["render_layer"],
                    "#FFFFFF" if "map_color" not in item else item["map_color"],
                    item["destroy_time"],
                    item["digger"],
                    item["destroy_special"],
                    0 if "level" not in item else item["level"],
                    item["explosion_resistance"],
                    "true" if "solid" not in item else item["solid"],
                    "true" if "pathable" not in item else item["pathable"],
                    "direction" if "face_directional" not in item else item["face_directional"],
                    loot_tablesItem % (item["name"]) if "loot_tables" in item and
                                                        item[
                                                            "loot_tables"][
                                                            "name"] != "" else "",
                    blockJson % (item["movable"], item["tick"]) if "block_entity" in item and item[
                        "block_entity"] == "true" else ""
                )

                f = open("netease_blocks/" + item["name"] + ".json", "w")
                f.write(down)
                f.close()

                onWallJson = """
{
    "format_version": "1.10.0",
    "minecraft:block": {
        "description": {
            "identifier": "%s",
            "category": "Construction",
            "register_to_creative_menu": false
        },
        "components": {
            "minecraft:block_light_emission": {
                "emission": %s
            },
            "minecraft:block_light_absorption": {
                "value": %s
            },
            "netease:render_layer": {
                "value": "%s"
            },
            "minecraft:map_color": {
                "color": "%s"
            },
            "minecraft:destroy_time": {
                "value": %s
            },
            "netease:tier": {
                "digger": "%s",
                "destroy_special": %s,
                "level": %s
            },
            "minecraft:explosion_resistance": {
                "value": %s
            },
            "netease:solid": {
                "value": %s
            },
            "netease:pathable": {
                "value": %s
            },
            "netease:face_directional": {
                "type": "%s"
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
                        0.0,
                        0.0,
                        0.0
                    ],
                    "max": [
                        0,
                        0,
                        0
                    ]
                }
            }
            %s
            %s
        }
    }
}
            """
                up = onWallJson % (
                    item["identifier"] + "_wall",
                    0.0 if "block_light_emission" not in item else item["block_light_emission"],
                    0.0 if "block_light_absorption" not in item else item["block_light_absorption"],
                    "opaque" if "render_layer" not in item else item["render_layer"],
                    "#FFFFFF" if "map_color" not in item else item["map_color"],
                    item["destroy_time"],
                    item["digger"],
                    item["destroy_special"],
                    0 if "level" not in item else item["level"],
                    item["explosion_resistance"],
                    "true" if "solid" not in item else item["solid"],
                    "true" if "pathable" not in item else item["pathable"],
                    "direction" if "face_directional" not in item else item["face_directional"],
                    loot_tablesItem % (item["name"]) if "loot_tables" in item and
                                                        item[
                                                            "loot_tables"][
                                                            "name"] != "" else "",
                    blockJson % (item["movable"], item["tick"]) if "block_entity" in item and item[
                        "block_entity"] == "true" else ""
                )

                f = open("netease_blocks/" + item["name"] + "_wall.json", "w")
                f.write(up)
                f.close()
            elif item["type"] == "staircase":
                staircaseJson = """
{
    "format_version": "1.10.0",
    "minecraft:block": {
        "description": {
            "identifier": "%s",
            "category": "Construction",
            "register_to_creative_menu": true
        },
        "components": {
            "minecraft:block_light_emission": {
                "emission": %s
            },
            "minecraft:block_light_absorption": {
                "value": %s
            },
            "netease:render_layer": {
                "value": "%s"
            },
            "minecraft:map_color": {
                "color": "%s"
            },
            "minecraft:destroy_time": {
                "value": %s
            },
            "netease:tier": {
                "digger": "%s",
                "destroy_special": %s,
                "level": %s
            },
            "minecraft:explosion_resistance": {
                "value": %s
            },
            "netease:solid": {
                "value": %s
            },
            "netease:pathable": {
                "value": %s
            },
            "netease:face_directional": {
                "type": "%s"
            },
            "netease:aabb": {
                "collision": [
                    {
                        "min": [
                            0,
                            0,
                            0
                        ],
                        "max": [
                            1,
                            0.5,
                            1
                        ]
                    },
                    {
                        "min": [
                            0,
                            0.5,
                            0.5
                        ],
                        "max": [
                            1,
                            1,
                            1
                        ]
                    }
                ],
                "clip": [
                    {
                        "min": [
                            0,
                            0,
                            0
                        ],
                        "max": [
                            1,
                            0.5,
                            1
                        ]
                    },
                    {
                        "min": [
                            0,
                            0.5,
                            0.5
                        ],
                        "max": [
                            1,
                            1,
                            1
                        ]
                    }
                ]
            }
            %s
            %s
        }
    }
}
                            """
                staircase = staircaseJson % (
                    item["identifier"],
                    0.0 if "block_light_emission" not in item else item["block_light_emission"],
                    0.0 if "block_light_absorption" not in item else item["block_light_absorption"],
                    "opaque" if "render_layer" not in item else item["render_layer"],
                    "#FFFFFF" if "map_color" not in item else item["map_color"],
                    item["destroy_time"],
                    item["digger"],
                    item["destroy_special"],
                    0 if "level" not in item else item["level"],
                    item["explosion_resistance"],
                    "true" if "solid" not in item else item["solid"],
                    "true" if "pathable" not in item else item["pathable"],
                    "direction" if "face_directional" not in item else item["face_directional"],
                    loot_tablesItem % (item["name"]) if "loot_tables" in item and
                                                        item[
                                                            "loot_tables"][
                                                            "name"] != "" else "",
                    blockJson % (item["movable"], item["tick"]) if "block_entity" in item and item[
                        "block_entity"] == "true" else ""
                )

                f = open("netease_blocks/" + item["name"] + ".json", "w")
                f.write(staircase)
                f.close()
            elif item["type"] == "fence":
                fenceJson = """
{
    "format_version": "1.10.0",
    "minecraft:block": {
        "description": {
            "identifier": "%s",
            "category": "Construction",
            "register_to_creative_menu": true
        },
        "components": {
            "netease:connection": {
                "blocks": [
                  %s
                ]
            },
            "minecraft:block_light_absorption": {
                "value": %s
            },
            "minecraft:block_light_emission": {
                "emission": %s
            },
            "netease:render_layer": {
                "value": "opaque"
            },
            
            "minecraft:map_color": {
                "color": "%s"
            },
            "minecraft:destroy_time": {
                "value": %s
            },
            "netease:tier": {
                "digger": "%s",
                "destroy_special": %s,
                "level": %s
            },
            "minecraft:explosion_resistance": {
                "value": %s
            },
            "netease:solid": {
                "value": false
            },
            "netease:pathable": {
                "value": false
            },
            "netease:face_directional": {
                "type": "direction"
            },
            "netease:aabb": {
                "collision": [
					{
					  "min": [0.375, 0.0, 0.375],
					  "max": [0.625, 1.5, 0.625]
					},
					{
					  "enable": "query.is_connect(2)",
					  "min": [0.375, 0.0, 0.0],
					  "max": [0.625, 1.5, 0.375]
					},
					{
					  "enable": "query.is_connect(3)",
					  "min": [0.375, 0.0, 0.625],
					  "max": [0.625, 1.5, 1.0]
					},
					{
					  "enable": "query.is_connect(4)",
					  "min": [0.0, 0.0, 0.375],
					  "max": [0.375, 1.5, 0.625]
					},
					{
					  "enable": "query.is_connect(5)",
					  "min": [0.625, 0.0, 0.375],
					  "max": [1.0, 1.5, 0.625]
					}
				],
				"clip": [
					{
					  "min": [0.375, 0.0, 0.375],
					  "max": [0.625, 1.0, 0.625]
					},
					{
					  "enable": "query.is_connect(2)",
					  "min": [0.375, 0.0, 0.0],
					  "max": [0.625, 1.0, 0.375]
					},
					{
					  "enable": "query.is_connect(3)",
					  "min": [0.375, 0.0, 0.625],
					  "max": [0.625, 1.0, 1.0]
					},
					{
					  "enable": "query.is_connect(4)",
					  "min": [0.0, 0.0, 0.375],
					  "max": [0.375, 1.0, 0.625]
					},
					{
					  "enable": "query.is_connect(5)",
					  "min": [0.625, 0.0, 0.375],
					  "max": [1.0, 1.0, 0.625]
					}
				]
            }
            %s
            %s
        }
    }
}
                            """
                fence = fenceJson % (
                    item["identifier"],
                    ",".join(fenceConnectList),
                    0.0 if "block_light_absorption" not in item else item["block_light_absorption"],
                    0.0 if "block_light_emission" not in item else item["block_light_emission"],
                    "#FFFFFF" if "map_color" not in item else item["map_color"],
                    item["destroy_time"],
                    item["digger"],
                    item["destroy_special"],
                    0 if "level" not in item else item["level"],
                    item["explosion_resistance"],
                    loot_tablesItem % (item["name"]) if "loot_tables" in item and
                                                        item[
                                                            "loot_tables"][
                                                            "name"] != "" else "",
                    blockJson % (item["movable"], item["tick"]) if "block_entity" in item and item[
                        "block_entity"] == "true" else ""
                )

                f = open("netease_blocks/" + item["name"] + ".json", "w")
                f.write(fence)
                f.close()
        elif item["type"] == "shuaguaixiang":
            mob_spawner = """
{
  "format_version": "1.10.0",
  "minecraft:block": {
    "description": {
      "identifier": "%s",
	  "register_to_creative_menu": true,
	  "is_experimental": false,
	  "base_block": "mob_spawner"
    },
    "components": {
	  "netease:mob_spawner": {
	    "type": "%s"
	  }
    }
  }
}
            """ % (item["identifier"], item["spawn_type"])
            f = open("netease_blocks/" + item["name"] + ".json", "w")
            f.write(mob_spawner)
            f.close()
        elif item["type"] == "bow":
            bowJson = """
{
  "format_version": "1.10",
  "minecraft:item": {
    "description": {
      "identifier": "%s",
      "register_to_create_menu":true,
	  "category": "Equipment",
      "custom_item_type": "ranged_weapon"
    },
    "components": {
      "minecraft:use_duration": 72000,
      "minecraft:max_damage": %s
    }
  }
}
            """ % ("mwh_pam_%s:bow" % str(item["identifier"]).replace("mwh_pam:bow_", ""), item["max_damage"])
            f = open("netease_items_beh/" + item["name"] + ".json", "w")
            f.write(bowJson)
            f.close()
        elif item["type"] == "crossbow":
            json = """
            {
                "format_version": "1.10",
                "minecraft:item": {
                    "components": {
                        "minecraft:foil": false,
                        "minecraft:max_damage": %s,
                        "minecraft:max_stack_size": %s
                    },
                    "description": {
                        "category": "Items",
                        "identifier": "%s",
                        "register_to_create_menu": true
                    }
                }
            }
            """ % (item["max_damage"], item["max_stack_size"], item["identifier"])
            f = open("netease_items_beh/" + item["name"] + ".json", "w")
            f.write(json)
            f.close()

        elif item["type"] == "plant":
            create_crop(item)

        lootTableJson = """
{
    "pools": [
        {
            "entries": [
                {
                    "functions": [
                        {
                            "count": {
                                "max": %s,
                                "min": %s
                            },
                            "function": "set_count"
                        },
                        {
                            "data": %s,
                            "function": "set_data"
                        },
                        {
                            "function": "looting_enchant",
                            "count": {
                                "min": 0,
                                "max": 1
                            }
                        }
                    ],
                    "name": "%s",
                    "type": "item",
                    "weight": 1
                }
            ],
            "rolls": 1
        }
    ]
}
"""
        if "loot_tables" in item:
            f = open("loot_tables/netease/" + item["name"] + ".json", "w")
            f.write(lootTableJson % (item["loot_tables"]["max"],
                                     item["loot_tables"]["min"],
                                     item["loot_tables"]["data"],
                                     "mwh_pam:" + str.lower(
                                         item["loot_tables"]["name"]).replace(" ", "_")
                                     if "minecraft:" not in item["loot_tables"]["name"] else
                                     item["loot_tables"]["name"])

                    if "loot_tables" in item and item["loot_tables"] else "")
            f.close()
