# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:30:42 2018

@author: uma maheswari
"""

myDict1 = {}
print(myDict1)

myDict2 = {1: "Sky", 2: "Water", 3: "Land"}
print(myDict2)

myDict3 = {"SName": "Anu", "SMarks":(100,99,98,100,94), 20181189:'2018-1-1-189' }
print(myDict3)

myDict4 = dict({1: "Sky", 2: "Water", 3: "Land"})
print(myDict4)


myDict5 = dict([(1, "Sky"), (2, "Water"), (3, "Land")])
print(myDict5)

print(myDict3['SName'])
print(myDict3.get('SMarks'))

myDict3['SName']='Abi'
print(myDict3['SName'])

fibo = {1:0, 2:1, 3:1, 4:2, 5:3, 6:5, 7:8}
print(fibo)
fibo.pop(4)
print(fibo)
fibo.popitem()
print(fibo)
del(fibo[1])
print(fibo)
del fibo
#print(fibo)


#sort a dictionary by value
myDict6 = {5:'five', 2:'two', 3:'three'}
print(sorted(myDict6))

myDict6.update({1:'one'})
print(myDict6)

d1 = {'a': 'apple'}
d2 = {'b': 'bat'}
d3 = {'c': 'cat'}

d4 = {}

for d in (d1, d2, d3): 
    d4.update(d)
    
print(d4)


def IsKeyPresent(x,d):
    if x in d:
        print("The key is present.")
    else:
        print("The key is not present.")

IsKeyPresent('a', d4)


for key, value in d4.items():
    print(key, '  ', value)


n=int(input("Enter a number: "))
d5 = dict()
for x in range(1,n+1):
    d5[x]=x*x*x
print(d5) 

d6 = {'x1': 10, 'y1': 20}
d7 = {'x2': 5, 'y2': 5}
d8 = d6.copy()
d8.update(d7)
print(d8)

print(sum(d8.values()))

d9 = {'p1':100,'p2':200,'p3':300}
product=1
for key in d9:    
    product=product * d9[key]
print(product)
print(d9.keys)
print(d9.values)


d10 = {'a':1,'b':2,'c':3,'d':4}
print(d10)
if 'a' in d10: 
    del d10['a']
print(d10)


d10 = {'d':4,'b':2, 'c':3,'a':1}
for key in sorted(d10):
    print(key, '   ', d10[key])

keyMax = max(d10.keys())
keyMin = min(d10.keys())
print('Maximum key = ',keyMax )
print('Minimum key = ', keyMin )
print('Maximum Value = ', d10[keyMax] )
print('Minimum Value = ', d10[keyMin] )


d11 = {'d':4,'b':2, 'c':3,'a':1, 'a':1, 'a':1}
d12 = {}
for key, value in d10.items():
    if value not in d12.values():
        d12[key] = value

print(d12)
print(len(d12))

print(d11)
print(d12)

d12.update({'e':5, 'f':6})
print(d12)
d13 = {}
for key, value in d11.items():
    if key in d12:
        print('Yes')
        d13[key] = value+d12[key]
print(d13)


letters = "abcdefabcdefghi"
histogram = {}

for aLetter in letters:
    histogram[aLetter] = histogram.get(aLetter,0) + 1

for item in histogram.items():
    print(item)
    
     
phone_book={"S&H":"326","CSE":"123",
            "IT":"233","EEE":"241"}
print("Press enter to quit")
 
while True:
    entry=input("Enter contact name:")
    if entry==" ":
        break
    if entry in phone_book:
        print(entry,"'s number:",phone_book[entry] )
        break
    else:
        print(entry," does not exist in your phonebook")
        choice = input("Add to the phonebook (y/n) ?")
        if choice =='y':
            new_num=input("Enter contact's number:")
            phone_book[entry]=new_num
            print("Your phonebook has been updated.")
            break
        else:
            break
        

