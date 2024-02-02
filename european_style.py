import shutil
from pathlib import Path
import re

# Get the current working directory as a Path object
absWorkingDir = Path.cwd()

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)


### Loop over the files in the working directory.
for amerFilename in absWorkingDir.glob('*'):
    # Convert Path object to string
    amerFilename = str(amerFilename)

    mo = datePattern.search(amerFilename)
    
    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    
    
    # print(mo.group(1))
    # print(mo.group(2))
    # print(mo.group(3))
    # print(mo.group(4))
    # print(mo.group(5))
    # print(mo.group(6))
    # print(mo.group(7))
    # print(mo.group(8))

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    print("euroFilename:", euroFilename)

    # Get the full, absolute file paths using Path.
    amerFilePath = absWorkingDir / amerFilename
    # print(absWorkingDir)
    print(amerFilename)
    # print(amerFilePath)
    euroFilePath = absWorkingDir / euroFilename

    # Rename the files.
    print(f'Renaming "{amerFilePath}" to "{euroFilePath}"...')
    # Uncomment the line below after testing and confirming correctness
    shutil.move(amerFilename, euroFilename)   # uncomment after testing
