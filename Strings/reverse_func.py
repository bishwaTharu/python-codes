num = 1023
reverse = 0
while (num!=0):
    digit = num % 10
    # print(digit)
    reverse = reverse * 10 + digit
    # print(reverse)
    num //=10
print(reverse)      
    

