'''
P-1.29
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
'''
import copy
def print_strings(pre_0, my_list):
    for i in my_list:
        pre = pre_0 + i
        print(pre)
        new_list = copy.deepcopy(my_list)
        new_list.remove(i)
        print_strings(pre, new_list)

print_strings("",['c','a','t','d','o','g'])
