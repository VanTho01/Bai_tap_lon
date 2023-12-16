from customtkinter import *
from PIL import Image

class Home:
    def __init__(self, win):
        self.win = win
        win.geometry('1560x988')
        win.configure(fg_color = "#B48989")
        self.frame1 = CTkLabel(win, fg_color="#FBFBFB", width = 1515, height = 858, text = '')
        self.frame1.place(x = 23, y = 113)

        self.iconWelcome = CTkImage(light_image = Image.open('asset/iconWelcome.png'), size = (1302, 577))
        self.tabWelcome = CTkLabel(win, text = '',image=self.iconWelcome, fg_color = "#51BF56", width = 1302, height = 577)
        self.tabWelcome.place(x = 140, y = 221)
if __name__ == "__main__":
    win = CTk()
    app = Home(win)
    win.mainloop()
