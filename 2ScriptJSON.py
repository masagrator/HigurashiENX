import json

Filenames = []
MSGSET_Orig = []
MSGSET_Orig2 = []
MSGSET_New = []
MSGSET_New2 = []
MSGSET_Count = 0
SELECT_Orig = []
SELECT_New = []
LOGSET_Orig = []
LOGSET_New = []
SAVEINFO_Orig = []
SAVEINFO_New = []

with open("ChaptersList.txt", 'r', encoding="UTF-8") as f:
    Filenames = [line.strip("\r\n").strip("\n").split("\t", -1)[0] for line in f]

for x in range(0, len(Filenames)):

    file = open("HigurashiENX-texts/%s.json" % (Filenames[x]), "r", encoding="UTF-8")

    Temp = json.load(file)
    file.close()
    Main = Temp['Main']

    for i in range(0, len(Main)):
        if (Main[i]['type'] == "MSGSET"):
            MSGSET_Orig.append("        MSGSET %dmi, 1b, -1n, L\"%s%s@r%s%s%s\"\n" % (
                Main[i]['MessageID'],
                Main[i].get("PreNameTags", ""),
                Main[i].get("NamesJPN", ""),
                Main[i].get("PreTextTags", ""),
                Main[i]['TextJPN'],
                Main[i].get("AfterTextTags", "")
                ))
            MSGSET_Orig2.append("        MSGSET %dmi, 0b, -1n, L\"%s%s@r%s%s%s\"\n" % (
                Main[i]['MessageID'],
                Main[i].get("PreNameTags", ""),
                Main[i].get("NamesJPN", ""),
                Main[i].get("PreTextTags", ""),
                Main[i]['TextJPN'],
                Main[i].get("AfterTextTags", "")
                ))
            MSGSET_New2.append("        MSGSET %dmi, 0b, -1n, L\"%s%s@r%s%s%s\"\n" % (
                Main[i]['MessageID'],
                Main[i].get("PreNameTags", ""),
                Main[i].get("NamesENG", ""),
                Main[i].get("PreTextTags", ""),
                Main[i]['TextENG'].replace("—", "―").replace("~", "～").replace("é", "e").replace(" ", " ").replace("<i>", "*").replace("</i>","*").replace("--","―").replace("ï", "i").replace("``","\x5c\x22") if Main[i]['TextENG'] != "" else Main[i]['TextJPN'],
                Main[i].get("AfterTextTags", "")
                ))
            MSGSET_New.append("        MSGSET %dmi, 1b, -1n, L\"%s%s@r%s%s%s\"\n" % (
                Main[i]['MessageID'],
                Main[i].get("PreNameTags", ""),
                Main[i].get("NamesENG", ""),
                Main[i].get("PreTextTags", ""),
                Main[i]['TextENG'].replace("—", "―").replace("~", "～").replace("é", "e").replace(" ", " ").replace("<i>", "*").replace("</i>","*").replace("--","―").replace("ï", "i").replace("``","\x5c\x22") if Main[i]['TextENG'] != "" else Main[i]['TextJPN'],
                Main[i].get("AfterTextTags", "")
                ))
            MSGSET_Count += 1
        elif (Main[i]['type'] == "SELECT"):
            if (Main[i]['count'] == 2):
                SELECT_Orig.append("        SELECT %s S\"%s\", S[\"%s\",\"%s\"]\n" % (
                    Main[i]['metadata'],
                    Main[i]['titleJPN'],
                    Main[i]['choice1JPN'],
                    Main[i]['choice2JPN']
                    ))
                SELECT_New.append("        SELECT %s S\"%s\", S[\"%s\",\"%s\"]\n" % (
                    Main[i]['metadata'],
                    Main[i]['titleENG'] if (Main[i]['titleENG'] != "") else Main[i]['titleJPN'],
                    Main[i]['choice1ENG'] if (Main[i]['choice1ENG'] != "") else Main[i]['choice1JPN'],
                    Main[i]['choice2ENG'] if (Main[i]['choice2ENG'] != "") else Main[i]['choice2JPN']
                    ))
            elif (Main[i]['count'] == 3):
                SELECT_Orig.append("        SELECT %s S\"%s\", S[\"%s\",\"%s\",\"%s\"]\n" % (
                    Main[i]['metadata'],
                    Main[i]['titleJPN'],
                    Main[i]['choice1JPN'],
                    Main[i]['choice2JPN'],
                    Main[i]['choice3JPN']
                    ))
                SELECT_New.append("        SELECT %s S\"%s\", S[\"%s\",\"%s\",\"%s\"]\n" % (
                    Main[i]['metadata'],
                    Main[i]['titleENG'] if (Main[i]['titleENG'] != "") else Main[i]['titleJPN'],
                    Main[i]['choice1ENG'] if (Main[i]['choice1ENG'] != "") else Main[i]['choice1JPN'],
                    Main[i]['choice2ENG'] if (Main[i]['choice2ENG'] != "") else Main[i]['choice2JPN'],
                    Main[i]['choice3ENG'] if (Main[i]['choice3ENG'] != "") else Main[i]['choice3JPN']
                    ))
            elif (Main[i]['count'] == 4):
                SELECT_Orig.append("        SELECT %s S\"%s\", S[\"%s\",\"%s\",\"%s\",\"%s\"]\n" % (
                    Main[i]['metadata'],
                    Main[i]['titleJPN'],
                    Main[i]['choice1JPN'],
                    Main[i]['choice2JPN'],
                    Main[i]['choice3JPN'],
                    Main[i]['choice4JPN']
                    ))
                SELECT_New.append("        SELECT %s S\"%s\", S[\"%s\",\"%s\",\"%s\",\"%s\"]\n" % (
                    Main[i]['metadata'],
                    Main[i]['titleENG'] if (Main[i]['titleENG'] != "") else Main[i]['titleJPN'],
                    Main[i]['choice1ENG'] if (Main[i]['choice1ENG'] != "") else Main[i]['choice1JPN'],
                    Main[i]['choice2ENG'] if (Main[i]['choice2ENG'] != "") else Main[i]['choice2JPN'],
                    Main[i]['choice3ENG'] if (Main[i]['choice3ENG'] != "") else Main[i]['choice3JPN'],
                    Main[i]['choice4ENG'] if (Main[i]['choice4ENG'] != "") else Main[i]['choice4JPN']
                    ))
        elif (Main[i]['type'] == "LOGSET"):
            LOGSET_Orig.append("        LOGSET L\"%s@r%s%s\"\n" % (
                Main[i].get("NamesJPN", ""),
                Main[i].get("PreTextTags", ""),
                Main[i]['TextJPN']
                ))
            LOGSET_New.append("        LOGSET L\"%s@r%s%s\"\n" % (
                Main[i].get("NamesJPN", ""),
                Main[i].get("PreTextTags", ""),
                Main[i]['TextENG']
                ))
        elif (Main[i]['type'] == "SAVEINFO"):
            SAVEINFO_Orig.append("        SAVEINFO %dn, S\"%s\"\n" % (
                Main[i]['category'],
                Main[i]['JPN']
                ))
            SAVEINFO_New.append("        SAVEINFO %dn, S\"%s\"\n" % (
                Main[i]['category'],
                Main[i]['ENG']
                ))

