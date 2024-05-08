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
obj = Problem3()
# obj.factorial_of_number()
# obj.eb_calculator()
# obj.average_n_number()
# obj.discount_of_product()
# obj.distance_bt_two_point()