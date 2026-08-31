# printing from 10 to 1
'''def display(n):
    if n==11:
        return
    display(n+1)
    print(n)

display(1)'''

# reverse a string

'''def display(s,n):
    if n==len(s):
        return
    display(s,n+1)
    print(s[n],end='')

display("codegnan",0)'''

# priting a string with a width you given
'''def display(s,n,w):
    if len(s)-w+1 == n:
        return
    print(s[n :n+w])
    display(s,n+1,w)
s = input("Enter a string: " )
w = int(input("enter the width: "))
display(s,0,w)'''

#implementing a list and sum it
'''def display(l,ind):
    if ind == len(l):
        return 0
    return l[ind] + display(l,ind+1)
l = [4,23,2,34,28,90]
print(display(l,0))'''


'''def display(l):
    if l ==0 :
        return 0
    return l%10 + display(l//10)


l = 12345
print(display(l))'''

#factiorial number:
'''def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
print(factorial(4))
print(factorial(6))'''

#febinacci series
#normal flow
'''n = int(input("Enter  the number:"))
if n==1:
    print(0)
elif n==2:
    print(0,1)
else:
    a,b = 0,1
    print(a,b)
    for i in range(n-2):
        a,b = b,a+b
        print(b,end=" ")'''



#fib in recuursion

def fib(n):
    if n==0:
        return 0
    elif  n==1:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(10):
    print(fib(i))