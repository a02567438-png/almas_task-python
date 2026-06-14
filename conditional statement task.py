'''#largest num:
a=int(input("enter the num"))
b=int(input("enter the num"))
if a>b:
    print("a is the largest num")
else:
    print("b is the largest num")
    
#smallest num
a=int(input("enter the num:"))
b=int(input("enter the num:"))
if a>b:
    print("b is the smallest num")
else:
    print("a is the smallest num")

#absolute value means dist from 0 on
#a num line exactly (| | vertical bars)
a=int(input("enter the num:"))
print(abs(a))
#absolute value using if else condition
n=int(input("enter the num:"))
if n<0:
    print(-n)
else:
    print(n)

#even or odd
s=int(input("enter the num:"))
if s%2==0:
    print("it is even")
else:
    print("odd")

#multiple of 5
a=int(input("enter the num:"))
if a%5==0:
    print("it is a multiple of 5")
else:
    print("not a multiple of 5")
    #to check two digit num or not
r=int(input("enter the num:"))
if r//10==0:
    print("it is a single digit num:")
elif r//100==0:
    print("it is a two digit num")
else:
    print("neither a two or single digit num:")

# checks that the num ends with 0 or not:
n=int(input("enter the num:"))
if n%10==0:
    print("the last digit ends with zero")
else:
    print("last digit does not ends with zero")

#to accept the num and checks the squ is <50 or >50:
a=int(input("enter the num"))
if a>0:
    print("accepting the num")
    if a**2>50:
        print("the square of the num is greater then 50")
    else:
        print("the square of the num is less then 50")
else:
    print("invalid num")
    #to accept the num and sub the num then check diff ans is 0
a=int(input("enter the num"))
b=int(input("enter the num"))
if a>0 or b>0:
    print("accepting the num")
    if a-b==0:
        print("diff ans is 0")
    else:
        print("0 is not the ans")
else:
    print("invalid num")

#to find pass or fail
n=int(input("enter the num:"))
if n>50:
    print("the student is passed")
else:
    print("the student has been failed")

# to accept the num and checks that the num is divisible by 10:
d=int(input("enter the num:"))
if d>0:
    print("the num is accepted")
    if d%10==0:
        print("it is div by 10")
    else:
        print("it is not div by 10")
else:
    print("the num is not accepted")
