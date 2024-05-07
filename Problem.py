import inquirer
import math
class Problem:
    def __init__(self):
          pass
    def findPropertyAndShapes(self):
        questions = [
            inquirer.List(
                "Property",
                message="Which property you want to find?",
                choices=["Area", "Perimeter","Surface Area", "Volume"],
            ),
        ]
        answers = inquirer.prompt(questions)
        shape = answers['Property']
        area = [
            inquirer.List(
                "Shape",
                message="What area, you want find?",
                choices=["Circle", "Triangle","Square", "Rectangle", "Isosceles Triangle", "Parallelogram", "Rhombus","Equilateral Triangle"],
            ),
        ]
        perimeter = [
            inquirer.List(
                "Shape",
                message="What perimeter, you want find?",
                choices=["Circle", "Triangle","Square", "Parallelogram", "Rectangle", "Rhombus"],
            ),
        ]
        volume = [
            inquirer.List(
                "Shape",
                message="What volume, you want find?",
                choices=["Cone", "Prism","Cylinder", "Sphere", "Pyramid"],
            ),
        ]
        surface = [
            inquirer.List(
                "Shape",
                message="What surface, you want find?",
                choices=["Cylinder", "Cube"],
            ),
        ]
        match shape:
            case "Area":
                area_answers = inquirer.prompt(area)
                self.findAreaOfShape(area_answers['Shape'])
            case "Perimeter":
                perimeter_answers = inquirer.prompt(perimeter)
                self.findPerimeterOfShape(perimeter_answers['Shape'])
            case "Volume":
                volume_answers = inquirer.prompt(volume)
                self.findVolumeOfShape(volume_answers['Shape'])
            case "Surface Area":
                surface_answers = inquirer.prompt(surface)
                self.findSurfaceOfShape(surface_answers['Shape'])
    def findAreaOfShape(self,shape):
        match shape:
            case "Circle":
                r = int(input("Radius of Circle:"))
                area = math.pi * math.pow(r,2)
                print(f"Area of Circle: {round(area,2)}")
            case "Triangle":
                b = int(input("Enter Triangle Base :"))
                h = int(input("Enter Triangle Height :"))
                area = (1/2)*(b*h)
                print(f"Area of Triangle: {round(area,2)}")
            case "Square":
                a = int(input("Enter Square of Area :"))
                area = math.pow(a,2)
                print(f"Area of Square: {round(area,2)}")
            case "Rectangle":
                l = int(input("Enter Rectangle Length :"))
                w = int(input("Enter Rectangle width :"))
                area = l * w
                print(f"Area of Rectangle: {round(area,2)}")
            case "Isosceles Triangle":
                b = int(input("Enter Triangle Base :"))
                h = int(input("Enter Triangle Height :"))
                area = (1/2)*(b*h)
                print(f"Area of Isosceles Triangle: {round(area,2)}")
            case "Parallelogram":
                b = int(input("Enter Parallelogram Base :"))
                h = int(input("Enter Parallelogram Height :"))
                area = (b*h)
                print(f"Area of Parallelogram: {round(area,2)}")
            case "Rhombus":
                d1 = int(input("Enter Rhombus D1 :"))
                d2 = int(input("Enter Rhombus D2 :"))
                area = (d1*d2)/2
                print(f"Area of Rhombus: {round(area,2)}")
            case "Equilateral Triangle":
                a = int(input("Enter Equilateral Triangle of Area :"))
                area =  (math.sqrt(3)/4) * math.pow(a,2)
                print(f"Area of Equilateral Triangle: {round(area,2)}")
    def findPerimeterOfShape(self,shape):
        match shape:
            case "Circle":
                 area = 0
            case "Triangle":
                area = 0
            case "Square":
                area = 0
            case "Rectangle":
                area = 0
            case "Parallelogram":
                area = 0
            case "Rhombus":
                area = 0
    def findVolumeOfShape(self,shape):
        match shape:
            case "Cone":
                 area = 0
            case "Prism":
                area = 0
            case "Cylinder":
                area = 0
            case "Sphere":
                area = 0
            case "Pyramid":
                 area = 0
    def findSurfaceOfShape(self,shape):
        match shape:
            case "Cylinder":
                area = 0
            case "Cube":
                area = 0
        
        
obj = Problem()
obj.findPropertyAndShapes()