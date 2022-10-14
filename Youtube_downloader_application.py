from tkinter import *
from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

canv = Tk()
canv.geometry("600x400")
canv.title("Youtube Downloader")
Label(canv, text="Youtube Video Downloader", font="arial 20 bold").pack()
lvar = StringVar()
lvar.set("Enter the link below")
Label(canv, textvariable=lvar, font="arial 15 bold").pack(pady=20)
url = StringVar()
Entry(canv, textvariable=url, width=70).pack(pady=5)

def download():
    try:
        lvar.set("Downloading...")
        canv.update()
        YouTube(url.get()).streams.first().download()
        lvar.set("Downloaded")
    except Exception as e:
        lvar.set("Error : " + str(e))
        canv.update()

Button(canv, text="Download", font="arial 15 bold", bg="pale violet red", padx=2, command=download).pack(pady=20)
canv.mainloop()
