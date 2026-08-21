'''#proble on for loop
n = int(input("Enter the input: "))
res = []
for i in range(1,n+1):
    if n%i ==0:
        res.append(i)
print(f'Factors of {n} = {res}')'''



'''data = {'biryani': 500,
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
for i in data:
    print(i.ljust(20),data[i])
    prods = input("Enter the products : ").split()
    print("______________bill_____________")
    bill = 0
    for i in prods:
        print(i.ljust(20),data[i])
        bill += data[i]
        print("Total bill".ljust(20),bill'''


'''s = 'python programming'
d = {}
for i in s :
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)'''


s = 'sssssssssssssdeeeeeeedddddddddddeeeeeeesssssssssnnvvvvvvvvvvvfffffffffffff'
c=1
res = ''
for i in range(len(s)-1):
        if s[i]==s[i+1]:
            c+=1
        else:
            res+= s[i]+str(c)
            c=1
print(res+s[i]+str(c))
    