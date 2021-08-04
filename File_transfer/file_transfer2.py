





import shutil
import os
import datetime

# this is where the files are located
source = '/Users/alda/Desktop/FolderA/'

# this is the destination path
destination = '/Users/alda/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    abPath = source+i
    modDate = datetime.datetime.fromtimestamp(os.path.getmtime(abPath))
    currentDate = datetime.datetime.today()

    # this is the date/time 24 hours from current date/time
    modDateLimit = modDate + datetime.timedelta(days=1)

    # copy's file if edited less than 24 hours ago
    if modDateLimit > currentDate:
        shutil.copy(abPath, destination)
