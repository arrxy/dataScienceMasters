l = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

l = sorted(l, key = lambda x: x[1])
print(l)   

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(map(lambda x: x ** 2, l))
print(l)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = tuple(map(lambda x: str(x), l))
print(l)

from functools import reduce 
l = reduce(lambda x, y: x * y ,range(1, 26))
print(l)

l = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
l = list(filter(lambda x: x % 2 == 0 or x % 3 == 0, l))
print(l)

l = ['python', 'php', 'aba', 'radar', 'level']
l = list(filter(lambda x: x[::-1] == x, l))
print(l)