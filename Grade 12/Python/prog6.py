Stack = []

def Push():
    Doc_ID = int(input("Enter The Doctor's ID: "))
    Doc_Name = input("Enter Doctor's Name: ")
    Spl = input("Enter The Doctor's Specialisation: ")
    
    if Spl.lower() == "ent":
        Stack.append([Doc_ID, Doc_Name])
        print("Record Added Successfully!")  # <-- Confirmation
    else:
        print("Record NOT added. Specialisation must be 'ent'.") # <-- Warning message

def Pop():
    if Stack == []:
        print("The Stack Is Empty")
    else:
        print(Stack.pop())

def Peek():
    if Stack == []:
        print("The Stack Is Empty")
    else:
        print(Stack[-1])

def Display():
    if Stack == []:
        print("The Stack Is Empty")
    else:
        for i in Stack[::-1]:
            print(i)

op = "y"
 
while op == "y":
    print("1. Push Items")
    print("2. Pop Top Most Item")
    print("3. Peek Top Most Element")
    print("4. Display Stack")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        Push()
    elif choice == 2:
        Pop()
    elif choice == 3:
        Peek()
    elif choice == 4:
        Display()
    else:
        print("Invalid Choice")


    op = input("Enter Y/y If You Want To Add Another Record Or Any Other Letter For Done: ")
