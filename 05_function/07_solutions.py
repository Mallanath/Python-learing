# Write a function that takes varible number of arguments and returns their sum

def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,3,4,5))
# print(sum_all(1,3,5,6,7,8))