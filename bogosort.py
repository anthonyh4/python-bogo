import random

def bogosort(elements):
""" This function will take a list of elements, entitled elements, it will then perform bogosort on them"""
	random.seed()

	def inorder(x):
	"""This function will go through each element in the list and check if the preceding are in order"""
    	i = 0
    	j = len(x)
    	while i + 1 < j:
        	if x[i] > x[i + 1]:
            	return False
        	i += 1
    	return True

	def bogo(x):
	"""This performs the primary function of bogosort, resulting in the returned list being presented"""
    	while not inorder(x):
        	random.shuffle(x)
    	return x
	return bogo(elements)
