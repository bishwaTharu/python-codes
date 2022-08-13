"""
using default string function to return its corressponding outputs
on string 
some common string function are  demostrated below

"""
str1 = "Hello,Bishwa! Goodmorning"
print(str1.endswith('ing')) # Returns Boolean values i.e True or False

str2 = " Owl, Owl, Nightbird"
print(str2.count('Owl')) # returns number of occurrence of Owl in the str2 variable

str3 = " find my index "
print(str3.find('index')) 

print(str3.replace('index','error'))

# Escape Sequence --> returns newline 

print('This is me.\nI am a data scientist')

print_me = 'I\'m a data scientist'
print(print_me)