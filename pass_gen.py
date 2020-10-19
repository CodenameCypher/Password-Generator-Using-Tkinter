from tkinter import *
import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
chars = []
chars.extend(s1)
chars.extend(s2)
chars.extend(s3)
chars.extend(s4)

def generate():
    l = int(passLen.get())
    passLen.delete(0,END)
    random.shuffle(chars)
    password = "".join(chars[0:l])
    txtLabel['text'] = password
    root.update()

root = Tk()
root.geometry('500x200+550+200')
root.title("Password Generator")
root.resizable(0,0)
root.iconbitmap('images/icon.ico')

#backgroud image
bg = PhotoImage(file='images/bg.png')
bgLabel = Label(root, image = bg)
bgLabel.pack()
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

#entry
passLen = Entry(bgLabel,font=('times new roman',16,'bold'),width=9,justify=CENTER,relief=GROOVE) 
passLen.pack()
passLen.place(x=90,y=90)

#button
btn = Button(bgLabel,text='Generate',font=('comic sans ms',15,'bold'),relief=GROOVE,bg='#008080',fg='white',command=generate)
btn.pack()
btn.place(x=90,y=130)

#pass shower
txtLabel = Label(bgLabel,text='',font=('times new roman',16,'bold'),bg="#093e4c",fg='#ADFF2F')
txtLabel.pack()
txtLabel.place(anchor=CENTER,x=140,y=50)

root.mainloop()