# Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# '''

name = input("Enter the name")
Date = input("Enter the Date")
print('''
Dear '''  name 
'''You are selected!''' 
Date 
'''
/'/'/'
''')