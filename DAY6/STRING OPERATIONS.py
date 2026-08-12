Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #STRING OPERATIONS::::::::::
>>> 
>>> 
>>> #STRING CONCATINATION::
>>> #STRING REPEATATION
>>> 
>>> #STRING CONCA.......
>>> s = 'sai'
>>> s
'sai'
>>> type(s)
<class 'str'>
>>> s = ''
>>> s
''
>>> a = 'sai;
SyntaxError: unterminated string literal (detected at line 1)
>>> a = 'sai'
>>> b = 'prasad'
>>> a+b
'saiprasad'
>>> fname = 'sai'
>>> lname = 'prasad'
>>> fname + lname
'saiprasad'
>>> a
'sai'
>>> a*10
'saisaisaisaisaisaisaisaisaisai'
>>> a*\n10
SyntaxError: unexpected character after line continuation character
>>> a*'\n'10
SyntaxError: invalid syntax
>>> a'\n'*10
SyntaxError: invalid syntax
>>> 


#CONCATINANTION
#REPETATION
#INDEXING
#SLICING
#MEMBERSHIP





names
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'fname'?
names = 'sai', 'nithin', 'sreenu'
names
('sai', 'nithin', 'sreenu')
names =[::]
SyntaxError: invalid syntax
names [::]
('sai', 'nithin', 'sreenu')
names[:5]
('sai', 'nithin', 'sreenu')
names[5:10
      j
      
SyntaxError: '[' was never closed
names[3: 7]
      
()
()
      
()
names[7:12]
      
()
names = 'sai nithin sreenu'
      
names
      
'sai nithin sreenu'
names[:5]
      
'sai n'
names[-6:-5]
      
's'
names[-7:-10]
      
''
names[-10:--12]
      
'hin s'
len(names)
      
17
ord(names)
      
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    ord(names)
TypeError: ord() expected a character, but string of length 17 found
sorted(names)
      
[' ', ' ', 'a', 'e', 'e', 'h', 'i', 'i', 'i', 'n', 'n', 'n', 'r', 's', 's', 't', 'u']
max(names)
      
'u'
min(names)
      
' '
ord(a0
    h
    
SyntaxError: '(' was never closed
ord(a)
    
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 3 found
ord('a')
    
97
ord('e')
    
101
ord('i')
    
105
ord('o')
    
111
ord('u')
    
117
ord(99)
    
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    ord(99)
TypeError: ord() expected string of length 1, but int found
ord(10)
    
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    ord(10)
TypeError: ord() expected string of length 1, but int found
chr(10)
    
'\n'
chr(9)
    
'\t'
chr(100)
    
'd'
chr(101)
    
'e'

#case conversion method
    
s = 'saiprasad jaada '
    
s.upper()
    
'SAIPRASAD JAADA '
s.lower()
    
'saiprasad jaada '
s.swapcase(0
           j
           
SyntaxError: '(' was never closed
s.swapcase()
           
'SAIPRASAD JAADA '
s.capitalize()
           
'Saiprasad jaada '
s.tytle()
           
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s.tytle()
AttributeError: 'str' object has no attribute 'tytle'. Did you mean: 'title'?
s.title()
           
'Saiprasad Jaada '
s.casefold()
           
'saiprasad jaada '
"abcdefghijklmnopqrstuvwxyz".casefold()
           
'abcdefghijklmnopqrstuvwxyz'
"SAIPRAsadJAada".casefold().
           
SyntaxError: invalid syntax
"SAIPRAsadJAada".casefold()
           
'saiprasadjaada'
"SAIPRAsadJAada".casefold().upper()
           
'SAIPRASADJAADA'
#allignment methods
           

s.centre(50'_')
           
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.centre(50,'_')
           
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s.centre(50,'_')
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
s.center(50,"_")
           
'_________________saiprasad jaada _________________'
s.ljust(50,"_")
           
'saiprasad jaada __________________________________'
s.rjust(50,"_")
           
'__________________________________saiprasad jaada '
"123".zfill
           
<built-in method zfill of str object at 0x000001ABF7783030>
"123".zfill(3)
           
'123'
"123".zfill(1)
           
'123'
"123".zfill(10)
           
'0000000123'


#INDEX
           
#FIND INDEX
           
s
           
'saiprasad jaada '
s.find('sai')
           
0
s.find("prasad")
           
3
s.find("i")
           
2
s.rfind("j")
           
10
s.index('s")
        
SyntaxError: unterminated string literal (detected at line 1)
s.index('s')
        
0
s.index('j')
        
10
s.count('p')
        
1
#replace and take method
        

s
        
'saiprasad jaada '
s.replace('m','b')
        
'saiprasad jaada '
s.replace('s','m')
        
'maipramad jaada '
#ENCODE AND DECODE
        
s.maketrans('aeiou','#@$&*')
        
{97: 35, 101: 64, 105: 36, 111: 38, 117: 42}
s.translate(s.maketrans('aeiou','#@$&*')d
            
SyntaxError: '(' was never closed
s.translate(s.maketrans('aeiou','#@$&*')
            j
            
SyntaxError: '(' was never closed
s.translate(s.maketrans('aeiou','#@$&*'))
            
's#$pr#s#d j##d# '
#ENCODE and DECODE
            
text.encode()
            
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    text.encode()
NameError: name 'text' is not defined. Did you mean: 'next'?
text = "HII"
            
text.encode()
            
b'HII'
b'HII'.decode()
            
'HII'
