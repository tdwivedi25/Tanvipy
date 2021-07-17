import sys
#Simple Calculator
# Function to add numbers
def add(num1,num2):
       return num1+num2

#Function to subtract numbers
def sub(num1,num2):
        return num1 - num2

#Function to multply numbers
def multiply(num1,num2):
        return num1*num2

#Function to divide numbers
def divide(num1,num2):
        return num1/num2

def power(base,exp):
        return pow(base,exp)

print('Choose the operation choice number you want to perform\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exponent Power')
choice=int(input('Enter the choice number here: '))

if choice>5:
   print('Invalid choice.')
   sys.exit()


n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: '))

if choice==1:
   print(n1,"+",n2,'=',add(n1,n2))

elif choice==2:
    print(n1,"-",n2,'=',sub(n1,n2))

elif choice==3:
    print(n1,"X",n2,'=',multiply(n1,n2))

elif choice==4:
    print(n1,"÷",n2,'=',divide(n1,n2))

elif choice==5:
    print(n1,"^",n2,'=',power(n1,n2))

else:
    print('Invalid input')