#!/bin/bash

import random

# Define the number of addition facts you want to generate
num_facts = 10000000  # ten million facts

# Open a text file in write mode
with open('random_multiplication_examples.txt', 'w') as file:
# Newline serves as both BOS and EOS
    file.write("\n")
    for _ in range(num_facts):
        # Generate two random integers in the range [0,999] and [0,9999] (10^4 and 10^3 possibilities)
        # Thus there are 10^7 different facts possible.
        # Generating 10^6 facts means that only about 1 in 10 of the possible facts will appear in the results.
        a = random.randint(0, 999)
        b = random.randint(0, 9999)

        # Write the multiplication fact to the file followed by a newline
        file.write(f" {a}*{b}={a*b} \n")

