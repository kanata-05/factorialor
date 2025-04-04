import sys 
sys.set_int_max_str_digits(2147483647)

def getPrecedingDigits(num):
    precedingDigits = list()
    for i in range(1, num+1):
        precedingDigits.append(num)
        num-=1
    return precedingDigits

def multiplyListObjects(list):
    factorialValue=1
    for i in range(1, len(list)+1):
        factorialValue *= list[i-1]
        i-=1
    return factorialValue

def factorial(num):
    precedingDigits = getPrecedingDigits(num)
    factorialValue = multiplyListObjects(precedingDigits)
    return factorialValue

print(factorial(int(input()))) 
 
