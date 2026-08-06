Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = 12
>>> type(a)
<class 'int'>
>>> #float
>>> b = 3.14
>>> type(b)
<class 'float'>
>>> #complex
>>> c = 12+4j
>>> type(c)
<class 'complex'>
\
>>> #above all are numerical datatypes
>>> 
>>> 
>>> #sequens datatypes
>>> # 1. string 2.list 3.tuple
>>> 
>>> #string
>>> #string is a collection of characters enclosed in single quotes or double queots
>>> # string is immutable it can not be changed
>>> #string can be consist of any kind of characters
>>> 
>>> #list
>>> #list is collection of elements enclosed b/tsquare braces
>>> 1 = [1,2,3,4,5]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> type(1)
<class 'int'>
>>> l = [1,2,3,4,5,6]
>>> type(l)
<class 'list'>
>>> id(l)
2023771392960
>>> l.append(12)
>>> l
[1, 2, 3, 4, 5, 6, 12]
>>> # list is oredered
>>> #mutable
>>> #dynamiccaly sized
>>> #it can be changed
>>> #allow duplicates
>>> #hetrogenious
>>> 

#tuple is a collection elements encloseed b/t paranthises
# properties:
 #immutable
#  duplicates allowes
#fixig sizes
# it is ordered
#hetrogenious
#ex: google maps latitude and longitude nymbers




# mapping datatypes
#1. set 2.dict
#set
# it is an collection of elements enclosed b/w
 #open braces
# muttable
# not allowed any duplicatres
#hetrogenious
# un ordered
s = {1,2,3,4,5}
s
{1, 2, 3, 4, 5}
type(s)
<class 'set'>

# dictionary is a collection key value pairs encklosed b/w curly braces
d = {'pronoun' : 'xxx','price':876,'stock':True}
d
{'pronoun': 'xxx', 'price': 876, 'stock': True}
#dict is a mutable
# follows oreder
#dynamically sized
# hetrogenious
s = {1,2,3}
s = frozenset ({1,1,1,116,18,2,3)}
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
s = frozenset ({1,1,1,116,18,2,3})
s
frozenset({1, 2, 3, 18, 116})
# booleaan datatype
#either true or false
