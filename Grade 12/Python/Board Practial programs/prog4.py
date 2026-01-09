#Write a python program to create and search Employee record in CSV file “emp.csv”. Each record contains data in the following format. [Emp_No, Emp_Name, Emp_salary]. Search for an Employee No and display the Name and Salary of that Employee. If not found, display appropriate message.

import csv

def Create():

    f = open("emp.csv", "a", newline = "")
    wr = csv.writer(f)
    op = "y"
    while op == "y":
        print("Enter Employee Details To Add Records:")
        Emp_No = int(input("Enter Employee Number: "))
        Emp_Name = input("Enter Employee Name: ")
        Emp_Salary = float(input("Enter Employee's Salary: "))
        l=[Emp_No,Emp_Name,Emp_Salary]
        wr.writerow(l)
        op = input("Enter Y/y If You Want To Add Another Record Or Any Other Letter For Done: ").lower()
    f.close()
Create()

def Search():
    f = open("emp.csv", "r", newline = "\n")
    r = csv.reader(f)
    Number = int(input("Enter The Employee's Number To Display Their Records: "))
    for i in r:
        if int(i[0]) == Number:
            print("Details Of The Employee You Requested:")
            print("Employee Name:", i[1])
            print("Employee Salary:", i[2])
            break
    else:
        print("The Employee Number You Requested Was Not Found:~_~")
    f.close()

Search()

print("Thank You ☺")
