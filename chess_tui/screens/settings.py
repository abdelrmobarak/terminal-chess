_skill = 1

def getSkill():
    return _skill

def changeSkill():
    while True:
        global _skill
        _skill = int(input("Enter the bot's skill level (1-20): "))
        if _skill > 20 or _skill <= 0:
            print("Please pick a value between 1-20!")
        else:
            return
