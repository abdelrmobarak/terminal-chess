_skill = 1
_depth = 2


def getSkill():
    return _skill

def changeSkill():
    while True:
        global _skill
        try:
            _skill = int(input("Enter the bot's skill level (1-20): "))
        except ValueError:
            print("Please enter a valid entry")
            continue

        if _skill > 20 or _skill <= 0:
            print("Please pick a value between 1-20")
        else:
            return

        
def getDepth():
    return _depth

def changeDepth():
    while True:
        global _depth
        try:
            _depth = int(input("Enter the bot's depth (1-20): "))
        except ValueError:
            print("Please enter a valid entry")
            continue
        
        if _depth > 20 or _depth <= 0:
            print("Please pick a value between 1-20")
        else:
            return

def settings():
    while True:
        try:
            choice = int(input("1. change skill level, 2. change depth level, 3. exit: "))
        except ValueError:
            print("Please enter a valid entry")
            continue
        
        if choice == 1:
            changeSkill()
        elif choice == 2:
            changeDepth()
        elif choice == 3:
            return
        else:
            print("Please enter a valid entry")
        