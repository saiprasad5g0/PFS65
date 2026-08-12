Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#TUPLE

#tuple declaration
t = ()
t = tuple()
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t = (1)
t
1
t = (1,)
t
(1,)
t = (1,1,1,1)
t
(1, 1, 1, 1)
type(t)
<class 'tuple'>
t = (1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)

"""FOR ALL THESE DATATYPES ARE IN 5 TYPES THAT ARE CONCATINANTION,INDEXING,SLICING,MEMBERSHIP"""
'FOR ALL THESE DATATYPES ARE IN 5 TYPES THAT ARE CONCATINANTION,INDEXING,SLICING,MEMBERSHIP'


#OPERATITIONS ARE:::

(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1]
23.4
t[-1]
True
t[2]
'str'
t[3;7)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
t[3:7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t[::]
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[:1]
(1,)
t[1:-1]
(23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
23.4 in t
True
"str" not in t
False
true in t
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    true in t
NameError: name 'true' is not defined. Did you mean: 'True'?
True in t
True
sorted(t)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
sorted(t)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
t = (12,789,32,13,76,32,453,123,7898,1321,32)
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1321, 32)
sorted(t)
[12, 13, 32, 32, 32, 76, 123, 453, 789, 1321, 7898]
max(t)
7898
min(t)
12
len(t)
11
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1321, 32)
t.index()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    t.index()
TypeError: index expected at least 1 argument, got 0
t.index(32)
2
t.index(7898)
8
>>> t.count(7898)
1
>>> all((1,2,3))
True
>>> any((1,2,3,00,0))
True
>>> all((1,2,3,00,0))
False
>>> t = (1,2,3)
>>> t
(1, 2, 3)
>>> a,b,c = t
>>> a
1
>>> b
2
>>> c
3
>>> t = (1,2,3,4[1,2,3],5)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    t = (1,2,3,4[1,2,3],5)
TypeError: 'int' object is not subscriptable
>>> t = (1,2,3,4,[1,2,3],5)
>>> t
(1, 2, 3, 4, [1, 2, 3], 5)
>>> t[4]
[1, 2, 3]
>>> t[4].append(1)
>>> t
(1, 2, 3, 4, [1, 2, 3, 1], 5)
>>> t
(1, 2, 3, 4, [1, 2, 3, 1], 5)
>>> t = (1,2,34,4)
>>> sum(t)
41
>>> 
>>> 
