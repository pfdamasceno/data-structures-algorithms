'''
P-1.30
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
'''
def divide_integer(my_int):
    if my_int <= 2:
        raise ValueError('number has to be larger than 2')
    i = 0
    while my_int > 2:
        my_int /= 2
        i += 1
    return(i)

divide_integer(100)
