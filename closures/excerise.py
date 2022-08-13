# 5 * 9
# def multiplier_of(n):
#     def multiplier(number):
#         return number*n
#     return multiplier

# multiplywith5 = multiplier_of(5)
# print(multiplywith5(9)) 
# print(multiplywith5.__name__)

# def sum_of(n):
#     def this_sum(number):
#         return n+number
#     return this_sum
# sum_with5 = sum_of(5)
# print(sum_with5(5))

def addOne(one):
    def addTwo(two):
        def addThree(three):
            return one + two + three
        return addThree
    return addTwo

one = addOne(1)
two = one(2)
three = two(3)
print(three)