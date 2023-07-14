def remove_common_letters(name1, name2):
    """
    Removes the common letters between two names.
    """
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
    return name1, name2

def calculate_flames(count):
    """
    Calculates the FLAMES result based on the count.
    """
    flames = ['Friends', 'Lovers', 'Affection', 'Marriage', 'Enemies', 'Siblings']
    while len(flames) > 1:
        index = count % len(flames)
        if index == 0:
            index = len(flames)
        flames.pop(index - 1)
    return flames[0]

def play_flames():
    """
    Plays the FLAMES game by taking user input.
    """
    print("Welcome to the FLAMES game!")
    print("FLAMES stands for Friends, Lovers, Affection, Marriage, Enemies, Siblings.")
    print("Please enter two names to check their relationship:")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    name_1, name_2 = remove_common_letters(name1, name2)
    count = len(name_1) + len(name_2)
    result = calculate_flames(count)
    print("Relationship between", name1, "and", name2, "is:", result)

# Run the game
play_flames()