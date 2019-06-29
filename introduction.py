# print("Hello!!^_^")
# print("multiline comments by ctrl+/ same to undo")
# var=20
# print(var)
# print('var')  #single quotes doesn't make it a character
# print(var,'var')   #to print in the same line
# print(var,end='%')
# print('var')   #when we want to use two print statements but output in one line, we use end kw.

# var=input()
# print(var)
# var=int(var)
# var=var+1
# print(var)

# name=input("Enter name")
# city=input("Enter city")
# phn=int(input("Enter phone number"))
# married=bool(input("Enter marital status"))    # this prints true or false according to the input provided
# #if any input is provided then true else false in case if no input

# print('Name:' , name)
# print("City", city)
# print('phone', phn)
# print('married', married)

# a=4
# b=7
# a,b=b,a
# print(a,b)

# for i in range(0,10):
#     print('Hello World ',i)

# for i in range(10,0,-1):
#     print('Hello World ',i)

# for i in range(0,10,3):
#     print(i)

# a=int(input('Enter starting range'))
# b=int(input('Enter stopping range'))
# if(a<b):
#     for i in range(a,b+1):
#         print(i,end=' ')
# elif(a>b):
#     for i in range(b, a+1):
#         print(i, end=' ')
# else:
#     print("numbers are equal")
#
# for i in range(10):                                #start = 0 by default; step=+1, stop should be defined
#     if(i==5):
#         continue                         #continue continues the loop so 5 ko chdkr sb print hoga break b use krke dekho
#     print(i)

# def fname():
#     for i in range(4):
#         print('Hello World')
# fname()
# print('how are u ??')

# a=int(input("Enter number 1"))
# b=int(input("Enter number 2"))
#
# def sum(a,b):
#     return a+b
# var=sum(a,b)
# if(var%2==0):
#     print("even sum")
# else:
#     print("odd sum")

# for i in range(0,3):
#     for j in range(0,i+1):
#         print('*', end=' ')
#     print()     #for next line

# for i in range(3,0,-1):
#     for j in range(0,i):
#         print(j+1,end=' ')
#     print()

# for i in range(0,3):
#     for j in range(0,i+1):
#         print(j+1, end=' ')
#     print()

# def multiplevaluedfunc(first, second, *third):           #here, *third variable is acting as a list it'll tk all values
#     result=first+second
#     for i in range(0,len(third)):
#         result=result+third[i]
#     print(result)
# multiplevaluedfunc(10,20,50,10,80,20)

# first=int(input('Enter first value'))
# second=int(input('Enter second value'))

# def division(first,second=1):              #setting defalut value
#     result=first/second
#     print('Division result is : ',result)
#
# if(second==0):
#     print('You have entered sec num as 0, that is invalid')
#     division(first)
# else:
#     division(first,second)


# def division(first,second):
#     res=first/second
#     print(res)
# division(second=10,first=20)   #values can be sent accrdng to our order of argmnts


# str=input("Enter any string")
# for i in str:
#     print(i)

# import calendar
# print(calendar.calendar(2019 ))

#Day3
# var="python"
# print(var[::-1])

# var="python"
# for i in range(len(var)-1, -1, -1):
#     print(var[i], end=' ')

#list=[1,2,3,34,'abc','xyz',33.214, 67.5,True]
#print(list1)
# list1.append('append')
# print(list1)
# list1.insert(3,'inserted')
# print(list1)
# print(list1[3])
# print(list1[-3])
# print(len(list1))
# print(list1)
# print(list1[3:])
# print(list1[:3])
# print(list1[2:8:2])

#print(list1[20])
# newlist=list[:20]
# print(newlist)

####tuple####
# tup=(1,4,5,8,'ggj','ufhvjh', 37.7, 320.1, True)
# print(tup)
# print(len(tup))      #same as tuple, the only diff is () and can't b chnged

# dict1={
#     "Name":'Berry',
#     "Phone": 7060030972,
#     'Height': 5.8,
#     'Married':False
# }
# print(dict1)
# print(dict1['Name'])
# dict1['Name']='Jerry'
# dict1['City']='Kangra'
#
# print(dict1)
#
# compressedlist=[i for i in range(0,101) if(i%2==0)]
# print(compressedlist)
#
# list1=[int(input("Enter any value")) for i in range(0,10)]
# print(list1)                                                #input in one line


# str=input("Enter a string seperated by 3 dots").split('.')
# print(str)

