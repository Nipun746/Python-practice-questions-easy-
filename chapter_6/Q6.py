# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50 => F 

marks = int(input())
if 90<=marks :
    print("Ex grade")
    exit()
elif 80<=marks :
    print("A grade")
    exit()
elif 70<=marks:
    print("B grade")
    exit() 
elif 60<=marks:
    print("C grade")
    exit() 
elif 50<=marks:
    print("D grade")
    exit() 
elif marks<50:
    print("Fail")
    exit() 