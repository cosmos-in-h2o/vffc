from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tool
import mysty
import os


class VideoToAudioButton:
    def __init__(self, title, geometry):
        self.window = Toplevel()
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.config(bg="#252930")
        self.window.resizable(False, False)

        self.separation = Label(self.window, bg="#252930")
        self.separation.grid()

        self.inputLabel = Label(self.window, text="输入:", bg="#252930", fg="#4e76b7")
        self.inputLabel.grid(row=1, column=0)
        self.inputEntry = Entry(self.window, width=40)
        self.inputEntry.grid(row=1, column=1)
        self.inputFileExploreButton = mysty.button2(self.window, "浏览", self.inputFileExploreAction)
        self.inputFileExploreButton.grid(row=1, column=2, padx=8)

        self.outputLabel = Label(self.window, text="输出:", bg="#252930", fg="#4e76b7")
        self.outputLabel.grid(row=2, column=0)
        self.outputEntry = Entry(self.window, width=40)
        self.outputEntry.grid(row=2, column=1)
        self.outputFileExploreButton = mysty.button2(self.window, "浏览", self.outputFileExploreAction)
        self.outputFileExploreButton.grid(row=2, column=2, padx=8)

        self.convertButton = mysty.button(self.window, "转换", self.convertAction)
        self.convertButton.grid(row=3, column=1)

        self.label = Label(self.window, text="", bg="#252930", fg="#4e76b7")
        self.label.grid(row=4, column=1)

    def inputFileExploreAction(self):
        filetypes = [
            # 常见的视频文件格式
            ("Video files", "*.mp4;*.avi;*.mkv;*.mov;*.flv;*.wmv;*.asf;*.asx;*.rm;*.rmvb;*.3gb;*.mov;*.m4p;*.vob;"),
        ]
        path = tkinter.filedialog.askopenfilename(title="Select a video file", filetypes=filetypes)
        if path:
            self.inputEntry.delete(0, END)
            self.inputEntry.insert(0, path)

    def outputFileExploreAction(self):
        path = tkinter.filedialog.asksaveasfilename(title="Save out file")
        if path:
            self.outputEntry.delete(0, END)
            self.outputEntry.insert(0, path)

    def convertAction(self):
        iname = self.inputEntry.get()
        oname = self.outputEntry.get()
        # 文件不存在
        if not os.path.exists(iname):
            tkinter.messagebox.showerror("警告", f"\"{iname}\"不存在!")
            self.label.configure(text="转换失败!")
            return
        if os.path.exists(oname):
            if not tkinter.messagebox.askyesno("提示", f"\"{oname}\"已存在，是否继续转换(继续转换将会覆盖原有文件)?"):
                self.label.configure(text="转换失败!")
                return
        self.label.configure(text="正在转换...")
        tool.convertSingle(iname, oname)
        self.label.configure(text="转换成功!")
        tkinter.messagebox.showinfo("提示", f"已经成功将\"{iname}\"转换为\"{oname}\"!")

    def run(self):
        self.window.mainloop()
