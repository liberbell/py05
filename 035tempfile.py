import tempfile

tempFile = tempfile.TemporaryFile()

tempFile.write(b'Save this special number for me: 98322451')
tempFile.seek(0)

print(tempFile.read())
tempFile.close()
