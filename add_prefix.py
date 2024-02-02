import os

#specify the filename
filename = "eggs.txt"
prefix = "spam_"

#form the new filename with the prefix

new_filename = prefix + filename


#rename the file
os.rename(filename, new_filename)
