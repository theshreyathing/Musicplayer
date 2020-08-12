import os #to fetch songs and directories
from tkinter.filedialog import askdirectory #for selecting our song directory
import pygame #for playing music
from mutagen.id3 import ID3 # for tagging the meta data to our songs
from tkinter import * # for UI
root = Tk() #creates an empty window
root.minsize(800,600) #Set size
listofsongs = []
realnames = []
v = StringVar()
songlabel = Label(root,textvariable = v,width = 40)
def directorychooser():
    directory = askdirectory()
    os.chdir(directory) #Loop over all the files in that directory
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file) # only add them if they end with .mp3
            audio = ID3(realdir) # load the meta data of that song
            realnames.append(audio['TIT2'].text[0]) # TIT2 refers to the TITLE of the song
            listofsongs.append(file)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])  # load the first song pygame.mixer.music.play()
def updatelabel():
    global index # If you do not use global, new index variable will be defined
    global songname # set our StringVar to the real name
    v.set(realnames[index]) #return songname
def nextsong():
    global index # get index from globals
    index += 1 # increment index
    pygame.mixer.music.load(listofsongs[index]) # get the next song from listofsongs
    pygame.mixer.music.play() # play it away
    updatelabel() #update the label
def prevsong():
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
def stopsong(event):
    pygame.mixer.music.stop() # stop the current song which is playing
    v.set("")  # set our Label to empty
label = Label(root,text = "Music Player by The.shreya.thing") # set the heading I personalised mine you can do yours
label.pack() # pack it inside root window
listbox = Listbox(root)
listbox.pack()
realnames.reverse()
for item in realnames:
    listbox.insert(0,items)
realnames.reverse()
nextbutton = Button(root,text = "Next song")
nextbutton.pack()
previousbutton = Button(root,text = "Pervious song")
previousbutton.pack()
stopbutton = Button(root,text = "Stop song")
stopbutton.pack()
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",previousbutton)
stopbutton.bind("<Button-1>",stopbutton)
songlabel.pack()
root.mainloop()



