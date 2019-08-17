import zipfile

zip = zipfile.ZipFile('archive.zip', r)
print(zip.namelist())
