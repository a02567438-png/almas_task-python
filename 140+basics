 #file handeling
#with open
##with open(r"C:\Users\a0256\OneDrive\Desktop\new.txt","a") as f:
##    print(f.write("iam learning python"))

#write mode
##f=open(r"C:\Users\a0256\OneDrive\Desktop\New folder.txt","a")
##L=["hii this is live wire\nlocation salem\nstate Tamil Nadu"]
##f.writelines(L)
##f.close()


##f=open(r"C:\Users\a0256\OneDrive\Desktop\lina.txt","w")
##L=["hii this is almas ,learning python"]
##f.writelines(L)
##f.close()

##f=open(r"C:\Users\a0256\OneDrive\Desktop\haju.txt","w+")
##L=["hii this is almas ,learning python"]
##f.writelines(L)
##f.seek(0)
##print(f.read())
##f.close()

##f=open(r"C:\Users\a0256\OneDrive\Desktop\new.txt","r+")
##L=["hii this is almas ,learning python"]
##f.writelines(L)
##f.seek(0)
##print(f.read())
##f.close()
##
#task

##a=input("enter std name")
##b=(input("enter std mark"))
##c=(input("enter std id"))
##f=open(r"C:\Users\a0256\OneDrive\Desktop\college_details.txt","a")
##f.write(a+"\n"+b+"\n"+c)
##f.close()

#login 
##f=open(r"C:\Users\a0256\OneDrive\Desktop\pass_details.txt","w")
##a=input("enter your name")
##b=input("enter pass")
##f.write(a+"\n"+b)
##f.close()

#attendance
##f=open(r"C:\Users\a0256\OneDrive\Desktop\new folder.txt","a")
##a=input("enter the name")
##b=input("enter date")
##c=input("entering their attendance")
##f.write(a+"\n"+b+"\n"+c)
##f.close()

#bank
##a=input("enter whether it is a deposit or withdrawl")
##b=input("enter the amount")
##f=open(r"C:\Users\a0256\OneDrive\Desktop\bank_trans","a")
##if a=="deposit":
##    f.write(a+"\n"+b)
##    print("amount has been deposited")
##else:
##    f.write(a+"\n"+b)
##    print("withdrawl amount")
##f.close()


#factorial of num:
##num=int(input("enter num"))#4=4*3*2*1
##factorial=1
##if num<0:
##    print("factorial does not exist for negative number")
##elif num==0:
##    print("factorial of 0 is 1")
##else:
##    for i in range(1,num+1):
##        factorial=factorial*i
##    print(f'the factorial of {num} is {factorial}')

#multiple table
##num=int(input("display multiplication table of"))
##
##for i in range(1,11):
##    print(f"{num}x{i}={num*i}")
        
#fibonacci
##a=0
##b=1
##for i in range(1,50):
##    if a<=50:
##        c=a+b
##        print(a)
##        a=b
##        b=c

#armstron num in interval
##lower=int(input("enter lower limit interval"))
##upper=int(input("enter upper limit interval"))
##
##for num in range(lower,upper+1):
##    order=len(str(num))#find num of digit
##    temp_num=num
##    sum=0
##
##    while temp_num>0:
##        digit=temp_num%10
##        sum+=digit**order
##        temp_num//=10
##
##    if num==sum:
##        print(num)

##limit=int(input("enter the limit"))
##sum=0
##for i in range(1, limit +1):
##    sum+=1
##print("the sum of natural numbers up to",limit,"is:",sum)
#lcm
##a=int(input("enter num"))
##b=int(input("enter num"))
##c=max(a,b)
##a!=0
##for i in range(1,c+1):
##    if i%a==0 and i%b==0:
##        a1=i
##        print(a1)
##print(lcm())
##a=5
##b=8
##
##a,b=b,a
##print("after swapping")
##print("a=",a)
##print("b=",b)

#posative or negative:
##n=int(input("enter num"))
##if n>0:
##    print("positive num")
##elif num == 0:
##    print("zero")
##else:
##    pint("negative num")



