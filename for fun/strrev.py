astring = "Hello world!"
# reverse the string
print(astring[::-1]) 
name = 'Bishwa'
print(name[::-1])

# upper case and lowercase in string
print(astring.upper())
print(astring.lower())

# returns boolean 
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

""" This splits the string into a bunch of
 strings grouped together in a list."""
afewwords = astring.split(" ")
print(afewwords)