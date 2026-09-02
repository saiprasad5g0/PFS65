#reels count
'''def reels():
    data = ['1..100','101..200','201..300','301..400','401..500']
    for i in data:
        yield i

res = reels()

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print((next(res)))'''


#number  count
'''def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

res = countdown()
for i in  res:
    print(i) '''

#facters of a number
'''def facters(num):
    for i in range(1,num+1):
        if num % i== 0:
            yield i
res = facters(12)
for i in  res:
    print(i)'''
#prime numbers 
def prime(num):
    for i in range(2,num+1):
        for j in range(2,i//2+1):
            if i%j == 0:
                break
        else:
            yield i
res = prime(100)
for i in  res:
    print(i,end=" ")
