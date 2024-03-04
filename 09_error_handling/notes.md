# enumerate example
list = [{'name': 'chai', 'time': }] 
  File "<stdin>", line 1
    list = [{'name': 'chai', 'time': }]
                                   ^
SyntaxError: expression expected after dictionary key and ':'
>>> list = [{'name': 'chai', 'time': '2min'}, {'name': 'python', 'time': '5min'}] 
>>> list
[{'name': 'chai', 'time': '2min'}, {'name': 'python', 'time': '5min'}]
>>> enumerate(list, start=1) 
<enumerate object at 0x000002B6A7B6DC10>
>>> list(enumerate(list, start=1)) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> for i in enumerate(list, start=1):
...     print(i) 
...
(1, {'name': 'chai', 'time': '2min'})
(2, {'name': 'python', 'time': '5min'})
>>> for i, video  in enumerate(list, start=1): 
...     print(f"{i}, {video['name']}") 
...
1, chai
2, python
>>>