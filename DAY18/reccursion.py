#RECCURSION function is calling itself 
#generally 2 functions 1. base function 2. reccursion function
#syntax: 

def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(10)


'''def display(s,n):
    if n==len(s):
        return
    print(s[n])
    display(s,n+1)

display("PYTHON",0)'''

