# ASCII VALUE

char="a"
print("ASCII VALUE of",char, "is", ord(char))

print("******************")

# Octal, Hexadecimal, Binary (8,16,2)

decimal=int(input("Enter a number: "))
print("Conversion of decimal number.", decimal, "is: ")
print(bin(decimal),"in binary")
print(oct(decimal),"in octal")
print(hex(decimal),"in hexadecimal")

# Using recursion

def ConvertBinary(n):
    if n>1:
        ConvertBinary(n//2)
    print(n%2, end= "")

num=int(input('Enter number for conversion:'))
(ConvertBinary(num))



