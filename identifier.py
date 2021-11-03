# coding=utf-8
import json

from attack_speed import attack_speed
from bow_data import bow_data
from createItem import createItem
from create_cake import create_cake
from create_crop import create_crop
from crossbow_data import crossbow_data
from fruitTree import create_fruitTree
from furnace import furnace
from itemList import itemList
from note import note
from recipes import recipes
from textLang import lang
from texture import toolTexture

namespace = "mwh_pam"
newList = []


def identifier(itemList):
    toughnessStr = """toughness = %s"""
    toughness = {}
    bowAttackStr = """bowAttack = %s"""
    bowAttack = {}
    ammunitionStr = """ammunition = %s"""
    ammunition = {}
    sacrifice = {}

    addItemList = []

    for item in itemList:
        if item["type"] != "fruitTree" and item["type"] != "cake" and item["type"] != "plant":
            newList.append(item)
            if "物品名" in item:
                item["name"] = str.lower(item["物品名"]).replace(" ", "_").replace("-", "_")
                del item["物品名"]
            else:
                print item

            item["identifier"] = namespace + ":" + item["name"]
            if "自定义掉落" in item:
                item["loot_tables"] = item["自定义掉落"]
                del item["自定义掉落"]
                if "掉落最小数" in item["loot_tables"]:
                    item["loot_tables"]["min"] = item["loot_tables"]["掉落最小数"]
                    del item["loot_tables"]["掉落最小数"]
                if "掉落最大数" in item["loot_tables"]:
                    item["loot_tables"]["max"] = item["loot_tables"]["掉落最大数"]
                    del item["loot_tables"]["掉落最大数"]
                if "掉落特殊值" in item["loot_tables"]:
                    item["loot_tables"]["data"] = item["loot_tables"]["掉落特殊值"]
                    del item["loot_tables"]["掉落特殊值"]
                if "掉落物名字" in item["loot_tables"]:
                    item["loot_tables"]["name"] = item["loot_tables"]["掉落物名字"]
                    del item["loot_tables"]["掉落物名字"]
            if "转化为" in item:
                item["using_converts_to"] = item["转化为"]
                del item["<饱食度>"]

            if "饱食度" in item:
                item["nutrition"] = item["饱食度"]
                del item["饱食度"]

            if "饱和度" in item:
                item["saturation_modifier"] = item["饱和度"]
                del item["饱和度"]

            if "防御力" in item:
                item["defense"] = item["防御力"]
                del item["防御力"]

            if "韧性" in item:
                item["toughness"] = item["韧性"]
                toughness[item["identifier"]] = item["toughness"]
                del item["韧性"]

            if "附魔能力" in item:
                item["enchantment"] = item["附魔能力"]
                del item["附魔能力"]
            else:
                item["enchantment"] = 10

            if "攻击速度" in item:
                item["attack_speed"] = item["攻击速度"]
                del item["攻击速度"]

            if "速度" in item:
                item["speed"] = item["速度"]
                del item["速度"]

            if "最大耐久" in item:
                item["max_damage"] = item["最大耐久"]
                del item["最大耐久"]

            if "合成配方列表" in item:
                item["recipes"] = item["合成配方列表"]
                del item["合成配方列表"]

            if "拉弓时间" in item:
                item["use_duration"] = item["拉弓时间"]
                del item["拉弓时间"]

            if "模型类型" in item:
                item["block_type"] = item["模型类型"]
                del item["模型类型"]

            if "发光等级" in item:
                item["block_light_emission"] = item["发光等级"]
                del item["发光等级"]
            if "吸光等级" in item:
                item["block_light_absorption"] = item["吸光等级"]
                del item["吸光等级"]
            if "透明类型" in item:
                item["render_layer"] = item["透明类型"]
                del item["透明类型"]
            if "地图显示颜色" in item:
                item["map_color"] = item["地图显示颜色"]
                del item["地图显示颜色"]
            if "破坏时间" in item:
                item["destroy_time"] = item["破坏时间"]
                del item["破坏时间"]
            if "挖掘工具" in item:
                item["digger"] = item["挖掘工具"]
                del item["挖掘工具"]
            if "限制挖掘等级" in item:
                item["destroy_special"] = item["限制挖掘等级"]
                del item["限制挖掘等级"]
            if "最小挖掘等级" in item:
                item["level"] = item["最小挖掘等级"]
                del item["最小挖掘等级"]
            if "防爆等级" in item:
                item["explosion_resistance"] = item["防爆等级"]
                del item["防爆等级"]
            if "是否实心" in item:
                item["solid"] = item["是否实心"]
                del item["是否实心"]
            if "阻挡寻路" in item:
                item["pathable"] = item["阻挡寻路"]
                del item["阻挡寻路"]
            if "面向" in item:
                item["face_directional"] = item["面向"]
                del item["面向"]
            if "是否实体方块" in item:
                item["block_entity"] = item["是否实体方块"]
                del item["是否实体方块"]
            if "tick事件" in item:
                item["tick"] = item["tick事件"]
                del item["tick事件"]
            if "活塞推动" in item:
                item["movable"] = item["活塞推动"]
                del item["活塞推动"]
            if "声音" in item:
                item["sound"] = item["声音"]
                del item["声音"]
            if "贴图相同" in item:
                item["textures"] = item["贴图相同"]
                del item["贴图相同"]
            if "碰撞体积" in item:
                item["collision"] = item["碰撞体积"]
                del item["碰撞体积"]
            if "生成生物id" in item:
                item["spawn_type"] = item["生成生物id"]
                del item["生成生物id"]

            if "最大堆叠" in item:
                item["max_stack_size"] = item["最大堆叠"]
                del item["最大堆叠"]

            if "中文名" in item:
                item["zh_CN"] = item["中文名"]
                del item["中文名"]

            if "备注" in item:
                item["note"] = item["备注"]
                del item["备注"]

            if "block_type" in item:
                item["type"] = item["block_type"]

            if "level" not in item:
                item["level"] = 2

            if "speed" not in item:
                item["speed"] = 2

            if "can_always_eat" not in item:
                item["can_always_eat"] = "false"

            if "攻击力" in item:
                item["attack_damage"] = item["攻击力"]
                if item["type"] in ["bow", "crossbow"] or "Staff" in item["identifier"]:
                    bowAttack[item["identifier"]] = item["attack_damage"]
                del item["攻击力"]
            if "献祭等级" in item:
                sacrifice[item["identifier"]] = {"level": item["献祭等级"], "exp": item["给予经验"]}
            if "弹药" in item:
                ammunition[item["identifier"]] = item["弹药"]
        elif item["type"] == "fruitTree":
            create_fruitTree(item)
        elif item["type"] == "cake":
            create_cake(item)
        elif item["type"] == "plant":
            create_crop(item)

        f = open("toughness.py", "w")
        f.write(toughnessStr % toughness)
        f.close()
        f = open("ammunition.py", "w")
        f.write(ammunitionStr % json.dumps(ammunition, encoding='utf-8', ensure_ascii=False))
        f.close()
        f = open("bowAttack.py", "w")
        f.write(bowAttackStr % bowAttack)
        f.close()
        f = open("sacrifice.py", "w")
        f.write(sacrifice.__str__())
        f.close()

    # itemList = [  # 物品列表
    #     {  # 物品 1
    #         "物品名":
    #             "diamond_block",  # 物品名
    #         "note": "aaa",
    #         "max_stack_size": 64,  # 最大堆叠
    #         "type": "item",
    #         "zh_CN": "钻石块",
    #         "recipes":  # 合成配方列表
    #             [
    #                 {  # 合成表1
    #                     "materials":  # 素材列表，格子不需要物品填写 None
    #                         ["minecraft:diamond", "minecraft:diamond", "minecraft:diamond",
    #                          "minecraft:diamond", "minecraft:diamond", "minecraft:diamond",
    #                          "minecraft:diamond", "minecraft:diamond", "minecraft:diamond"],
    #                     "type": "3x3",  # 合成所需格子2x2 或 3x3
    #                     "count": 2  # 合成输出个数
    #                 },
    #                 {  # 合成表2
    #                     "materials":  # 素材列表
    #                         ["minecraft:diamond", "minecraft:diamond",
    #                          "minecraft:diamond", "minecraft:diamond"],
    #                     "type": "2x2",  # 合成所需格子2x2 或 3x3
    #                     "count": 1  # 合成输出个数
    #                 }
    #             ],
    #         "furnace": {  # 熔炉配方，如没有，则不写
    #             "input": {  # 输入物品属性
    #                 "id": "minecraft:diamond_ore",  # 输入物品id
    #                 "data": 0,  # 输入物品特殊值
    #                 "count": 1  # 输入物品个数
    #             },
    #             "output": {
    #                 "id": "minecraft:diamond",  # 输出物品id
    #                 "data": 0,  # 输出物品特殊值
    #                 "count": 1  # 输出物品个数
    #             }
    #         }
    #     },
    #     {  # 武器/工具 1
    #         "物品名":
    #             "diamond_sword",  # 物品名
    #         "max_stack_size": 1,  # 最大堆叠
    #         "type": "sword",  # 类型：剑 斧 锄 锹 镐 sword,hatchet,hoe,shovel,pickaxe
    #         "zh_CN": "钻石剑",  # 中文名
    #         "max_damage": 1800,  # 耐久
    #         "attack_damage": 7,  # 攻击伤害
    #         "enchantment": 6,  # 附魔属性，越高附魔越好
    #         "level": 3,  # 工具等级
    #         "speed": 6,  # 挖掘速度
    #         "recipes":  # 合成配方列表
    #             [
    #                 {  # 合成表1
    #                     "materials":  # 素材列表，格子不需要物品填写 None
    #                         [None, "minecraft:diamond", None,
    #                          None, "minecraft:diamond", None,
    #                          None, "minecraft:stick", None],
    #                     "type": "3x3",  # 合成所需格子2x2 或 3x3
    #                     "count": 1  # 合成输出个数
    #                 }
    #             ],
    #
    #     },
    #     {  # 食物 1
    #         "物品名":
    #             "apple",  # 物品名
    #         "max_stack_size": 64,  # 最大堆叠
    #         "type": "food",
    #         "zh_CN": "苹果",
    #
    #         "nutrition": 10,  # 食用后获得多少饥饿值
    #         "saturation_modifier": "low",  # 食物所提供的饱和度，有poor，low，normal，good，max，supernatural六个等级
    #         "using_converts_to": "minecraft:dirt",  # 没有可不写该键值对，吃完后会转化为另一个物品，例如使用甜菜汤后留下碗
    #         "cooldown_type": "chorusfruit",  # 食用后是否有冷却，如紫菘果，没有可不写该键值对
    #         "cooldown_time": "100",  # 冷却时间，如有冷却则必须写该键值对
    #         "can_always_eat": False  # 即便饱食度已满是否仍然可以吃
    #
    #     },
    # {  # 武器/工具 1
    #     "物品名":
    #         "diamond_boots",  # 物品名
    #     "max_stack_size": 1,  # 最大堆叠
    #     "type": "boots",  # 类型：剑 斧 锄 锹 镐 sword,hatchet,hoe,shovel,pickaxe
    #     "zh_CN": "钻石靴",  # 中文名
    #     "max_damage": 1800,  # 耐久
    #     "enchantment": 6,  # 附魔属性，越高附魔越好
    #     "defense": 8,  # 盔甲防御值，只有类型为helmet，cheastplate，leggings，boots时需要写
    #     "recipes":  # 合成配方列表
    #         [
    #             {  # 合成表1
    #                 "key": {"A": {"id": "minecraft:diamond", "data": 0}},
    #                 "pattern": [" A ", " A ", "A A"],
    #                 "type": "3x3",  # 合成所需格子2x2 或 3x3
    #                 "count": 1  # 合成输出个数
    #             }
    #         ],
    #
    # }


# ]

if __name__ == "__main__":
    identifier(itemList)
    createItem(newList)
    lang(newList)
    recipes(newList)
    furnace(newList)
    toolTexture(newList)
    note(newList)
    crossbow_data(newList)
