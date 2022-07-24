#Imports
from tkinter import *
from pytube import YouTube
#Functions
def temporaryTxtDel(e):
   userUrl.delete(0,"end")

def temporaryTxtAdd(e):
   userUrl.insert(0, "url...")

def downloader():
    try:
        url = YouTube(str(userUrl.get()))
        video = url.streams.get_by_itag(139)
        video.download("D:\Downloads YouTube")
    except:
        erro = Label(root, bg="red", text="X")
        erro.place(width=51, height=51, x=75, y=155)
        print("Error")
    else:
        sucesso = Label(root, bg="green", text="")
        sucesso.place(width=51, height=51, x=75, y=155)
        print("success")        
        userUrl.delete(0,"end")

def resolucoes():
    url = YouTube(str(userUrl.get()))
    i = url.streams.all()
    print(i)


#Main
root = Tk()

root.title("Youtube Downloader")
root.geometry('800x400+610+153')
root.config(bg='black')
root.iconbitmap(default="")
root.resizable(width=1, height=1)
#Photos
erroIco = PhotoImage(file=r"Python\Yt downloader\img\cancel2.png")
background = PhotoImage(file=r"Python\Yt downloader\img\fundo.png")
botaoPhoto = PhotoImage(file=r"D:\Downloads (D)\Python-Aulas\Python\Yt downloader\img\botao.png")
#Background
labelFundo = Label(root, image=background)
labelFundo.pack()

#Button
botao = Button(root, image=botaoPhoto, command=downloader)
botao.place(width=260, height=70, x=269, y=243)


botaoResolucao = Button(root, text="Resolutions", command=resolucoes)
botaoResolucao.place(width=80, height=51, x=700, y=155)


#Entry input
userUrl = Entry(root, bd=2, font=("Calibri" ,15), justify=CENTER)
userUrl.place(width=544, height=74, x=128, y=143)
userUrl.insert(0, "Url...")


userUrl.bind("<FocusIn>", temporaryTxtDel)
userUrl.bind("<FocusOut>", temporaryTxtAdd)

root.mainloop()