'''
R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
'''
def sum_of_squares(n): return(sum([i**2 for i in range(n)]))
