# import tkinter as tk
#
# mainWindow=tk.Tk()
# mainWindow.title("Sample Window")
#
# heading_label=tk.Label(mainWindow, text="Hello World")
# heading_label.pack()
#
# name_feild=tk.Entry(mainWindow)
# name_feild.pack()
#
# def takeValueInput():
#
# button = tk.Button(mainWindow, text="Get Value", command=lambda: takeValueInput())
# button.pack()
#
# mainWindow.mainloop()
#     name=name_feild.get()
#     print(name)

#title-calculator
#label-Firstno, secondno inke dono entry
#four buttons label operations, *,/,-,+

# import tkinter as tk
# window=tk.Tk()
# window.title("Calculator")
#
# label1=tk.Label(window, text="First number")
# label1.pack()
# feild1=tk.Entry(window)
# feild1.pack()
#
# label2=tk.Label(window, text="Second number")
# label2.pack()
# feild2=tk.Entry(window)
# feild2.pack()
#
# def add():
#     v1 = feild1.get()
#     v2 = feild2.get()
#     print(int(v1)+int(v2))
#
# def sub():
#     v1 = feild1.get()
#     v2 = feild2.get()
#     print(int(v1)-int(v2))
#
# def mul():
#     v1 = feild1.get()
#     v2 = feild2.get()
#     print(int(v1)*int(v2))
#
# def div():
#     v1 = feild1.get()
#     v2 = feild2.get()
#     print(int(v1)/int(v2))
#
# button1 = tk.Button(window, text="+", command=lambda: add())
# button1.pack()
# button2 = tk.Button(window, text="-", command=lambda: sub())
# button2.pack()
# button3 = tk.Button(window, text="*", command=lambda: mul())
# button3.pack()
# button4 = tk.Button(window, text="/", command=lambda: div())
# button4.pack()
#
# window.mainloop()

# import sqlite3
# connection=sqlite3.connect('student.db')
# print("Database opened successfully")
#
# TABLE_NAME = "student_table"
# STUDENT_ID = "student_id"
# STUDENT_NAME = "student_name"
# STUDENT_COLLEGE = "student_college"
# STUDENT_ADDRESS = "student_address"
# STUDENT_PHONE = "student_phone"
#
# connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME +
#                     "( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + STUDENT_NAME + " TEXT, " +
#                    " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
#                    STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE +
#                    " INTEGER);")
#
# print("table created successfully!")
# connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", "+
#                    STUDENT_COLLEGE + ", " +
#                    STUDENT_ADDRESS + ", " +
#                    STUDENT_PHONE + ") VALUES ( 'Ishita', 'UPES', " + " 'Dehradun, Uttarakhand', 7060030972 ); ")
#
# connection.commit()

# name = input("Enter your name")
# college = input("Enter your college")
# address = input("Enter your address")
# phone = input("Enter your phone number")
#
# connection.execute("INSERT INTO " + TABLE_NAME + " ( " +
#                    STUDENT_NAME + ", " +
#                    STUDENT_COLLEGE + ", " + STUDENT_ADDRESS +
#                    ", " + STUDENT_PHONE + ") VALUES ( '"+name+"', '"+college+"', '"+address+"', "+phone+"); ")
# connection.commit()


# num = int(input("Enter number of times u wanna input"))
# for i in range(num):
#     name = input("Enter your name")
#     college = input("Enter your college")
#     address = input("Enter your address")
#     phone = input("Enter your phone number")
#
#     connection.execute("INSERT INTO " + TABLE_NAME + " ( " +
#                        STUDENT_NAME + ", " +
#                        STUDENT_COLLEGE + ", " + STUDENT_ADDRESS +
#                        ", " + STUDENT_PHONE + ") VALUES ( '"+name+"', '"+college+"', '"+address+"', "+phone+"); ")
#     connection.commit()

# cursor = connection.execute("SELECT * FROM " + TABLE_
# NAME + " ;")
# for row in cursor:
#     print("Student id is: ", row[0])
#     print("Student name is:  ", row[1])
#     print("Student college is: ", row[2])
#
# connection.close()

# import tkinter as tk
# hwin=tk.title("Welcome to TIC TAC TOE")
# 
# click=True
#
# def ttt(buttons):
#     global click





