##def add(x,y):
##    return x+y
##def subtract(x,y):
##    return x-y
##def multiplay (x,y):
##    return x*y
##def divide (x,y):
##    return x/y
##
##print("select operation")
##print("1.add")
##print("2.subtract")
##print("3.multiplay")
##print("4.divide")
##
##while True:
##    choice=input("enter choice(1/2/3/4):")
##
##    if choice in('1','2','3','4'):
##        try:
##            num1=float(input("enter first num"))
##            num2=float(input("enter second num"))
##        except ValueError:
##            print("Invalid input.Please enter a number")
##            continue
##        if choice=='1':
##            print(num1,"+",num2,"=",add(num1,num2))
##        elif choice=='2':
##            print(num1,"-",num2,"=",subtract(num1,num2))
##        elif choice=='3':
##            print(num1,"*",num2, "=",multiply(num1,num2))
##        elif choice=='4':
##            print(num1,"/",num2, "=",divide(num1,num2))
##
##        next_calculation=input("let's do next calculation? (yes/no):")
##        if next_calculation=="no":
##           break
##    else:
##        print("Invalid Input")
##
#fibonacci sequence

##def recur_fibo(n):
##    if n<=1:
##        return n
##    else:
##        return(recur_fibo(n-1)+recur_fibo(n-2))
##
##nterms=int(input("enter the num of terms(grater than 0):"))
##if nterms<=0:
##    print("please enter positive integer")
##else:
##    print("Fibonaaci sequence")
##    for i in range(nterms):
##        print(recur_fibo(i))
# factorial of num using recursion

##def recur_factorial(n):
##    if n==1:
##        return n
##    else:
##        return n*recur_factorial(n-1)
##num=int(input("enter the number"))
##if num<0:
##    print("sorry ,factorial does not exist for negative number")
##elif num==0:
##    print("the factorial of 0 is 1")
##else:
##    print("the factorial of",num,"is",recur_factorial(num))

##def bodymassindex(height,weight):
##    return round((weight/height**2),2)
##
##h=float(input("enter your height in meters"))
##w=float(input("enter your height in kg"))
##
##print("WELCOME TO BMI CALCULATOR")
##bmi=bodymassindex(h,w)
##print("Your BMI is: ",bmi)
##
##
##if bmi<=18.5:
##    print("your underweight")
##elif 18.5<bmi<=24.9:
##    print("your weight is normal")
##elif 25<bmi<=29.29:
##    print("you are overweight")
##else:
##    print("you are obese")

##import math
##num=float(input("enter a number"))
##if num<=0:
##    print("please enter positive number")
##else:
##    result=math.log(num)
##    print(f"The natural logaramathm of {num} is:{result}")

#cube of first n natural number
##def cube_sum_of_natural_numbers(n):
##    if n<=0:
##        return 0
##    else:
##        total=sum([i**3 for i in range(1,n+1)])
##        return total
##n=int(input("enter the value of n"))
##
##if n<=0:
##      print("please enter the positive integer")
##else:
##    result=cube_sum_of_natural_numbers(n)
##    print(f"The cube sum of the first {n} natural number is:{result}")
##
#python program to find sum of array
#finding the sum of array
##arr=[1,2,3,4,6]
##ans=sum(arr)
##print('sum of the array is ',ans)
#function to find sum of element in an array
##def sum_of_array(arr):
##    total=0
##
##    for element in arr:
##        total+=element
##
##    return total
##array=[1,2,3]
##result=sum_of_array(array)
##print("sum of the array",result)

#find largest element in the array
##def find_largest_element(arr):
##    if not arr:
##        return "Array is empty"
##    largest_element=arr[0]
##    for element in arr:
##        if element>largest_element:
##            largest_element=element
##    return largest_element
##my_array=[10,20,30,99]
##result=find_largest_element(my_array)
##print(f"The largest _element in the array is:{result}")
##
#python program for array rotation.
##def rotion_array(arr,d):
##    n=len(arr)
##
##    if d<0 or d>=n:
##        return "Invalid rotation value"
##    rotated_arr=[0]*n
##
##    for i in range(n):
##        rotated_arr[i]=arr[(i+d)%n]
##    return rotated_arr
##arr=[1,2,3,4,5]
##d=2
##result=rotion_array(arr,d)
##print("Original Array",arr)
##print("Rotated Array",result)

