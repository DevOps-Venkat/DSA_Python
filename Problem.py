class Problem:
    @staticmethod
    def oddOrEven():
        num = int(input("Enter your input as Digit:"))
        if num % 2 == 0:
            print(f"{num} is a Even Number")
        else:
            print(f"{num} is a Odd Number")
    @staticmethod
    def printName():
        name = input("Enter your name:")
        print(f"Hi {name}, Welcome to DSA Learning!!!")
    @staticmethod
    def simpleInterest():
        p = int(input("Please enter the Principal Value:"))
        t = int(input("Please enter the Time as Year:"))
        r = int(input("Please enter the Rate (%):"))
        si = p * (1 + ((r/100) * t))
        print(f"Total Amount {si} INR, and Interest {si - p} INR");
    @staticmethod
    def simpleCalculator():
        a,b = input("Enter the two numbers with spaces:").split()
        operator = input("Enter the Operator (+, -, *, /):")
        a = int(a)
        b = int(b)
        result = 0
        if operator == "+":
            result = a+b
        elif operator == "-":
            result = a-b
        elif operator == "*":
            result = a*b
        elif operator == "/":
            result = a/b
        else :
            print("Please enter correct inputs")
        print(f"Result of Value are: {result}")
    @staticmethod
    def largestTwoNumbers():
        a  = int(input("Enter the A Number:"))
        b  = int(input("Enter the B Number:"))
        if a == b:
            print("A and B are equals")
        elif a> b:
            print("A is Largest Number than B")
        else:
            print("B is Largest Number than A")
    @staticmethod
    def INR_To_USD():
        USD = 	0.0119826 
        INR = float(input("Please enter Rupees Currency Amount:"))
        print(f" USD value is : {round(INR * USD,2)}$")
    @staticmethod
    def fibonnicSeries():
        sum = 0
        n1 = 0
        n2 = 1
        n = int(input("Enter the Series Value:"))
        print(n1)
        print(n2)
        for element in range(n-2):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            print(n3)
    @staticmethod
    def palindromeString():
        data = input("Enter the string :")
        if data == data[::-1]:
            print("Palindrome String")
        else :
            print("Not Palindrome String") 
    @staticmethod
    def armstrongNumber():
        data = input("Enter the value:")
        sum = 0
        for element in data:
            sum = sum + pow(int(element),3)
        if(str(sum) == data):
            print("Armstrong Number")
        else :
            print("Not Armstrong Number")

            
        
#OBJECT CREATION FLOW:
obj = Problem()

#1. Write a program to print whether a number is even or odd, also take input from the user.
# obj.oddOrEven()

#2. Take name as input and print a greeting message for that particular name.
# obj.printName()

#3. Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.
# FORMULA: Simple_Interest = Principl_Amount * (1 + ( (Rate/100) * Years))
# obj.simpleInterest()  

#4. Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)
# obj.simpleCalculator()  

#5. Take 2 numbers as input and print the largest number.
# obj.largestTwoNumbers()

# 6. Input currency in rupees and output in USD.
# obj.INR_To_USD()

# 7. To calculate Fibonacci Series up to n numbers.
# obj.fibonnicSeries()

# 8. To find out whether the given String is Palindrome or not.
# obj.palindromeString()

# 9. To find Armstrong Number between two given number.
# obj.armstrongNumber()