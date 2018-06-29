
def update(*args, **kwargs):
	for arg in args:
		print(type(arg), ' = ', arg)

	for key in kwargs.keys():
		print(type(arg), ' = ', key)

update('a','b','palavra qualquer',k1=1,k2=5)