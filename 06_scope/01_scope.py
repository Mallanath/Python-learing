username = "chaiaurcode"

def test():
    #username = "chai"
    print(username)

print(username)
test()

x = 99
# def fun2(y):
#     z = x + y
#     return z

# result = fun2(23)
# print(result)


# def func3():
#     global x # never use this
#     x = 12

# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()
