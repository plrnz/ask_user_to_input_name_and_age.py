# List to store the name and age
names = [] # List for storing names
ages = [] # List for storing ages

# Start of Loop
# Loop 1: Ask for input
while True:
    # Loop 2: Ask for a valid name
    while True:
        participants_names = input("Please input a name: ")
        if participants_names.isalpha(): # Upper case and lower case letters only
            break
        else:
            print("Invalid name. Please input a valid name: ")
    
    # Loop 3: Ask the user to input a valid age
    while True:
        participants_ages = input("Please Input age: ")
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
    print(f"The oldest person is {names[oldest_index]} with an age of {ages[oldest_index]}.")
else:
    print("No valid entries were addded.")
