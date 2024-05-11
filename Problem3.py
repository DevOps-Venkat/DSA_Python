import math
class Problem3:
    def __init__(self) -> None:
        pass
    def factorial_of_number(self):
        fact = int(input("Enter the Factorial number:"))
        sum = 1
        for i in range(1,fact+1):
            sum = sum * i
        print(f"Factorial: {sum}")
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
obj.futureInvestementValue()