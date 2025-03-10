#Inputs - accept data from the user
#User will choose the desired operation
#Operation - perform the operation
#Output - display the result to the user


def calculator():
     print("Welcome to the calculator.")
     print("Select operation: ")

     print("1. Addition (+)")
     print("2. Subtraction (-)")
     print("3. Multiplication (*)")
     print("4. Division (/)")

     choice =  input("Enter choice (1/2/3/4): ") #variable

     if choice in ('1', '2', '3', '4'):
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))

          if choice == '1':
               result = num1 + num2
               operation = 'Addition'
          elif choice == '2':
               result = num1 - num2
               operation = 'Subtraction'
          elif choice == '3':
               result = num1 * num2
               operation = 'Multiplication'
          elif choice == '4':
               if num2 == 0:
                    print("Error: Division by zero")
                    return
               result = num1 / num2
               operation = 'Division'
          print(f"{operation} of {num1} and {num2} is {result}")
     else:
          print("Select a valid operation.")


#Run the calculator function
calculator()

# PS D:\Python-Classes\introduction> python3 calculator.py
# Welcome to the calculator.
# Select operation: 
# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# Enter choice (1/2/3/4): 1
# Enter first number: 30
# Enter second number: 45
# Addition of 30.0 and 45.0 is 75.0
# PS D:\Python-Classes\introduction> 