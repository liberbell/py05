import itertools

for x in itertools.count(50, 5):
    print(x)
    if x == 60:
        break

x = 0
for c in itertools.cycle('RACECAR'):
    print(c)
    x += 1
    if x > 50:
        break
