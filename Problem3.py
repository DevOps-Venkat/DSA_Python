import math
import datetime
import calendar
class Problem3:
    def __init__(self) -> None:
        pass
    def factorial_of_number(self,fact):
        # fact = int(input("Enter the Factorial number:"))
        sum = 1
        for i in range(1,fact+1):
            sum = sum * i
        return sum
    def eb_calculator(self):
        units = int(input("Enter your EB Unit:"))
        cost = 0
        if units <= 100:
            cost = 0.0
        elif units <= 200:
            cost = (units - 100) * 2.50
        elif units <= 300:
            cost = 100 * 2.50 + (units - 200) * 3.00
        elif units <= 400:
            cost = 100 * 2.50 + 100 * 3.00 + (units - 300) * 5.00
        else:
            cost = 100 * 2.50 + 100 * 3.00 + 100 * 5.00 + (units - 400) * 6.00
        print(cost)
    def average_n_number(self):
        n = input("Enter value:").split()
        sum = 0
        for element in n:
            sum = sum + int(element)
        print(f"Average of N number is: {sum/(len(n))}")
    def discount_of_product(self):
        price = float(input("Enter the price of product:"))
        discount = float(input("Enter the discount of product:"))
        print(f"Final Product Price is: {price - price * (discount/100)}, Your Discount Amount: {price * (discount/100)}")
    def distance_bt_two_point(self):
        # Formula: d=√((x2 – x1)² + (y2 – y1)²)
        points = input("Enter the four points [x1,x2,y1,y2]:").split()
        x1 = float(points[0])
        x2 = float(points[1])
        y1 = float(points[2])
        y2 = float(points[3])
        d = 0
        d = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
        print(f"Distance between two points: {d}")
    def calculate_commission_percentage(self):
        # Formula: commission amount = sale price × commission percentage / 100
        buy_price = float(input("Enter the Buy Price:"))
        sale_price = float(input("Enter the Sale Price:"))
        comm_percent = ((sale_price - buy_price ) / buy_price) * 100
        print(f"Commission Percentage: {round(comm_percent,2)}%, Commission Amount: { (sale_price - buy_price )}")
    def power(self):
        data = int(input("Enter the value:"))
        power = int(input("Enter the power:"))
        print(math.pow(data,power))
    def depreciation_value(self):
        asset = float(input("Enter the Asset Value:"))
        salvage  = float(input("Enter the Salvage Value:"))
        year = float(input("Enter year of Assets:"))
        print(f"Straight Line Balance : Depreciation Value: { (asset - salvage)/year}")
    def batting_avg(self):
        data = input("Enter the All score by space:").split(" ")
        sum = 0 
        for score in data:
            sum =sum + float(score)
        print(f"Average Batting is : {sum/(len(data))}")
    def average_mark(self):
        data = input("Enter the All marks by space:").split(" ")
        sum = 0 
        for score in data:
            sum =sum + float(score)
        print(f"Average Mark is : {round(sum/(len(data)),2)}")
    def sum_of_number(self):
        sum =0
        value = input("Enter the all value with space:").split(" ")
        for element in value:
            sum = sum + int(element)
        print(f"Sum of Number: {sum}")
    def armstrong_number(self):
        sum = 0
        data = input("Enter the value:")
        for element in data:
            sum = sum + math.pow(int(element), 3)
        if(sum == float(data)):
            print("Armstrong Number")
        else:
            print("Not Armstrong Number")
    def reverse_string(self):
        my_str = input("Enter the String:")
        print(my_str[::-1])
    def palindrome_number(self):
        data = input("Enter the value:")
        if data == data[::-1]:
            print("Palindrome Number")
        else :
            print("Not Palindrome Number")
    def futureInvestementValue(self):  
        # FV=I×(1+(R×T))
        # where:
        # I=Investment amount
        # R=Interest rate
        # T=Number of years
        I = float(input("Enter the Present Value:"))
        R  = float(input("Interest Rate:"))
        T  = float(input("Year of Inverstment:"))
        FV = I * (1 + (R+T))
        print(f"Future Investement Value: {FV}")
    def hcf_lcm(self):
        num1 = int(input("Enter the Number One:"))
        num2 = int(input("Enter the Number Two:"))
        if num1> num2:
            x = num1
        else:
            x = num2
        hcf =0
        lcm =0
        for i in range(1,x):
         if num1%i==0 and num2%i==0:
          hcf = i
        while(True):
            if((x % num1 == 0) and (x % num2 == 0)):
                lcm = x
                break
            x += 1
        print(f"HCF {hcf}, LCM {lcm}")
    def vowel_consonant(self):
        data = input("Enter the value:")
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for element in data:
            if element in vowels:
                print(f"{element} is Vowel")
            else :
                print(f"{element} is Consonant")
    def perfect_number(self):
        num = int(input("Enter the number:"))
        sum = 0
        for i in range(1,num):
            if num % i == 0:
                sum = sum + i
        if sum == num :
            print("Perfect Number")
        else :
            print("Not Perfect Number")
    def sum_of_digit(self):
        data = input("Enter the value:")
        sum =0
        for element in data:
            sum = sum + int(element)
        print(f"Sum of Digit: {sum}")
    def leapyear(self):
        year = int(input("Enter the year:"))
        if year % 400 == 0 and year % 100 == 0 :
            print("Leap year")
        elif year % 4 == 0  and year % 100 != 0:
            print("Leap year")
        else :
            print("Not a Leap year")
    def sum_of_even_neg_odd_from_all(self):
        print("Please enter the Value:\n")
        neg_sum = 0
        pos_sum_odd = 0
        pos_sum_even = 0
        while(True): 
            data = int(input())
            if data == 0:
                break
            else:
                if data < 0: 
                 neg_sum += data
                elif data%2 == 0:
                 pos_sum_even +=data
                else:
                 pos_sum_odd+=data
        print(f"Sum of Negative Number: {neg_sum}")
        print(f"Sum of Even  Number: {pos_sum_even}")
        print(f"Sum of Odd Number: {pos_sum_odd}")
    def findEvenDaysCount(self):
        y = 2024
        m = 8
        print(calendar.month(y, m))
        for day in range(1,32):
            if day%2 ==0:
                print(day)
    def find_ncr_npr(self):
        n = 0
        r = 0
        n = int(input("Enter the Total number of books: "))
        r = int(input("Enter the No.of books is selected:"))
        fact_n = self.factorial_of_number(n)
        fact_r = self.factorial_of_number(r)
        fact_n_r = self.factorial_of_number(n-r)
        result = fact_n/(fact_n_r * fact_r)
        p_result = fact_n/fact_n_r
        print(f"NCR : {result} , NPR : {p_result}")
    def componend_interest(self):
        p = float(input("Enter the Principal Value:"))
        r = float(input("Enter the Interest Rate:"))
        n = float(input("No of times interest is compounded per year:"))
        t = float(input("Enter the year:"))
        A = p * math.pow(1+(r/100),t)
        print(f"Componend Interest: {A}")
    def cgpa_calculator(self):
        English = 9.1  
        Hindi = 8.5  
        Maths = 9.5  
        Science =9.6;  
        SocialStudy = 8.6  
        CGPA = (9.1+8.5+9.5+9.6+8.6)/(5.0)  
        CGPAper = 9.5 * (CGPA)  
        print(f"CGPA : {CGPA}")
        print(f"CGPA percentage is: {CGPAper}");  
        
obj = Problem3()
# obj.factorial_of_number()
# obj.eb_calculator()
# obj.average_n_number()
# obj.discount_of_product()
# obj.distance_bt_two_point()
# obj.calculate_commission_percentage()
# obj.power()
# obj.depreciation_value()
# obj.batting_avg()
# obj.average_mark()
# obj.sum_of_number()
# obj.armstrong_number()
# obj.reverse_string()
# obj.palindrome_number()
# obj.futureInvestementValue()
# obj.hcf_lcm()
# obj.vowel_consonant()
# obj.perfect_number()
# obj.sum_of_digit()
# obj.leapyear()
# obj.sum_of_even_neg_odd_from_all()
# obj.findEvenDaysCount()
# obj.find_ncr_npr()
# obj.componend_interest()
# obj.cgpa_calculator()