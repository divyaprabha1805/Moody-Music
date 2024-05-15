import tkinter as tk
from PIL import ImageTk,Image
from tkinter.ttk import *
from fer import FER
import cv2
import sqlconnect
import musicplayer

#CREATING TKINTER WINDOW

root=tk.Tk()
root.title("MOODY MUSIC")
root.geometry("1000x1000")

#PLAYLIST

def playlist(top1,language,fe):
    if language=="English" and fe=="happy":
        pl="happy_hollywood"
    elif language=="English" and fe=="sad":
        pl="sad_hollywood"
    elif language=="English" and fe=="angry":
        pl="angry_hollywood"
    elif language=="Tamil" and fe=="happy":
        pl="happy_kollywood"
    elif language=="Tamil" and fe=="sad":
        pl="sad_kollywood"
    elif language=="Tamil" and fe=="angry":
        pl="angry_kollywood"
    elif language=="Hindi" and fe=="happy":
        pl="happy_bollywood"
    elif language=="Hindi" and fe=="sad":
        pl="sad_bollywood"
    elif language=="Hindi" and fe=="angry":
        pl="angry_bollywood"
    musicplayer.mp(top1,pl)
    
 #EMOTION DETECTION
    
def face(top):
            top.withdraw()
            top1=tk.Toplevel(top)
            top1.title("MOODY MUSIC")
            top1.geometry("1000x1000")
            
            def exp():
                global fe
                cam = cv2.VideoCapture(0)
                
                while True:
                    ret, frame = cam.read()
                    cv2.imshow("SCANNING...", frame)
                    k = cv2.waitKey(1)
                    if k%256 == 27:        
                        break
                    elif k%256 == 32:
                        iname="photo.jpg"
                        cv2.imwrite(iname, frame)       
                        break
                cam.release()
                cv2.destroyAllWindows()
                img = cv2.imread(iname)
                detector = FER()
                e=detector.top_emotion(img)
                fe=e[0]
                if fe not in ["happy","angry","sad"]:
                    exp()
                else:
                    top1.withdraw()
                    playlist(top1,language,fe)
            path ="scan.png"
            an= ImageTk.PhotoImage(Image.open(path))
            l1= tk.Label(top1, image = an)
            l1.image = img
            l1.pack(side = "bottom", fill = "y", expand = "yes")
            top1.configure(background='black')
            path ="sb.png"
            scan = ImageTk.PhotoImage(Image.open(path))
            b1=tk.Button(top1,image=scan,command=exp)
            b1.place(x=650,y=170)
            top1.mainloop()

def tops():

    root.withdraw()
    top=tk.Toplevel(root)
    top.title("MOODY MUSIC")
    top.geometry("1000x1000")

    def hollywood():
        global language
        language="English"
        face(top)
    def kollywood():
        global language
        language="Tamil"
        face(top)
    def bollywood():
        global language
        language="Hindi"
        face(top)

    path ="sl.png"
    img = ImageTk.PhotoImage(Image.open(path))
    l1 = tk.Label(top, image = img)
    l1.pack(side = "bottom", fill = "y", expand = "yes")
    top.configure(background='black')
    path ="english.png"
    eng = ImageTk.PhotoImage(Image.open(path))
    path ="tamil.png"
    tam = ImageTk.PhotoImage(Image.open(path))
    path ="hindi.png"
    hin = ImageTk.PhotoImage(Image.open(path))
    b1=tk.Button(top,image=eng,command=hollywood)
    b1.place(x=425,y=350)
    b2=tk.Button(top,image=tam,command=kollywood)
    b2.place(x=425,y=465)
    b3=tk.Button(top,image=hin,command=bollywood)
    b3.place(x=425,y=580)

    top.mainloop()

path ="M.png"
img = ImageTk.PhotoImage(Image.open(path))
l = tk.Label(root, image = img)
l.pack(side = "bottom", fill = "y", expand = "yes")
root.configure(background='black')
path ="start.jpg"
i = ImageTk.PhotoImage(Image.open(path))
b=tk.Button(root,image=i,command=tops)
b.place(x=520,y=415)

root.mainloop()