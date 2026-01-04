#Write a python program to read a text file “Poem.txt” line by line and display each word separated by #.
def file():
    f = open("Poem.txt", "r")
    r = f.readlines()
    for i in r:
        s = i.split()
        for k in s:
            print(k, end="#\n")
        print()
    f.close()
file()
