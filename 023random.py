import random

print(random.random())
decider = random.randrange(2)
if decider == 0:
    print('Heads')
else:
    print('Tails')
