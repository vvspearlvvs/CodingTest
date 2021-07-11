def split_and_join(line):
    line=line.split(" ")
    return "-".join(line)

line="this is a string"
print(split_and_join(line))
