# # Question 1
# grade = input()
# grade = int(grade)
# if grade > 90:
#     print('A')
# elif grade > 80:
#     print('B')
# elif grade >= 60:
#     print('C')
# else:
#     print('D')

# #Question 2
# price = int(input())
# tax = 0
# if price > 100000:
#     tax = 0.15 * price
# elif price > 50000:
#     tax = 0.1 * price
# else:
#     tax = 0.05 * price
# print(tax)

# # question 3
# cityMap = {
#     "Delhi":"Red Fort",
#     "Agra" : "Taj Mahal",
#     "Jaipur": "Taj Mahal"
# }
# city = input()
# print(cityMap.get(city, "Not Found"))

#question 4

number = int(input())
count = 0
while (number > 10):
    count+=1
    number /= 3
print(count)

#question 5
'''
while loop can be used when a specific terminating condition is known
eg. above code
'''

#question 6

#question 7 & 8
cnt = 10
while (cnt > 0):
    print(cnt, end = ' ')
    cnt-=1
print()