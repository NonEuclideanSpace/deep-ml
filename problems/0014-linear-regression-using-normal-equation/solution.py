import numpy as np

def transpose(X):
	X_transpose=[]
	if X==[]:
		return []
	for j in range(len(X[0])):
		vector=[]
		for i in range(len(X)):
			vector.append(X[i][j])
		X_transpose.append(vector)
	return X_transpose

def dot_product(v1,v2):
	res=0
	for i in range(len(v1)):
		res+=(v1[i]*v2[i])
	return res

def matrix_mult(A,B):
	B_transpose=transpose(B)
	res=[]
	for i in range(len(A)):
		row=[]
		for j in range(len(B_transpose)):
			row.append(dot_product(A[i],B_transpose[j]))
		res.append(row)
	return res

def matrix_vector_product(A,v):
	res=[]
	for i in range(len(A)):
		res.append(dot_product(A[i],v))
	return res


def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:

	theta=np.linalg.solve(matrix_mult(transpose(X),X),matrix_vector_product(transpose(X),y))

	theta=np.round(theta,4).tolist()
	return theta