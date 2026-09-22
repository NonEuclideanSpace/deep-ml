def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result=[]
	for i in range(len(matrix)):
		vector=[]
		for j in range(len(matrix[0])):
			vector.append(matrix[i][j]*scalar)
		result.append(vector)
	return result