
myFile = open('scores.txt', 'w')

print('Name ' + myFile.name)
print('Mode ' + myFile.mode)

myFile.write('GBJ: 100\nKHD: 90\nBBB: 89')
myFile.close()

myFile = open('scores.txt', 'r')
print('reading...\n' + myFile.read(9))
print('reading again...\n' + myFile.read(9))
