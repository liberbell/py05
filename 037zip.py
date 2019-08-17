import zipfile

zip = zipfile.ZipFile('archive.zip', 'r')
print(zip.namelist())

for meta in zip.infolist():
    print(meta)

info = zip.getinfo('purchased.txt')
print(info)

print(zip.read('wishlist.txt'))
with zip.open('wishlist.txt') as f:
    print(f.read())

zip.extract('purchased.txt')
