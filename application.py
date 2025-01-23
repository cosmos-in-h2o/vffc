from tkinter import *
import mysty
import vtoa
import bvtoa


def openVideoToAudioAction():
    window = vtoa.VideoToAudioButton("视频转音频", "400x200")
    window.run()


def openBatchVideoToAudioAction():
    window = bvtoa.BatchVideoToAudioButton("批量视频转音频", "420x300")
    window.run()


class Application:
    def __init__(self, title: str, geometry: str):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.config(bg="#252930")
        self.window.resizable(False, False)

        self.separation = Label(self.window, bg="#252930")
        self.separation.pack()

        self.videoToAudioButton = mysty.button(self.window, "视频转音频", openVideoToAudioAction)
        self.videoToAudioButton.pack()

        self.separation = Label(self.window, bg="#252930")
        self.separation.pack()

        self.batchVideoToAudioButton = mysty.button(self.window, "批量视频转音频", openBatchVideoToAudioAction)
        self.batchVideoToAudioButton.pack()

    def run(self):
        self.window.mainloop()
