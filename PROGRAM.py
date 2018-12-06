import random
import tkinter as tk


xls = open('sample-songlist.xlsx')

class Playlist:

    def __init__ (self):
        self.length = 10
        self.name = "TB named"
        self.songs = set()
        #self.songs = {"song1","song2","song3","song4","song5",
        #              "song6","song7","song8","song9","song10"}

    def __repr__ (self):
        return ("Playlist:" + " " +(self.name))

    def set_length(self,x):
        self.length = x
        self.songs = set()
        for i in range(0,x):
            self.songs.add(random.random())# Instead of a song set currently just a random number set
            

    def rename(self,x):
        self.name = str(x)
    


testpl = Playlist()


#okno = tk.Tk()





