




from tkinter import *
import tkinter as tk
import webbrowser
import os
import webpage_generator_main
import webpage_generator_func

def userInput(self):
    userInput = self.txtBody.get()

    # Opens html file in web browser
    htmlFile = open('webpage_generator.html', 'w')
    message = """<html><body> <h1>""" + userInput + """</h1></body></html>"""
    htmlFile.write(message)
    htmlFile.close()
    filename = 'file:///' +os.getcwd() + '/' + 'webpage_generator.html'
    webbrowser.open_new_tab(filename)
