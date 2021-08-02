




from tkinter import *
import tkinter as tk
import webpage_generator_main
import webpage_generator_func


def load_gui(self):

    # Button
    self.btn = Button(self.master, text="Create Webpage", command=lambda: webpage_generator_func.userInput(self))
    self.btn.grid(row=4,column=1, pady=(3,0), sticky = E)

    # Entry
    v = StringVar()
    v.set("Type here")

    self.txtBody = Entry(self.master,textvariable = v , width=30)
    self.txtBody.grid(row=1,rowspan=3, column=1, columnspan =4, padx=(10,0), pady=(10,0))



if __name__ == "__main__":
    pass
