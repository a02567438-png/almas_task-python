to print the first N natural numbers.
n = int(input("Enter N value: "))
for i in range(1, n + 1):
    print(i)

# First N even natural numbers
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(i * 2)

# First N odd natural numbers
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(2*i+1)


#first n multiple of 3
n=int(input("enter n:"))
for i in range(1,n+1):
       print(i*3)

#first n multiple of 5
n=int(input("enter n:"))
for i in range(1,n+1):
    print(i*5)

#multiples of 2 till n
n=int(input("enter n:"))
for i in range(1,n+1):
  if i%2==0:
        print(i)

#multiples of either 2 or 3 till n
n=int(input("enter n:"))
for i in range(1,n+1):
    if i%2==0 or i%3==0:
        print(i)

#multiple of either or 2,5 or 7 till n
n=int(input("enter n:"))
for i in range(1,n+1):
   if i%2==0 or i%5==0 or i%7==0:
      print(i)

#count num of digit
n=int(input("enter a num"))
c=0
while n>0:
    n//=10
    c+=1
    print(c)

#factor of a num
n=int(input("enter num:"))
for i in range(1,n+1):
 if n%i==0:
  print(i)

#count factor
n=int(input("enter num:"))
count=0
for i in range(1,n+1):
    if n%i==0:
      count+=1
print(count)

#prime number
n=int(input("enter num:"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("yes")
else:
    print("no")

#all prime number from 2 and upto n
n=int(input("enter a number"))
for i in range (2,n+1):
      c=0
      for j in range(1,i+1):
        if i%j==0:
          c+=1
      if c==2:
        print(i)

#fibonacci series(0 to 50)
a=0
b=1
while a<=50:
    print(a)
    c=a+b
    a=b
    b=c
