import sympy as sym
from customtkinter import *
from tkinter import messagebox, filedialog
from PIL import Image

class calLimit:
    def __init__(self, win):
        

        self.win = win
        win.configure(fg_color = '#B48989')
        win.geometry('1560x988')

        CTkLabel(win, corner_radius=8, text = "",fg_color = '#FF9A7A', width = 1515, height = 858).place(x = 23, y = 113)
        CTkLabel(win, corner_radius=8, text = "", width = 1042, height = 774).place(x = 277, y = 150)


        CTkLabel(win, corner_radius=8, text = "Chọn Cận", font = ('Times new roman', 25), fg_color = '#C59FF5', text_color = 'Black', width = 263, height = 70).place(x = 374, y = 305)

        self.selected_option = StringVar()
        self.selected_option.set('-')
        self.options = ['-','+']
        self.option_menu = CTkOptionMenu(win, font = ('Times new roman', 25), corner_radius = 10, variable = self.selected_option,  values = self.options, hover = True, button_hover_color = '#4287f5', text_color = 'black', width = 172, height = 70)
        self.option_menu.place(x = 1038, y = 305)

        self.radio_var1 = StringVar()
        self.radio_var1.set('cận 1 phía')
        self.options2 = ['cận 1 phía', 'cận 2 phía']
        self.can_value = CTkOptionMenu(win, font = ('Times new roman', 25), corner_radius= 10, variable = self.radio_var1,  values = self.options2, hover = True, button_hover_color = '#4287f5', text_color = 'black', width = 276, height = 70)
        self.can_value.place(x = 658, y = 305)

        self.expression_label = CTkLabel(win, corner_radius = 10, text = "Hàm f(x)", font = ('Times new roman', 25), fg_color = '#C59FF5', text_color = 'Black', width = 263, height = 70)
        self.expression_label.place(x = 374, y = 192)
        self.expression_entry = CTkTextbox(win, corner_radius=6, font = ('Times new roman', 25), text_color = 'Black', width = 552, height = 70)
        self.expression_entry.place(x = 658, y = 192)

        self.output = CTkTextbox(win, corner_radius = 10, font = ('Times New Roman', 25), height = 309, width = 552)
        self.output.configure(text_color = 'black', fg_color = "white")
        self.output.place(x = 658, y = 531)

        self.file = CTkTextbox(win, corner_radius = 10, font = ('Times New Roman', 25), height = 82, width = 186)
        self.file.configure(text_color = 'black', fg_color = "white")
        self.file.place(x = 1338, y = 152)

        #expression = expression_entry.get()
        self.x0 = StringVar()
        CTkLabel(win, corner_radius= 10, text = "Giá trị limit", font = ('Times new roman', 25), fg_color = '#C59FF5', text_color = 'Black', width = 263, height = 70).place(x = 374, y = 418)
        CTkEntry(win, corner_radius= 10, textvariable = self.x0, font = ('Times new roman', 25), text_color = 'Black', fg_color = 'white', width = 276, height = 70).place(x = 658, y = 418)
        #type_can = on_radio_button_select()

        self.limit_button = CTkButton(win, corner_radius = 10, text = "Kết Quả", command = self.compute_Limit, font = ('Times new roman', 25), fg_color = '#C59FF5', text_color = 'Black', width = 263, height = 110, hover = True, hover_color='#37a4de', border_color = '#37a4de', border_width = 3)
        self.limit_button.place(x = 374, y = 531)

        self.exit_button = CTkButton(win, corner_radius = 10, text = "Thoát", command = self.Exit, font = ('Times new roman', 25), fg_color = '#C6E8B1', text_color = 'Black', width = 217, height = 89, hover = True, hover_color='#37a4de', border_color = '#37a4de', border_width = 3)
        self.exit_button.place(x = 39, y = 261)

        self.iconUpload = CTkImage(light_image = Image.open('asset/iconUpload.jpg'), size = (83, 77))
        self.upload = CTkButton(win, image = self.iconUpload, corner_radius = 10, text = "", command = self.upFile, font = ('Times new roman', 25), fg_color = '#C6E8B1', text_color = 'Black', width = 83, height = 77, hover = True, hover_color='#37a4de', border_color = '#37a4de', border_width = 3)
        self.upload.place(x = 1422, y = 20)

        self.help_button = CTkButton(win, corner_radius = 10, text = "Help", font = ('Times new roman', 25), fg_color = '#C6E8B1', text_color = 'Black', width = 217, height = 89, hover = True, hover_color='#37a4de', border_color = '#37a4de', border_width = 3)
        self.help_button.place(x = 39, y = 148)


        if os.path.isfile("calLimit/expression.txt") == True and os.path.isfile("calLimit/resultLimit.txt") == True:
            pre_express = open("calLimit/expression.txt", "r")
            self.expression_entry.insert(INSERT, pre_express.read())
            pre_result = open("calLimit/resultLimit.txt", "r")
            text="Giới hạn của hàm số: " + pre_result.read()
            self.output.insert(INSERT, text)
    def compute_Limit(self):
        try:
            expr = open("calLimit/expression.txt", "w")
            result = open("calLimit/resultLimit.txt", "w")
            self.output.delete("1.0", "end")
            type_can = self.radio_var1.get()
            x = sym.symbols('x')
            expression = self.expression_entry.get("1.0", "end")
            expr.write(expression)
            if (str(type_can) == 'cận 1 phía'):
                integral = sym.limit(expression, x, int(self.x0.get()), str(self.selected_option.get()))
                text="Giới hạn của hàm số: " + str(integral)
                self.output.insert(INSERT, text)
                result.write(str(integral))
            if (str(type_can) == 'cận 2 phía'):
                integral = sym.limit(expression, x, int(self.x0.get()))
                text="Giới hạn của hàm số: " + str(integral)
                self.output.insert(INSERT, text)
                result.write(str(integral))
        except:
            messagebox.showerror('Error', 'Kiểm tra lại đầu vào!')
    def upFile(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = file_path.split("/")[-1]
            express = open(file_path, "r")

            self.file.delete("1.0", "end")
            self.file.insert(INSERT, file_name)

            self.expression_entry.delete("1.0", "end")
            self.expression_entry.insert(INSERT, express.read())
        
    def Exit(self):
        os.remove("calLimit/expression.txt")
        os.remove("calLimit/resultLimit.txt")
        exit()

if __name__ == "__main__":
    win = CTk()
    app = calLimit(win)
    win.mainloop()
