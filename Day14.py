# trash_bin_cleaner.py

# Environment setup
trash_bin = ["file1.txt", "file2.png", "file3.jpg", "file4.cd"]
agents = ["agent_1", "agent_2"]
clean_file_count = 0

# Agents observing and acting in the environment
for i, agent in enumerate(agents):
    file = trash_bin[i % len(trash_bin)]
    print(f"{agent} sees: {file}")

    # Decision making and action
    if file.endswith(".txt") or file.endswith(".cd"):
        print(f"{agent} is cleaning the file: {file}")
        clean_file_count += 1
    else:
        print(f"{agent} finds no need to clean: {file}")
    print("..........")

# Final scoreboard
print(f"\nTotal number of cleaned files: {clean_file_count}")
print(".............")
