'''i = 1   #initialation 
while i<=10:  #condition
    print(i)
    i+=1 #updatation
'''



'''i = 10
while i>0:
    print(i)
    i-=1'''

'''i = 5
while i<=50:
    print(i)
    i+=5'''

'''s = 'While loop'
i = 0
while i = len(s):
    print(i)
    i+=1'''


'''l = [1234,2345,3456,4567]
i = 0
while i<len(l):
    print(l[i])
    i+=1'''

'''n = 1234
i =0
while n>0:
    i += n%10
    n//=10
print(i)'''

'''n = 34567
res = 0
while n>0:
    rem = n%10
    res = res*10 +rem
    n//=10
print(res)'''


'''n = 123456789
res = 0
while n>0:
    rem  = n%10
    if rem%2==0:
        res+=rem
    n//=10
print(res)'''

'''n = [11,0,2,3,0,44,0,9,0,7,0,5,8,0,0,0,]
while 0 in n:
    n.remove(0)
print(n)

l = [2,3,6,76,12,4,1,4,5,6,7,8,9]
i = 0 
j = len(l)-1
while i <= j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1'''
data = {'biryani': 500,
        'pizza':350,
        'pasta':250,
        'burger':220,
        'shawrama':180,
        'pastry':120,
        'milshake':100,
        'bun':80,
        'coffe':60,
        'tea':30
       }
bill = 0 
while True:
    product  = input("Enter the products name or [E]xit: ")
    if product == 'E':
        print("THANKS FOR SHOPPONG")
        print("TOTAL BILL:",bill)
        break
    else:
        quantity  = int(input("ENTER the quantity:"))
        bill += data[product]*quantity