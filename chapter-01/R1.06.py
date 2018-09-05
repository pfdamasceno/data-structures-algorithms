'''
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''
def sum_of_odd_squares(n):
    if not isinstance(n,(int)) or n < 0:
        raise TypeError("n must be a positive integer")
    return(sum([i**2 for i in range(1,n,2)]))
