# STEP 1: Import tools to talk to OpenAI  
from openai import OpenAI  
import os  
from dotenv import load_dotenv  

# STEP 2: Load your OpenAI password (API key)  
load_dotenv()  
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  

# STEP 3: Tell the AI agent HOW to behave  
system_rules = """  
When the user asks about a website, ALWAYS output:  
{"tool": "get_speed", "url": "WEBSITE_HERE"}  
Example:  
User: How fast is google.com?  
Output: {"tool": "get_speed", "url": "google.com"}  
"""  

# STEP 4: Ask a question  
messages = [  
    {"role": "system", "content": system_rules},  
    {"role": "user", "content": "What is the speed of learnwithhasan.com?"}  
]  

# STEP 5: Get the AI’s answer  
response = client.chat.completions.create(  
    model="gpt-3.5-turbo",  
    messages=messages  
)  

# STEP 6: Print the answer  
print(response.choices[0].message.content)  