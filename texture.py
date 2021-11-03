# coding=utf-8
def toolTexture(itemList):
    blocks = """
    {
        "format_version": [
            1,
            1,
            0
        ],
        %s
    }"""
    blockItem = """
    "%s": {
        "sound": "%s",
        "textures": {
            "down": "%s",
            "up": "%s",
            "side": "%s"
        }
    }
        """
    plantItem = """
"%s": {
    "sound": "%s",
    "netease_model": "%s"
}
    """
    blockTextureJson = \
        """
{
    "resource_pack_name": "vanilla",
    "texture_data": {
        %s
    },
    "texture_name": "atlas.terrain"
}
        """
    blockTexture_item = """
"%s": {
    "textures": "textures/blocks/%s"
}
    """

    itemTexture = \
        """{
            "resource_pack_name": "vanilla",
            "texture_data": {
                %s
            },
            "texture_name": "atlas.items"
        }"""

    texture_data = """
    "%s": {
        "textures": "textures/items/%s"
    }
    """
    texture_datas = ""
    itemIndex = 0
    blockIndex = 0
    blockTexture_index = 0
    blocks_datas = ""
    blockTexture_datas = ""
    for item in itemList:
        texture = str(item["name"])
        # .replace("material_", "") \
        # .replace("sblock", "") \
        # .replace("mineral_", "") \
        # .replace("gemstone_", "") \
        # .replace("inweapon_", "") \
        # .replace("slate_", "") \
        # .replace("cannons_", "") \
        # .replace("seed_", "") \
        # .replace("boss_", "") \
        # .replace("skillsmaterials_", "") \
        # .replace("callboard_", "") \
        # .replace("currency_", "") \
        # .replace("ammunition_", "") \
        # .replace("sundries_", "") \
        # .replace("halfbrick_", "") \
        # .replace("staircase_", "") \
        # .replace("fence_", "") \
        # .replace("banner_", "") \
        # .replace("missile_", "") \
        # .replace("uppack_", "") \
        # .replace("plant_", "") \
        # .replace("sitems_", "") \
        # .replace("coloredegg_", "") \
        # .replace("ore_", "") \
        # .replace("lamp_", "") \
        # .replace("altar_", "") \
        # .replace("enhancer_", "") \
        # .replace("funblock_", "") \
        # .replace("brushbox_", "") \
        # .replace("statue_", "") \
        # .replace("portal_", "") \
        # .replace("tool_", "") \
        # .replace("dagger_", "") \
        # .replace("gsword_", "") \
        # .replace("hammer_", "") \
        # .replace("crossbow_", "") \
        # .replace("bow_", "") \
        # .replace("blastergun_", "") \
        # .replace("shotgun_", "") \
        # .replace("gun_", "") \
        # .replace("sniperrifle_", "") \
        # .replace("turbidstaff_", "") \
        # .replace("staff_", "") \
        # .replace("armor_", "") \
        # .replace("food_", "") \
        # .replace("flag_", "")
        #
        # if "kaiyu_temple" not in texture:
        #     texture = texture.replace("block_", "")
        # else:
        #     texture = texture.replace("block_kaiyu", "kaiyu")

        block_texture = texture.replace("_stairs", "") \
            .replace("_gate", "planks") \
            .replace("_slab", "")

        if item["type"] in ["helmet", "chestplate", "leggings", "boots"]:
            metal = texture.replace("_boots", "") \
                .replace("_leggings", "") \
                .replace("_helmet", "") \
                .replace("_chestplate", "")
            json = """
            {
                "format_version": "1.8.0",
                "minecraft:attachable": {
                    "description": {
                        "geometry": {
                            "default": "geometry.humanoid.armor.%s"
                        },
                        "identifier": "%s",
                        "materials": {
                            "default": "armor",
                            "enchanted": "armor_enchanted"
                        },
                        "render_controllers": [
                            "controller.render.armor"
                        ],
                        "scripts": {
                            "parent_setup": "variable.boot_layer_visible = 0.0;"
                        },
                        "textures": {
                            "default": "textures/models/armor/%s",
                            "enchanted": "textures/misc/enchanted_item_glint"
                        }
                    }
                }
            }""" % (item["type"], item["identifier"], "%s_%s" % (metal, "legs" if item["type"] == "leggings" else ""))
            f = open("attachables/" + item["name"] + ".json", "w")
            f.write(json)
            f.close()
            resJson = """
                            {
                                "format_version": "1.10",
                                "minecraft:item": {
                                    "components": {
                                        "minecraft:icon": "%s"
                                    },
                                    "description": {
                                        "identifier": "%s"
                                    }
                                }
                            }
                        """ % (item["identifier"], item["identifier"])
            if itemIndex == 0:
                texture_datas = texture_datas + texture_data % (item["identifier"], texture)
            else:
                texture_datas = texture_datas + "," + texture_data % (
                    item["identifier"], texture)
            itemIndex += 1
            f = open("netease_items_res/" + item["name"] + ".json", "w")
            f.write(resJson)
            f.close()
        elif item["type"] in ["item", "sword", "hatchet", "hoe", "pickaxe", "shovel"]:
            json = """
                {
                    "format_version": "1.10",
                    "minecraft:item": {
                        "components": {
                            "minecraft:icon": "%s"
                        },
                        "description": {
                            "identifier": "%s"
                        }
                    }
                }
            """ % (item["identifier"], item["identifier"])
            if itemIndex == 0:
                texture_datas = texture_datas + texture_data % (item["identifier"], texture)
            else:
                texture_datas = texture_datas + "," + texture_data % (item["identifier"], texture)
            itemIndex += 1
            f = open("netease_items_res/" + item["name"] + ".json", "w")
            f.write(json)
            f.close()
        elif item["type"] in ["food"]:
            json = """
                {
                    "format_version": "1.10",
                    "minecraft:item": {
                        "components": {
                            "minecraft:use_animation": "eat",
                            "minecraft:icon": "%s"
                        },
                        "description": {
                            "identifier": "%s"
                        }
                    }
                }
            """ % (item["identifier"], item["identifier"])
            if itemIndex == 0:
                texture_datas = texture_datas + texture_data % (item["identifier"], texture)
            else:
                texture_datas = texture_datas + "," + texture_data % (item["identifier"], texture)
            itemIndex += 1
            f = open("netease_items_res/" + item["name"] + ".json", "w")
            f.write(json)
            f.close()
        elif item["type"] in ["block", "normal"]:
            if "声音" in item:
                item["sound"] = item["声音"]
                del item["声音"]
            if "贴图相同" in item:
                item["textures"] = item["贴图相同"]
                del item["贴图相同"]
            if "textures" in item and item["textures"] == "true":
                blockTexture = blockItem % (item["identifier"],
                                            item["sound"],
                                            item["identifier"],
                                            item["identifier"],
                                            item["identifier"]
                                            )
                if blockTexture_index == 0:
                    blockTexture_datas = blockTexture_datas + blockTexture_item % (item["identifier"], block_texture)
                else:
                    blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (
                        item["identifier"], block_texture)
            else:
                blockTexture = blockItem % (item["identifier"],
                                            item["sound"],
                                            item["identifier"] + "_down",
                                            item["identifier"] + "_up",
                                            item["identifier"] + "_side",
                                            )

                if blockTexture_index == 0:
                    blockTexture_datas = blockTexture_datas + blockTexture_item % (item["identifier"] + "_down",
                                                                                   texture + "_up")
                    blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (item["identifier"] + "_up",
                                                                                         texture + "_up")
                    blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (item["identifier"] + "_side",
                                                                                         texture + "_side")
                else:
                    blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (item["identifier"] + "_down",
                                                                                         texture + "_up")
                    blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (item["identifier"] + "_up",
                                                                                         texture + "_up")
                    blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (item["identifier"] + "_side",
                                                                                         texture + "_side")

            if blockIndex == 0:
                blocks_datas = blocks_datas + blockTexture
            else:
                blocks_datas = blocks_datas + "," + blockTexture

            blockIndex += 1
            blockTexture_index += 1
        elif item["type"] in ["typex", "carpet"]:

            if item["type"] == "carpet":
                carpetJson = """
                {
                    "format_version": "1.13.0",
                    "netease:block_geometry": {
                        "bones": [
                            {
                                "cubes": [
                                    {
                                        "origin": [
                                            -16,
                                            0,
                                            0
                                        ],
                                        "pivot": [
                                            0,
                                            0,
                                            0
                                        ],
                                        "rotation": [
                                            0,
                                            0,
                                            0
                                        ],
                                        "size": [
                                            16,
                                            1,
                                            16
                                        ],
                                        "uv": {
                                            "down": {
                                                "texture": 0,
                                                "uv": [
                                                    0,
                                                    0
                                                ],
                                                "uv_size": [
                                                    16,
                                                    16
                                                ]
                                            },
                                            "east": {
                                                "texture": 0,
                                                "uv": [
                                                    0,
                                                    0
                                                ],
                                                "uv_size": [
                                                    16,
                                                    1
                                                ]
                                            },
                                            "north": {
                                                "texture": 0,
                                                "uv": [
                                                    0,
                                                    0
                                                ],
                                                "uv_size": [
                                                    16,
                                                    1
                                                ]
                                            },
                                            "south": {
                                                "texture": 0,
                                                "uv": [
                                                    0,
                                                    0
                                                ],
                                                "uv_size": [
                                                    16,
                                                    1
                                                ]
                                            },
                                            "up": {
                                                "texture": 0,
                                                "uv": [
                                                    16,
                                                    16
                                                ],
                                                "uv_size": [
                                                    -16,
                                                    -16
                                                ]
                                            },
                                            "west": {
                                                "texture": 0,
                                                "uv": [
                                                    0,
                                                    0
                                                ],
                                                "uv_size": [
                                                    16,
                                                    1
                                                ]
                                            }
                                        }
                                    }
                                ],
                                "name": "unknown_bone",
                                "pivot": [
                                    0,
                                    0,
                                    0
                                ]
                            }
                        ],
                        "description": {
                            "identifier": "%s",
                            "textures": [
                                "%s"
                            ],
                            "use_ao": true
                        }
                    }
                }""" % (item["identifier"],
                        item["identifier"])
                f = open("models/netease_block/" + item["name"] + ".json", "w")
                f.write(carpetJson)
                f.close()

            elif item["type"] == "typex":
                typexJson = """
    {
        "format_version": "1.13.0",
        "netease:block_geometry": 
            {
                "description": {
                    "identifier": "%s",
                    "textures": ["%s"],
                    "item_texture": "%s"
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
    }""" % (
                    item["identifier"],
                    item["identifier"],
                    item["identifier"])
                f = open("models/netease_block/" + item["name"] + ".json", "w")
                f.write(typexJson)
                f.close()

            if "声音" in item:
                item["sound"] = item["声音"]
                del item["声音"]

            plantTexture = plantItem % (item["identifier"],
                                        item["sound"],
                                        item["identifier"]
                                        )
            if blockTexture_index == 0:
                blockTexture_datas = blockTexture_datas + blockTexture_item % (item["identifier"], block_texture)
            else:
                blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (
                    item["identifier"], block_texture)
            if blockIndex == 0:
                blocks_datas = blocks_datas + plantTexture
            else:
                blocks_datas = blocks_datas + "," + plantTexture
            blockIndex += 1
            blockTexture_index += 1
        elif item["type"] == "halfbrick":
            halfbrickDownJson = """
            {
                "format_version": "1.13.0",
                "netease:block_geometry": {
                    "bones": [
                        {
                            "cubes": [
                                {
                                    "origin": [
                                        -16,
                                        0,
                                        0
                                    ],
                                    "pivot": [
                                        0,
                                        0,
                                        0
                                    ],
                                    "rotation": [
                                        0,
                                        0,
                                        0
                                    ],
                                    "size": [
                                        16,
                                        8,
                                        16
                                    ],
                                    "uv": {
                                        "down": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                0
                                            ],
                                            "uv_size": [
                                                16,
                                                16
                                            ]
                                        },
                                        "east": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                8
                                            ],
                                            "uv_size": [
                                                16,
                                                8
                                            ]
                                        },
                                        "north": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                8
                                            ],
                                            "uv_size": [
                                                16,
                                                8
                                            ]
                                        },
                                        "south": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                8
                                            ],
                                            "uv_size": [
                                                16,
                                                8
                                            ]
                                        },
                                        "up": {
                                            "texture": 0,
                                            "uv": [
                                                16,
                                                16
                                            ],
                                            "uv_size": [
                                                -16,
                                                -16
                                            ]
                                        },
                                        "west": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                0
                                            ],
                                            "uv_size": [
                                                16,
                                                8
                                            ]
                                        }
                                    }
                                }
                            ],
                            "name": "unknown_bone",
                            "pivot": [
                                0,
                                0,
                                0
                            ]
                        }
                    ],
                    "description": {
                        "identifier": "%s",
                        "textures": [
                            "%s"
                        ],
                        "use_ao": true
                    }
                }
            }""" % (
                item["identifier"],
                item["identifier"])
            f = open("models/netease_block/" + item["name"] + ".json", "w")
            f.write(halfbrickDownJson)
            f.close()
            halfbrickTopJson = """
            {
                "format_version": "1.13.0",
                "netease:block_geometry": {
                    "bones": [
                        {
                            "cubes": [
                                {
                                    "origin": [
                                        -16,
                                        8,
                                        0
                                    ],
                                    "pivot": [
                                        0,
                                        8,
                                        0
                                    ],
                                    "rotation": [
                                        0,
                                        0,
                                        0
                                    ],
                                    "size": [
                                        16,
                                        8,
                                        16
                                    ],
                                    "uv": {
                                        "down": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                0
                                            ],
                                            "uv_size": [
                                                16,
                                                16
                                            ]
                                        },
                                        "east": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                0
                                            ],
                                            "uv_size": [
                                                16,
                                                8
                                            ]
                                        },
                                        "north": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                0
                                            ],
                                            "uv_size": [
                                                16,
                                                8
                                            ]
                                        },
                                        "south": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                0
                                            ],
                                            "uv_size": [
                                                16,
                                                8
                                            ]
                                        },
                                        "up": {
                                            "texture": 0,
                                            "uv": [
                                                16,
                                                16
                                            ],
                                            "uv_size": [
                                                -16,
                                                -16
                                            ]
                                        },
                                        "west": {
                                            "texture": 0,
                                            "uv": [
                                                0,
                                                0
                                            ],
                                            "uv_size": [
                                                16,
                                                8
                                            ]
                                        }
                                    }
                                }
                            ],
                            "name": "unknown_bone",
                            "pivot": [
                                0,
                                0,
                                0
                            ]
                        }
                    ],
                    "description": {
                        "identifier": "%s",
                        "textures": [
                            "%s"
                        ],
                        "use_ao": true
                    }
                }
            }""" % (
                item["identifier"] + "_top",
                item["identifier"])
            f = open("models/netease_block/" + item["name"] + "_top.json", "w")
            f.write(halfbrickTopJson)
            f.close()

            if "声音" in item:
                item["sound"] = item["声音"]
                del item["声音"]

            if blockTexture_index == 0:
                blockTexture_datas = blockTexture_datas + blockTexture_item % (
                    item["identifier"], block_texture + "_planks" if "木" in item["zh_CN"] else block_texture)
            else:
                blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (
                    item["identifier"], block_texture + "_planks" if "木" in item["zh_CN"] else block_texture)

            if blockIndex == 0:
                blocks_datas = blocks_datas + plantItem % (item["identifier"],
                                                           item["sound"],
                                                           item["identifier"]
                                                           )
                blocks_datas = blocks_datas + plantItem % (item["identifier"] + "_top",
                                                           item["sound"],
                                                           item["identifier"] + "_top"
                                                           )
            else:
                blocks_datas = blocks_datas + "," + plantItem % (item["identifier"],
                                                                 item["sound"],
                                                                 item["identifier"]
                                                                 )
                blocks_datas = blocks_datas + "," + plantItem % (item["identifier"] + "_top",
                                                                 item["sound"],
                                                                 item["identifier"] + "_top"
                                                                 )

            blockIndex += 1
            blockTexture_index += 1
        elif item["type"] in ["banner", "flag"]:
            bannerJson = """
{
    "format_version": "1.13.0",
    "netease:block_geometry": {
        "bones": [
            {
                "cubes": [
                    {
                        "origin": [
                            -2.0,
                            28.5,
                            5.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2.5,
                            2.5,
                            2.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    1.875,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0.625
                                ],
                                "uv_size": [
                                    -0.625,
                                    -0.625
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -16.5,
                            28.5,
                            5.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2.5,
                            2.5,
                            2.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    1.875,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0.625
                                ],
                                "uv_size": [
                                    -0.625,
                                    -0.625
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -14.5,
                            29,
                            5.75
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6.5,
                            1.5,
                            1.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.375
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    1.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.375
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.375,
                                    1.75
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.75
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.75
                                ],
                                "uv_size": [
                                    -1.625,
                                    -0.375
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    3.625,
                                    1.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.375
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -8.0,
                            29,
                            5.75
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6.5,
                            1.5,
                            1.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.375
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    1.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.375
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.375,
                                    1.75
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.75
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.75
                                ],
                                "uv_size": [
                                    -1.625,
                                    -0.375
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    3.625,
                                    1.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.375
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -13,
                            5.5,
                            6.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            10,
                            24.0,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    8.625
                                ],
                                "uv_size": [
                                    2.5,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    2.75
                                ],
                                "uv_size": [
                                    0.125,
                                    6.0
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    2.75
                                ],
                                "uv_size": [
                                    2.5,
                                    6.0
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2.5,
                                    2.75
                                ],
                                "uv_size": [
                                    2.5,
                                    6.0
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    2.375,
                                    2.75
                                ],
                                "uv_size": [
                                    0.125,
                                    6.0
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -12,
                            4.5,
                            6.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            8,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.25,
                                    8.875
                                ],
                                "uv_size": [
                                    2.0,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.25,
                                    8.875
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.25,
                                    8.875
                                ],
                                "uv_size": [
                                    2.0,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2.75,
                                    8.875
                                ],
                                "uv_size": [
                                    2.0,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    2.125,
                                    8.875
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -12.5,
                            5,
                            6.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            9.0,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.125,
                                    8.75
                                ],
                                "uv_size": [
                                    2.25,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.125,
                                    8.75
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.125,
                                    8.75
                                ],
                                "uv_size": [
                                    2.25,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2.625,
                                    8.75
                                ],
                                "uv_size": [
                                    2.25,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    2.25,
                                    8.75
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -11.5,
                            4,
                            6.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            7.0,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    0,
                                    0
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.375,
                                    9
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.375,
                                    9
                                ],
                                "uv_size": [
                                    1.75,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2.875,
                                    9
                                ],
                                "uv_size": [
                                    1.75,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    9
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -11,
                            3.5,
                            6.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.5,
                                    9.125
                                ],
                                "uv_size": [
                                    1.5,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.5,
                                    9.125
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.5,
                                    9.125
                                ],
                                "uv_size": [
                                    1.5,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3,
                                    9.125
                                ],
                                "uv_size": [
                                    1.5,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.875,
                                    9.125
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -10.5,
                            3,
                            6.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            5.0,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    9.25
                                ],
                                "uv_size": [
                                    1.25,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    9.25
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    9.25
                                ],
                                "uv_size": [
                                    1.25,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.125,
                                    9.25
                                ],
                                "uv_size": [
                                    1.25,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.75,
                                    9.25
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -10,
                            2.5,
                            6.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            4,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.75,
                                    9.375
                                ],
                                "uv_size": [
                                    1.0,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.75,
                                    9.375
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.75,
                                    9.375
                                ],
                                "uv_size": [
                                    1.0,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.25,
                                    9.375
                                ],
                                "uv_size": [
                                    1.0,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.625,
                                    9.375
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -9.5,
                            2,
                            6.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            3.0,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.875,
                                    9.5
                                ],
                                "uv_size": [
                                    0.75,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.875,
                                    9.5
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.875,
                                    9.5
                                ],
                                "uv_size": [
                                    0.75,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.375,
                                    9.5
                                ],
                                "uv_size": [
                                    0.75,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.5,
                                    9.5
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -9,
                            1.5,
                            6.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    1,
                                    9.625
                                ],
                                "uv_size": [
                                    0.5,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    1,
                                    9.625
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    1,
                                    9.625
                                ],
                                "uv_size": [
                                    0.5,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.5,
                                    9.625
                                ],
                                "uv_size": [
                                    0.5,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.375,
                                    9.625
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -8.75,
                            29.5,
                            7.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            1.5,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    2.75,
                                    1
                                ],
                                "uv_size": [
                                    0.375,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    2.625,
                                    1.125
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.125,
                                    1.125
                                ],
                                "uv_size": [
                                    0.375,
                                    0.125
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    3.5,
                                    1.125
                                ],
                                "uv_size": [
                                    -0.375,
                                    -0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    3.5,
                                    1.125
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -8.75,
                            29,
                            7.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            1.5,
                            0.5,
                            1.0
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    3.25,
                                    0.5
                                ],
                                "uv_size": [
                                    0.375,
                                    0.25
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    2.625,
                                    0.75
                                ],
                                "uv_size": [
                                    0.25,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    3.25,
                                    0.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.625,
                                    0.75
                                ],
                                "uv_size": [
                                    0.25,
                                    0.125
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    3.25,
                                    0.75
                                ],
                                "uv_size": [
                                    -0.375,
                                    -0.25
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    3.25,
                                    0.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -8.75,
                            0,
                            7.25
                        ],
                        "pivot": [
                            -8,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            1.5,
                            29,
                            1.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    5.5,
                                    7.625
                                ],
                                "uv_size": [
                                    0.375,
                                    0.375
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    5.125,
                                    0.375
                                ],
                                "uv_size": [
                                    0.375,
                                    7.25
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    5.5,
                                    0.375
                                ],
                                "uv_size": [
                                    0.375,
                                    7.25
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    6.25,
                                    0.375
                                ],
                                "uv_size": [
                                    0.375,
                                    7.25
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    5.875,
                                    0.375
                                ],
                                "uv_size": [
                                    -0.375,
                                    -0.375
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    5.875,
                                    0.375
                                ],
                                "uv_size": [
                                    0.375,
                                    7.25
                                ]
                            }
                        }
                    }
                ],
                "name": "bone",
                "pivot": [
                    0,
                    0,
                    0
                ],
                "rotation": [
                    0,
                    0,
                    0
                ]
            }
        ],
        "description": {
            "identifier": "%s",
            "textures": [
                "%s"
            ],
            "use_ao": true
        }
    }
}""" % (
                item["identifier"],
                item["identifier"])
            f = open("models/netease_block/" + item["name"] + ".json", "w")
            f.write(bannerJson)
            f.close()

            bannerOnWallJson = """
{
    "format_version": "1.13.0",
    "netease:block_geometry": {
        "bones": [
            {
                "cubes": [
                    {
                        "origin": [
                            -2.0,
                            29.5,
                            0.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2.5,
                            2.5,
                            2.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    1.875,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0.625
                                ],
                                "uv_size": [
                                    -0.625,
                                    -0.625
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -16.5,
                            29.5,
                            0.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2.5,
                            2.5,
                            2.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    1.875,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0.625
                                ],
                                "uv_size": [
                                    -0.625,
                                    -0.625
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.25,
                                    0.625
                                ],
                                "uv_size": [
                                    0.625,
                                    0.625
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -14.5,
                            30,
                            0.75
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6.5,
                            1.5,
                            1.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.375
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    1.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.375
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.375,
                                    1.75
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.75
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.75
                                ],
                                "uv_size": [
                                    -1.625,
                                    -0.375
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    3.625,
                                    1.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.375
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -8.0,
                            30,
                            0.75
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6.5,
                            1.5,
                            1.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.375
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    1.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.375
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.375,
                                    1.75
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.75
                                ],
                                "uv_size": [
                                    1.625,
                                    0.375
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    1.75
                                ],
                                "uv_size": [
                                    -1.625,
                                    -0.375
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    3.625,
                                    1.75
                                ],
                                "uv_size": [
                                    0.375,
                                    0.375
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -13,
                            6.5,
                            1.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            10,
                            24.0,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    8.625
                                ],
                                "uv_size": [
                                    2.5,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    2.75
                                ],
                                "uv_size": [
                                    0.125,
                                    6.0
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    2.75
                                ],
                                "uv_size": [
                                    2.5,
                                    6.0
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2.5,
                                    2.75
                                ],
                                "uv_size": [
                                    2.5,
                                    6.0
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    2.375,
                                    2.75
                                ],
                                "uv_size": [
                                    0.125,
                                    6.0
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -12,
                            5.5,
                            1.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            8,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.25,
                                    8.875
                                ],
                                "uv_size": [
                                    2.0,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.25,
                                    8.875
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.25,
                                    8.875
                                ],
                                "uv_size": [
                                    2.0,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2.75,
                                    8.875
                                ],
                                "uv_size": [
                                    2.0,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    2.125,
                                    8.875
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -12.5,
                            6,
                            1.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            9.0,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.125,
                                    8.75
                                ],
                                "uv_size": [
                                    2.25,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.125,
                                    8.75
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.125,
                                    8.75
                                ],
                                "uv_size": [
                                    2.25,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2.625,
                                    8.75
                                ],
                                "uv_size": [
                                    2.25,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    2.25,
                                    8.75
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -11.5,
                            5,
                            1.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            7.0,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    0,
                                    0
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.375,
                                    9
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.375,
                                    9
                                ],
                                "uv_size": [
                                    1.75,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    2.875,
                                    9
                                ],
                                "uv_size": [
                                    1.75,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    9
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -11,
                            4.5,
                            1.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.5,
                                    9.125
                                ],
                                "uv_size": [
                                    1.5,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.5,
                                    9.125
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.5,
                                    9.125
                                ],
                                "uv_size": [
                                    1.5,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3,
                                    9.125
                                ],
                                "uv_size": [
                                    1.5,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.875,
                                    9.125
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -10.5,
                            4,
                            1.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            5.0,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    9.25
                                ],
                                "uv_size": [
                                    1.25,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    9.25
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.625,
                                    9.25
                                ],
                                "uv_size": [
                                    1.25,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.125,
                                    9.25
                                ],
                                "uv_size": [
                                    1.25,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.75,
                                    9.25
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -10,
                            3.5,
                            1.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            4,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.75,
                                    9.375
                                ],
                                "uv_size": [
                                    1.0,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.75,
                                    9.375
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.75,
                                    9.375
                                ],
                                "uv_size": [
                                    1.0,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.25,
                                    9.375
                                ],
                                "uv_size": [
                                    1.0,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.625,
                                    9.375
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -9.5,
                            3,
                            1.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            3.0,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0.875,
                                    9.5
                                ],
                                "uv_size": [
                                    0.75,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0.875,
                                    9.5
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0.875,
                                    9.5
                                ],
                                "uv_size": [
                                    0.75,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.375,
                                    9.5
                                ],
                                "uv_size": [
                                    0.75,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.5,
                                    9.5
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -9,
                            2.5,
                            1.25
                        ],
                        "pivot": [
                            -8,
                            9,
                            3
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2,
                            0.5,
                            0.5
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    1,
                                    9.625
                                ],
                                "uv_size": [
                                    0.5,
                                    0.125
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    1,
                                    9.625
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    1,
                                    9.625
                                ],
                                "uv_size": [
                                    0.5,
                                    0.125
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    3.5,
                                    9.625
                                ],
                                "uv_size": [
                                    0.5,
                                    0.125
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    1.375,
                                    9.625
                                ],
                                "uv_size": [
                                    0.125,
                                    0.125
                                ]
                            }
                        }
                    }
                ],
                "name": "bone",
                "pivot": [
                    0,
                    1,
                    -5
                ],
                "rotation": [
                    0,
                    0,
                    0
                ]
            }
        ],
        "description": {
            "identifier": "%s",
            "textures": [
                "%s"
            ],
            "use_ao": true
        }
    }
}""" % (
                item["identifier"] + "_wall",
                item["identifier"])
            f = open("models/netease_block/" + item["name"] + "_wall.json", "w")
            f.write(bannerOnWallJson)
            f.close()

            if "声音" in item:
                item["sound"] = item["声音"]
                del item["声音"]

            if blockTexture_index == 0:
                blockTexture_datas = blockTexture_datas + blockTexture_item % (item["identifier"], block_texture)
            else:
                blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (
                    item["identifier"], block_texture)

            if blockIndex == 0:
                blocks_datas = blocks_datas + plantItem % (item["identifier"],
                                                           item["sound"],
                                                           item["identifier"]
                                                           )
                blocks_datas = blocks_datas + plantItem % (item["identifier"] + "_wall",
                                                           item["sound"],
                                                           item["identifier"]
                                                           )
            else:
                blocks_datas = blocks_datas + "," + plantItem % (item["identifier"],
                                                                 item["sound"],
                                                                 item["identifier"]
                                                                 )
                blocks_datas = blocks_datas + "," + plantItem % (item["identifier"] + "_wall",
                                                                 item["sound"],
                                                                 item["identifier"]
                                                                 )

            blockIndex += 1
            blockTexture_index += 1
        elif item["type"] == "staircase":
            staircaseJson = """
{
    "format_version": "1.13.0",
    "netease:block_geometry": {
        "bones": [
            {
                "cubes": [
                    {
                        "origin": [
                            -16,
                            0,
                            0
                        ],
                        "pivot": [
                            0,
                            0,
                            0
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            16,
                            8,
                            16
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    16,
                                    16
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    8
                                ],
                                "uv_size": [
                                    16,
                                    8
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    16,
                                    8
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    8
                                ],
                                "uv_size": [
                                    16,
                                    8
                                ]
                            },
                            "up": {
                                "rot": 90,
                                "texture": 0,
                                "uv": [
                                    16,
                                    16
                                ],
                                "uv_size": [
                                    -16,
                                    -16
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    8
                                ],
                                "uv_size": [
                                    16,
                                    8
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -16,
                            8,
                            8
                        ],
                        "pivot": [
                            0,
                            8,
                            8
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            16,
                            8,
                            8
                        ],
                        "uv": {
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    8,
                                    8
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    16,
                                    8
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    16,
                                    8
                                ]
                            },
                            "up": {
                                "rot": 90,
                                "texture": 0,
                                "uv": [
                                    16,
                                    8
                                ],
                                "uv_size": [
                                    -16,
                                    -8
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    8,
                                    8
                                ]
                            }
                        }
                    }
                ],
                "name": "unknown_bone",
                "pivot": [
                    0,
                    0,
                    0
                ]
            }
        ],
        "description": {
            "identifier": "%s",
            "textures": [
                "%s"
            ],
            "use_ao": true
        }
    }
}""" % (item["identifier"], item["identifier"])

            f = open("models/netease_block/" + item["name"] + ".json", "w")
            f.write(staircaseJson)
            f.close()

            if "声音" in item:
                item["sound"] = item["声音"]
                del item["声音"]

            plantTexture = plantItem % (item["identifier"],
                                        item["sound"],
                                        item["identifier"]
                                        )
            if blockTexture_index == 0:
                blockTexture_datas = blockTexture_datas + blockTexture_item % (
                    item["identifier"], block_texture + "_planks" if "木" in item["zh_CN"] else block_texture)
            else:
                blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (
                    item["identifier"], block_texture + "_planks" if "木" in item["zh_CN"] else block_texture)
            if blockIndex == 0:
                blocks_datas = blocks_datas + plantTexture
            else:
                blocks_datas = blocks_datas + "," + plantTexture
            blockIndex += 1
            blockTexture_index += 1
        elif item["type"] == "fence":
            fenceJson = """
{
    "format_version": "1.13.0",
    "netease:block_geometry": {
        "bones": [
            {
                "cubes": [
                    {
                        "origin": [
                            -10,
                            0,
                            6
                        ],
                        "pivot": [
                            -6,
                            0,
                            6
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            4,
                            16,
                            4
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    6,
                                    6
                                ],
                                "uv_size": [
                                    4,
                                    4
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    6,
                                    0
                                ],
                                "uv_size": [
                                    4,
                                    16
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    6,
                                    0
                                ],
                                "uv_size": [
                                    4,
                                    16
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    6,
                                    0
                                ],
                                "uv_size": [
                                    4,
                                    16
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    10,
                                    9
                                ],
                                "uv_size": [
                                    -4,
                                    -4
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    6,
                                    0
                                ],
                                "uv_size": [
                                    4,
                                    16
                                ]
                            }
                        }
                    }
                ],
                "name": "unknown_bone",
                "pivot": [
                    0,
                    0,
                    0
                ]
            },
            {
                "cubes": [
                    {
                        "origin": [
                            -9,
                            12,
                            10
                        ],
                        "pivot": [
                            -7,
                            12,
                            10
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2,
                            3,
                            6
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    2,
                                    6
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    6
                                ],
                                "uv_size": [
                                    -2,
                                    -6
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    10,
                                    1
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -9,
                            6,
                            10
                        ],
                        "pivot": [
                            -7,
                            6,
                            10
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2,
                            3,
                            6
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    2,
                                    6
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    6
                                ],
                                "uv_size": [
                                    -2,
                                    -6
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    10,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            }
                        }
                    }
                ],
                "name": "south",
				"enable": "query.is_connect(3)",
                "pivot": [
                    0,
                    0,
                    0
                ],
                "rotation": [
                    0,
                    0,
                    0
                ]
            },
            {
                "cubes": [
                    {
                        "origin": [
                            -16,
                            12,
                            7
                        ],
                        "pivot": [
                            -10,
                            12,
                            7
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6,
                            3,
                            2
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    2
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    1
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    10,
                                    1
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    16,
                                    9
                                ],
                                "uv_size": [
                                    -6,
                                    -2
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -16,
                            6,
                            7
                        ],
                        "pivot": [
                            -10,
                            6,
                            7
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6,
                            3,
                            2
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    2
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    10,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    6,
                                    9
                                ],
                                "uv_size": [
                                    -6,
                                    -2
                                ]
                            }
                        }
                    }
                ],
                "name": "east",
				"enable": "query.is_connect(5)",
                "pivot": [
                    -8,
                    12,
                    0
                ],
                "rotation": [
                    0,
                    0,
                    0
                ]
            },
            {
                "cubes": [
                    {
                        "origin": [
                            -9,
                            6,
                            0
                        ],
                        "pivot": [
                            -7,
                            6,
                            0
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2,
                            3,
                            6
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    2,
                                    6
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    2,
                                    3
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    6
                                ],
                                "uv_size": [
                                    -2,
                                    -6
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -9,
                            12,
                            0
                        ],
                        "pivot": [
                            -7,
                            12,
                            0
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            2,
                            3,
                            6
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    2,
                                    6
                                ]
                            },
                            "east": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    0
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    2,
                                    6
                                ],
                                "uv_size": [
                                    -2,
                                    -6
                                ]
                            },
                            "west": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    1
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            }
                        }
                    }
                ],
                "name": "north",
				"enable": "query.is_connect(2)",
                "pivot": [
                    0,
                    0,
                    0
                ],
                "rotation": [
                    0,
                    0,
                    0
                ]
            },
            {
                "cubes": [
                    {
                        "origin": [
                            -6,
                            6,
                            7
                        ],
                        "pivot": [
                            0,
                            7,
                            7
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6,
                            3,
                            2
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    10,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    2
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    10,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    16,
                                    9
                                ],
                                "uv_size": [
                                    -6,
                                    -2
                                ]
                            }
                        }
                    },
                    {
                        "origin": [
                            -6,
                            12,
                            7
                        ],
                        "pivot": [
                            0,
                            13,
                            7
                        ],
                        "rotation": [
                            0,
                            0,
                            0
                        ],
                        "size": [
                            6,
                            3,
                            2
                        ],
                        "uv": {
                            "down": {
                                "texture": 0,
                                "uv": [
                                    10,
                                    7
                                ],
                                "uv_size": [
                                    6,
                                    2
                                ]
                            },
                            "north": {
                                "texture": 0,
                                "uv": [
                                    10,
                                    1
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "south": {
                                "texture": 0,
                                "uv": [
                                    0,
                                    1
                                ],
                                "uv_size": [
                                    6,
                                    3
                                ]
                            },
                            "up": {
                                "texture": 0,
                                "uv": [
                                    6,
                                    9
                                ],
                                "uv_size": [
                                    -6,
                                    -2
                                ]
                            }
                        }
                    }
                ],
                "name": "west",
				"enable": "query.is_connect(4)",
                "pivot": [
                    0,
                    0,
                    0
                ],
                "rotation": [
                    0,
                    0,
                    0
                ]
            }
        ],
        "description": {
            "identifier": "%s",
            "textures": [
                "%s"
            ],
            "use_ao": true
        }
    }
}""" % (item["identifier"], str(item["identifier"]).replace("fence", "planks"))

            f = open("models/netease_block/" + item["name"] + ".json", "w")
            f.write(fenceJson)
            f.close()

            if "声音" in item:
                item["sound"] = item["声音"]
                del item["声音"]

            plantTexture = plantItem % (item["identifier"],
                                        item["sound"],
                                        item["identifier"]
                                        )
            if blockTexture_index == 0:
                blockTexture_datas = blockTexture_datas + blockTexture_item % (item["identifier"], block_texture.replace("fence", "planks"))
            else:
                blockTexture_datas = blockTexture_datas + "," + blockTexture_item % (
                    item["identifier"], block_texture.replace("fence", "planks"))
            if blockIndex == 0:
                blocks_datas = blocks_datas + plantTexture
            else:
                blocks_datas = blocks_datas + "," + plantTexture
            blockIndex += 1
            blockTexture_index += 1
        elif item["type"] == "shuaguaixiang":
            mob_spawnerJson = """
    "%s":{
        "textures": "mob_spawner",
        "sound": "metal"
    }
            """
            plantTexture = mob_spawnerJson % (item["identifier"])
            if blockIndex == 0:
                blocks_datas = blocks_datas + plantTexture
            else:
                blocks_datas = blocks_datas + "," + plantTexture

            blockIndex += 1
            blockTexture_index += 1
        elif item["type"] == "bow":
            bowJson = """{
    "format_version": "1.10",
    "minecraft:item": {
        "description": {
            "identifier": "%s"
        },
        "components": {
            "minecraft:icon": "%s",
            "netease:frame_animation": {
                "frame_count": 3,
                "texture_name": "%s_frame",
                "animate_in_toolbar": true
            }
        }
    }
}""" % (item["identifier"], item["identifier"], item["identifier"])
            f = open("netease_items_res/" + item["name"] + ".json", "w")
            f.write(bowJson)
            f.close()

            bowTextureJson = """
    "%s": {
      "textures": "textures/items/%s"
    },
    "%s_frame": {
      "textures": [
        "textures/items/%s_0",
        "textures/items/%s_1",
        "textures/items/%s_2"
      ]
    }"""
            if itemIndex == 0:
                texture_datas = texture_datas + bowTextureJson % (item["identifier"],
                                                                  texture,
                                                                  item["identifier"],
                                                                  texture,
                                                                  texture,
                                                                  texture)
            else:
                texture_datas = texture_datas + "," + bowTextureJson % (item["identifier"],
                                                                        texture,
                                                                        item["identifier"],
                                                                        texture,
                                                                        texture,
                                                                        texture)
            itemIndex += 1

    f = open("textures/item_texture.json", "w")
    f.write(itemTexture % texture_datas)
    f.close()
    f = open("blocks.json", "w")
    f.write(blocks % blocks_datas)
    f.close()
    f = open("textures/terrain_texture.json", "w")
    f.write(blockTextureJson % blockTexture_datas)
    f.close()
