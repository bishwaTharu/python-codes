# # define enclosing function
# from email import message
"""
A Closure is a function object that remembers
values in enclosing scopes even if they are not present in memory
"""
def outerfunc(msg):
    message = msg
    def innerfunc():
        print(message)
    return innerfunc
Hi_func = outerfunc('Hi')
hello_func = outerfunc('hello')
print(Hi_func.__name__)
print(hello_func.__name__)
Hi_func()
hello_func() 
# another example of closures
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter
# function call and function name     
name_func= transmit_to_space("Test message") 
print(name_func.__name__)
name_func() 
my_msg = transmit_to_space('Hello there!')
my_msg()