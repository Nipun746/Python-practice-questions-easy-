# Write a program to find whether a given username contains less than 10 
# characters or not. 

a = input("Enter the username")

if len(a) <= 10 :
    print("Accepted")
else :
    print("The username should be less than 10 characters")