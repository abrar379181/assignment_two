# final code with comments

# Global variable declaration
global_variable = 100
# Dictionary declaration
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Function to process numbers in a list
def numbers():
    # Accessing global variable
    global global_variable
    # Local variable
    local_variable = 5
    # List of numbers
    numbers = [1, 2, 3, 4, 5]

    # Loop until local_variable is greater than 0
    while local_variable > 0:
        # If local_variable is even, remove it from the list
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        # Decrement local_variable
        local_variable -= 1

    return numbers

# List with repeated numbers
my_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
# Corrected function call without argument (numbers was unnecessary)
result = numbers()

# Function to modify a dictionary
def modify_dict():
    local_variable = 10
    # Add a new key-value pair to the dictionary
    my_dict['key4'] = local_variable

# Call the function to modify the dictionary
modify_dict()

# Function to update global_variable
def update_global():
    global global_variable
    global_variable += 10  # Increment the global variable

# For loop that calls the parity function (f is not defined, correcting to len(my_list))
for i in range(len(my_list)):
    # The parity function is likely a placeholder (should replace with print for now)
    print(f"Item {i} in my_list: {my_list[i]}")
    i += 1

# Check if my_list is not None and if the value for 'key4' in my_dict is 10
if my_list is not None and my_dict['key4'] == 10:
    print("Condition met!")

# Check if 5 is not in my_dict's keys
if 5 not in my_dict:
    print("5 not found in the dictionary!")

# Print global_variable, my_dict, and my_list to see the results
print(global_variable)
print(my_dict)
print(my_list)
