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
root.config(bg='red')
root.iconbitmap(default="")
root.resizable(width=1, height=1)

background = PhotoImage(file=r"Python\Yt downloader\img\botao.png")
botao = PhotoImage(file=r"D:\Downloads (D)\Python-Aulas\Python\Yt downloader\img\botao.png")

Label(root, text="Download Video", fg='white', bg='red').grid(row=1, column=2, padx=10)

userUrl = Entry(root)
userUrl.insert(0, "url...")
userUrl.grid(row=2, column=2)

userUrl.bind("<FocusIn>", temporaryTxtDel)
userUrl.bind("<FocusOut>", temporaryTxtAdd)

Button(root, text="Download Video", command=downloader, bg="black", fg="white").grid(row=3, column=2)

root.mainloop()