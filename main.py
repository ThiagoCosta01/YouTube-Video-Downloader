from tkinter import *
from pytube import YouTube

def temporaryTxtDel(e):
    userUrl.delete(0,"end")

def temporaryTxtAdd(e):
    userUrl.insert(0, "url...")

def downloader():
    try:
        url = YouTube(str(userUrl.get()))
        video = url.streams.first()
    except:
        print("Error")
    else:
        print("success")
        video.download()
        userUrl.delete(0,"end")

root = Tk()

root.title("Youtube Downloader")
root.geometry('800x400+610+153')

root.iconbitmap(default="")
root.resizable(width=1, height=1)

background = PhotoImage(file=r"Python\Yt downloader\img\botao.png")
botao = PhotoImage(file=r"Python\Yt downloader\img\botao.png")

labelFundo = Label(root, image=background)
labelFundo.pack()


# userUrl = Entry(root)
# userUrl.insert(0, "url...")
# userUrl

# userUrl.bind("<FocusIn>", temporaryTxtDel)
# userUrl.bind("<FocusOut>", temporaryTxtAdd)

# Button(root, text="Download Video", command=downloader, bg="black", fg="white")

root.mainloop()