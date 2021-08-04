






from tkinter import *
from tkinter import filedialog
import shutil
import os
import datetime

import file_transfer_main
import file_transfer_func

def load_gui(self):

    # Label
    self.lblSource = Label(self.master, text="Select a folder with files to transfer:")
    self.lblSource.grid(row=0,column=1,columnspan=2,padx=(20,0),pady=(20,0),sticky=W)
    self.lblDest = Label(self.master, text="Select a folder to receive files:")
    self.lblDest.grid(row=2,column=1,columnspan=2,padx=(20,0),pady=(20,0),sticky=W)

    # Result label
    self.result= StringVar()
    self.lblResult = Label(self.master, textvariable=self.result)
    self.lblResult.config(font=("Arial",12))
    self.lblResult.grid(row=5, column=1,columnspan=2,pady=(20,0))

    # Entry
    self.sourceDir= StringVar()
    self.destDir = StringVar()
    self.entrySource = Entry(self.master,width=35,textvariable=self.sourceDir)
    self.entrySource.grid(row=1,column=1,columnspan=2, padx=(20,0))
    self.entryDest = Entry(self.master,width=35,textvariable=self.destDir)
    self.entryDest.grid(row=3,column=1,columnspan=2, padx=(20,0))


    # Buttons
    self.btnSelect = Button(self.master, width=10,height=2,text="Browse",command=lambda:file_transfer_func.onSelect(self))
    self.btnSelect.grid(row=1,column=3,padx=(20,15),pady=(0,0),sticky=W)
    self.btnCopy = Button(self.master, width=10,height=2,text="Browse",command=lambda:file_transfer_func.onCopy(self))
    self.btnCopy.grid(row=3,column=3,padx=(20,15),pady=(0,0),sticky=W)
    self.btnFileCheck = Button(self.master, width=35,height=2,text="Process files", command=lambda:file_transfer_func.fileCheck(self))
    self.btnFileCheck.grid(row=4,column=1,columnspan=2,padx=(5,15),pady=(10,0,))



if __name__ == "__main__":
    pass
