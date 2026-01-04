#Write a python program to read a text file “Poem.txt” and display the number of vowels / consonants/ lower case / upper case characters.
def letter():
    u=l=c=v=0
    f = open("Poem.txt", "r")
    r = f.read()
    for i in r:
        if i.isupper():
            u +=1
        if i.islower():
            l +=1
        if i in 'aeiouAEIOU':
            v +=1
        if i.isalpha() and i not in 'aeiouAEIOU':
            c += 1
    print("Upper case letters:", u)
    print("Lower case letters:", l)
    print("Vowels:", v)
    print("Consonants:", c)
letter()
