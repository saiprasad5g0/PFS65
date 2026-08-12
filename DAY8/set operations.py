#SET OPERATIONS::::::::


s = {}
s
{}
s = set{}
SyntaxError: invalid syntax
s = set()
type()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
type(s)
<class 'set'>
s = {1,2,3,4,5,6,123456,34567,788912,312}
s
{123456, 1, 2, 3, 4, 5, 6, 34567, 788912, 312}
s = {1,1,1,1,1}
s
{1}
s = set()
s.add()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s.add(1)
s.add(3.14)
s.add("str")
s
{1, 3.14, 'str'}
s
{1, 3.14, 'str'}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add(False)
s
{False, 1, 3.14, 'str'}
{False, 1, 3.14, 'str'}
{False, 1, 3.14, 'str'}


a = {1,2,3,4,5}
b = {3,5,7,8,9}
2 in a
True
10 not in a
True
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a ! b
SyntaxError: invalid syntax
a - b
{1, 2, 4}
b - a
{8, 9, 7}
a ^ b
{1, 2, 4, 7, 8, 9}
a & b
{3, 5}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}<=a
True
{1,7,8,9}<=a
False
a>={1,2}
True
a>={15,16}
False
m = {1,2,3}
n = {4,5,6}
n.isdisjoint(m)
True
a.isdisjoint(b)
False





#SEET METHODS

a = {12,43,,1,7,,89,40,23,44}
SyntaxError: invalid syntax

a

a = {12,43,,1,7,89,40,23,44)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
    a = {12,43,,1,7,89,40,23,44}
    
SyntaxError: unexpected indent
a = {12,43,,1,7,89,40,23,44}
SyntaxError: invalid syntax
a = {12,43,1,2,879,5,7667,}
a
{1, 2, 7667, 5, 43, 12, 879}
sorted(a)
[1, 2, 5, 12, 43, 879, 7667]
max(a)
7667
min(a)
1
len(a)
7
a.count(a)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    a.count(a)
AttributeError: 'set' object has no attribute 'count'
all({1,1,23,43,13,1})
True
any(1,4,35)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    any(1,4,35)
TypeError: any() takes exactly one argument (3 given)
any(1,098)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
any(1,10)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    any(1,10)
TypeError: any() takes exactly one argument (2 given)
any({1,10,})
True
sum(a)
8609
a ={1,2,3}
a
{1, 2, 3}
b =a
b
{1, 2, 3}
b = a.copy()
b
{1, 2, 3}
b.add(4)
b
{1, 2, 3, 4}
a
{1, 2, 3}
a.add(4,5,6)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a.add(4,5,6)
TypeError: set.add() takes exactly one argument (3 given)
a.add(4)
a
{1, 2, 3, 4}
a.add(5)
a
{1, 2, 3, 4, 5}
a.add(100)
a
{1, 2, 3, 4, 5, 100}
a.add(50)
a
{1, 2, 3, 4, 5, 100, 50}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 100, 50}
a.pop()
3
a
{4, 5, 100, 50}
a.remove(101)
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    a.remove(101)
KeyError: 101
a.remove(100)
a
{4, 5, 50}
a.discard(100)
a
{4, 5, 50}
a.clear9)
SyntaxError: unmatched ')'
a.clear()
a
set()
a = frozenset({1,2,3,4})
a
frozenset({1, 2, 3, 4})
a.add(10)
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    a.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    a.remove(1)
AttributeError: 'frozenset' object has no attribute 'remove'
