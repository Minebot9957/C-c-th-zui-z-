
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
import webbrowser

root = Tk()
root.geometry("1000x510+250+50")
root.title("Hello World")
 
load = Image.open('background.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.place(x=0,y=0)
head = Label(root, text="I Am Steve",fg="#FFFFFF",bd=0)
head.config(font=("Transformers Movie", 30))
head.pack(pady= 10)
l = Label(root, text='Lịch sử trò chuyện', fg='White', bg='blue')
l.place(x = 920, y = 10, width=150, height=50)
button_frame=Frame(root).pack(side=BOTTOM)
box=Text(root,width=40,height=30,font=("ROBOTO",20), bg='black')
box.pack(pady=20)
def trending():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)
call_button=Button(button_frame,text='nhan vao day di',font=(("Arial"),15,'bold'),bg='#303030',fg='#FFFFFF',command=trending)	
call_button.pack(side=RIGHT, padx=11, pady=10)
root.mainloop()