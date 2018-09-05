'''
R-1.02 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''
def is_even(k):
    subtracted = k
    is_odd     = True
    if k == 0:
        return(True)
    for i in range(k):
        subtracted -= 1
        is_odd      = not(is_odd)
        if subtracted == 0:
            return(is_odd)
