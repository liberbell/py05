import random

print(random.random())
# decider = random.randrange(2)
# if decider == 0:
#     print('Heads')
# else:
#     print('Tails')

# Heads = 0
# Tails = 0
# for i in range(1000):
#     decider = random.randrange(2)
#     # Heads = 0
#     # Tails = 0
#     if decider == 0:
#         print('Heads')
#         Heads += 1
#     else:
#         print('Tails')
#         Tails += 1
#
# print('Heads are {0} times, and Tails are {1} times.'.format(Heads, Tails))

print('Your rolled a ' + str(random.randrange(1, 7)))

lotteryWinners = random.sample(range(100), 5)
print(lotteryWinners)

possiblePets = ['cat', 'dog', 'fish']
print(random.choice(possiblePets))

cards = ['Jack', 'Queen', 'King', 'Ace']
random.shuffle(cards)
print(cards)
