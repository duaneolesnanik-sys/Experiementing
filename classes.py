class Point:
    def draw(self):
        print("Point drawn")

point = Point()  # Creates a Point object
point.draw() 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(2, 3)  # Initializes with x=2, y=3