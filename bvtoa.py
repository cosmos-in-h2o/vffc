from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tool
import mysty
import os


class BatchVideoToAudioButton:
    def __init__(self, title, geometry):
        self.window = Toplevel()
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.config(bg="#252930")
        self.window.resizable(False, False)

        self.separation = Label(self.window, bg="#252930")
        self.separation.grid()

        self.inputFrame = Frame(self.window, bg="#252930")
        self.inputFrame.grid()
        self.inputLabel = Label(self.inputFrame, text="文件夹:", bg="#252930", fg="#4e76b7")
        self.inputLabel.grid(row=1, column=0)
        self.inputEntry = Entry(self.inputFrame, width=40)
        self.inputEntry.grid(row=1, column=1)
        self.inputDirExploreButton = mysty.button2(self.inputFrame, "浏览", self.inputDirExploreAction)
        self.inputDirExploreButton.grid(row=1, column=2, padx=8)

        self.fileTypesFrame = Frame(self.window, bg="#252930")
        self.fileTypesFrame.grid()
        self.fileTypes = ["mp4", "avi", "mov", "flv", "wmv", "mkv", "m4v", "webm", "3gp", "ts", "mxf", "mpeg", "mpg",
                          "vob"]
        self.fileTypeCheckButtons = list()
        for i in self.fileTypes:
            self.fileTypeCheckButtons.append(
                Checkbutton(self.fileTypesFrame, text=i, bg="#252930", fg="#4e76b7", activebackground="#252930",
                            activeforeground="#4e76b7"))
        n = 0
        length = 5  # 每行的复选框数量
        for i in self.fileTypeCheckButtons:
            i.grid(row=int(n / length), column=n % length)
            n += 1

        self.outputFrame = Frame(self.window, bg="#252930")
        self.outputFrame.grid()
        self.outputLabel = Label(self.outputFrame, text="输出到:", bg="#252930", fg="#4e76b7")
        self.outputLabel.grid(row=0, column=0)
        self.outputEntry = Entry(self.outputFrame, width=40)
        self.outputEntry.grid(row=0, column=1)
        self.outputDirExploreButton = mysty.button2(self.outputFrame, "浏览", self.outputDirExploreAction)
        self.outputDirExploreButton.grid(row=0, column=2, padx=8)

        self.suffixFrame = Frame(self.window, bg="#252930")
        self.suffixFrame.grid()
        self.suffixLabel = Label(self.suffixFrame, text="输出后缀:", bg="#252930", fg="#4e76b7")
        self.suffixLabel.grid(row=0, column=0)
        self.suffixEntry = Entry(self.suffixFrame, width=10)
        self.suffixEntry.grid(row=0, column=1)

        self.convertButtonFrame = Frame(self.window, bg="#252930")
        self.convertButtonFrame.grid()
        self.convertButton = mysty.button(self.convertButtonFrame, "转换", self.convertAction)
        self.convertButton.grid()

        self.frame = Frame(self.window, bg="#252930")
        self.frame.grid()
        self.label = Label(self.frame, text="", bg="#252930", fg="#4e76b7")
        self.label.grid()

    def inputDirExploreAction(self):
        path = tkinter.filedialog.askdirectory()
        if path:
            self.inputEntry.delete(0, END)
            self.inputEntry.insert(0, path)

    def outputDirExploreAction(self):
        path = tkinter.filedialog.askdirectory()
        if path:
            self.outputEntry.delete(0, END)
            self.outputEntry.insert(0, path)

    def convertAction(self):
        iname = self.inputEntry.get()
        oname = self.outputEntry.get()
        suffix = self.suffixEntry.get()

        # 检查
        audioTypes = [
            "mp3", "wav", "m4a", "aac", "flac", "ogg", "wma", "amr", "opus"
        ]
        if self.suffixEntry.get() not in audioTypes:
            tkinter.messagebox.showerror("错误", f"不支持转化为\"{suffix}\"文件!")
            self.label.configure(text="转换失败!")
            return
        if not os.path.exists(iname):
            tkinter.messagebox.showerror("错误", f"不存在文件夹\"{iname}\"!")
            self.label.configure(text="转换失败!")
            return
        if not os.path.exists(oname):
            os.makedirs(oname)
        fileLs = list()
        for i in self.fileTypes:
            fileLs = list(set(fileLs + tool.getFiles(iname, i)))

        self.label.configure(text="正在转换...")
        for i in fileLs:
            tool.convertSingle(i, os.path.join(oname, tool.getFileName(i) + '.' + suffix))
        self.label.configure(text="转换成功!")
        tkinter.messagebox.showinfo("提示", f"已经成功转换了{len(fileLs)}个文件!")

    def run(self):
        self.window.mainloop()
