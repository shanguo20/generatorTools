def note(itemList):
    noteList = \
        """{
    %s
}
        """
    noteItem = """ 
    "%s":'''%s'''
    """
    noteText = ""
    index = 0
    for item in itemList:
        if "note" in item:
            if index == 0:
                noteText += noteItem % (item["identifier"], item["note"])
            else:
                noteText += ("," + noteItem % (item["identifier"], item["note"]))
            index += 1
    noteList = noteList % noteText
    f = open("notes.py", "w")
    f.write(noteList)
    f.close()
