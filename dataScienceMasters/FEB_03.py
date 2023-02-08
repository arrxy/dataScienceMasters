def odd_number_generator(lo = 1, hi = 25):
    return [i for i in range(lo, hi + 1, 1) if i % 2 == 1]

# print(odd_number_generator())

def func1(*args):
    return sum(i for i in args)

def func2(**kwargs):
    for [_,v] in kwargs.items():
        return sum(v)

# print(func2(arr = [1,2,3,4]))

# list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# iterator = iter(list1)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

import math
def generate_primes(limit = 1000):
    def is_prime(no):
        if no <= 1:
            return False
        cnt = 0
        for i in range(2, int(math.sqrt(no)) + 1, 1):
            if no % i == 0:
                cnt += 1
                if (no/i != i):
                    cnt += 1
        if cnt > 0:
            return False
        return True 
    for i in range(2, limit + 1):
        # print(":::",i)
        if is_prime(i):
            yield i

pri = generate_primes()
for i in range(20):
    print(next(pri))

def fibo(n):
    fibo = [0, 1, 1]
    for i in range(3, n + 1):
        fib_no = fibo[i - 2] + fibo[i - 1]
        fibo.append(fib_no)
    return fibo[n]

# print(fibo(89))

var = [i for i in "pwskills"]
# print(var)

number = input()
lo, hi = 0, len(number) - 1
flag = True
while (lo <= hi):
    if number[lo] != number[hi]:
        flag = False
        break
    lo += 1
    hi -= 1
if flag == True:
    print("pallindrome")
else:
    print("not pallindrome")

var1 = sum([i for i in range(1, 101) if i % 2 == 1])
print(var1)

