'''def like_post(username, post):
    print(username, "liked", post)

like_post("Sai", "My New Photo")
like_post("Rahul", "Travel Photo")'''

'''def gst(price):
    print("Original price: ",price)
    print("final price",price+price*0.18)
gst(1000)
gst(5000)
gst(500)
gst(890)
gst(100)'''



'''def table(n):
    print(f'{n}-Table')
    print("----------------")
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
for i in range(1,21):
    table(i)'''


'''def isleap(year):
    if year%400 ==0 or(year%4==0 and year%100!=0):
        return " Leap year"
    else:
        return " Not a Leap Year"
print(isleap(2012))
print(isleap(2014))
print(isleap(2016))
print(isleap(2020))
print(isleap(2024))
print(isleap(2026))'''

'''def isprime(n):
    for i in range(1,n//2+1):
        if n%i==0:
            return "NOT a prime"
        
    return " Prime"
    
print(isprime(5))
print(isprime(10))'''


# positional aruguments:

'''def display(name,email,pw):
    print("name: ",name)
    print("email: ",email)
    print("pw:",pw)
display('sai','sai@gmail','s123')
display('sai@gmail','sai','s123')
display('s123','sai','sai@gmail')'''


#KEyword arguments:

def display(name,email,pw):
    print("name: ",name)
    print("email: ",email)
    print("pw:",pw)
display(name='sai',email='sai@gmail',pw='s123')
display(email='sai@gmail',name='sai',pw='s123')
display(pw='s123',name='sai',email='sai@gmail')
