def ones(size):
	vec = range(size)
	for i in vec:
		vec[i] = 1
	return vec

def dot(scale, your_list):
	your_list[:] = [scale * x for x in your_list]
	return your_list

"""
def extract_min_max(data,criterion="max"):
	if criterion == "min":

	else:

	return
"""