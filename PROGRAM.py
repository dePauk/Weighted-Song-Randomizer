import random
import tkinter as tk


#repetition_happened = False

xls = open('sample-songlist.xlsx')

all_songs_set = {"Martin Garrix - Animals (Oliver Heldens Remix)",
"Disclosure feat. Sam Smith - Latch (Oliver Heldens Remix)",
"Koos - Switch",
"Showtek - 90s By Nature feat. MC Ambush (Curbi Remix)",
"Oliver $ & Jimi Jules - Pushing On (Tchami Remix)",
"Asino - Ouverture in Major",
"Boothed - Octopussy",
"Tchami - Shot Caller",
"David Guetta ft. Akon - Sexy Bitch",
"The Black Eyed Peas - Just Can't Get Enough",
"Clinton Sparks - Geronimo (Gregor Salto Remix)",
"Eiffel 65 - Blue (Da Ba Dee)",
"Mesto - Tetris",
"Robin Thicke - Feel Good (Oliver Heldens Remix)",
"Duke Dumont - Won't Look Back (Shadow Child Remix)",
"Linkin Park - Hit The Floor",
"Godlips - The Power Of The Dark Side",
"Yeah Yeah Yeahs x A-Trak - Heads Will Roll (Jonas Aden Remix)",
"Dirty Rush & Gregor Es - EVRBDY",
"Queen - Bohemian Rhapsody",
"Mesto - Rio",
"Naten - 2077",
"Gigi D'Agostino - L'Amour Toujours",
"Ben Van Kuringen - Life",
"French Affair - My Heart Goes Boom",
"Virtual Self - Ghost Voices",
"Matthew Koma - Kisses Back (KBN & NoOne Bootleg)",
"Freischwimmer - California Dreamin",
"Mr. Belt & Wezol - Shiver",
"Liquido - Narcotic"
}

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
        #reps = 0
        if x > 20: # Change later in process
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
                    #print(self.songs) ###)
                else:
                    repetition_happened = True
                    
                    #Change this for no repetitions, option repetitions on/off?

           
            if repetition_happened == True:
                reps = x - len(self.songs)
                reps_str = str(reps)
                if reps == 1:                
                    print (reps_str + " repetition occured.")
                elif reps > 1:
                    print (reps_str + " repetitions occured.")
                else:
                    pass
                self.set_length(x)
            
            
            return self.songs

    def rename(self,x):
        self.name = str(x)

        #input


        
    


testpl = Playlist()


##window = tk.Tk()
##titular = tk.Frame(window).pack()
##title = tk.Label(titular, text = "Weighted song randomizer").pack()
##
##
##
##window.mainloop()






