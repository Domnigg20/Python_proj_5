# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)
    print("name of folder is:" , folder)  # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # TODO: Create the ZIP file.
    print(f'Creating {zipFilename}...')
    new_zip = zipfile.ZipFile(zipFilename, "w")

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        #print("foldername:", foldername)
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        new_zip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            print("filename:", filename)
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't back up the backup ZIP files
            new_zip.write(os.path.join(foldername, filename))
    new_zip.close()

    print('Done.')

backupToZip('/home/peter/Python_proj_5')
