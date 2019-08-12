import random

print(random.random())
decider = random.randrange(2)
if decider == 0:
    print('Heads')
else:
    print('Tails')

for i in range(1000):
    decider = random.randrange(2)
    if decider == 0:
        print('Heads')
    else:
        print('Tails')
