#simple AI agent
environment = ["walls", "openspace", "trashbin"]

def move_through_environment(environment):
    for element in environment:
        if element == "walls":
            print("due to wall ahead, can't move")
        elif element == "openspace":
            print("there is openspace for me to move freely")
        elif element == "trashbin":
            print("reached at the goal, will get the job done")

move_through_environment(environment)
environment = ["walls","open area", "trash bin"]
def move_through_environment(environment):
    for element in environment:
        if element == "walls":
            print("there is a wall and I can't move")
        elif element == "open area":
            print("I am in the opern area and can move freely")
        elif element == "trash bin":
            print("found the trash bin and I'll now remove the trash")

move_through_environment(environment)
environment = ["walls","open area", "trash bin"]
def move_through_environment(environment):
    for element in environment:
        if element == "walls":
            print("there is wall, I will turn left to find a way")
        elif element == "open area":
            print("Open area! I can move freely")
        elif element == "trash bin":
            print("found the trash bin and I'll remove the trash")
move_through_environment(environment)
environment= ['walls', 'open area', 'trash bin']
def move_through_environment(environment):
    for element in environment:
        print(f"checking: {element}")
        if element == "walls":
            print("due to wall, I make a turn")
        elif element == "open area":
            print("I am in the open area and can make movement freely")
        elif element == "trash bin":
            print("found the trash bin and will remove the trash from bin now")
move_through_environment(environment) 