import itertools

for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break;

for c in itertools.cycle('RACECAR'):
    print(c)
