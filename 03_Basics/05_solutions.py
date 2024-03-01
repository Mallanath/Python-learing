# Give a string, find the non-reapeted character

input_str = "Mallanath"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("char is:", char)
        break