from tkinter import Tk, Label, Button, Listbox
import glob, os
from pygame import mixer

class Window:
    def __init__(self,master):
        self.master = master
        master.title("A simple GUI")
        self.playListBox = Listbox(master,selectmode="SINGLE")
        self.playListBox.pack()
        self.play = Button(master, text="Play")
        self.play.pack()

    def getPlayListBox(self):
        return self.playListBox


class PlayListData:
    playListData = []

    def __init__(self):
        os.chdir("C:/Users/Jude/Desktop")
        i = 0
        for file in glob.glob("*.mp3"):
            self.playListData.insert(i,file)



class Controller:

    def __init__(self,root):
        self.window = Window(root)
        self.play_list = PlayListData()
        self.music_player = MusicPlayer()
        for index, song in enumerate(self.play_list.playListData):
            self.window.playListBox.insert(index,song)
        self.window.playListBox.bind("<Double-Button-1>", self.on_double_click)
        self.window.play.bind("<Button-1>",self.on_double_click)

    def on_double_click(self, event):
        self.music_player.play_music(self.play_list.playListData, self.window.playListBox.curselection())


class MusicPlayer:
    def play_music(self, song_list, indexes,):
       song = song_list[indexes[0]]
       directory = 'C:/Users/Jude/Desktop/'
       print(song)
       fullPath = directory + song
       print(fullPath)
       mixer.init()
       mixer.music.load(fullPath)
       mixer.music.play()



root = Tk()
controller = Controller(root)
root.mainloop()

