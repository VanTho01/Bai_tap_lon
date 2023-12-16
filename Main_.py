from tkinter import *
from tkinter.constants import BOTH
import subprocess

win = Tk()
win.geometry('500x350')
win.title('Menu')
win.resizable(True, True)
#win.configure(bg = '#FFF4D3')
frame_menu = Frame(win, highlightbackground='#FFF4D3', highlightthickness=2)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)
def Muc1():
    file= 'Math_solution/muc1.py'
    subprocess.call(['python', file])
def Muc2():
    file= 'Math_solution/muc2.py'
    subprocess.call(['python', file])
def Muc3():
    file= 'Math_solution/muc3.py'
    subprocess.call(['python', file])
def Muc4():
    file= 'Math_solution/muc4.py'
    subprocess.call(['python', file])

Label(win, text = "Hỗ trợ bạn môn giải tích", font = ('Times new roman', 15), bg = 'white', fg = 'Black', width = 20, height = 1, relief='solid', borderwidth = 2).place(x = 140, y = 2)

limit_button = Button(win,height = 4, text = " Tính giới hạn ",command = Muc1, font = ('Times new roman', 13), bg = '#45C3A4', fg = 'Black', width = 20, relief='solid', borderwidth = 2)
limit_button.place(x = 60, y = 70)
integral_button = Button(win,height = 4, text = " Tính tích phân \n đạo hàm",command = Muc2, font = ('Times new roman', 13), bg = '#45C3A4', fg = 'Black', width = 20, relief='solid', borderwidth = 2)
integral_button.place(x = 260, y = 70)
sovle_button = Button(win,height = 4, text = " Giải phương trình \nn bậc",command = Muc3, font = ('Times new roman', 13), bg = '#45C3A4', fg = 'Black', width = 20, relief='solid', borderwidth = 2)
sovle_button.place(x = 60, y = 170)
sovle_linear_button = Button(win,height = 4, text = " Giải hệ phương trình\n với n phương trình \nn ẩn",command = Muc4, font = ('Times new roman', 13), bg = '#45C3A4', fg = 'Black', width = 20, relief='solid', borderwidth = 2)
sovle_linear_button.place(x = 260, y = 170)
exit_button = Button(win,height = 2, text = " Thoát ",command = exit, font = ('Times new roman', 13), bg = 'orange', fg = 'Black', width = 10, relief='solid', borderwidth = 2)
exit_button.place(x = 200, y = 280)

win.mainloop()

