myFile = open('scores.txt', 'r')

print('My one Line: ' + myFile.readline())
myFile.seek(0)

for line in myFile:
    newHighScore = line.replace('BBB', 'PDJ')
    print(newHighScore)

myFile.close()
