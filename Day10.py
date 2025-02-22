#make the AI agent more smarter by adding 
environment = ["trash", "wall", "cleaned area", "obstacle"]
def perceive(item):
    print("seeing:", item)
    if item == "trash":
        print("I saw the trash and will remove it from the bin")
    elif item == "wall":
        print("this wall has stopped me moving straight, I am turning left now")
    elif item == "cleaned area":
        print("area is found cleaned: jpb done")
    elif item == "obstacle":
        print("obstacle detected; tuning around")

for item in environment:
    perceive(item)