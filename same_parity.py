def same_parity(n:int, *args:int):
        lst = []
        for num in args:
             if num % n == 0:
                 lst.append(num)
        return lst 

print(same_parity(5, 21, 70, 6))
