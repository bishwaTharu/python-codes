"""
map(func, *iterables)
returns a map object which is a generator object
The number of arguments 
to func must be the number of iterables listed.
"""
# example one
arr = [1,2,3,4]
arr_multiply2 = list(map(lambda X: X*2,arr))
print(arr_multiply2)
# example two
# chars_ = 'sinu'
# upper_ = chars_.upper()
# print(upper_) 
astring = ['harry','bishwa','chintu','pintu']
# make upper case with map function
astring_upper = list(map(str.upper,astring))
print(astring_upper) 
# example 3
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))
"""
range(1, 7) function acts as the second argument 
to the round function
(the number of required decimal places per iteration).
"""
print(result) 