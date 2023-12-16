from customtkinter import *
import os

win = CTk()

f = open("file1.txt", "r")

a = StringVar()
entry1 = CTkTextbox(win)
entry1.grid(column = 1, row = 1)
entry1.insert(INSERT, f.read())
def store():
    t = open("file3.txt", "w")
    t.write(entry1.get("1.0", "end"))
    t.close()
def Exit():
    #os.remove("file1.txt")
    os.remove("file3.txt")
    exit()

CTkButton(win, command=store).grid(column = 1, row = 0)
CTkButton(win, command=Exit).grid(column = 2, row = 0)

win.mainloop()