import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if a==[]:
		return []
	elif len(a)*len(a[0])!=new_shape[0]*new_shape[1]:
		return []
	else:
		reshaped_matrix=[]
		vector=[]
		cnt=0
		for i in range(len(a)):
			for j in range(len(a[0])):
				vector.append(a[i][j])
				cnt+=1
				if cnt==new_shape[1]:
					cnt=0
					reshaped_matrix.append(vector)
					vector=[]
	return reshaped_matrix