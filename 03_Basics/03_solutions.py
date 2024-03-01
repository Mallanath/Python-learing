#Print the multiplication table for a given number up to 10,
#but skip the  5 iteration

number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(number, "X", i, "=", number * i )

