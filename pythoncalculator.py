# how to build a calculator 

# function to add two numbers 
def add (num1, num2):
    num1 + num2

# function to subtract two numbers
def subtract (num1, num2):
    num1 - num2

# function to multiply two numbers
def multiply (num1, num2):
    num1 * num2 

# functionto divide two numbers
def divide (num1, num2):
    num1 / num2 

print ("Please select operation -\n" 
         "1. Add \n" 
         "2. Subtract \n" 
         "3. Multiply \n" 
         "4. Divide \n ")

# Take input from the user 
select = float(input("Select operations from 1, 2, 3, 4 :"))

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

if select == 1:
    result = float(number_1) + float(number_2)
    print(result)

elif select == 2:
    result = float(number_1) - (number_2)
    print(result) 


elif select == 3:
    result = float(number_1) * (number_2)
    print(result)

elif select == 4:
    result = float(number_1) / (number_2)
    print (result)


else:
    print("Invalid input")