# pass by value:
#if the variable value can be chnages dont effect on the global variables , also known as immutability(int, float,list tuple)
#f the variable value can be chnages  effect on the global variables , also known as mutability(str, set,dict)


#by using datatypes int, float, str, list, tuple,set,bool
''''def display(n):
    n = 10.3
    print("inside the function",n)

n = 10+10.3
display(n)
print("Outside the function",n)'''

#float
'''def display(n):
    n = 10.3
    print("inside the function",n)

n = 10+10.3
display(n)
print("Outside the function",n)'''


#str
def display(n):
    n = "sai"
    print("inside the function",n)

n = 10+10.3
display(n)
print("Outside the function",n)

