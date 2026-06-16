#to add a key to a dictionary
#new keys 'c' with value 3 is added to the dict
a={'a':1,'b':2}
a['c']=3
print(a)

#to concatenate the following dictionaries to create a new one.
#update() combines all dict into one
Dic1={1:10, 2:20} 
Dic2={3:30, 4:40} 
Dic3={5:50, 6:60}
D={}
D.update(Dic1)
D.update(Dic2)
D.update(Dic3)
print(D)

#to iterate over dictionaries using for loops.
#items()return both key and value 
d={'a':1,'b':2,'c':3}
for key,value in d.items():
    print(key,value)
    
#to print a dictionary where the keys are numbers between 1 and 15 and the values are the square of the keys
#stores num as key and its square as value
d={}
for i in range(1,16):
    d[i]=i*i
    print(d)

# to merge two Python dictionaries.
#update()merge d2 into d1
d1={'a':1,'b':2}
d2={'c':3,'d':4}
d1.update(d2)
print(d1)

#to sum all the values in a dictionary.
#value() gets all value and sum() adds them
d={'a':10,'b':20,'c':30}
print(sum(d.values()))

#to get the key, value and item in a dictionary
#keys()-all keys
#values()-all values
#items()-key-value pairs together
d={'a':10,'b':20}
print("keys:",d.keys())
print("values:",d.values())
print("items:",d.items())

#to add a key to a dictionary
#new keys 'c' with value 3 is added to the dict
a={'a':1,'b':2}
a['c']=3
print(a)

#to concatenate the following dictionaries to create a new one.
#update() combines all dict into one
Dic1={1:10, 2:20} 
Dic2={3:30, 4:40} 
Dic3={5:50, 6:60}
D={}
D.update(Dic1)
D.update(Dic2)
D.update(Dic3)
print(D)

#to iterate over dictionaries using for loops.
#items()return both key and value 
d={'a':1,'b':2,'c':3}
for key,value in d.items():
    print(key,value)
    
#to print a dictionary where the keys are numbers between 1 and 15 and the values are the square of the keys
#stores num as key and its square as value
d={}
for i in range(1,16):
    d[i]=i*i
    print(d)

# to merge two Python dictionaries.
#update()merge d2 into d1
d1={'a':1,'b':2}
d2={'c':3,'d':4}
d1.update(d2)
print(d1)

#to sum all the values in a dictionary.
#value() gets all value and sum() adds them
d={'a':10,'b':20,'c':30}
print(sum(d.values()))

#to get the key, value and item in a dictionary
#keys()-all keys
#values()-all values
#items()-key-value pairs together
d={'a':10,'b':20}
print("keys:",d.keys())
print("values:",d.values())
print("items:",d.items())

#to add a key to a dictionary
#new keys 'c' with value 3 is added to the dict
a={'a':1,'b':2}
a['c']=3
print(a)

#to concatenate the following dictionaries to create a new one.
#update() combines all dict into one
Dic1={1:10, 2:20} 
Dic2={3:30, 4:40} 
Dic3={5:50, 6:60}
D={}
D.update(Dic1)
D.update(Dic2)
D.update(Dic3)
print(D)

#to iterate over dictionaries using for loops.
#items()return both key and value 
d={'a':1,'b':2,'c':3}
for key,value in d.items():
    print(key,value)
    
#to print a dictionary where the keys are numbers between 1 and 15 and the values are the square of the keys
#stores num as key and its square as value
d={}
for i in range(1,16):
    d[i]=i*i
    print(d)

# to merge two Python dictionaries.
#update()merge d2 into d1
d1={'a':1,'b':2}
d2={'c':3,'d':4}
d1.update(d2)
print(d1)

#to sum all the values in a dictionary.
#value() gets all value and sum() adds them
d={'a':10,'b':20,'c':30}
print(sum(d.values()))

#to get the key, value and item in a dictionary
#keys()-all keys
#values()-all values
#items()-key-value pairs together
d={'a':10,'b':20}
print("keys:",d.keys())
print("values:",d.values())
print("items:",d.items())

#to add a key to a dictionary
#new keys 'c' with value 3 is added to the dict
a={'a':1,'b':2}
a['c']=3
print(a)

#to concatenate the following dictionaries to create a new one.
#update() combines all dict into one
Dic1={1:10, 2:20} 
Dic2={3:30, 4:40} 
Dic3={5:50, 6:60}
D={}
D.update(Dic1)
D.update(Dic2)
D.update(Dic3)
print(D)

#to iterate over dictionaries using for loops.
#items()return both key and value 
d={'a':1,'b':2,'c':3}
for key,value in d.items():
    print(key,value)
    
#to print a dictionary where the keys are numbers between 1 and 15 and the values are the square of the keys
#stores num as key and its square as value
d={}
for i in range(1,16):
    d[i]=i*i
    print(d)

# to merge two Python dictionaries.
#update()merge d2 into d1
d1={'a':1,'b':2}
d2={'c':3,'d':4}
d1.update(d2)
print(d1)

#to sum all the values in a dictionary.
#value() gets all value and sum() adds them
d={'a':10,'b':20,'c':30}
print(sum(d.values()))

#to get the key, value and item in a dictionary
#keys()-all keys
#values()-all values
#items()-key-value pairs together
d={'a':10,'b':20}
print("keys:",d.keys())
print("values:",d.values())
print("items:",d.items())

'''
armstrong num
1.len find(l)
2.last digit get(%10)
3.each last take a pow(rem**l)
4.pow value sum
5.last digit remove
6.sum num equal=
'''
a=int(input("Enter a num"))
c=0
t=a
while a>0:
    a//=10
    c+=1
a=t
s=0
while a>0:
    r=a%10
    s+=r**c
    a//=10
print(s)
if t==s:
    print("armstrong num")
else:
    print("not a armstrong num")
