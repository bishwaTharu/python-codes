# to check whether my function is a generator or not
import types
# define a genrator function
import random
def lottary():
    for i in range(6):
        # generates  6 random numbers b/w 1 and 49
        yield random.randint(1,49)
# check whether lottary is a genrator or not
if type(lottary())==types.GeneratorType:
    print("This is a genrator")
    for random_num in lottary():
        print(f'Random numbers is {random_num}')

    