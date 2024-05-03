class Problem:
    @staticmethod
    def leapYear(years):
        for year in years:
            if (year % 400 ==0) and (year % 100 ==0):
                print(f"{year} its Leap Year")
            elif (year % 4 == 0) and (year % 100 != 0):
                print(f"{year} its Leap Year")
            else : 
                print(f"{year} its Not Leap Year")
    @staticmethod
    def SumOfTwo(num1,num2):
        print(num1+num2)
    @staticmethod
    def multiplicationTable():
        divisible = int(input("Enter the number to Divisible:"))
        for i in range(1,41):
            print(f"{i} x {divisible} = {i*divisible}")
    @staticmethod
    def findLCMHCF():
        a,b = input("Enter the a,b input:").split()
        a = int(a)
        b = int(b)
        if a>b:
            x = int(a)
        else: 
            x = int(b)
        hcf = 0
        lcm = 0
        for i in range(1,x):
            if a%i ==0 & b%i== 0:
                hcf = i
        print("Limit Start and End:",x,(a*b))
        for j in range(x, a*b):
             print(j,a,b)
             if j%a ==0 & j%b== 0:
                lcm = j
                break
        print(f"HCM : {hcf}, LCM : {lcm}")
    @staticmethod
    def sumOfAll():
        sum = 0
        print("Enter the your Value:")
        while True:
            data = input()
            if (data == 'x'):
                print(f"Sum of all value are: {sum}")
                break
            else:
                sum = sum + int(data)
    @staticmethod
    def compute_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    @staticmethod
    def compute_lcm(x, y):
        lcm = (x*y) #compute_gcd(x,y)
        return lcm

obj = Problem()

# 1. Input a year and find whether it is a leap year or not.
# year = [1997,1996,1600,1800]
# obj.leapYear(year)

# 2. Take two numbers and print the sum of both.
# obj.SumOfTwo(1.3233,2.23)

# 3. Take a number as input and print the multiplication table for it.
# obj.multiplicationTable()

# 4. Take 2 numbers as inputs and find their HCF and LCM.
# obj.findLCMHCF()
# print("The L.C.M. is", compute_lcm(num1, num2))

# 5. Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.
# obj.sumOfAll()