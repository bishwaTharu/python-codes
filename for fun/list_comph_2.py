for i in range(2):
    for j in range(5):
        print(i+j)
num = [i+j for i in range(2) for j in range(5)]
print(num) 
# list within a list
new_num = [[i+j for i in range(2)]for j in range(5)]
print(new_num)

# conditional list comprehesion
number = [num**2 for num in range(1,11) if num%2!=0]
print(number)
even_num = [n**2 if n%2 != 0 else 'Even' for n in range(1,11)]
print(even_num) 
