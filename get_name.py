import os

folder_path = "C:/Users/BTTB/Downloads"  # replace with your folder path
output_file = "filenames.txt"  # replace with your desired output file name

with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(folder_path):
        name, extension = os.path.splitext(filename)
        f.write(name + "\n")
