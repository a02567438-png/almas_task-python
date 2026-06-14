#num changing pyramid
##n=4
##a=1
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(a,end=" ")
##        a+=1
##    print()
#num increasing pyramid
##n=4
##for i in range (1,n+1):
##    for j in range(1,i+1):
##        print(i,end=" ")
##    print()
#left triangle
##n=5
##for i in range(5,0,-1):
##    for j in range(1,i+1):
##        print("*",end="")
##    print()
#right primide
##n=5
##for i in range(1,n+1):
##    for j in range(1,n-i+1):
##        print(" ",end=" ")
##    for k in range(1,i+1):
##        print("*",end=" ")
##    print()

###rhombus
##n=5
##
##for i in range(n+1):
##    for j in range(1, i+1):
##        print("*", end=" ")
##    print()
#rev star
##n=5
##for i in range(5,0,-1):
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print()

#rev increasing star
##n=5
##for i in range(1,n+1):
##    for j in range(1,n-i+1):
##        print(" ",end=" ")
##    for k in range(1,2*i):
##        print("*",end=" ")
##    print()

#fully *
n=5
i=1

while i<=n:
    j=1
    while j<=n:
        print("*",end=" ")
        j+=1
    print()
    i +=1











    



