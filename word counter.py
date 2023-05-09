import sys

# Accept a file path as input from the user
if len(sys.argv) != 2:
    print("Usage: python word_counter.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

# Read the contents of the file
try:
    with open(file_path, "r") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Error: file '{file_path}' not found")
    sys.exit(1)

# Count the number of words, characters, and lines in the file
num_words = len(contents.split())
num_chars = len(contents)
num_lines = len(contents.split("\n"))

# Output the results to the console
print(f"Words: {num_words}")
print(f"Characters: {num_chars}")
print(f"Lines: {num_lines}")
