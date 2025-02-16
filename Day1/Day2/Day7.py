environment= ["walls", "open area", "trash bin"]
def perceive(element):
    print(f"I see: {element}")
    for element in environment:
        perceive(element)
    
  