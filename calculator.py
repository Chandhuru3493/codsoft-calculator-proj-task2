num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))         #    getting inputs from user

# basic operators
print("\nselect any one of the operator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplitation")
print("4. Divition")

user = input("\nEnter your choice (1/2/3/4): ")            # user's choice for the operation

if user == '1':
    print("\nThe result of add is:",num1+num2)

elif user == '2':
    print("\nThe result of subtract is:",num1-num2)

elif user == '3':
    print("\nThe result of multiply is:",num1*num2)

elif user == '4':

    if num1 == 0 or num2 == 0:
        print("\nOops sorry! zero can't be divisible. Use any other numbers")

    else:
        print("\nThe result of divide is:",num1/num2)

else:
    print("\nInvalid inputs")