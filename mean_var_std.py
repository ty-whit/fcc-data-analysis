import numpy as np

def calculate(listNums):
    # First, check to see if we have the right number of elements. 
    if len(listNums) != 9:
        # if not, return an error.
        raise ValueError("List must contain nine numbers.")

    # Turn the list of 9 numbers into a 3x3 matrix
    matrix = np.reshape(listNums, (3, 3))

    # Start an empty dictionary to hold all the information. 
    calculations = {}
    # Using a defined function below, we calculate each of the items required 
    # for the dictionary. These are also saved into the dictionary at the same time. 
    calculations['mean'] = compute_function(matrix, np.mean)
    calculations['variance'] = compute_function(matrix, np.var)
    calculations['standard deviation'] = compute_function(matrix, np.std)
    calculations['max'] = compute_function(matrix, np.max)
    calculations['min'] = compute_function(matrix, np.min)
    calculations['sum'] = compute_function(matrix, np.sum)

    # Return the dictionary to the calling function.
    return calculations

def compute_function(matrix,function):
    # calculates the value passed in by the function 
                                     # by the first axis,
    calculations = [function(matrix, axis=0).tolist(), 
                                     # and the second axis,
                    function(matrix, axis=1).tolist(), 
                    # Then for the matrix as a whole.
                    function(matrix)]
    # Return a list of the calculations to the calling function. 
    return calculations