# define function 
def recursive_sum(num):
    if num<= 1:
        return num
    else:
        return num + recursive_sum(num-1)
# print(recursive_sum(3)) 
num = int(input('sum upto: '))
# if num<0:
#     print('Please input a valid number')
# else:
#     print(f'sum is {recursive_sum(num)}') 

    
    
