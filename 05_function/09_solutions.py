#Generator Function with Yeild
# Write a Generator Function that yeild even numbers up to a specified limit

# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         print(i)

def even_generator(limit):
    for i in range(2, limit + 1, 2):
     yield i


for num in even_generator(10):
   print(num)
    
