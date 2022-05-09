# Extracting Name
name_list = []
with open('./Input/Names/invited_names.txt') as file:
    name_list = file.readlines()

# Extracting Sample Letter
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
# Making Letters
for i in name_list:
    name = i.strip()
    with open(f"./Output/ReadyToSend/{name}.txt", mode='w') as file:
        final_letter = letter.replace('[name]', f"{name}")
        file.write(final_letter)


