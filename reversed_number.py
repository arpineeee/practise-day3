number = int(input("Enter a number: "))
reverse_num = 0
while number != 0:
  reverse_num *= 10
  reverse_num += number % 10
  number = number // 10
  
print(f'Your reserved number is: {reverse_num} ' )
