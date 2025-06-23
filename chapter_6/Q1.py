# Write a program to find the greatest of four numbers entered by the user. 
a = []
max = 0
for i in range(4):
    a.append(int(input()))        
for i in range(4):
    if a[i] > max:
        max = a[i]

print(f'{max} is the greatest number among the four')