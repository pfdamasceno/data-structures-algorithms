'''
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''
def sum_of_squares(n):
    if not isinstance(n,(int)) or n < 0:
        raise TypeError("n must be a positive integer")
    my_sum = 0
    for i in range(n):
        my_sum += i*i
    return(my_sum)
