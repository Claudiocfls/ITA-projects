class RegularPolygon():
	quantity = 0

	def __init__(self, sides, size):
		self.number_of_sides = sides
		self.size = size
		type(self).quantity += 1

	@classmethod
	def existing_regular_polygons(cls):
		print('there is ',cls.quantity,' polygons created')
		return cls.quantity

	def area(self):
		pass

class Square(RegularPolygon):
	def __init__(self, size):
		super().__init__(4, size)

	def area(self):
		area = self.size * self.size
		print(area)
		return area
quadrado = Square(10)
print(quadrado.__class__.mro())