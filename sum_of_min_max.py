def max_min(lst):
    max = lst[0]
    min = lst[0]
    for num in lst:
        if num > max:
            max = num
        if num < min:
            min = num
    sum = max + min
    return sum
    
lst = [21, 13, 9, 57, 11]
print(f'The sum of maximum and minimum elements: {max_min(lst)}')
