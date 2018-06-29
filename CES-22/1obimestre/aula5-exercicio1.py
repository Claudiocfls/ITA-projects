# Crie um exemplo usando métodos abstratos, métodos
# estáticos e métodos de classe. O exemplo deve ilustrar
# as vantagens de cada tipo de método.
# [TODO]
import abc

class RegularPolygon():
	__metaclass__ = abc.ABCMeta
	quantity = 0

	def __init__(self, sides, size):
		self.number_of_sides = sides
		self.size = size
		type(self).quantity += 1

	@classmethod
	def existing_regular_polygons(cls):
		print('there is ',cls.quantity,' polygons created')
		return cls.quantity

	@abc.abstractclassmethod
	def area(self):
		pass

class Square(RegularPolygon):
	def __init__(self, size):
		super().__init__(4, size)

	def area(self):
		area = self.size * self.size
		print(area)
		return area

RegularPolygon.existing_regular_polygons()
quadrado = Square(10)
quadrado.area()
RegularPolygon.existing_regular_polygons()