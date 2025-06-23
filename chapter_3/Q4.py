# Replace the double space from problem 3 with single spaces. 


a = input("Enter a string")

if "  " in a :
    a.replace("  "," ")
    print(a)
else:
    print(False)
