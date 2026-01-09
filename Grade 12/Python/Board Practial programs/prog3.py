#Write a python program to read the lines from “poem.txt” and display those words which are less than 4 characters.
def display():
    f = open("Poem.txt", "r")
    r = f.readlines()
    for i in r:
        s = i.split()
        for j in s:
            if len(j)<4:
                print(j)
        print()
display()
