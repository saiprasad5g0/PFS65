Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#LIST OPERATIONS

l = []
l =list()
type(l)
<class 'list'>
l = [1,2,3,"str",True,[1,2,3],(1,2,3){1,2,3},{1:1,2:2,3:3},3+8j]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l = [1,2,3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},3+8j]
l
[1, 2, 3, 'str', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, (3+8j)]
l = [1,1,1,1]
l
[1, 1, 1, 1]
a = [1,2,3]
b = [4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a=[567,76,13,433,134,234]
a
[567, 76, 13, 433, 134, 234]
a[1]
76
a[3]
433
a[-1]
234
a[-3]
433
a
[567, 76, 13, 433, 134, 234]
a[1:4]
[76, 13, 433]
a[::-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[::-1]
[234, 134, 433, 13, 76, 567]
a[1::2]
[76, 433, 234]
a[1::5]
[76]
a
[567, 76, 13, 433, 134, 234]
76 in a
True
76 not in a
False




#LIST METHODS




a
[567, 76, 13, 433, 134, 234]
max(a)
567
min(a0
    min(a)
    
SyntaxError: '(' was never closed
min(a)
    
13
sorted(a)
    
[13, 76, 134, 234, 433, 567]
len(a)
    
6
a
    
[567, 76, 13, 433, 134, 234]
id(a)
    
2365839261440
a[0]
    
567
a[0]=56
    
a
    
[56, 76, 13, 433, 134, 234]
a[3]=43
    
a
    
[56, 76, 13, 43, 134, 234]
a.append(50)
    
a
    
[56, 76, 13, 43, 134, 234, 50]
a.append(60,70,80)
    
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.append(60,70,80)
TypeError: list.append() takes exactly one argument (3 given)
a.append(60)
    
a
    
[56, 76, 13, 43, 134, 234, 50, 60]
a.insert(1,60)
    
a
    
[56, 60, 76, 13, 43, 134, 234, 50, 60]
a.extend([1,2,3,4])
    
a
    
[56, 60, 76, 13, 43, 134, 234, 50, 60, 1, 2, 3, 4]
a.pop()
    
4
a.pop(1)
    
60
a
    
[56, 76, 13, 43, 134, 234, 50, 60, 1, 2, 3]
a.pop(5)
    
234
del a[1]
    
a
    
[56, 13, 43, 134, 50, 60, 1, 2, 3]
a.clear()
    
a
    
[]
a.remove(1)
    
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
a = [123, 234,345,456]
    
a
    
[123, 234, 345, 456]
a.remove(1)
    
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
a.remove(123)
    
a
    
[234, 345, 456]
a
    
[234, 345, 456]
a.index(3)
    
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.index(3)
ValueError: list.index(x): x not in list
>>> a.index(234)
...     
0
>>> a.count(456)
...     
1
>>> a
...     
[234, 345, 456]
>>> b = a
...     
>>> b
...     
[234, 345, 456]
>>> b.append(1230
...          hwwe
...          
SyntaxError: '(' was never closed
>>> b.append(123)
...          
>>> b
...          
[234, 345, 456, 123]
>>> l.sort()
...          
>>> l
...          
[1, 1, 1, 1]
>>> a.sort()
...          
>>> a
...          
[123, 234, 345, 456]
>>> a.reverse()
...          
>>> a
...          
[456, 345, 234, 123]
