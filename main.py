from tkinter import *
import tkinter.font as tkFont
from pytube import YouTube

root = Tk()

def GButton_157_command():
        var = url.get()
        video = YouTube(var)
        stream = video.streams.get_highest_resolution()
        stream.download()
        GLabel_34=Label(root)
        ft = tkFont.Font(family='Times',size=15)
        GLabel_34["font"] = ft
        GLabel_34["bg"] = "#000000"
        GLabel_34["fg"] = "#87fe00"
        GLabel_34["justify"] = "center"
        GLabel_34["text"] = "Video Descargado."
        GLabel_34.place(x=130,y=200,width=245,height=30)

root.title("YouTube Video Downloader")
width=507
height=266
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

GLabel_761=Label(root)
GLabel_761["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=10)
GLabel_761["font"] = ft
GLabel_761["fg"] = "#333333"
GLabel_761["justify"] = "center"
GLabel_761["text"] = ""
GLabel_761.place(x=0,y=0,width=507,height=266)

GLabel_766=Label(root)
GLabel_766["bg"] = "#ffffff"
ft = tkFont.Font(family='Times',size=10)
GLabel_766["font"] = ft
GLabel_766["fg"] = "#333333"
GLabel_766["justify"] = "center"
GLabel_766["text"] = ""
GLabel_766.place(x=0,y=50,width=507,height=3)

GLabel_942=Label(root)
ft = tkFont.Font(family='Times',size=12)
GLabel_942["font"] = ft
GLabel_942["bg"] = "#000000"
GLabel_942["fg"] = "#ffffff"
GLabel_942["justify"] = "center"
GLabel_942["text"] = "YouTube Video Downloader"
GLabel_942.place(x=100,y=10,width=290,height=30)

GLabel_360=Label(root)
ft = tkFont.Font(family='Times',size=11)
GLabel_360["font"] = ft
GLabel_360["bg"] = "#000000"
GLabel_360["fg"] = "#ffffff"
GLabel_360["justify"] = "center"
GLabel_360["text"] = "Video URL:"
GLabel_360.place(x=160,y=60,width=162,height=32)

url = StringVar()
GLineEdit_218=Entry(textvariable=url)
GLineEdit_218["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_218["font"] = ft
GLineEdit_218["fg"] = "#000000"
GLineEdit_218["justify"] = "center"
GLineEdit_218.place(x=130,y=100,width=228,height=33)

GButton_157=Button(root)
GButton_157["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=14)
GButton_157["font"] = ft
GButton_157["fg"] = "#000000"
GButton_157["justify"] = "center"
GButton_157["text"] = "Descargar"
GButton_157.place(x=180,y=140,width=139,height=30)
GButton_157["command"] = GButton_157_command

root.mainloop()
