num_list = "0123456789"   
>>> 
>>> num_list[:] 
'0123456789'
>>> num_list[3:] 
'3456789'
>>> num_list[:7]  
'0123456'
>>> num_list[0:7:2] 
'0246'
>>> num_list[0:7:4]
'04'
>>> num_list[0:7:3]
'036'
>>>
chai = "   Masala chai   "
>>> chai
'   Masala chai   '
>>> print(chai.strip())
Masala chai
>>> chai = "Lemon chai"
>>> print(chai.replace("Lemon", "Ginger"))
Ginger chai
>>> chai
'Lemon chai'
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> print(chai.split())
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
>>> print(chai.split(",")) 
['Lemon', ' Ginger', ' Masala', ' Mint']
//format

>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {} chai" 
>>> order
'I ordered {} cups of {} chai'
>>> print(order.format(quantity, chai_type)) 
I ordered 2 cups of Masala chai
//converting lists into strings
chai_variet = ['Lemon', ] 
>>> chai_variet = ['Lemon', 'Masala', 'Ginger' ]
>>> chai_variet
['Lemon', 'Masala', 'Ginger']
>>> print(''.join(chai_variet)) 
LemonMasalaGinger
>>> print(' '.join(chai_variet)) 
Lemon Masala Ginger
>>> print('-'.join(chai_variet))  
Lemon-Masala-Ginger
>>> print(', '.join(chai_variet)) 
Lemon, Masala, Ginger

//
chai = 'Masala chai' 
>>> chai
'Masala chai'
>>> for letter in chai:
...     print(letter) 
...
M
a
s
a
l
a

c
h
a
i
>>> chai = "He said, \"Masala chai is awesome\" "
>>> chai
'He said, "Masala chai is awesome" '
>>> chai = "Masala\nchai"
>>> chai
'Masala\nchai'
>>> print(chai)
Masala
chai
>>> chai = r"Masala\nchai"
>>> print(chai)
Masala\nchai