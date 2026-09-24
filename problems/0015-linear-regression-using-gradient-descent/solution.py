import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:

    m, n = X.shape
    y = y.reshape(-1, 1) 
    theta = np.zeros((n, 1)) 

    for i in range(iterations):
        r=(X @ theta)-y
        grad=(X.T @ r)/m
        theta=theta-alpha*grad
    return theta.flatten()