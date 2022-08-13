number = []
for i in range(1,11):
    number.append(2*i)
print(number)
# list comprehension
new_num = [2*n for n in range(1,11)]
print(new_num)
if (number==new_num):
    print('yes')
else:
    pass