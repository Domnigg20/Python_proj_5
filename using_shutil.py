import shutil, os
from pathlib import Path
p = Path.home()
print(p)

#lets copy from the home path to some
shutil.copy(p / 'stderrr.txt', p / 'mysite')