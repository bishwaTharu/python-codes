import json
# Python provides built-in JSON libraries to encode and decode JSON.
"""
To encode a data structure to JSON, use the "dumps" method. 
This method takes an object and returns a String:
"""
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
print(type(json_string))

"""
To load JSON back to a data structure, use the "loads" method.
This method takes a string and turns it back into the json object 
datastructure:
"""
print(json.loads(json_string))
print(type(json.loads(json_string))) 

