# define a fuction
def num_sum(num1,num2):
    return sum([num1,num2])
# getting function in a dictionary
my_dict = {1:num_sum}
func = my_dict.get(1)
print(func(1,2)) 
