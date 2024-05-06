import inquirer

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
                r = int(input("Please enter circle radius"))
                area = 0
            case "Triangle":
                area = 0
            case "Square":
                area = 0
            case "Rectangle":
                area = 0
            case "Isosceles Triangle":
                 area = 0
            case "Parallelogram":
                area = 0
            case "Rhombus":
                area = 0
            case "Equilateral Triangle":
                area = 0
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