class circle:
    def __init__(self,radius):
        self.radius=radius
    def circle_area(self):
        return 3.142 * self.radius**2
    def circle_perimeter(self):
        return 2 * 3.142 * self.radius

radius=float(input("radius of the circle:"))
circle=circle(radius)
area=circle.circle_area()
perimeter=circle.circle_perimeter()

print("area of the circle:",area)
print("perimeter of the circle:",perimeter)