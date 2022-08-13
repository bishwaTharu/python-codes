# create a dictionary 
my_dict = {'age': 24,
            'name':'bishwa',
            'salary':30000}
# Iterating over dictionaries
for features, value in my_dict.items():
   print('features', features)
   print('values',value) 

# Removing a value
del my_dict['name'] # pop deletes the mentioned key 
print(my_dict)