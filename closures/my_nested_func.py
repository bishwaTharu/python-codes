# a = 2
# b = 3
# print(sum([2,3]))
def num(a,b,c):
    # this is enclosing function
    a,b,c = a,b,c
    # this is a nested function
    def this_sum():
        print(sum([a,b,c]))
    return this_sum 
my_sum = num(1,2,3)
your_sum = num(3,4,5)
# check function name
print(my_sum.__name__)
my_sum() 

