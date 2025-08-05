myfunc = lambda x: x * 2
print(myfunc(12))

a = [(29, 5), (5, 9), (20, 67), (12, 76)]

a.sort(key=lambda x: x[1])
print(a)

mylist = [4, 6, 8, 3, 598.559, 4]
print(list(map(lambda x: x * 2, mylist)))

numbers = [10, 8, 19, 49, 15, 25, 9, 65, 87]
print(list(map(lambda x: 'big' if x > 10 else 'smale', numbers)))

mylist = [23, 4, 7, 1, 44, 89, 8]
print(list(filter(lambda x: x % 2 != 0, mylist)))
