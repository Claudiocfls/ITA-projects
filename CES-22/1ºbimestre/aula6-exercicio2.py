# desenvolva um decorador exemplo

def include_text(func):
	def func_decorated(quantity):
		return "you have " + str(func(quantity)) + " orange(s)."
	return func_decorated

@include_text
def calculate_oranges(quantity):
	return quantity

print(calculate_oranges(5))
print(calculate_oranges(6))
print(calculate_oranges(7))