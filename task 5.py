#FUNCTION TASK
'''
#prime no
def prime():
    a=int(input("enter the no:"))
    c=0
    for i in range(2,a):
        if a%i==0:
            c+=1
    if c==0:
        return " it is a prime no"
    else:
        return " not a prime no"
print(prime())
'''
#max no
'''def largest(a,b,c):
    return "largest no is:",max(a,b,c)
print(largest(2,3,4))
'''
#swapping
'''def swap(a,b):
    return b,a
print(swap(27,72))'''
#counting'''
def count():
    a=int(input("entera num"))
    c=0
    while a>0:
        a=a//10
        c+=1
        return aprint(count())
'''#count of vowel and consonant'''
def vowel():
    a=input("enter str")
    vowel="aeiouAEIOU"
    v=c=0
    for i in a:
        if i in vowel:
            v+=1
            else:
                c+=1
                print("vowel is",a,"count",v)
                print("consonant is",a,"count",c)vowel()
'''#palindrome in string'''
def palindrome():
    a=input("enter the string")
    b=a[::-1]
    if b==a:
        return "it is a palindrome"
    else:
        return "not a palindrome"print(palindrome())
'''#to calculate the simple interest'''
def si():
    p=int(input("enter the no:"))
    r=int(input("enter the no:"))
    t=int(input("enter the no:"))
    return p*r*t/100print(si())
'''#to find the factorials'''
def factorial():
    n=int(input("enter the no:"))
    for i in range(1,n+1):
        if n%i==0:
            print(i)
factorial()
'''# to return sum of even no to the list'''
def sum_even(lst):
    t=0
    for i in lst:
        if i%2==0:
            t+=i
            return tprint(sum_even([1,2,3,4,6]))
'''#celsius to farenhit'''
def celsius_farenhit(n):
    return ((n*1.8)+32)
print(celsius_farenhit(20))
'''# armstrong no'''
def armstrong():
    a=int(input("enter the no:"))
    b=a
    s=0
    c=0
    while a>0:
        a=a//10
        s+=1
        while b>0:
            r=b%10
            c=c+r**s
            b=b//10
            print("rem is",r)
            print("arm no is",c)
            print("updated value",b)armstrong()
'''#removing the duplicates from the list'''
def duplicates(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
            print(b)duplicates([1,2,3,2,3,4,5])
'''#to find the largest no:'''
def largest():
    a=int(input("enter the no:"))
    b=int(input("enter the no:"))
    c=int(input("enter the no:"))
    if a>b and a>c:
        return"a is the 1st largest"
    elif b>a and b>c:
        return"b is the 2nd largest"
    else:
        return"c is the 3rd largest"
print(largest())
'''#to find 2nd largest:'''
def second_largest(a,b,c):
    num=[a,b,c]
    num.sort()
return num[-2]
print(second_largest(10,99,12))'''
#to find the perfect no'''
def perfectno():
    a=int(input("enter the no:"))
    s=0
    for i in range(1,a):
        if a%i==0:
            s+=i
            if s==a:
                print("it is a perfect no:")
            else:
                print("it is not a perfect no:")
perfectno()'''
#to get n fibo num'''
def fibo(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+bfibo(5)'''
# to get the power of the num'''
def power(x,n):
    result=1
    for i in range(n):
        result=result*x
        return resultprint(power(2,5))'''
#to find the gcd:'''
def gcd():
    a=int(input("enter the no:"))#7
    b=int(input("enter the no:"))#21
    while b!=0:
        a,b=b,a%b
        print(b)gcd()'''
#email'''
def email():
    a=input("enter the name")
    print(len(a))
    if len(a)>=9 and '@gmai.com'in a:
       print("valid email")
    else:
       print("invalid email")
email()'''
#gcd


















