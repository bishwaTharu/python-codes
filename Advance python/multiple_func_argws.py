def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    # gives list of numbers
    print("And all the rest... %s" %(list(therest)))
# function call 
foo(1, 2, 3, 4, 5)
# define multiple awrgs
def mul_awrgs(a,b,c,d,*r):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')
    print(f'd={d}')
    print(f'r={r}')
# fuction call 
mul_awrgs(1,2,3,4,5,6,7,8)
