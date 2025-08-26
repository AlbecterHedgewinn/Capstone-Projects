# Make a list that asks classmates for their names and stores them in a list.
# Then print the list.
# Daniel Bittner Aug 25, 2025


names = []      # Makes a list to store names
while True:     # Initiate loop to keep asking for names
    name = input("Enter the name of a class you are taking (or type 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    names.append(name)

print("These are your classes: ")
for all_names in names:         # all_names is a temp variable
    print(all_names)