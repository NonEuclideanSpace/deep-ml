def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    if a==[]:
        return []
    a_transposed=[]
    for i in range(len(a[0])):
        vector=[]
        for j in range(len(a)):
            vector.append(a[j][i])
        a_transposed.append(vector)
    return a_transposed