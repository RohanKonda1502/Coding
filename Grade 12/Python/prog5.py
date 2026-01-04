#Write a python program to create and search a record in a binary file “stu.dat”. Each record contains data in the following format [Rollno, Name]. Search for a Roll no and display the details if the Roll no is present. If not found display appropriate message.

import pickle

def Create():
    f = open("stu.dat", "wb")
    op = "y"
    while op == "y":
        Rollno = int(input("Enter Roll Number: "))
        Name = input("Enter The Name Of The Student: ")
        L = [Rollno, Name]
        pickle.dump(L,f)
        op = input("Enter Y/y If You Want To Add Another Record Or Any Other Letter For Done: ")
    f.close()

Create()

def Search():
    f = open("stu.dat", "rb")
    find = input("Enter The Roll Number You Want To Search: ")
    found = False
    try:
        while True:
            L = pickle.load(f)
            if L[0] == find:
                    print("Details Of The Student You Requested:")
                    print("The", find, "Name Is", L[1])
                    found = True
                    print(found)
    except:
        f.close()
        if found == False:
            print("Details Of The Student You Requested Was Not Found:~_~")

Search()
