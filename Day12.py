trash_bin = ["file1.txt", "file2.png","file3.jpg", "file4.cd"]
agents = ["agent1","agent2","agent3","agent4"]
for i, agent in enumerate(agents):
    file = trash_bin[i]
    print(f"{agent} sees:{file}")
    if file.endswith(".txt") or file.endswith(".png"):
        print("The file has been cleaned",file)
    else:
        print("No need to clean this file",file)
#adding the counting of action taken
trash_bin = ["file1.txt","file2.png","file3.jpg","file4.cd"]
agents = ["agent_1","agent_2","agent_3","agent_4"]
cleaned_file_count = 0
for i, agent in enumerate(agents):
    file = trash_bin[i]
    print(f"{agent} sees: {file}")
    if file.endswith(".txt") or file.endswith(".cd"):
        print("file has been cleaned: ",file)
        cleaned_file_count += 1
    else:
        print("No need to clean this file. ",file)
    print(".......")
print(f"\ntotal files cleaned: {cleaned_file_count}")
#smart AI agent
trash_bin= ["file1.txt","file2.png","file3.jpg","file4.cd"]
agents = ["agent_1","agent_2","agent_3","agent_4"]
cleaned_file_count= 0
for i, agent in enumerate(agents):
    file = trash_bin[i]
    print(f"{agent} sees: {file}")
    if file.endswith(".png") or file.endswith(".jpg"):
        print("I am going to clean up this file: ",file)
        cleaned_file_count += 1
    else:
        print("No need to clean this file: ",file)
    print("......")
print(f"\nTotal number of cleaned files: {cleaned_file_count}")
print("......")
#with 2 agents now instead of 4
trash_bin = ["file1.txt","file2.png","file3.jpg","file4.cd"]
agents = ["agent_1","agent_2"]
cleaned_file_count = 0
for i, file in enumerate(agents):
    agent = agents[i %len(agents)]
    print(f"{agent} sees: {file}")
    if file.endswith(".jpg") or file.endswith(".png"):
        print("I am going to clean this file: ",file)
        cleaned_file_count += 1
    else:
        print("No need to clean this file: ",file)
    print(".......")
print(f"\nTotal number of cleaned files: {cleaned_file_count}")
print("......")
# Define the trash bin and agents
trash_bin = ["file1.txt", "file2.png", "file3.jpg", "file4.cd"]
agents = ["agent1", "agent2"]

# Initialize the cleaned file count
cleaned_file_count = 0

# Iterate through the trash bin using enumerate
for i, file in enumerate(trash_bin):
    # Select the agent in a rotating manner using the % operator
    agent = agents[i % len(agents)]
    
    # Display which agent sees which file
    print(f"{agent} sees: {file}")
    
    # Check if the file needs to be cleaned
    if file.endswith(".txt") or file.endswith(".cd"):
        print("I am going to clean the file:", file)
        cleaned_file_count += 1
    else:
        print("No need to clean this file:", file)
    
    print(".......")

# Display the total number of cleaned files
print(f"\nTotal files cleaned: {cleaned_file_count}")
print("........")


    
