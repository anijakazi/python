'''num=int (input("enter the value to check:"))
flag=0
if num<=1:
 print("not prime")
else:
  for i in range(2,num):
    if(num%i==0):
      flag= flag + 1

  if flag!=0:
   print("not prime")
  else:
   print("prime")'''


####problems


#wap to check numder is even or odd

'''num=int(input("enter the value to check:"))

if num==0 :
    print("number is zero")
elif num<0 :
    print("number is negative")   
else : 
    print("number is positive")  
'''



#wap Take a number from the user and check if it is even or odd.



'''num=int(input("enter the number:"))
if num % 2==0:
    print("even")
else:
    print("odd")
    '''

# Write a program to find the greatest of two numbers.

"""x=int (input("enter the value of x:"))
y=int (input("enter the value of y:"))

if x > y :
  print("x is grater")

else :
  print("y is grater")"""


#Write a program to find the greatest of three numbers

"""x=int (input("enter the value of x:"))
y=int (input("enter the value of y:"))
z=int (input("enter the value of z:"))

if x > y  and x > z :
  print("x is grater")

elif y > x and  y > z :
  print("y is grater")


else :
  print("z is grater")"""




# Take the age of a person and check if they are eligible to vote (18 or above).

"""age= int (input("enter the your age:"))

if age >= 18 :
    print("eligibal to vote")

else :
    print("not eligibal to vote")"""

#  Write a program that asks marks of a student and prints their grade using this rule:90–100 → a75–89 → B50–74 → CBelow 50 →Fail



marks=int(input("enter the marks:"))
if marks > 1 and marks < 101 :
  if marks >= 90 and marks <= 100 :
    print("a class")

  elif marks <= 89 and marks >=75 :
    print("b class")

  elif marks < 74 and marks >= 50 :
    print("c class")

  else :
    print("fail") 
else:
  print(" not consider as markas")   