# Factorial Calculator with while loop
#6*5*4*3*2*1

number = 6
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial of number is:", factorial)