import numpy as np

def calculate(listNums):
    if len(listNums) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.reshape(listNums, (3, 3))

    calculations = {}
    calculations['mean'] = compute_function(matrix, np.mean)
    calculations['variance'] = compute_function(matrix, np.var)
    calculations['standard deviation'] = compute_function(matrix, np.std)
    calculations['max'] = compute_function(matrix, np.max)
    calculations['min'] = compute_function(matrix, np.min)
    calculations['sum'] = compute_function(matrix, np.sum)

    return calculations

def compute_function(matrix,function):
    calculations = [function(matrix, axis=0).tolist(), 
                    function(matrix, axis=1).tolist(), 
                    function(matrix)]
    return calculations