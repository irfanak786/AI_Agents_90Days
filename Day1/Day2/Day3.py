#list & loops 
ai_tools = ['chatgpt', 'claude', 'gemini']
ai_tools.append('deepseek')
print(ai_tools)
ai_tools = ['chatgpt', 'claude', 'gemini']
ai_tools.remove('chatgpt')
print(ai_tools)
ai_tools = ['chatgpt', 'claude', 'gemini']
ai_tools[1]= "lama"
print(ai_tools)

message = ["hello AI", "python can solve the problem", "tell me a joke", "AI agents are cool"]
for msg in message:
    if "AI" in msg:
        print("important: ", msg)

fruits = ["banana", "apple", "orange", "pineapple"]
for fr in fruits:
    if "n" in fr:
        print("awesome: ", fr)
numbers_list = [1,2,3,4,5,6,7,8]
for i in numbers_list:
    if i %2==0:
        print("number is even: ", i)
    else:
        print("number is odd: ", i)
def good_night():
    print("good night with sweet dreams")