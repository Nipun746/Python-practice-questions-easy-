#  A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

comment = str(input("Enter the comment"))
spams = ["make a lot of money","buy now","subscribe this","click this"]
for phrase in spams :
    if phrase in comment.lower() :
        print("Spam comment")
        exit()
    