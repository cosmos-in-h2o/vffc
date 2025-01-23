from moviepy import AudioFileClip
import os


def getFiles(path, suffix):
    _suffix = '.' + suffix
    # 获取文件夹下所有的文件名
    fileLs = list()
    for root, dirs, names in os.walk(path):
        for name in names:
            ext = os.path.splitext(name)[1]
            if ext == _suffix:
                fromdir = os.path.join(root, name)
                fileLs.append(fromdir)
    return fileLs


def getFileName(name: str):
    fileName = os.path.basename(name)
    dirStr, ext = os.path.splitext(fileName)
    return dirStr


def convertSingle(iname: str, oname: str):
    audio = AudioFileClip(iname)
    audio.write_audiofile(oname)
