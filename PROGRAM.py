import random
import tkinter as tk



xls = open('sample-songlist.xlsx')

class Playlist:
    def __init__ (self):
        playlist_length = 10
    def __repr__ (self):
        return ("A Playlist")

    def set_length(self,x):
        playlist_length = x
        

testpl = Playlist()

okno = tk.Tk()





