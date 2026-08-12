Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"License()"
'License()'
Licence()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Licence()
NameError: name 'Licence' is not defined. Did you mean: 'license'?
#WHITESPACE AND TRIMMING METHODS:::::::::::::::::::::::::::;
s = '                 python programming                    '
s.strip()
'python programming'
s  = lstrip()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s  = lstrip()
NameError: name 'lstrip' is not defined
s.lstrip()
'python programming                    '
s.rstrip()
'                 python programming'
s.replace('','')
'                 python programming                    '
KeyboardInterrupt
s.replace(' ','')
'pythonprogramming'

##SPILITING AND JOINING::::::::::




#
partition string
SyntaxError: invalid syntax
''' partition string'''
' partition string'
s = 'sai-nithin-srenu-ayaaz-karthik'
s
'sai-nithin-srenu-ayaaz-karthik'
s.split('_',2)
['sai-nithin-srenu-ayaaz-karthik']
s.split('_')
['sai-nithin-srenu-ayaaz-karthik']
s.rsplit('_',2)
['sai-nithin-srenu-ayaaz-karthik']
l = '''sai'''
l = '''sai'''
'srenu'
'srenu'
s.split('-')
['sai', 'nithin', 'srenu', 'ayaaz', 'karthik']
s.rsplit('-',2)
['sai-nithin-srenu', 'ayaaz', 'karthik']
s.lsplit('-',2)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.lsplit('-',2)
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
l =  '''sai'''
l = '''sai'''
SyntaxError: multiple statements found while compiling a single statement
l = '''sai'''
l = '''sai'''
SyntaxError: multiple statements found while compiling a single statement
l = '''sai'''
l = '''sai'''
l = '''sai'''
l = '''sai
nithin
srenu
ayaaz
karthik'''
l
'sai\nnithin\nsrenu\nayaaz\nkarthik'
'.'.join((l)

         nqss
         
SyntaxError: '(' was never closed
'.'.join(l)
         
's.a.i.\n.n.i.t.h.i.n.\n.s.r.e.n.u.\n.a.y.a.a.z.\n.k.a.r.t.h.i.k'
'@'.join(l)
         
's@a@i@\n@n@i@t@h@i@n@\n@s@r@e@n@u@\n@a@y@a@a@z@\n@k@a@r@t@h@i@k'
s
         
'sai-nithin-srenu-ayaaz-karthik'
s.partition('.')
         
('sai-nithin-srenu-ayaaz-karthik', '', '')
s.rpartition('.')
         
('', '', 'sai-nithin-srenu-ayaaz-karthik')
#partition string
         

#is upper and lower
         
a = 'strings.png')
SyntaxError: unmatched ')'
a = 'strings.png'
a.startswitch('str')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.startswitch('str')
AttributeError: 'str' object has no attribute 'startswitch'. Did you mean: 'startswith'?
a.startswith('str')
True
a.startswith('list')
False
a.startswith('py')
False
a.startswith('png')
False
a.endswith('.py')
False
a.endswith('.png')
True
'pyhtonv.13'.islower()
True
'Pythnv.13'.islower()
False
'PYTHON1234!@#$%'.isuppper()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    'PYTHON1234!@#$%'.isuppper()
AttributeError: 'str' object has no attribute 'isuppper'. Did you mean: 'isupper'?
'PYTHON1234!@#$%'.isupper()
True
>>> 'sertujhs'.isalnum()
True
>>> '123446579'.isalnum()
True
>>> '      '.isspace()
True
>>> '   123344'.isspace()
False
>>> 'Hlo Wrd'.istitle()
True
>>> 'HLO wrd'.istitle()
False
>>> 'my_var'.isidentifier()
True
>>> 'my@var'>isidetifier()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    'my@var'>isidetifier()
NameError: name 'isidetifier' is not defined
>>> 
... 'my@var'.isidentifier()
False
>>> a.partiton(' ')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.partiton(' ')
AttributeError: 'str' object has no attribute 'partiton'. Did you mean: 'partition'?
>>> '1233456799'.isdecimal()
True
>>> 'HGWEDQUYRGF1323445'.isdecimal()
False
>>> '123234',isdigit()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    '123234',isdigit()
NameError: name 'isdigit' is not defined
>>> '13234536'.isdigit()
True
>>> '3242344'.isnumerics()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    '3242344'.isnumerics()
AttributeError: 'str' object has no attribute 'isnumerics'. Did you mean: 'isnumeric'?
>>> '1242346343567'.isnumeric()
True
