import itertools

election = {1: 'Berb', 2: 'Karen', 3: 'Erin'}
for p in itertools.permutations(election):
    print(p)

for p1 in itertools.permutations(election.values()):
    print(p1)

colorsForPainting = ['Red', 'Blue', 'Purple', 'Orange', 'Yellow', 'Pink']
for c in itertools.permutations(colorsForPainting, 3):
    print(c)
