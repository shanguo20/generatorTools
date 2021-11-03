def lang(itemList):
    item_lang = """
item.%s.name=%s
"""
    block_lang = """
tile.%s.name=%s
"""
    langs = ""
    for item in itemList:
        if item["type"] not in ["block", "typex", "carpet", "halfbrick", "staircase", "banner", "normal",
                                "shuaguaixiang", "flag", "fence"]:
            langs = langs + item_lang % (item["identifier"], item["zh_CN"])
        else:
            langs = langs + block_lang % (item["identifier"], item["zh_CN"])
    f = open("texts/zh_CN.lang", "w")
    f.write(langs)
    f.close()
