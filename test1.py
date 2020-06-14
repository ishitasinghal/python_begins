#Basic programs in Python



###1. Write a Python program to find the repeated items of a tuple.###

# tuple1 = ('Apple', 34, 'Chocolates', 45.6, 'd', True, 'Apple', 'Chocolates', 'Bananas', 45.6)
# for i in tuple1:
#     ct = tuple1.count(i)
#     print(i, "occured ",ct, "times." )

#OUTPUT
# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# Apple occured  2 times.
# 34 occured  1 times.
# Chocolates occured  2 times.
# 45.6 occured  2 times.
# d occured  1 times.
# True occured  1 times.
# Apple occured  2 times.
# Chocolates occured  2 times.
# Bananas occured  1 times.
# 45.6 occured  2 times.
#
# Process finished with exit code 0



###2. Write a Python program to replace last value of a list.###

# list1 = ['Apple', 'Bananas', 'Mango', 'Strawberry', 'Guava', 'Grapes', 'Potato']
# print("Currently the list is : ", list1)
# rep = input("with which fruit you want to replace the last element?")
#
# list1[-1] = rep
# print(list1)

#OUTPUT
# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# Currently the list is :  ['Apple', 'Bananas', 'Mango', 'Strawberry', 'Guava', 'Grapes', 'Potato']
# with which fruit you want to replace the last element?litchi
# ['Apple', 'Bananas', 'Mango', 'Strawberry', 'Guava', 'Grapes', 'litchi']
#
# Process finished with exit code



###3. Write a Python script to merge two Python dictionaries.###

# dict1 = {
#     'Fruit' : 'Mango',
#     'Vegetable' : 'Tomato',
#     'Sport' : 'Cricket',
#     'Player' : 'Bumrah',
#     'Hobby' : 'Sketching',
# }
#
# dict2 = {
#     'College' : 'UPES',
#     'Sap' : 500060649,
#     'Roll no.' : 25,
#     'Back' : False,
#     'Grade' : 'O'
# }
#
# print("Merged dictionaries : ")
# print({**dict1, **dict2})

#OUTPUT

# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# Merged dictionaries :
# {'Fruit': 'Mango', 'Vegetable': 'Tomato', 'Sport': 'Cricket', 'Player': 'Bumrah', 'Hobby': 'Sketching', 'College': 'UPES', 'Sap': 500060649, 'Roll no.': 25, 'Back': False, 'Grade': 'O'}
#
# Process finished with exit code 0



###4. Write a Python program to combine two dictionary adding values for common keys.###

# dict1 = {
#     'a': 1,
#     'b' : 2,
#     'c' : 3,
#     'd' : 4,
#     'e' : 5
# }
# print("Dictionary 1 = ", dict1)
# dict2 = {
#     'a': 10,
#     'f' : 5,
#     'j' : 6,
#     'c' : 40,
#     'e' : 15
# }
# print("Dictionary 2 = ", dict2)
#
# for i in dict1:
#     if i in dict2:
#         dict1[i] = dict1[i]+dict2[i]
# #print(dict1)
# dict3 = {}
# for j in dict2:
#     if j not in dict1:
#         dict3[j] = dict2[j]

#print({**dict1, **dict3})

#OUTPUT

# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# Dictionary 1 =  {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Dictionary 2 =  {'a': 10, 'f': 5, 'j': 6, 'c': 40, 'e': 15}
# {'a': 11, 'b': 2, 'c': 43, 'd': 4, 'e': 20, 'f': 5, 'j': 6}
#
# Process finished with exit code 0



###5. You are driving a little too fast, and a police officer stops you.
# Write a function to return one of 3 possible results:
# "No ticket", "Small ticket", or "Big Ticket".
# If your speed is 60 or less, the result is "No Ticket".
# If speed is between 61 and 80 inclusive, the result is "Small Ticket".
# If speed is 81 or more, the result is "Big Ticket".
# Unless it is your birthday (encoded as a boolean value in the parameters of the function)
# -- on your birthday, your speed can be 5 higher in all cases.

