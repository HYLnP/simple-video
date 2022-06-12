# -*- coding:utf-8 -*-
# 用户：HYL
# 日期：2022年06月12日
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import filedialog
from you_get import common
from threading import Thread
from moviepy.editor import *


def tq():
    url = text.get()
    ad = text2.get()
    label = tk.Label(window, text= "视频提取中.......", bg="white", fg="green")
    label.pack()
    common.any_download(url=url, output_dir=ad, merge=True)
    msg.showinfo(title="信息提示", message="下载完成")
    label.destroy()


def zh():
    name1 = text3.get()
    name2 = name1[:-3]+ '.wav'
    label = tk.Label(window, text= "视频转换中.......", bg="white", fg="green")
    label.pack()
    video = VideoFileClip(name1)  # 格式 video = VideoFileClip(r'文件位置')
    audio = video.audio
    audio.write_audiofile(name2)  # 格式 audio.write_audiofile('新文件位置和格式 wav/mp3')
    msg.showinfo(title="信息提示", message="转换成功")
    label.destroy()


#输入文件夹路径
def selectPath_dir():
    path_ = filedialog.askdirectory()
    var_name.set(path_)


#输入文件路径
def selectPath_file():
    path_ = filedialog.askopenfilename(filetypes=[("视频文件",[".mp4"])])
    var_name2.set(path_)
 

window = tk.Tk()
window.title("视频提取和视频转换")
window.geometry("600x400")
window.resizable(False, False)

lab = tk.Label(window, text="请输入要提取的视频、音频网址")
lab.pack()
text = tk.Entry(window)
text.pack()

# ------------------------------------------------------------
var_name=tk.StringVar() #文件夹输入路径变量
lab2 = tk.Label(window, text="请选择文件夹位置(例：d:/blbl)")
lab2.pack()

text2 = tk.Entry(window, textvariable=var_name)
text2.pack()

dir_button = tk.Button(window, text="选择文件夹", command=selectPath_dir)
dir_button.pack()

button = tk.Button(window, text="提取视频", command=lambda: Thread(target=tq).start())
button.pack()
#--------------------------------------------------------------
var_name2=tk.StringVar() #文件输入路径变量
lab3 = tk.Label(window, text="请选择文件位置(例：d:/blbl/123.mp4)")
lab3.pack()

text3 = tk.Entry(window, textvariable=var_name2)
text3.pack()

file_button =  tk.Button(window, text="选择文件", command=selectPath_file)
file_button.pack()

button2 = tk.Button(window, text="视频转音频", command=lambda: Thread(target=zh).start())
button2.pack()

lab5 = tk.Label(window, text="提取视频和视频转音频的小工具")
lab5.pack()


window.mainloop()