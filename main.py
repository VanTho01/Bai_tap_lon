from customtkinter import *
from PIL import Image
import screenHome
import calLimit.screenLimit as screenLimit

class Home:
    def __init__(self, win):
        self.win = win
        win.geometry('1560x988')
        win.configure(fg_color = "#B48989")
        self.frame1 = CTkLabel(win, fg_color="#FBFBFB", width = 1515, height = 858, text = '')
        self.frame1.place(x = 23, y = 113)
        
        self.tabview1 = CTkLabel(win, corner_radius=10, text = '', fg_color = "#A56666", width = 1560, height = 113)
        self.tabview1.place(x = 0, y = 0)

        self.tabview2 = CTkLabel(win, corner_radius=10, text = '', fg_color = "#54AFC3", width = 1083, height = 86)
        self.tabview2.place(x = 36, y = 14)

        self.iconHome = CTkImage(light_image = Image.open('asset/iconHome.png'), size = (48, 48))
        self.buttonHome = CTkButton(win, image=self.iconHome, compound='left', command = self.fctHome, text = '   Home', width = 256, font = ('Times New Roman', 25), text_color='black', height = 60, corner_radius=3, fg_color="#5FE4DC", hover_color="#e82c90")
        self.buttonHome.place(x = 64, y = 26)

        self.iconIntegral = CTkImage(light_image = Image.open('asset/iconIntegral.png'), size = (48, 48))
        self.buttonIntegral = CTkButton(win, image=self.iconIntegral, compound='left', text = '  Integral', width = 256, font = ('Times New Roman', 25), text_color='black', height = 60, corner_radius=3, fg_color="#5FE4DC", hover_color="#e82c90")
        self.buttonIntegral.place(x = 318, y = 26)

        self.iconLimit = CTkImage(light_image = Image.open('asset/iconLimit.png'), size = (48, 48))
        self.buttonLimit = CTkButton(win, image=self.iconLimit, compound='left', command=self.fctLimit, text = '  Limit', width = 256, font = ('Times New Roman', 25), text_color='black', height = 60, corner_radius=3, fg_color="#5FE4DC", hover_color="#e82c90")
        self.buttonLimit.place(x = 574, y = 26)

        self.iconEquation = CTkImage(light_image = Image.open('asset/iconEquation.png'), size = (48, 48))
        self.buttonEquation = CTkButton(win, image=self.iconEquation, compound='left', text = 'Equation', width = 256, font = ('Times New Roman', 25), text_color='black', height = 60, corner_radius=3, fg_color="#5FE4DC", hover_color="#e82c90")
        self.buttonEquation.place(x = 830, y = 26)

        self.iconUpload = CTkImage(light_image = Image.open('asset/iconUpload.jpg'), size = (83, 77))
        self.tabUpload = CTkButton(win, corner_radius=3, border_width = 2, text = '',image=self.iconUpload, fg_color = "#54AFC3", width = 82, height = 76)
        self.tabUpload.place(x = 1422, y = 18)

    def fctHome(self):
        screenHome.Home(win)

    def fctLimit(self):
        screenLimit.calLimit(win)

if __name__ == "__main__":
    win = CTk()
    app = Home(win)
    win.mainloop()