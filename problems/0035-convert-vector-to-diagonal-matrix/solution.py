import numpy as np

def make_diagonal(x):
	n=len(x)
	result=[]
	for i in range(n):
		vector=[]
		for j in range(n):
			if(j==i):
				vector.append(x[j])
			else:
				vector.append(0)
		result.append(vector)
	return result