class Problem2:
    def __init__(self) -> None:
        pass
    def fibonnic_series(self):
        n = int(input("Enter limit to go for Fibonnic Series:"))
        n1 = 0
        n2 = 1
        print(n1)
        print(n2)
        for element in range(n-2):
            n3 = n1+n2
            n1 = n2
            n2 = n3
            print(n3)
    def subtract_prod_sum_int(self):
        data = input("Enter the Value :")
        prod = 1
        sum = 0
        for element in data:
            prod *= int(element)
            sum  += int(element)
        print(f"Result become : {prod - sum}")
    def factors_of_number(self):
        data = int(input("Enter the number you want be Factor:"))
        list = []
        for i in range(1,data):
            if data % i == 0:
                list.append(i)
        print(list)
    def sum_of_numbers_from_all(self):
        print("Please enter the Value:\n")
        sum = 0
        while(True): 
            data = int(input())
            if data == 0:
                break
            else:
                sum = sum + data
        print(f"Sum of value are: {sum}")
    def largest_of_number_from_all(self):
        print("Please enter the Value:\n")
        largest = 0
        while(True): 
            data = int(input())
            if data == 0:
                break
            else:
                if largest<data:
                    largest = data
        print(f"Larest Value is: {largest}")
    def add_two(self):
        num1 = int(input("Enter the Num1"))
        num2 = int(input("Enter the Num2"))
        print(num1+num2)
obj = Problem2()
# obj.fibonnic_series()
# obj.subtract_prod_sum_int()
# obj.factors_of_number()
# obj.sum_of_numbers()
# obj.largest_of_number_from_all()
obj.add_two()
