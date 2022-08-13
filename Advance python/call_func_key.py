def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
# code here 
def multipy(first,second,third,**options):
    if options.get('action')=='multiply':
        print('The multiply is %d'%(first*second*third))
    if options.get('number')=='second':
        return second
# function call 
multipy(1,2,3,action='multiply', number='second')
print('Result:%d'%(result))