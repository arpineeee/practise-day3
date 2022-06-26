import random
def random_passwd(n):
    passwd = ' '
    i = 0
    while i < n:
        passwd = passwd + chr(random.randint(33, 126))
        i += 1
    return passwd
    
print(random_passwd(9))
