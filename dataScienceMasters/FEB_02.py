#question2
_sum, _product = 0, 1
for i in range(1, 11, 1):
    _sum += i
    _product *= i

print(_sum, _product)
_sum = 0
_product = 1
cnt = 10
while (cnt > 0):
    _sum += cnt
    _product *= cnt
    cnt -= 1
print("Q2 => ",_sum, _product)

#question3

units = int(input())
price = min(units, 100) * 4.5 + max(0, min(units - 100, 100)) * 6 + max(0, min(units - 200, 100)) * 10 + max(0, units - 300) * 20
print("Q3 => ",price) 

#question4
res = []
for i in range(1, 101, 1):
    a = i * i * i
    if a % 4 == 0 or a % 5 == 0:
        res.append(i)
print("Q4 => ",res)

# Q5
str = "I want to become a data scientist"
str = str.lower()
st = {'a','e', 'i','o','u'}

cnt = 0
for i in str:
    if i in st:
        cnt+=1

print("Q5 => ",cnt)

