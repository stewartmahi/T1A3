import sys

# Accept a file path as input from the user
if len(sys.argv) != 2:
    print("Usage: python word_counter.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
