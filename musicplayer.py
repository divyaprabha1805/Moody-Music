import tkinter as tk
from PIL import ImageTk,Image
import os
os.add_dll_directory("C:\Program Files\VideoLAN\VLC")
import vlc
import pafy
import sqlconnect
from tkinter import ttk

#CREATING MUSIC PLAYER

def mp(top1,pl):
    global z
    z="none"
    def  song(d):
        global z
        if d=="d":
                 return z
        else:
            if z=="none":
                query="select URL from "+pl+" where SongName = '"+songchoosed+"'"
                sqlconnect.cur.execute(query)
                ul=sqlconnect.cur.fetchone()
                for i in ul:
                    url=i
                    x = pafy.new(url)
                    w=x.length
                    y = x.streams[0]
                    z = vlc.MediaPlayer(y.url)
                    z.play()
            else:
                z.set_pause(0)                

    def pause():
        fn=song("d")
        fn.set_pause(1)
        
    def player():
        song(1)    
        
    def stop():
        fn=song("d")
        fn.stop()
   # sqlconnect.cur.execute("select SongName from "+pl)
   # k=sqlconnect.cur.fetchall()

    top2=tk.Toplevel(top1)
    top2.title("MOODY MUSIC")
    top2.geometry("1200x1200")
    path ="mp.png"
    img = ImageTk.PhotoImage(Image.open(path))
    l1 = tk.Label(top2,image = img)
    l1.pack(side = "bottom", fill = "y", expand = "yes")
    top2.configure(background='black')

    #COMBOBOX
    sqlconnect.cur.execute("select SongName from "+pl)
    k=sqlconnect.cur.fetchall()
    n = tk.StringVar()
    songchoosen = ttk.Combobox(top2, width = 25,justify="center",textvariable = n,state='readonly',height=15,font=("times new roman",23,"italic"))
    songchoosen['values'] =k
    songchoosen.place(x=400,y=300)
    def selected_item():
        global songchoosed
        songchoosed=songchoosen.get()

    def end():
        top2.destroy()
        sqlconnect.cur.execute("drop database moody_music;")
    path ="pause.png"
    pa= ImageTk.PhotoImage(Image.open(path))
    path ="play.png"
    pla= ImageTk.PhotoImage(Image.open(path))
    path ="stop.png"
    st= ImageTk.PhotoImage(Image.open(path))
    path ="select.png"
    se= ImageTk.PhotoImage(Image.open(path))
    path ="end.png"
    en= ImageTk.PhotoImage(Image.open(path))


    b1=tk.Button(top2,image=pa,command=pause)
    b1.place(x=600,y=450)
    b2=tk.Button(top2,image=pla,command=player)
    b2.place(x=400,y=450)
    b3=tk.Button(top2,image=st,command=stop)
    b3.place(x=800,y=450)
    b4=tk.Button(top2,image=se,command=selected_item)
    b4.place(x=400,y=150)
    b5=tk.Button(top2,image=en,command=end)
    b5.place(x=600,y=650)

    
    top2.mainloop()







 




