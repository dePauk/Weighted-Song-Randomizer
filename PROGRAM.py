import random
import tkinter as tk

#repetition_happened = False

xls = open('sample-songlist.xlsx')

all_songs_set = {"song1","song2","song3","song4","song5","song6",
             "song7","song8","song9","song10","song11","song12",
             "song13","song14","song15","song16","song17","song18",
             "song19","song20"}

all_songs_tuple = tuple(all_songs_set)

#print (random.choice(all_songs_tuple))

#----------------------------------------------------------------------------------------------------------------


class Playlist:

    def __init__ (self):
        self.length = 10
        self.name = "TB named"
        self.songs = set()
        self.songs = {"song1","song2","song3","song4","song5",
                      "song6","song7","song8","song9","song10"}

    def __repr__ (self):
        return ("Playlist:" + " " +(self.name))

    def set_length(self,x):
        repetition_happened = False
        if x > 10: # Change later in process
            return "Error. Currently only playlists of up to 10 songs allowed."
        else:
            self.length = x
            self.songs = set()
            already_chosen = set()
            for i in range(0,x):
                chosen_song = random.choice(all_songs_tuple)
                if chosen_song not in already_chosen:                                
                    self.songs.add(chosen_song)
                    already_chosen.add(chosen_song)
                else:
                    repetition_happened = True
                    #Change this for no repetitions, option repetitions on/off?

           
            if repetition_happened == True:
                print ("A repetition happened.")
            else:
                pass
            
            return self.songs
            repetition_happened = False



    def rename(self,x):
        self.name = str(x)


        
    


testpl = Playlist()


#okno = tk.Tk()





