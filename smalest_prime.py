def is_simple(n):
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1    
    return True    
    
num = int(input("Enter number: "))
num1 = num + 1
while not is_simple(num1):
    num1 += 1
    
print(f'The number that is simple and larger than num: {num1}' )
