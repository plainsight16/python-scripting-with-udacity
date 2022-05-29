# Write your code here

# HINT: create a dictionary from flowers.txt
flowers = {}

first_name, last_name = input("Enter full name seperated by a space: ").title().split()

# HINT: create a function to ask for user's first and last name
def populate_flowers():
    with open("./flowers.txt", "r") as f:
        for line in f:
            line_split = line.split(":")
            flowers[line_split[0]] = line_split[1]

def get_unique_flower():
    first_letter = first_name[0]
    return flowers.get(first_letter)

populate_flowers()

print("Unique flower name with the first letter: {}".format(get_unique_flower()))


# print the desired output

