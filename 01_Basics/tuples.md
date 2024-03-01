 tea_types = ("Black", "Green", "Oolang")
>>> tea_types
('Black', 'Green', 'Oolang')
>>> tea_types[0] 
'Black'
>>> tea_types[-1] 
'Oolang'
>>> tea_types[0] = "Lemon" 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> len(tea_types) 
3

//
more_tea = ("Herbal", "Earl Grey")  
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolang')
>>> if "Green" in all_tea:
...     print("I have green tea")
... 
I have green tea
>>> more_tea.count("Herbal")                 
1


///
#tuples ko use kar sakte ho tuple ko unwrap karne ke liye
>>> tea_types = ("Black", "Green", "Oolang")
>>> tea_types
('Black', 'Green', 'Oolang')
>>> (black, green, Oolang) = tea_types
>>> black
'Black'
>>> green
'Green'
>>> type(tea_types) 
<class 'tuple'>