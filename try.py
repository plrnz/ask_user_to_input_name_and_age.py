# List to store names and ages
names = []
ages = []

# Loop to keep asking for inputs
while True:
    # Loop to ask for a valid name
    while True:
        name = input("Please input name (letters only): ")
        if name.isalpha():
            break
        else:
            print("Invalid name. Please use letters only.")

    # Loop to ask for a valid age (just checking if it's a number)
    while True:
        age = input("Please input age (numbers only): ")
        if age.isdigit():  # Check if the age is a number
            age = int(age)  # Convert age to an integer
            break
        else:
            print("Invalid age. Please enter a valid number.")

    # Store the name and age in the lists
    names.append(name)
    ages.append(age)

    # Ask if the user wants to add another entry
    retry = input("Do you want to add another person? (y/n): ").lower()
    if retry == 'n':
        break

# Check who is the oldest (if there are any entries)
if len(names) > 0:
    oldest_index = ages.index(max(ages))
    print(f"\nThe oldest person is {names[oldest_index]} with an age of {ages[oldest_index]}.")
else:
    print("No valid entries were added.")