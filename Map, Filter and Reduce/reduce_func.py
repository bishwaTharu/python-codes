"""
syntax: reduce(func, iterable[, initial])
* Where func is the function on which each element 
in the iterable gets cumulatively applied to
* Initial is the optional value that gets placed before the elements of the iterable in the calculation,
 and serves as a default when the iterable is empty.
"""
# example1:
from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
# define a custom fuction
def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers,9)
print(result) 
# because reduce, initially ,uses 9 as the first argument to custom_sum.

