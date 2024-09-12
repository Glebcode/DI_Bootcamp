circle_list = []


class Circle:
    def __init__(self, radius, name):
        self.radius = radius
        self.diameter = radius*2
        self.name = name

    @classmethod
    def circleArea(cls, radius):
        circle_area = 3.14159 * pow(radius, 2)
        return circle_area # the idea is coreect but you should return instance of the class
    def comparingCircles(self, other_radius, other_name):
        if self.radius > other_radius:
            print(f"{self.name} bigger then {other_name}")
        elif self.radius == other_radius:
            print(f"{self.name} equal to {other_name}")
        else:
            print(f"{other_name} bigger then {self.name}")
    def listingCircles(self, other_name):
        circle_list.append(self.name)
        circle_list.append(other_name)
        circle_list.sort()
        print(circle_list)
        # Missing alot of implementations


circle1 = Circle.circleArea(10)
circle2 = Circle.circleArea(20)
print(circle1 + circle2)
circle01 = Circle(10, 'circle01')
circle02 = Circle(20, 'circle02')
circle01.comparingCircles(20, 'circle02')
circle01.listingCircles('circle02')
