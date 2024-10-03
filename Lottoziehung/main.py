import random

# Initialize an empty list to store the number range
l = []
# Set the number of lottery simulations (rounds)
rounds = 1000
# Define the range of possible lottery numbers (1 to 45)
number_range = 45
# Initialize an empty dictionary to store the count of each number's occurrences
statistics_dic = {}

# Function to generate a set of 6 unique lotto numbers
def generate_lotto_numbers():
    # Initialize an empty list to store the generated numbers
    generated_numbers = []

    # Use local variables to keep track of the remaining range and list of numbers
    local_number_range = number_range
    local_list = l.copy()  # Copy the global list to avoid modifying it directly

    # Loop 6 times to generate 6 unique numbers
    for count in range(6):
        # Randomly select an index within the range of available numbers
        generated_number = random.randint(0, local_number_range - 1)

        # Pop (remove) the number at the selected index and add it to the result list
        element = local_list.pop(generated_number)
        generated_numbers.append(element)

        # Decrease the available number range for the next iteration
        local_number_range -= 1

    # Return the 6 generated numbers
    return generated_numbers

# Function to update the statistics dictionary based on the drawn numbers
def update_statistics(numbers):
    # For each number in the generated set, increment its count in the statistics dictionary
    for number in numbers:
        statistics_dic[number] += 1

# Fill the list 'l' with numbers from 1 to 45
l = list(range(1, number_range + 1))

# Initialize the statistics dictionary: set the count of each number to 0
for i in range(1, number_range + 1):
    statistics_dic[i] = 0

# Print the list of numbers from 1 to 45
print("List:", l)

# Simulate the drawing process for the specified number of rounds (1000 times)
for round in range(rounds):
    # Generate lotto numbers and update their occurrence in the statistics dictionary
    update_statistics(generate_lotto_numbers())

# Print the final statistics of how many times each number was drawn
print("Statistics of drawn numbers:", statistics_dic)
