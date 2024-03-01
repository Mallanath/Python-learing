f  = open("chai.py") 
>>> f
<_io.TextIOWrapper name='chai.py' mode='r' encoding='cp1252'>
>>> f.readline()
'import time\n'
>>> f.readline()
'print("chai is here")\n'
>>> f.readline()
'username = "Mallanath"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
''

//__next__
>>> f  = open("chai.py") 
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'username = "Mallanath"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 

//
>>> for line in open("chai.py"):
...     print(line, end="")
... 
import time
print("chai is here")
username = "Mallanath"
print(username)>>> 
>>> f  = open("chai.py")
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end="")
... 
import time
print("chai is here")
username = "Mallanath"
print(username)>>>

///////////
 test = "Mallanath"
>>> if not test:
...     print("chai")
... 
>>>  test = "Mallanath"

test = ""
>>> if not test:
...     print("chai")
...
chai
>>>

////////////
>>> myList = [1,2,3,4]
>>> I = iter(myList) 
>>> I
<list_iterator object at 0x00000280CC3F5CC0>
>>> I.__next__()
1
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
//
/////////////

/// for file
// file ko jab app variable ke undar store le to ho Reference lete //ho.to apnene app me ek itereable object hai
////when you store a file inside a variable  you take its reference. it is an itereated object in itself 
>>> f = open("chai.py") 
>>> iter(f) is f         
True
>>> iter(f) is f.__iter__()
True

//Lekin list ko memory reference me useka naam diya hai uska iterable object nehi hai
//but if you have given its name in a memeory reference of the list , it is not a itereable object it is just a reference to that a actual object 
>>> myList = [1,2,3,4]
>>> 
>>> iter(myList) is myList
False

////////////// dictionery
 D = {'a': 1, 'b': 2}
>>> for keys in D.keys():
...     print(keys) 
... 
a
b
>>> I = iter(D)   
>>> 
>>> I
<dict_keyiterator object at 0x00000280CC13DC60>
>>> next(I) 
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

////range 
>>> range(0,5)
range(0, 5)
>>> R=range(5) 
>>> R
range(0, 5)
>>> I = iter(R) 
>>> next(I) 
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration