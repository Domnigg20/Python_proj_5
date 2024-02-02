#Create zipfile object by calling zipfile.ZipFile()

import zipfile, os

from pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p / 'combined.zip')

#namelist returns list of strings for all files and folders in the zip file.
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('shore.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)

f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!'
exampleZip.close()