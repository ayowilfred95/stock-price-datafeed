import fileinput

# Define the mapping of old names to new names
mapping = {"ABC": "APRL", "DEF": "GOOG"}

# Specify the file path
file_path = 'test.csv'

# Iterate over the file and perform the replacements
with fileinput.FileInput(file_path, inplace=True) as file:
    for line in file:
        for key, value in mapping.items():
            line = line.replace(key, value)
        print(line, end='')
