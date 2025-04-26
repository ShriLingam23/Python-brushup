class Line:
    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return (y2 - y1) / (x2 - x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

line = Line(coordinate1, coordinate2)
print("Distance between points:", line.distance())
print("Slope of line:", line.slope())


###

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * (self.radius ** 2) * self.height

    def surface_area(self):
        return (2 * 3.14 * self.radius ** 2) + (2 * 3.14 * self.radius * self.height)

cylinder = Cylinder(2,3)
print("Volume of Cylinder : {}".format(cylinder.volume()))
print(f"Surface Area of Cylinder {cylinder.surface_area()}")


# Reference : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp
