'''
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''
def minmax(data):
    min = +1e18
    max = -1e18
    for i in data:
        if i <= min:
            min = i
        if i >= max:
            max = i
    return(min,max)
