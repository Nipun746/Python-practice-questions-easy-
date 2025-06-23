# Write a program which finds out whether a given name is present in a list or not. 

a = ["a","b","c","d"]
x = input("Enter the name to be checked")
for name in a :
    if name in x :
        print("The name is present")
        exit()
print("Name not found")
