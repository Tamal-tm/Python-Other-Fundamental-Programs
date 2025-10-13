print("Mini Calculator.")

num1=float(input("Enter 1st number here: "))
num2=float(input("Enter 2nd number here: \n"))

print("Press 1 for addition\nPress 2 for Subtraction\nPress 3 for for multiplication\nPress 4 for division\n")

choice=int(input("Enter your choice from 1-4: "))

if choice ==1:
    print(num1+num2)
elif choice ==2:
    print(num1-num2)
elif choice ==3:
    print(num1*num2)
elif choice ==4:
    print(num1/num2)
else:
    print("Invalid input")



