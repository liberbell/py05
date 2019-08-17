myFile = open('scores.txt', 'r')

print('My one Line: ' + myFile.readline())
myFile.seek(0)