#Day4
# girls=['a','b','c']
# boys=['d','a','f']
# for i in girls:
#     for j in boys:
#         if(i==j):
#             print("Same value",i)

# list_var=[2,34,12,23,67,89,13]
# new=list(filter(lambda x: x>30, list_var))    #list is a func
# print(new)

# dictionary={
#     0: 'Sunday',
#     1: 'Monday',
#     2: 'Tuesday',
#     3: 'Wednesday',
#     4: 'Thursday',
#     5: 'Friday',
#     6: 'Saturday'
# }
# list_week=[7,2,5,4,9,1,4,6]
# list_weekdays=list(map(lambda x: dictionary.get(x,"Not found"),list_week))
# print(list_weekdays)
#
# from functools import reduce
# list_var=[9,3,2,43,5,6,7]
# mult=reduce(lambda x,y : x*y, list_var)        #reduce reduces the dataset
# print('Multiplication', mult)

# from functools import reduce
# listinp=[input("Enter values") for i in range(10)]
# convint=list(map(lambda x: int(x), listinp))
# listsum=reduce(lambda x,y: x+y, convint)
# print(listsum)

# import statistics
# list1=[20,30,40,10,9,35,24,12]
# a=statistics.median(list1)
# print("Median is :",a)
# l=list(filter(lambda x: x>a,list1))
# print(l)


# class Student:
#     def __init__(self,name='Python'):
#             self.name=name  #here name is local variable and self.name is class variable
#             print("Hello World")
#     def welcome(self):  #self is always the first parameter of any function
#             print(self.name)
#             print("welcome to Python Programming")
# obj=Student('Ishita')
# obj.welcome()
# obj1=Student()
# obj1.welcome()

# class Student:
#     def __init__(self,name, address="Dehradun", phone=0):
#             self.name=name  #here name is local variable and self.name is class variable
#             self.address=address
#             self.phone=phone
#             print("Welcome to the python world")
#
#     def display(self):  #self is always the first parameter of any function
#             print("Printing student details")
#             print(self.name)
#             print(self.address)
#             print(self.phone)
#
# name = input("Enter name")
# address= input("Enter address")
# phone = input("Enter phone number")
#
# if((len(address)>1) & (len(phone)>1)):
#     phone = int(phone)
#     obj=Student(name=name, address=address, phone=phone)
#     obj.display()
# elif (len(address)>1 & (len(phone)==0)):
#     obj=Student(name, address)
#     obj.display()
# elif (len(phone)>1 & (len(address)==0)):
#     phone=int(phone)
#     obj=Student(name=name, phone=phone)
#     obj.display()
# else:
#     obj=Student(name)
#     obj.display()

#
# class Student:
#     def __init__(self,name,address='Dehradun',phone=0):
#         self.name=name
#         self.address=address
#         self.phone=phone
#
#     def display(self):
#             print("Printing student details")
#             print(self.name)
#             print(self.address)
#             print(self.phone)
#
# num=int(input("For how many students you want to store data?"))
# listobj=[]
# for i in range(0,num):
#     name = input("Enter name")
#     address= input("Enter address")
#     phone = input("Enter phone number")
#     if((len(address)>1) & (len(phone)>1)):
#         phone = int(phone)
#         i=Student(name=name, address=address, phone=phone)
#         #obj.display()
#     elif (len(address)>1 & (len(phone)==0)):
#         i=Student(name, address)
#         #obj.display()
#     elif (len(phone)>1 & (len(address)==0)):
#         phone=int(phone)
#         i=Student(name=name, phone=phone)
#         #obj.display()
#     else:
#         i=Student(name)
#         #obj.display()
#
#     listobj.append(i)
# dis=input("Do you want to print the details?:   Press Y for yes ")
# if ( dis=='Y' or dis=='y'):
#     for j in listobj:
#         j.display()


##if we want to define a datatype, we use
## obj: Student
##similar to var=10, here datatype of var is int
##which we can also write as var : int



#EXCEPTIONAL HANDLING
# var_1 = input('Enter the value of first number: ')
# var_2 = input('Enter the value of second number: ')
#
# try:
#     var_1 = int(var_1)
#     var_2 = int(var_2)
#
#     if (var_2 != 0):
#         result = var_1 / var_2
#         print('Division Result is: ', result)
#     else:
#         print('Value of second variable cannot be zero.')
# except ValueError:
#     print("Can only enter integers")

