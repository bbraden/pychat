import webbrowser
from tkinter import *
from datetime import datetime
from dbtools import *
from PIL import Image, ImageTk
import re

root = Tk()
root.geometry('190x250')
root.title('chat')
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(1, weight=0)
root.configure(background='lightgray')

var = StringVar()
var.set('')

titleLabel = Label(text='chat app', bg="#8f8f8f")
titleLabel.grid(row=0, column=0)

chatBox = Entry()
chatBox.configure({"background": "#d1d0cd", "foreground": "black"})
chatBox.grid(row=1, column=0)

msg3 = ''


def insertToDB(message2):
    global msg3
    date2 = datetime.now().strftime("%x")
    time2 = datetime.now().strftime("%X")
    msg2 = {"message": message2, "date": date2, "time": time2}
    msg3 = msg2
    db.insert_one(msg2)


def getMsg():
    return db.find({})


def sendChat():
    global var
    time = datetime.now().strftime("%X")
    date = datetime.now().strftime("%x")
    k = chatBox.get()
    ms = {"message": k, "date": date, "time": time}
    db.insert_one(ms)
    setVar = ms['message']
    sv = str(setVar)
    if len(sv) >= 20:
        a = re.sub("(.{15})", "\\1\n", sv, 0, re.DOTALL)
        var.set(a)
    if len(sv) <= 20:
        var.set(sv)




def refresh():
    global var
    var.set(getMsg()['message'])


def openGithub():
    webbrowser.open('https://github.com/bbraden')


sendChatButton = Button(text='send!', command=sendChat, highlightbackground='#3E4149')
sendChatButton.grid(row=2, column=0)

newestMsg = Label(textvariable=var, bg="#bdbdbd")
newestMsg.grid(row=3, column=0)

lbl1 = Label(text='', bg='lightgray')
lbl1.grid(row=4, column=0)

lbl2 = Label(text='', bg='lightgray')
lbl2.grid(row=5, column=0)

gitButton = Button(text='github.com/bbraden', command=openGithub)
gitButton.grid(row=6, column=0)

image1 = Image.open("g.png")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

label1.grid(row=7, column=0)

c = 0
m = 0
date = datetime.now().strftime("%x")


def od():
    global m
    m += 1


currentMsg = 'message'


def my_mainloop():
    global c
    global m
    global currentMsg
    ttl = f'chat'
    root.title(ttl)
    tings = db.find({})
    for messages in tings:
        try:
            if date != messages["date"]:
                print(f"Today - {messages['time']}", 'red')
            else:
                print(f"Today - {messages['date']} - {messages['time']}", 'red')
            print("Message: ", messages['message'])
            sv = messages['message']
            if len(sv) >= 20:
                a = re.sub("(.{15})", "\\1\n", sv, 0, re.DOTALL)
                var.set(a)
            if len(sv) <= 20:
                var.set(sv)
            print('---------------------------')
        except:
            pass
    root.after(1000, my_mainloop)


root.after(1000, my_mainloop)

root.mainloop()
