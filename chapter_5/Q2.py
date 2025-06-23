# Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 
a = []
for i in range(8):
    a.append(input())

for i in range(len(a)):
    print(a[i],end=" ")