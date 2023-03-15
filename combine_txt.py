import os

# Directory containing the text files to be combined
directory = "W:/vu/khac/book"

# Output file name and path
output_file = "output.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), encoding="utf-8") as f:
                out.write(f.read() + "\n")
