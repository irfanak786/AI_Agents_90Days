# creating the agent
environment = ["walls", "open area", "trash bin"]

def decide_and_move(environment):
    for element in environment:
        print(f"checking: {element}")
        if element == "walls":
            print("A wall came in front of me and I am moving to another direction ")
        elif element == "open area":
            print("I am in the open area and can move freely")
        elif element == "trash bin":
            print("I found the trash bin and I'll take out all the trash from it")
        print(".......")

decide_and_move(environment)

environment = ["walls", "open area", "trash bin"]

def perceive(element):
    print(f"I see: {element}")

for element in environment:
    perceive(element)
    if element == "walls":
        print("I saw the wall and instead of moving forward, I changed my direction ")
    elif element == "open area":
        print("I see no obstacles, I can move around freely")
    elif element == "trash bin":
        print("trash bin found, I'll take out all the trash from it")

    print("......")
environment = ["walls", "open area", "trash bin"]

def perceive(element):
    print(f"I see: {element}")

for element in environment:
    perceive(element)
    
    if element == "walls":
        print("I saw the wall, hence I changed the direction")
    elif element == "open area":
        print("As I am in open area, I can move freely")
    elif element == "trash bin":
        print("Ah, trash bin found, I'll take out all the trash from it")
    
    print(".....")
print("hello! AI Agent")