 word = input("Enter the word: ")
rev_word = [None] * len(word)
ind = 0
ind1 = len(word) - 1
while ind1 >= 0:
    rev_word[ind] = word[ind1]
    ind +=1
    ind1 -=1
num2 =''
for num in rev_word:
    num2 = num2 + num
print(f'Reversed string is: {num2}')
