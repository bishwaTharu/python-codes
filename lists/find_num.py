
"""
Takes input from user and 
display num is present is the list or not 

"""
marks = [1,2,3,4,5]

def find_num(num):
    for i in range(len(marks)):
        if (num==marks[i]):
            return i
    return -1

print(find_num('apple'))
