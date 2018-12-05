import random
import tkinter as tk


xls = open('sample-songlist.xlsx')

class Playlist:

    def __init__ (self):
        self.length = 10
        self.name = "TB named"
        pass
    def __repr__ (self):
        return ("Playlist:" + " " +(self.name))

    def set_length(self,x):
        self.length = x
        
    def rename(self,x):
        self.name = str(x)
    



testpl = Playlist()



#okno = tk.Tk()





