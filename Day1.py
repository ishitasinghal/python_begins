#program to swap two numbers in one line
# a=4
# b=7
# a,b=b,a
# print(a,b)

#program to take two inputs from user and add them
# a=int(input('enter one number'))
# b=int(input('enter second number'))
# res=a+b
# print('Result is: ', res)

#program performing operations according to user

# a = int(input('enter one number'))
# b = int(input('enter second number'))
#
# switcher = {
#     'A': a + b,
#     'S': a - b,
#     'D': a / b,
#     'M': a * b,
#     'R': a % b,
# }
#
# choice = input('Press A for addition, S for subtraction, D for division, M for multilicaton. R for remainder')
#
# print('Result is :', switcher.get(choice, 'Invalid choice'))



#DAY 2
#WAP for eligibility of license
# age=int(input('Enter age'))
# if(age<16):
#     print('Not eligible')
# elif(age>=16 or age<18):
#     print('Eligible for learner license')
# else:
#     print('Eligible')

#WAP for quad eqn
# a=int(input("Enter a "))
# b=int(input("Enter b "))
# res=(2*a*a)+(3*b)
# print(res)


#WAP to check for leap year
# def is_leap(year):
#     leap = False
#
#     if(year%4==0):
#         if(year%100==0):
#             if(year%400==0):
#                 leap=True
#         else:
#             leap=True
#
#     return leap
#
# year = int(input("Enter year to check for leap year"))
# print(is_leap(year))

#WAP to find prime numbers between 1-100
# for i in range(2,101):
#     c=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             c=c+1
#     if(c==2):
#         print(i, end=' ')

#WAP to print table of a number
# num=int(input("Which number table do u want?"))
# for i in range(1,11):
#     print(num,'*',i,'=',i*num)

#WAP to print calendar
# import calendar
# print(calendar.month(2019,4))

#WAP to perform user defined func
# ch=input("Enter your choice:    A to add, S to subtract, D to divide, M to multiply")
#
# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b
#
# def div(a,b):
#     return a/b
#
# def mul(a,b):
#     return a*b
#
# a=int(input("Enter num1"))
# b=int(input("Enter num2"))
# if(ch=='a' or ch=='A'):
#     i=add(a,b)
#     print(i)
# if(ch=='s' or ch=='S'):
#     if(b>a):
#         j=sub(a=b,b=a)
#     else:
#         j=sub(a,b)
#     print(j)
# if(ch=='d' or ch=='D'):
#     k=div(a,b)
#     print(k)
# if(ch=='m' or ch=='M'):
#     l=mul(a,b)
#     print(l)


#WAP to find factorial
# a=int(input("Enter number to find factorial"))
#
# def fact(a):
#     if(a==1):
#         return 1
#     else:
#         return a*fact(a-1)
#
# f=fact(a)
# print("***********Factorial is  ************", f)

# Take age program and continue the program till the user has not entered 'n' character. Before exiting the program, print all the age parameters tested by the user.
# def check(age):
#     if(age<16):
#         print('Not eligible')
#     elif(age>=16 or age<18):
#         print('Eligible for learner license')
#     else:
#         print('Eligible')
# n=1
# agelist=[]
# while(n!=10):
#     age =int(input('Enter age'))
#     agelist.append(age)
#     check(age)
#     n=n+1
# print(agelist)


#Correct solution:
# tested_ages=[]
# while(True):
#     age=input("Enter your age")
#
#     if(age=='n'):
#         break
#     else:
#         age=int(age)
#         if(age>=18):
#             print("Eligible")
#         else:
#             print("Not eligible")
#
#         tested_ages.append(age)
#
# print("Age parameters tested: ", tested_ages)


# 2. Take age program, print a dictionary that should display the parameter entered by the user and then display the corresponding value for that age parameter.
# (Print all the key and values of dictionary separately.)

# eligible_age=[]
# noteligible_age=[]
# tested_dict={}
#
# while(True):
#     age = input("Enter your age")
#
#     if(age=='n'):
#         break
#
#     else:
#         age=int(age)
#         if(age>=18):
#             eligible_age.append(age)
#         else:
#             noteligible_age.append(age)
#
# tested_dict['Eligible']=eligible_age
# tested_dict['Not eligible']=noteligible_age

