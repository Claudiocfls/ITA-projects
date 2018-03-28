class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def slope_from_origin(self):
    	return self.y/self.x

    def get_line_to(self, point):
        m = (self.y - point.y)/(self.x - point.x)
        b = self.y - m*self.x
        return (m,b)

print(Point(4, 11).get_line_to(Point(6, 15)))