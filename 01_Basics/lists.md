>>> tea_varites = ["Black", "Green", "Oolang", "White"]
tea_varites                                        
['Black', 'Green', 'Oolang', 'White']
>>> print(tea_varites) 
['Black', 'Green', 'Oolang', 'White']

tea_varites = ["Black", "Green", "Oolang", "White"]  
>>> print(tea_varites[0]) 
Black
>>> print(tea_varites[-1]) 
White
>>> tea_varites[3] = "Herbal"                            
>>> print(tea_varites)        
['Black', 'Green', 'Oolang', 'Herbal']
>>>

tea_varites[1:2] = "Lemon"  
>>> tea_varites
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolang', 'Herbal']
>>> tea_varites = ["Black", "Green", "Oolang", "White"]
>>> tea_varites[1:2]
['Green']
>>> tea_varites[1:2] = ["Lemon"] 
>>> tea_varites
['Black', 'Lemon', 'Oolang', 'White']

>>> tea_varites
['Black', 'Green', 'Oolang', 'White']
>>> for tea in tea_varites:
...     print(tea) 
...
Black
Green
Oolang
White
>>>
>>> for tea in tea_varites:
...     print(tea, end="-") 
...
Black-Green-Oolang-White->>>
>>> tea_varites
['Black', 'Green', 'Oolang', 'White']
>>> if "Lemon" in tea_varites
  File "<stdin>", line 1
    if "Lemon" in tea_varites
                             ^
SyntaxError: expected ':'
>>> if "Lemon" in tea_varites:
...     print("i have lemon tea") 
...
>>> tea_varites.append("lemon")   
>>> tea_varites                   
['Black', 'Green', 'Oolang', 'White', 'lemon']
>>> tea_varites.pop()
'lemon'
>>> tea_varites       
['Black', 'Green', 'Oolang', 'White']
>>> tea_varites.remove("green") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> tea_varites
['Black', 'Green', 'Oolang', 'White']
>>> tea_varites.remove('green') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> tea_varites.remove('White') 
>>> tea_varites
['Black', 'Green', 'Oolang']
>>> tea_varites.insert(1,'white') 
>>> tea_varites
['Black', 'white', 'Green', 'Oolang']

tea_varites_copy = tea_varites
>>> tea_varites_copy
['Black', 'white', 'Green', 'Oolang']
>>> tea_varites = ['Black', 'white', 'Green', 'Oolang']
>>> tea_varites_copy = tea_varites.copy()
>>> tea_varites_copy
['Black', 'white', 'Green', 'Oolang']
>>> tea_varites_copy.append("ginger") 
>>> tea_varites_copy
['Black', 'white', 'Green', 'Oolang', 'ginger']
>>> tea_varites
['Black', 'white', 'Green', 'Oolang']
>>> range(10) 
range(0, 10)
>>> print(0,10) 
0 10
>>> print(range(10))
range(0, 10)
>>> squared_num = [x**2 for x in range(10)]
>>> squared_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num = [x**3 for x in range(5)]
>>> cube_num                  
[0, 1, 8, 27, 64]