# print("Age parameters tested are: ", tested_dict)

















# 3. Take three lines input from the user, separated by "." Using some inbuilt functions and
# add those lines in a list and then print those lines.

#print(input("enter any string including three lines").split('.'))


# 4. Take input from user a particular paragraph and print the frequency of words in that paragraph.
# stlist=input("Enter a paragraph").split(' ')
# nlist=[]
# for i in stlist:
#     if(i not in nlist):
#         nlist.append(i)
# for j in range(0,len(nlist)):
#     print('Frequency of ',nlist[j],'is', stlist.count(nlist[j]))



#5. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# clist1=[input("Enter colours for list one") for i in range(0,5)]
# clist2=[input("Enter colours for list two") for j in range(0,5)]
# nlist=[]
# for i in range(0,len(clist1)):
#     if(i not in clist2):
#         nlist.append(clist1[i])
# print(nlist)
# if we would have written set(nlist)
# then set removes the repeated elements, that is, it removes duplicacy.



# 6. Write a program to find maximum and minimum numbers from a set of inputs given by the user. [Do not use built-in functions.]
# list1 = [ int(input("Enter num")) for i in range(6)]
# min=list1[0]
# max = list1[0]
# for i in list1:
#     if ( i > max):
#         max=i
#     if ( i < min):
#         min=i
#
# print("Maximum value is : ", max)
# print("Minimum value is : ", min)




# 7. Using list comprehension, create a list of numbers in between a specific range.
# a=int(input("Enter strt of range"))
# b=int(input("Enter end of range"))
# print([i for i in range(a,b+1)])

# 8. Add more than 2 or more elements to the list in one line.
# listadd=[input("Enter element ") for i in range(0,5)]
# print(listadd)

# 9. Write a function to take in a list of girls and boys and find every possible girl-boy dance combinations for a dance partnership
# g=int(input("Enter number of girls"))
# girls=[input("Enter girl ") for i in range(0,g)]
# b=int(input("Enter number of boys"))
# boys=[input("Enter boy ") for j in range(0,b)]
#
# for i in girls:
#     for j in boys:
#         print(i,'-',j)


import tkinter as tk
import sqlite3
# con =sqlite3.connect('guidb.db')
#
# TABLE_NAME = "student_tablegui"
# STUDENT_ID = "student_id"
# STUDENT_NAME = "student_name"
# STUDENT_COLLEGE = "student_college"
# STUDENT_ADDRESS = "student_address"
# STUDENT_PHONE = "student_phone"
#
# window=tk.Tk()
# window.title("GUI Database")
#
#
# name_label = tk.Label(window, text="Enter name")
# name_label.pack()
# field1 = tk.Entry(window)
# field1.pack()
#
# college_label = tk.Label(window, text="Enter college")
# college_label.pack()
# field2 = tk.Entry(window)
# field2.pack()
#
# address_label = tk.Label(window, text="Enter address")
# address_label.pack()
# field3 = tk.Entry(window)
# field3.pack()
#
# phone_label = tk.Label(window, text="Enter phone")
# phone_label.pack()
# field4 = tk.Entry(window)
# field4.pack()
#
#
# def entries():
#     con.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME +
#                         "( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + STUDENT_NAME + " TEXT, " +
#                        STUDENT_COLLEGE + " TEXT, " +
#                        STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE +
#                        " INTEGER);")
#
#     print("table created successfully!")
#     name = field1.get()
#     college = field2.get()
#     address = field3.get()
#     phone = field4.get()
#
#     con.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
#                 STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " + STUDENT_PHONE + ") "
#                                                                                   "VALUES ( '"+name+"', '"+college+"', '"+address+"', "+phone+"); ")
#     con.commit()
#
# def display():
#     cursor = con.execute("SELECT * FROM " + TABLE_NAME + " ;")
#     for row in cursor:
#         print("Student id is: ", row[0])
#         print("Student name is:  ", row[1])
#         print("Student college is: ", row[2])
#         print("Student address is : ", row[3])
#         print("Student phone numbr is : ", row[4])
#
#     con.close()
#
#
# button = tk.Button(window, text="Submit", command=lambda: entries())
# button.pack()
#
# display_button = tk.Button(window, text="Display", command=lambda: display())
# display_button.pack()
#
# window.mainloop()