# try:
#     var_1 = int(var_1)
#     var_2 = int(var_2)
#
#     if (var_2 != 0):
#         result = var_1 / var_2
#         print('Division Result is: ', result)
#     else:
#         print('Value of second variable cannot be zero.')
# except ValueError:
#     print("You can only enter integer numbers.")

# var_1 = input('Enter the value of first number: ')
# var_2 = input('Enter the value of second number: ')
#
# try:
#     var_1 = int(var_1)
#     var_2 = int(var_2)
#
#     if (var_2 != 0):
#         result = var_1 / var_2
#         print('Division Result is: ', result)
#     else:
#         print('Value of second variable cannot be zero.')
# except ValueError:
#     print("Enter integer values only.")

# # take input from the user till the time the values are not integer.
# while True:
#     var1 = input('Enter the first number: ')
#     var2 = input('Enter the second number: ')
#
#     try:
#         int_var1 = int(var1)
#         int_var2 = int(var2)
#         break
#     except ValueError:
#         print('Enter only integer values.')
#
#
# # take value from variable 1, 2 and 3. Compute the difference of variable 1, 2 and then
# # divide it's result from variable 3
# var1 = int(input('Enter the value of first number: '))
# var2 = int(input('Enter the value of second number: '))
# var3 = int(input('Enter the value of third number: '))
#
# result = var1 - var2
#
# division_result = var3/result
#
# print(division_result)





#INhertiance

# introduction to Classes -
# class Student:  ## user defined datatype
    # def __init__(self, name='Python'):  # constructor
    #     self.name = name
    #     print("Hello World")
    #
    # def welcome(self):
    #     print(self.name)
    #     print('Welcome to python programming')

#
# obj = Student('Gurjas')
# obj.welcome()
# obj1 = Student()
# obj1.welcome()
#
#
# # Introduction to Inheritance
# class BaseClass:
#
#     def __init__(self):
#         self.var_1 = 2
#         print("Base Class")
#
#     def helloFxn(self, a=10):
#         print("Hello Inside base class")
#
#
# class DerivedClass(BaseClass):
#
#     def __init__(self):
#         super().__init__()
#         print("Derived Class")
#         super().helloFxn(a=20)
#         self.helloFxn()
#
#     def helloFxn(self):
#         print("Hello inside derived class")

#
# obj = DerivedClass()
#
#
# ## Static -- Students Class
#
# class Student:
#     def __init__(self, name, address="Dehradun", phone=0):
#         self.name = name
#         self.address = address
#         self.phone = phone
#         print("Welcome to Brillica Services")
#
#     def display_data(self):
#         print("Printing students details")
#         print(self.name)
#         print(self.address)
#         print(self.phone)
#
#
# name = input('Enter your name')
# address = input('Enter your address')
# phone = input('Enter your phone number')
#
# if ((len(address) > 1) & (len(phone) > 1)):
#     phone = int(phone)
#     obj = Student(name=name, address=address, phone=phone)
#     obj.display_data()
# elif (len(address) > 1 & (len(phone) == 0)):
#     obj = Student(name, address)
#     obj.display_data()
# elif (len(phone) > 1 & (len(address) == 0)):
#     phone = int(phone)
#     obj = Student(name=name, phone=phone)
#     obj.display_data()
# else:
#     obj = Student(name)
#     obj.display_data()


## Dynamic -- Students Class

# class Student:
#     def __init__(self, name, address="Dehradun", phone=0):
#         self.name = name
#         self.address = address
#         self.phone = phone
#         print("Welcome to Brillica Services")
#
#     def display_data(self):
#         print("Printing students details")
#         print(self.name)
#         print(self.address)
#         print(self.phone)
#
#
# students_count = input('Enter the number of records you want')
# students_count = int(students_count)
# students_records = []
# for i in range(students_count):
#     print('Enter the details of student:')
#     name = input('Enter the name of the student')
#     address = input('Enter the address of the student')
#     phone = input('Enter the phone number of the student')
#
#     obj: Student
#     if ((len(address) > 1) & (len(phone) > 1)):
#         phone = int(phone)
#         obj = Student(name=name, address=address, phone=phone)
#     elif (len(address) > 1 & (len(phone) == 0)):
#         obj = Student(name, address)
#     elif (len(phone) > 1 & (len(address) == 0)):
#         phone = int(phone)
#         obj = Student(name=name, phone=phone)
#     else:
#         obj = Student(name)
#
#     students_records.append(obj)
#
# for i in students_records:
#     i.display_data()







#ato add new cell above, b to add cell down dd to delete in selection mode, press escape




