# Movie Ticket Pricing
# Problem: Movie Ticket are  based on the age $12 for Adults (18 and over),
#$8 for children.Everyone gets a $2 discount on wednesday

age = 37
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Ticket price for you is $", price)