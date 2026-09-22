def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	row_sum=[]
	col_sum=[]
	a=matrix
	for i in range(len(a)):
		tmp=0
		for j in range(len(a[0])):
			tmp+=a[i][j]
		row_sum.append(tmp)
	for i in range(len(a[0])):
		tmp=0
		for j in range(len(a)):
			tmp+=a[j][i]
		col_sum.append(tmp)
	means=[]
	width=len(row_sum)
	height=len(col_sum)
	if mode=='row':
		for i in range(len(row_sum)):
			means.append(row_sum[i]/len(col_sum))
	if mode=='column':
		for i in range(len(col_sum)):
			means.append(col_sum[i]/len(row_sum))
	return means