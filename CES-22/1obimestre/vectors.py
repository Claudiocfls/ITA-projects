# lib for vector operations

# this function dont validate parameters
# always use same length vectors
def add_vectors(u,v):
	size = len(u)
	sum_vector = []
	for i in range(0, size):
		sum_vector.append(u[i] + v[i])

	return sum_vector

def scalar_mult(s,v):
	new_list = []
	for i in v:
		new_list.append(i*s)
	return new_list