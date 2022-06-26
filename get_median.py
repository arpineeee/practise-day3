def get_median(data):
    sum = 0
    count = 0
    for num in data:
        sum += num
        count += 1
    return sum / count
    
data = [22, 45, 6, 87, 1]
print(f'The median of data is: {get_median(data)}')
