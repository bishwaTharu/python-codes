"""
zip() function is a function that takes a number of iterables 
and then creates a tuple containing each of the elements in the iterables
"""
my_strings = ['a','b','c','d','e']
my_nums = [1,2,3,4]
# zipped = list(zip(my_strings,my_nums))
# print(zipped)
# custom zip function 
cus_zipped = list(map(lambda x,y:(x,y),my_strings,my_nums))
print(cus_zipped) 