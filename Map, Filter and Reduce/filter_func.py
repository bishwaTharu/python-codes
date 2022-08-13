"""
*Unlike map(), only one iterable is required.
*func argument is required to return a boolean type
*filter passes each element in the iterable through func 
and returns only the ones that evaluate to true
"""
# example1
ages = [1,12,15,18,20,2,19,25,24,28,30]
def over_18(age):
    return age>18
over_18_age = list(filter(over_18,ages))
print(over_18_age) 

# example2
dromes = ("demigod", "rewire", "madam", "freer", 
          "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes) 
