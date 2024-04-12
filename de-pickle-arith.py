import pickle

# Load the contents of the file
with open('data/arith_char/meta.pkl', 'rb') as file:
    metadata = pickle.load(file)

# Print the loaded metadata
print(metadata)
