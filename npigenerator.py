import random
from random import randint
storage=[]
def digits_of(n):
        return [int(d) for d in str(n)]
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    num = randint(range_start, range_end)
    while num in storage:
        num=randint(range_start, range_end)
    return num
def highestnumber(n):
    while n % 10 != 0:
        n=n+1
    return n
def generation():
    const=80840
    const=str(const)
    firstdigit=random.randint(1, 2)
    firstdigit=str(firstdigit)
    rndom=random_with_N_digits(8)
    rndom=str(rndom)
    number = const + firstdigit + rndom
    cpy = number
    digits = digits_of(number)
    even_digits = digits[-1::-2]
    odd_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    hnumber=highestnumber(checksum)
    checkdigit=hnumber-checksum
    checkdigit=str(checkdigit)
    npi=cpy+checkdigit
    return npi
def infinity():
    while True:
        yield
    
for _ in infinity():
    print(generation())
    if input()=="q":
        break