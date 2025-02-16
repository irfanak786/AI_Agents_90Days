environment = ["walls","open area","trash bin"]
memory = []
def perceive():
    for element in environment:
        print(f"I see: {element}")
        if element not in memory:
            memory.append(element)
            if element == "walls":
                print("Due to the wall in front of me, I can't go straight")
            elif element == "open area":
                print("I am in the open area, and thus can move freely")
            elif element == "trash bin":
                print("I came arcross the trash bin, and I am going to remove the trash from the bin")
        else:
            print("I saved you already from the environment, can't repeat")
        print(".......")
perceive()
# new code lines
environment = ["walls", "open area", "trash bin"]
memory = []
def perceive():
    for element in environment:
        print(f"I see: {element}")
        if element not in memory:
            memory.append(element)
            if element == "walls":
                print("I came across the wall, hence can't move forward")
                print("Now I'll turn left as a result of this obstacle")
            elif element == "open area":
                print("I am in open area and thus can move freely")
                print("I decided to move in all over the place and in all directions")
            elif element == "trash bin":
                print("I found trash bin, now I am going to clean it out")
                print("I'll make sure nothing left out in the bin")
        else:
            print("I already have saved this element, can't repeat the action")
        print(".......")
perceive()

