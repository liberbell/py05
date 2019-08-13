import itertools

election = {1: 'Berb', 2: 'Karen', 3: 'Erin'}
for p in itertools.permutations(election, 2):
    print(p)
