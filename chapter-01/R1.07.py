'''
R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function.
'''
def sum_of_odd_squares(n): return(sum([i**2 for i in range(n)]))
