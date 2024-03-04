#  when we execute example_function it will not run directly it has to go through @timer
# when you execute it will go with parameters in timer(func) then timer func is exection 
#first wrapper func will be exected 

# Ek method banyege uske undar aurek method baneyenge aur uske undar 
#jo bhi hamara func dey (timer(func)) use dalkar executer karte hai

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)