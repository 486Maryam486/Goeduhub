# -*- coding: utf-8 -*-
"""Assignment/Task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cgrXuCyTriUDGwa1hLWbPyUcZfoSvewQ

# Assignment/Task 1

# Question 1 (i): Write a program that asks user to enter a Color/Fruit/Animal name and it should tell which category belongs to , like its is a fruit or color or Animal
"""

Colors=["Yellow","Green","White","Black"]
Fruits=["Apple","Papaya","Mango","Orange"]
Animals=["Tiger","Lion","Deer","Zebra"]

l1=input("Please enter a Color/Fruit/Animal name ")
if l1 in Colors:
 print("It is a Color")
elif l1 in Fruits:
  print("It is a Fruit")
elif l1 in Animals:
  print("It is an animal")
else:
  print("The name was not defined")

"""## Question 1 (ii):Write a program that asks user to enter two cities and it tells you if they both are in same country or not."""

Canada= ["Toronto","Ottawa","Halifax","Vancuver"]
India=["Delhi","Mumbai","Bangalore","Hyderabad"]

C=input("Please enter the name of 1st city ")
I=input("Please enter the name of 2nd city ")

if C in Canada and I in Canada:
  print("both cities are in Canada")
elif C in India and I in India:
  print("both cities are in India")
else:
  print("They don't belong to same category")

"""# Question 2: Write a python program that can tell you if your grade score good or not . (Normal Score range is 40 to 60)"""

a=int(input("Please enter your grade"))
if a<40:
  print("Your score is low!")
if a>60:
   print("Your score is good!")
elif a>=40 and a<=60:
  print("Your score is normal")

"""## Question 3:  After appearing in exam 10 times you got this result,
result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]
Using for loop figure out how many times you got Pass

"""

list = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]
c=0
for i in list:
  if i=="Pass":
    c=c+1
print("you passed",c,"times")

"""# Question 4:  Write a program that prints following shape
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

"""

r= 5

for i in range(0,r):

    for j in range(0,i+1):

        print("*",end = " ")

    print(" ")

for i in range(r+1,0,-1):

    for j in range(1,i-1):

        print("*",end = " ")

    print(" ")

"""# Question 5:   Lets say you are running a 50 km race. Write a program that,
# ???	Upon completing each 10 km asks you "are you tired?"
# ???	If you reply "yes" then it should break and print "you didn't finish the race"
## ???If you reply "no" then it should continue and ask "are you tired" on every km
# ???	If you finish all 50 km then it should print congratulations message
"""

t=1
for i in range(1,51):
  if t==1:
   if i%10==0:
      print("It is",i,"KM")
      a=input("Are you tired?")
      if a=="Yes":
        print("you didn't finish the race")
        break
      elif a=="No":
        t=0
        continue
  else:
   print("It is",i,"KM")
   a=input("Are you tired?")
   if a=="Yes":
        print("you didn't finish the race")
        break
   elif a=="No":
        continue

   if i==50:
     print("congratulations! you finished the race")

"""## Question 6:  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)."""

for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
      print(x)

"""## Question 7:   Print square of all numbers between 10 to 20 except even numbers"""

n=2
for i in range(10,21):
  t=0
  if i%2!=0:
    t=i**n
    print(i,"**",n,"=",t)

"""# Question 8:  Your Marks for five Test(test1 to test5) looks like this,
# marks_list = [65, 75, 2100, 95, 83]
# Write a program that asks you to enter marks and program should tell you in which test that marks occurred. If marks is not found then it should print that as well.


"""

marks_list = [65, 75, 2100, 95, 83]
a = int(input("Enter marks: "))
if a in marks_list:
  print("Test",marks_list.index(Marks)+1)
else:
  print("This test is not found")