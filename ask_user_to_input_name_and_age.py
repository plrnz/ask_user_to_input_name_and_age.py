# Pseudocodes
# 1. Start
# 2. Initialize an empty list called people
# 3. Allow special characters for the names
# 4. Loop1: Ask for input
    # a. Loop2: Ask for a valid name
        # i. IF name is not valid, display error and ask again
    # b. Loop3: Ask for valid a valid age
        # i. If age is not valid, diplay error and ask again
    # c. Store name and age in the list
    # d. Ask user if they want to add another entry (yes/no)
    # e. If no, break the loop
# 5. If the list is not empty, find the oldest person
# 6. Display the oldest person's name and age
# 7. End

# List to store the name and age
names = [] # List for storing names
ages = [] # List for storing ages

# Allow special characters for names
def valid_name(name):
    for char in name:
        if not (char.isalpha() or char in [" ", "-", "'"]): # Allows space, hyphens, apostrophe
            return False
    return True
    # 
# Start of Loop
# Loop 1: Ask for input
while True:
    # Loop 2: Ask for a valid name
    while True:
        participants_names = input("Please input a name: ")
        if valid_name(participants_names): # Upper case letters, lower case letters, space, hyphens, and apostrophe cn be used
            break
        else:
            print("Invalid name. Please input a valid name: ")
    
    # Loop 3: Ask the user to input a valid age
    while True:
        participants_ages = input("Please input age: ")
        if participants_ages.isdigit(): # Numbers only. No special characters
            participants_ages = int(participants_ages)
            break
        else:
            print("Invalid age. Please input again: ")

    # Store the name and age in the list
    names.append(participants_names)
    ages.append(participants_ages)

    # Ask the user if they want to add another entry (yes/no)
    retry = input("Do you want to add another participant? (yes/no): ").lower()
    if retry == "no":
        break

# Check who is the oldest
if len(names) > 0:
    oldest_index = ages.index(max(ages))
    print(f"The oldest person among the participants is {names[oldest_index]} with an age of {ages[oldest_index]} years old.")
else:
    print("No valid entries were addded.")