#split array and fist part end
##def split_and_add(arr,k):
##    if k<=0 or k>=len(arr):
##        return arr
##    first_part=arr[:k]
##    second_part=arr[k:]
##    result=second_part+first_part
##    return result
##arr=[1,2,3,4,5]
##k=3
##result=split_and_add(arr,k)
##print("Original Array:",arr)
##print("Array after splitting add adding",result)
##    
#check array is monotonic.
##def is_monotonic(arr):
##    increasing=decreasing=True
##
##    for i in range(1,len(arr)):
##        if arr[i]>arr[i-1]:
##            decreasing=False
##        elif arr[i]<arr[i-1]:
##            increasing=False
##    return increasing or decreasing
##arr1=[1,2,2,3]
##arr2=[3,2,1]
##arr3=[1,3,2,4]
##
##print("arr1 is monotonic:",is_monotonic(arr1))
##print("arr2 is monotonic:",is_monotonic(arr2))
##print("arr3 is monotonic:",is_monotonic(arr3))

###add two matrices
##def add_matrices(mat1,mat2):
##    if len(mat1) != len(mat2) or len(mat1[0] != len(mat2[0])
##        return "Matrices must have the same dimentions for addition"
##
##    result=[]
##    for i in range(len(mat1)):
##        row=[]
##        for j in range(len(mat1)):
##            row.append(mat1[i][j]+mat2[i][j]
##                       result.append(row)
##                       return result
##                    matrix1=[
##    [1,2,3],
##    [4,5,6],
##    [3,2,1]
##]
##matrix2=[
##    [9,8,7],
##    [6,5,4],
##    [3,2,1]
##]
##result_matrix=add_matrices(matrix1,matrix2)
##if isinstance(result_matrix,str):
##    print(result_matrix)
##else:
##    print("Sum of matrices:")
##    for row in result_matrix:
##        print(now)

#multiple of two matrices{error}
##def multiply_matrices(mat1,mat2):
##    #determine the dimension of the input matrices
##    row1=len(mat1)
##    cols1=len(mat1[0])
##    row2=len(mat2)
##    cols2=len(mat2[0])
##    #check if multiplication if possible
##    if cols1!=rows2:
##        return "Multiplication is not possible.Number of columr"
##    result=[[0 for_in range(cols2)]for_in range(rows1)]
##
##    #matrix multiplication
##    for i in range(rows1):
##        for j in range(cols2):
##            for k in range(cols1):
##                result[i][j]+=mat[i][k]*mat2[k][j]
##        return result
##matrix1=[[1,2,3],
##         [4,5,6]]
##matrix2=[[7,8],
##         [9,10],
##         [11,12]]
##
##result_matrix=multiply_matrices(matrix1,matrix2)
##if isinstance(result_matrix,str):
##    print(result_matrix)
##else:
##    print("Result of matrix multiplicaton")
##    for row in result_matrix:
##        print(row)

#transport matrix in python
##def transpose_matrix(matrix):{error}
##    row,cols=len(matrix),len(matrix[0])
##
##    result=[[0 for_in range(rows)]for_in range(cols)]
##    
##    for i in range(rows):
##        for j in range(cols):
##            result[j][i]=matrix[i][j]
##            
##    return result
##
##matrix=[
##    [1,2,3],
##    [4,5,6]
##]
##
##transposed_matrix=transport_matrix(matrix)
##
##for row in transposed_matrix:
##    print(row)

#square patten
##n=5
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print("*",end=" ")
##    print()

#short words in alphabatical order
##my_str=input("Enter a string")
##
##words=[word.capitalize()for word in my_str.split()]
##
##words.sort()
##print("The sorted words are")
##for world in words:
##    print(words)

#remove punctution from string
##punctuation=''''!()-[]{};:'"\,<>./?@#$%&*_~'''
##
##my_str=input("Enter a string")
##no_punct=   ""
##for char in my_str:
##    if char not in punctuation:
##        no_punct=no_punct+char
##print(no_punct)

