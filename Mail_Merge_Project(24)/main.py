
PlACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() # converted names file into list
    # print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    # print(letter_content)
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PlACEHOLDER,stripped_name)
        # print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)

# ___ Can make 2 separate folders names input and output as given below ___ #
# 1. For directory path, enter the path where your files are stored

# 2. In input --> letter --> starting_letter : There's starting letter to be sent
# Format :
# Dear [name],
# You are invited to my birthday this Saturday.
# Hope you can make it!
# Stay Happy! Stay Safe!
# [Your name]


# 3. In input --> Names --> invited_names : There's a list of names to whome you want to invite.(Names per line format)

# 4. In output --> ReadyToSEnd --> Add files equals to names added in invited_names as invitation letter
# Format : AS GIVEN IN STARTING LETTER


 

