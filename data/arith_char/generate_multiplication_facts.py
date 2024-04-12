import random

# Define the number of addition facts you want to generate
num_facts = 500  # For example, 1,000,000 facts

# Open a text file in write mode
with open('random_multiplication_examples.txt', 'w') as file:
# Newline serves as both BOS and EOS
    file.write("\n")
    for _ in range(num_facts):
        # Generate two random integers in the range 0 through 99
        a = random.randint(0, 9)
        b = random.randint(0, 9)

        # Write the multiplication fact to the file followed by a newline
        file.write(f" {a}*{b}={a*b} \n")
