#SYNTAX::

'''
VAR = lambda arg: exp
'''



#examples:
wish =  lambda name: f"welcome to the course {name}"
print(wish("sai"))
print(wish("prasad"))

gst = lambda price: price+price*0.18
print(gst(800))

avg =lambda a,b,c:(a+b+c)/3
print(avg(2,3,4))
#even numbers 
iseven = lambda a: "even" if a%2 ==0 else "odd" 
print(iseven(6))
#vowels 
largest = lambda a,b,c: a if a>b and a>c else(b if b>c else c)
print(largest(4,5,6))
isvowel = lambda a:"vowel"if a in "aeiouAEIOU"  else "cons"
print(isvowel("aeiou"))

#update function
l = [1,2,3,4,5,6,7]
update = list(map(lambda  i: i+10,l))
print(update)
#discount of number
t = (789,421,3453,24253,35430)
discount = list(map(lambda i :i-i*0.3,t))
print(discount)

#odd numbers filter a modify below 1000
t = (789,421,3453,24253,35430)
discount = list(filter(lambda i: i>1000,t))
print(discount)

#retuens only domains
l = ['saiprasad@gmail.com','saiprasadjada@oyo.com','saiprasad@biryani.com']
res = list(map(lambda i:i.split('@') [1],l))
print(res)

#sum of the integers with reduce function
from functools import reduce
l = [1,2,3,4,5,6,7,8,89,9]
res  = reduce(lambda sum,i: sum+i,l)
print(res)
#product of the numbers 
from functools import reduce
l = [1,2,3,4,5,6,7,8,89,9]
res  = reduce(lambda sum,i: sum*i,l)
print(res)

seats = {'s1':True,
         's2':False,
         's3':False,
         's4':False,
         's5':True,
         's6':True}
availability = list(filter(lambda i: seats [i],seats))
print(availability) 




products = {'eggs': 80,
    'bread' : 60,
    'salt' : 40,
    'sugar' : 20
}
res = list(filter(lambda i : products [i]>50,products))
print(res)

products = {'eggs': 80,
    'bread' : 60,
    'salt' : 40,
    'sugar' : 20}

print(dict(sorted(products.items(),key = lambda i:i[1])))
print(dict(sorted(products.items(),key = lambda i:i[1],reverse= True)))