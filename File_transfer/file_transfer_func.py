






from tkinter import *
from tkinter import filedialog
import shutil
import os
import datetime
import file_transfer_main
import file_transfer_func

def onSelect(self):
    global folder_path_source

    folder_path_source = filedialog.askdirectory()

    self.sourceDir.set(folder_path_source)

# This opens the system directory 
def onCopy(self):
    global folder_path_dest
    
    folder_path_dest = filedialog.askdirectory()

    self.destDir.set(folder_path_dest)

def fileCheck(self):
    files = os.listdir(folder_path_source)

    for i in files:
        # Checks for files ending in .txt
        if i.endswith('.txt'):

            abPath = folder_path_source+"/"+i

            
            modDate = datetime.datetime.fromtimestamp(os.path.getmtime(abPath))
            currentDate = datetime.datetime.today()
            modDateLimit = modDate + datetime.timedelta(days=1)

            # If file was last edited less than 24 hours ago then it gets copied
            if modDateLimit > currentDate:
                shutil.copy(abPath, folder_path_dest)

            self.result.set("Successful, files have been copied over to destination folder!")



if __name__ == "__main__":
    pass