# def ticket(speed, bdy):
#     if ( bdy == "true") :
#         if ( speed <= 65):
#             print("No ticket!!")
#         elif ( speed > 65 and speed <= 85):
#             print("Small Ticket!!")
#         elif ( speed > 85):
#             print("Big Ticket")
#     else:
#         if ( speed <= 60):
#             print("No ticket!!")
#         elif ( speed > 60 and speed <= 80):
#             print("Small Ticket!!")
#         elif ( speed > 80):
#             print("Big Ticket")
#
# speed = input("--Enter the speed--")
# bdy = input("--Is it your birthday??--true/false")
#
# ticket(int(speed), bdy.lower())

#OUTPUT

# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# --Enter the speed--67
# --Is it your birthday??--true/falsetrue
# Small Ticket!!
#
# Process finished with exit code 0


###6. Write a function that takes multiple inputs from the user
# and perform mathematical operation on all the numbers.
# e.g. if the numbers sent are - 2, 3, 4, their result for
# addition is: 9, multiplication is: 24.

# num = input("How many numbers you want to enter??")
# num_list = [input("Enter numbers") for i in range(int(num))]
# add = sub = 0
# mul = div = 1
# #print(num_list)
# for i in num_list:
#     add = add + int(i)
#     mul = mul * int(i)
#     sub = sub - int(i)
#     div = div / int(i)
# print("Addition is ", add)
# print("Subtraction is ", sub)
# print("Multiplication is ", mul)
# print("division is ", div)

#OUTPUT

# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# How many numbers you want to enter??5
# Enter numbers1
# Enter numbers5
# Enter numbers3
# Enter numbers9
# Enter numbers6
# Addition is  24
# Subtraction is  -24
# Multiplication is  810
# division is  0.0012345679012345679
#
# Process finished with exit code 0



###7. Take a list from the user and get a list where all the
# elements from the list are shuffled.

# import random
# list1 = []
# for i in range(5):
#     element = input("Enter element")
#     list1.append(element)
# print("Original list : ",list1)
# random.shuffle(list1)
# print("Random list " , list1)

#OUTPUT

# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# Enter elementone
# Enter element2
# Enter element3
# Enter elementfour
# Enter elementfive
# Original list :  ['one', '2', '3', 'four', 'five']
# Random list  ['3', '2', 'four', 'one', 'five']
#
# Process finished with exit code 0



###8. What is the difference between range & xrange?

# print("For range")
# for i in range(5):
#     print(i)
# print("For xrange")
# for j in xrange(5):    #shows an error as it is no longer used in python 3
#     print(j)
#range creates a list of all the sequences in between the provided
#range whereas xrange in which operations can't be applied.

#OUTPUT

# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# For range
# 0
# 1
# 2
# 3
# 4
# For xrange
# Traceback (most recent call last):
#   File "C:/Users/lenovo/PycharmProjects/Project1/test1.py", line 227, in <module>
#     for j in xrange(5):    #shows an error as it is no longer used in python 3
# NameError: name 'xrange' is not defined
#
# Process finished with exit code 1



###9. I have a tuple_var = (10, 35, 12, 8, 32). What will the program return,
# if I use print(tuple_var[:10]) and print(tuple_var[10]).

# var = (10, 35, 12, 8, 32, 10, 9, 8, 7, 6, 5)
# print("Result of var[:10]",var[:10])     #this statement returns the first 10 elements of the tuple.
# #here, in this case we just have 5 elements so it returns all 5.
# print("Result of var[:10]", var[10])      #this statement returns the element present at index number 10.

#OUTPUT

# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# Result of var[:10] (10, 35, 12, 8, 32, 10, 9, 8, 7, 6)
# Result of var[:10] 5
#
# Process finished with exit code 0



###10. What is the use of ** operator in python? Using this operator print the square of 5.

#the ** operator is used to find the power of any number.
# print(2**4)
# #this returns 2 to the power of 4.
# print("Square of 5 is " ,(5**2))

#OUTPUT

# C:\Users\lenovo\PycharmProjects\Project1\venv\Scripts\python.exe C:/Users/lenovo/PycharmProjects/Project1/test1.py
# 16
# Square of 5 is  25
#
# Process finished with exit code 0
