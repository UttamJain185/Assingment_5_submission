import math

#Question No.1 

print("QUESTION No.1:")
    
string1 = input("Enter a string-:")    # input string variable
string2 = ""  #empty string
for i in string1:
    string2 = i + string2
    
print ("The reversed string is : ",string2,"\n") # reversed string

#Question No.2 

print("QUESTION No.2:")

a=int(input("Enter your first no.-:"))    # input value of lower range
b=int(input("Enter your second no.-:"))   # input value of upper range
num1=int(input("Enter the number which you will divide on entire range-:"))      # input of number you want to divide
print("All numbers in range",(a,b),"which are divisible by",num1,"are as follows-:")
for item in range(a,b) :
    if item%num1==0:
        print(item)
print("")

#Question No.3 

print("QUESTION No.3:")

import random


s1 = int(input("Enter your first side:-"))
s2 = int(input("Enter your second side:-"))
s3 = int(input("Enter your third side:-"))
s = (s1 + s2 + s3) / 2
if s1+s2>s3 and s3+s2>s1 and s1+s3>s3 :
        print("Area is equal to :-",(s*(s-s1)*(s-s2)*(s-s3))**(1/2))
else :
        print("The sides entered don't for a triangle!!!")

print("")

#Question No.4 

print("QUESTION No.4:")
print("The given pattern is as follows-:")
for i in range(0,10):
    if(i<5):
       for j in range(0,i+1,1):
        print("*",end="")
    else:
        for j in range(0,10-i,1) :
          print("*",end="")
    print("\n")
    
#Question No.5 

print("QUESTION No.5:")
      
rows = int(input("Enter the number of rows: "))
count=0
for i in range(0,rows):
    for j in range(0,i+1):
        if(count>25):
         count=0
        print(chr(65+count),end="")
        count+=1
    print("\n")
    
#Question No.6 

print("QUESTION No.6:")
    
lower=int(input())
upper=int(input())
count=0
print("The Prime Numbers in range ",(lower,upper),"are as follows-: ")
for i in range(lower,upper+1):
  count=0
  if i<=1:
        count=1
  for j in range(2,i):
    if i%j==0:
       count=1
  if count==0: 
    print(i)
    
print("")
    
#Question No.7

print("QUESTION No.7:")

print("Following are the numbers which are multiple of 7 and divisible by 11 in the range (1-500)-:")
for item in range(1,500):
    if (item%7==0)&(item%11==0):
        print(item)

print("")

#Question No.8

print("QUESTION No.8:")
    
print("you have to Enter 10 integers of your choice-:")
list1 = []
i=1
while i<11:

    num1=int(input("Enter an integer-:"))
    list1.append(num1)
    i=i+1


print("This is the list of integers entered by the user-:",list1)
print("positive numbers are as follows-:",end="")
for item in list1:
    if item>0:
        print(item,end=",")
print("\nnegative numbers are as follows-:",end="")
for item in list1:
    if item<0:
        print(item,end=",")
print("\nodd numbers are as follows-:",end="")
for item in list1:
    if (item%2!=0)&(item>0):
        print(item,end=",")
print("\neven numbers are as follows-:",end="")
for item in list1:
    if (item%2==0)&(item>0):
        print(item,end=",")
count1=int(input("\nEnter the number you want to count in list1-:"))
count_num=list1.count(count1)
print("The number -",count1,",","occurs",count_num,"times in the list1")

print("")

#Question No.9 

print("QUESTION No.9:")
    
a = list()         #intialising a list
num = int(input("input the number of values in list : "))   #inputs in the list
flag=0
print("input the list values : ")
for i in range(0,num):
    b=input()
    a.append(b)

#counting the number of occurences
print("number of occurences : ")
for i in range(0,num):
   for j in range (0,i):
        if(a[j]==a[i]):
            flag=1
   if flag==0:
    c = a[i]
    print("The number ",a[i]," counts ",a.count(c)," in the list")  
   else:
    flag=0
