pointsInGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInGame)
print(sortedGame)

children = ['Sue', 'Jerry', 'Linda']
sortedChildren = sorted(children)
print(sortedChildren)
print(sorted(children))
print(sorted(['Sue', 'Jerry', 'Linda']))

print(sorted('My favorite child is Linda'.split(), key=str.upper))
print(sorted(pointsInGame, reverse=True))

leaderBoard = {231: 'CKL', 123: 'ABC', 432: 'JKC'}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))

students = [('alice', 'B', 12), ('eliza', 'a', 16), ('tae', 'c', 15)]
print(sorted(students, key=lambda students:students[0]))
