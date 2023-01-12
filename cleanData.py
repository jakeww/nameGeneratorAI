import re

with open("rawNameData.txt", "r") as f:
    lines = set(f.readlines())

with open("cleanedNameData.txt", "w") as f:
    for line in lines:
        cleaned_line = line.strip().lower()
        cleaned_line = re.sub(r"[^a-zA-Z0-9\s]", "", cleaned_line)
        f.write(cleaned_line + "\n")
