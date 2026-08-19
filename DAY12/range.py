#range

#range (start,end+1,step):(0,,1)
'''for i in range (1,11):
    print(i)'''

'''for i in range(1,21,1):
    print(i)'''

'''for i in range (5,101,5):
    print(i)'''

#indexing

'''s = 'python programming'
for i in range (len(s)):
    print(i,s[i])'''

'''s = (456,4567,45678,456789)
for i in range(len(s)):
    print(i,s[i])'''

'''s = 'python programming'
for i in enumerate(s):
    print(i)'''
'''
s = [1234,12345,123456,1234567,12345678,123456789]
for i in enumerate(s):
    print(i[0])'''

'''d = {1:2,2:4,3:5,4:5,5:7}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])'''
'''for i in range(1,11):
    if i == 5:
        break
    print(i)'''
'''for i in range(1,11):
    if i == 5:
        continue
    print(i)'''

#use of break and else block and more...
 
l = [12,13,15,16,18,19]
n = [12,15]
for i in l:
    if i == n:
        print(n,"found")
        break
else:
    print(n, "Not found")

'''pin = 123
for i in range(5):
    epin = int(input("ENTER PIN : "))
    if epin  == pin:
        print("unlock phone")
        break
    else:
        print("invalid Pin")
else:
    print("try after 30 seconds")'''

'''n = 17
for i in range(2,n//2+1):
    if n%i == 0:
        print("not a prime number")
        break

else:
    print("prime numbers")'''