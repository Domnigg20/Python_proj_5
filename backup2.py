import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)

    print("name of folder is:" , folder)

backupToZip('/home/peter/Python_proj_5')