#sort world in alphabetic order
##my_str=input("Enter a string:")
##words=[word.capitalize()for word in my_str.split()]
##
##words.sort()
##
##print("The sorted words are:")
##for word in words:
##    print(word)

#given num is a disarium num{error}

##a="hello"
##
##for i,j in enumerate(a):
##    print(i,j)

##def is_disarium(number):
##
##    num_str=str(number)#4567
##
##    digit_sum=sum(int(i)**(index + 1)for index,i in enumerate(number))
##    
##    return digit_sum==number
##
##
##try:
##    num=int(input("Enter a number"))
##
##    if is_disarium(num):
##        print(f"{num}is a Disarium number.")
##    else:
##        print(f"{num}is not a Disarium number.")
##except ValueError:
##    print("Invalid input.Please enter a valid number.")
##
##disarium num bet 1 tom100{error}
##def is_disarium(num):
##    num_str=str(num)
##    digit_sum=sum(int(i)**(index+1)for index,i in enumerate(number))
##    return num==digit__sum
##disarium_numbers=[num for num in range(1,101)if is_disarium(num)]
##print("Disarium numbers between 1 and 100:")
##for num in disarium_numbers:
##    print(num,end=" \ ")

#happy number
##def is_happy_number(num):
##    seen=set()
##    while num!=1 and num not in seen:
##        seen.add(num)
##        num=sum(int(i)**2 for i in str(num))
##
##    return num==1
##num=int(input("Enter a number"))
##if is_happy_number(num):
##    print(f"{num}is a happy number")
##else:
##   print(f"{num}is not a Happy Number")

##class person:
##    def __init__(self,name,age):
##        self.n=name
##        self.a=age
##        
##    def add(self):
##        print(self.n)
##             
##n=input('enter')
##ag=input('enter')
##
##p=person(n,ag)
##print(p.n)
##print(p.a)
##

##class insta:
##    def __init__(self,course):
##        self.c=course
##        print('Welcom to my home page')
##        print(self.c)
##    def story(self):
##        self.count=10
##        print('story page')
##        print(self.count)
##    def reels(self):
##        print('reels Loding')
##v=insta("java")

##class telegram:
##    def __init__(self):
##        print('Welcome to movies page')
##    def post(self):
##        self.count=8
##        print('post page')
##        print(self.count)
##    def chat(self):
##        print('chat loding')
##g=telegram()
##g.chat()
##g.post()

##class spotify:
##    def __init__(self):
##        print('Welcome to spotify home page')
##    def music(self):
##        self.count=9
##        print('music page')
##        print(self.count)
##    def follow(self):
##        print('follow others')
##l=spotify()
##l.music()
##l.follow()
        
##class tiktok:
##    def __init__(self):
##        print('Welcome to tiktok home page')
##    def reels(self):
##        self.count=10
##        print('reels loding')
##        print(self.count)
##    def uplode(self):
##        print('uplode reels')
##    def follow(self):
##        print('follwers loding')
##m=tiktok()
##m.reels()
##m.uplode()
##m.follow()

##def is_harshad_number(num):
##    digit_sum=sum(int(i)for i in str (num))
##    return num%digit_sum==0
##num=int(input("Enter a number"))
##if is_harshad_number(num):
##    print(f"{num}is a harshad number.")
##else:
##    print(f"{num}is not a harshad number.")

##pronic num between 1 and 100

##def is_pronic_number(num):
##    for n in range(1,int(num**0.5)+1):
##        if n*(n+1)==num:
##            return True
##    return False
##
##print("Pronic number 1 and 100 are:")
##for i in range(1,101):
##    if is_pronic_number(i):
##        print(i,end="|")

# sum of element in a list{error}
##number=[10,20,30,40,50]
##
##sum_of_numbers=0
##
##for i in numbers:
##    sum_of_number+=1
##    
##print("Sum of element in the list:",sum_of_numbers)

##multiple of all num in list
number=[10,20,30,40,50]

product_of_numbers=1

for i in number:
    product_of_numbers*=1

print("Product of element in the list:",product_of_numbers)

















