firstName = 'Taylor'
lastName = 'Swift'
print(len(firstName))
print(len(lastName))

firstName.__len__()

ages = [1, 12, 25, 41, 38, 19]
print(len(ages))

i = 0
for i in range(0, len(ages)):
    print(ages[i])

print(len(['bob', 'mary', 'sam']))
