# functions
def greet(name):
    return f"Hello {name}"
greetings = greet("Irfan")
print(greetings)

def welcome_message(city):
    return f"we welcome you to {city}"
message = welcome_message("Doha")
print(message)
def favourite_foods(food):
    return f"my favourite food is {food}"
food_choice = favourite_foods('biryani')
print(food_choice)
def describe_person(name, age):
    return f"{name} is {age} year old"
person_description = describe_person("Ali", 25)
print(person_description)
def favourite_color(colors):
    return f"my favourite colors are {' , ' .join(colors)}"
choice_colors = ["red", "green", "black"]
print(favourite_color(choice_colors))
def add_numbers(num1, num2):
    return num1 + num2
add_result = add_numbers(40, 30)
print(add_result)
def food_basket(food):
    return f"I love the healthy foods like {' ,' ,' '.join()}"
food = ['cucumber','carrot','orange']
print(food)
def say_hello():
    print("hello, Ali")
say_hello()
def say_hello(name):
    print (f"hello, {name}")
say_hello("Irfan")
say_hello("Ali")
say_hello("khan")
def say_hello(name):
    return(f"Hello {name}, welcome on board")
greet = say_hello("Irfan")
print(greet)
def introduce(name1, age1, name2, age2, city):
    return(f"You {name1},aged {age1},and {name2}, aged {age2} are welcome to {city}")
intro = introduce("Rashid", 30, "Sara",25, "Dubai")
print(intro)
def calculate_salary(name1, amount1,name2, amount2):
    return f"the salary of {name1} is {amount1} and for {name2} is {amount2} for the month of January 2025"
salary = calculate_salary("Amjad",5000, "Imran", 6000)
print(salary)
def favourite_fruits(fruits):
    return f"my favourite fruits are: {', '.join(fruits)}"
fruit_list = ["apple", "orange", "grapes"]
result = favourite_fruits(fruit_list)
print(result)