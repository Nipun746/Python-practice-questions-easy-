# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 
marks = []
for i in range(1,4):
    marks.append(int(input(f'Enter marks of subject {i}')))
sum = 0
flag = True
for i in range(3):
    if marks[i]<33:
        flag = False
        print("The student failed")
        exit()
for i in range(3):
    sum+= marks[i]
if sum/3 < 44 :
    print("The student failed")
    exit()

print(f'The student passes the grade with {sum//3}% marks')