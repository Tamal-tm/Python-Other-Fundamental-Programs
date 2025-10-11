'''
string=input("Enter something here: ")

num=int(input("Enter a number here: "))

print(string+num) # Will give errors. Sometime type error and sometimes, Value error
'''


string=input("Enter something here: ")
try:
    num=int(input("Enter a number here: "))
    print(string+num)

except ( ValueError, ValueError) as a: # Storing the values in a 
    print(a) # Error handled here. Black text. Will continue If in red, error not handled.

print('Thank you.')

