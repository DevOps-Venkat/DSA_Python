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
                #Formula : 2PiR
                r = int(input("Radius of Circle:"))
                area = 2 * math.pi * r
                print(f"Perimeter of Circle: {round(area,2)}")
            case "Triangle":
                #Formula : a + b + c
                a = int(input("Enter the A Side:"))
                b = int(input("Enter the B Side:"))
                c = int(input("Enter the C Side:"))
                area = a + b + c
                print(f"Perimeter of Triangle: {round(area,2)}")
            case "Square":
                #Formula : 4a
                a = int(input("Enter the A Side:"))
                area = 4*a
                print(f"Perimeter of Square: {round(area,2)}")
            case "Rectangle":
                #Formula : 2(a+b)
                a = int(input("Enter the A Side:"))
                b = int(input("Enter the B Side:"))
                area = 2*(a+b)
                print(f"Perimeter of Rectangle: {round(area,2)}")
            case "Parallelogram":
                #Formula : 2(a+b)
                a = int(input("Enter the A Side:"))
                b = int(input("Enter the B Side:"))
                area = 2*(a+b)
                print(f"Perimeter of Parallelogram: {round(area,2)}")
            case "Rhombus":
                #Formula : 4a
                a = int(input("Enter the A Side:"))
                area = 4*a
                print(f"Perimeter of Rhombus: {round(area,2)}")
    def findVolumeOfShape(self,shape):
        match shape:
            case "Cone":
                #Formula : 	V=1/3hπr²
                r = int(input("Radius:"))
                h = int(input("Height:"))
                area = (1/3)*h*math.pi*(math.pow(r,2))
                print(f"Volume of Cone: {round(area,2)}")
            case "Prism":
                #Formula : (V) = B × h
                b = int(input("Base:"))
                h = int(input("Height:"))
                area = b * h
                print(f"Volume of Prism: {round(area,2)}")
            case "Cylinder":
                #Formula : V=πr2h
                r = int(input("Radius:"))
                h = int(input("Height:"))
                area = math.pi * r * 2 * h
                print(f"Volume of Cylinder: {round(area,2)}")
            case "Sphere":
                #Formula : V = 4/3 π r³
                r = int(input("Radius:"))
                area = (4/3) * math.pi * math.pow(r,3)
                print(f"Volume of Sphere: {round(area,2)}")
            case "Pyramid":
                #Formula : V=lwh/3
                l = int(input("Base length:"))
                w = int(input("Base width:"))
                h = int(input("Pyramid height:"))
                area = (l * w * h)/3
                print(f"Volume of Pyramid: {round(area,2)}")
    def findSurfaceOfShape(self,shape):
        match shape:
            case "Cylinder":
                # Formula : A=2πrh+2πr2
                r = int(input("Radius:"))
                h = int(input("Height:"))
                area = 2 * math.pi * r * h + (2 * math.pi * math.pow(r,2))
                print(f"Surface of Cylinder: {round(area,2)}")
            case "Cube":
                #Formula: A=6a2
                a = int(input("Edge:"))
                area = 6 * math.pow(a,2)
                print(f"Surface of Cube: {round(area,2)}")
        
        
obj = Problem()
obj.findPropertyAndShapes()