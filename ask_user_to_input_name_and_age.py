# Pseudocodes
# 1. Start
# 2. Initialize an empty list called people
# 3. Loop1: Ask for input
    # a. Loop2: Ask for a valid name
        # i. IF name is not valid, display error and ask again
    # b. Loop3: Ask for valid a valid age
        # i. If age is not valid, diplay error and ask again
    # c. Store name and age in the list
    # d. Ask user if they want to add another entry (yes/no)
    # e. If no, break the loop
# 4. If the list is not empty, find the oldest person
# 5. Display the oldest person's name and age
# 6. End

# List to store the name and age
name: [] # type: ignore
age: [] # type: ignore

# Start of Loop
# Loop 1: Ask for input
while True:
    # Loop 2: Ask for a valid name
    name = input("Please input a name: ")
    if name.isalpha():
        break
    else:
        print("Invalid name. Please input a valid name: ")
