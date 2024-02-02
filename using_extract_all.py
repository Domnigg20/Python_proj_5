#using extract all to to extract from zip files


import zipfile, os

from pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p / 'combined.zip')
