# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000




roman_int_map = {'I':1,'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def strToArr(word):
    arr = []
    for letter in word:
        arr.append(letter)
    return arr


def convert_roman_to_int(roman_num):
    ans = 0

    if(len(roman_num) == 1):
        return roman_int_map.get(roman_num)

    roman_num_to_arr = strToArr(roman_num) # ["X", "L"]

    for index,r_num in enumerate(roman_num_to_arr):
        val = roman_int_map.get(r_num)

        if(index < len(roman_num_to_arr) - 1 ):
            next_val =  roman_int_map.get(roman_num_to_arr[index + 1])

            if(val < next_val):
                ans = ans - val
        else:
            ans = ans + val

    return ans

print(convert_roman_to_int('I'))
print(convert_roman_to_int('V'))
print(convert_roman_to_int('III'))
print(convert_roman_to_int('IV'))

print(convert_roman_to_int('VI'))
print(convert_roman_to_int('VIII'))
print(convert_roman_to_int('IX'))
print(convert_roman_to_int('X'))
print('39', convert_roman_to_int('XXXIX'))
print('40', convert_roman_to_int('XL'))

# s = "MCMXCIV"
print('1994', convert_roman_to_int("CCC"))