Listing_buffer = []
NewString = []
offset = 0
chap_offset = 0
choice_offset = 0
log_offset = 0

with open("scenarionew/listing.temp", 'r', encoding="UTF-8") as f:
    Listing_buffer = [line for line in f]

for i in range(0, len(Listing_buffer)):
    if (offset < MSGSET_Count):
        if (Listing_buffer[i] == MSGSET_Orig[offset]):
            NewString.append(MSGSET_New[offset])
            offset = offset + 1
            continue
        elif (Listing_buffer[i] == MSGSET_Orig2[offset]):
            NewString.append(MSGSET_New2[offset])
            offset = offset + 1
            continue
    if (chap_offset < len(SAVEINFO_Orig)):
        if (Listing_buffer[i] == SAVEINFO_Orig[chap_offset]):
            NewString.append(SAVEINFO_New[chap_offset])
            chap_offset = chap_offset + 1
            continue
    if (choice_offset < len(SELECT_Orig)):
        if (Listing_buffer[i] == SELECT_Orig[choice_offset]):
            NewString.append(SELECT_New[choice_offset])
            choice_offset = choice_offset + 1
            continue
    if (log_offset < len(LOGSET_Orig)):
        if (Listing_buffer[i] == LOGSET_Orig[log_offset]):
            NewString.append(LOGSET_New[log_offset])
            log_offset = log_offset + 1
            continue
    NewString.append(Listing_buffer[i]) 

newlisting = open("scenarionew/listing.dat", "w", encoding="UTF-8")

for i in range(0, len(NewString)):
    newlisting.write(NewString[i])
newlisting.close()
print("Finished importing repo.")