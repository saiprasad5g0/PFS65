
#local and global variables 
#local variables are written inside the function and it can be accesses at within the function.
#global varoable can accesses throught out of the program that meeans both  local and globa.
#keyword is GLOBAL where global keyword can be accesses for both local and global variables.
'''def display():
    n = 10
    print("local Variables",n)
n =10
display()
print("Global Variables",n)'''

'''def display():
    global n
    n+= 10
    print("local Variables",n)

n = 10
display()
print("Global Variables",n)'''


#keyword NONLOCAL
'''def display():
    course ="PFS"
    def update():
        nonlocal course
        course ="JFS"
        print("Inner function",course)
    update()
    print("Outer function",course)

display()  '''

#if we use a built in function and again it is  used as variable, then it will be act as a variable it looses its built in function place
l = [1,2,3,4,5]
print(max(l))
max = 10
print(max)