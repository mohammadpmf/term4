from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class MyGame():
    def __init__(self, root, bg='gray', fg=None, fg2='black', text=None, font=None, bd=None, labelanchor=None, relief=None, abg=None, afg=None, padx=0, pady=0):
        self.combo_style = ttk.Style()
        self.combo_style.theme_create('combostyle', parent='alt',settings = {'TCombobox':{'configure':{'selectbackground': bg,'fieldbackground': bg,'background': bg}}})
        self.combo_style.theme_use('combostyle')
        self.combo_style.map('TCombobox', fieldbackground=[('readonly', bg)])
        self.combo_style.map('TCombobox', selectbackground=[('readonly', bg)])
        self.combo_style.map('TCombobox', selectforeground=[('readonly',  fg2)])

        self.root               = root
        self.frame              = LabelFrame(self.root, bg=bg, fg=fg2, text=text, font=font, labelanchor=labelanchor)
        self.l_name             = Label(self.frame, text="Game Name: ", bg=bg, fg=fg, font=font, bd=bd, padx=padx*2, pady=pady*2)
        self.l_company          = Label(self.frame, text="Company: ", bg=bg, fg=fg, font=font, bd=bd, padx=padx, pady=pady)
        self.l_age              = Label(self.frame, text="Age Classification: ", bg=bg, fg=fg, font=font, bd=bd, padx=padx, pady=pady)
        self.l_price            = Label(self.frame, text="Price: ", bg=bg, fg=fg, font=font, bd=bd, padx=padx, pady=pady)
        self.l_console_type     = Label(self.frame, text="Console: ", bg=bg, fg=fg, font=font, bd=bd, padx=padx, pady=pady)
        self.l_remained         = Label(self.frame, text="Amount Remained: ", bg=bg, fg=fg, font=font, bd=bd, padx=padx, pady=pady)
        self.l_address          = Label(self.frame, text="Picture Address: ", bg=bg, fg=fg, font=font, bd=bd, padx=padx, pady=pady)

        self.e_name             = Entry(self.frame, bg=bg, fg=fg2, font=font, bd=bd, insertbackground=fg2)
        self.e_company          = Entry(self.frame, bg=bg, fg=fg2, font=font, bd=bd, insertbackground=fg2)
        self.e_age              = ttk.Combobox(self.frame, values=['', '+3', '+7', '+10', '+12', '+15', '+17', '+25'], foreground=fg2, justify='center', font=font, state='readonly')
        self.e_price            = Entry(self.frame, bg=bg, fg=fg2, font=font, bd=bd, insertbackground=fg2)
        self.e_console_type     = Entry(self.frame, bg=bg, fg=fg2, font=font, bd=bd, insertbackground=fg2)
        self.e_remained         = Entry(self.frame, bg=bg, fg=fg2, font=font, bd=bd, insertbackground=fg2)
        self.e_address          = Button(self.frame, bg=bg, fg=fg2, font=font, bd=bd, text='...', command=self.seak_picture)

        self.l_name             .grid(row=1,  column=1, sticky='news', padx=padx, pady=pady)
        self.l_company          .grid(row=3,  column=1, sticky='news', padx=padx, pady=pady)
        self.l_age              .grid(row=5,  column=1, sticky='news', padx=padx, pady=pady)
        self.l_price            .grid(row=7,  column=1, sticky='news', padx=padx, pady=pady)
        self.l_console_type     .grid(row=9,  column=1, sticky='news', padx=padx, pady=pady)
        self.l_remained         .grid(row=11, column=1, sticky='news', padx=padx, pady=pady)
        self.l_address          .grid(row=13, column=1, sticky='news', padx=padx, pady=pady)

        self.e_name             .grid(row=1,  column=3, sticky='news', padx=padx, pady=pady)
        self.e_company          .grid(row=3,  column=3, sticky='news', padx=padx, pady=pady)
        self.e_age              .grid(row=5,  column=3, sticky='news', padx=padx, pady=pady)
        self.e_price            .grid(row=7,  column=3, sticky='news', padx=padx, pady=pady)
        self.e_console_type     .grid(row=9,  column=3, sticky='news', padx=padx, pady=pady)
        self.e_remained         .grid(row=11, column=3, sticky='news', padx=padx, pady=pady)
        self.e_address          .grid(row=13, column=3, sticky='news', padx=padx, pady=pady)

    def seak_picture(self):
        try:
            self.file_address = filedialog.askopenfilename()
            if self.file_address in [None, (), '']:
                self.file_address = None
                self.e_address.config(text='...', image='')
                return
            self.img = Image.open(self.file_address)
            self.img = self.img.resize((200, 200))
            self.img = ImageTk.PhotoImage(self.img)
            self.e_address.config(image=self.img)
        except:
            self.file_address = None
            self.e_address.config(text='...', image='')
            

    def grid(self, *args, **kwargs):
        self.frame.grid(*args, **kwargs)

    def place(self, *args, **kwargs):
        self.frame.place(*args, **kwargs)

    def pack(self, *args, **kwargs):
        self.frame.pack(*args, **kwargs)


class AddGame(MyGame):
    def __init__(self, root, bg=None, fg=None, fg2=None, text=None, font=None, bd=None, labelanchor=None, relief=None, abg=None, afg=None, padx=None, pady=None):
        super().__init__(root, bg, fg, fg2, text, font, bd, labelanchor, relief, abg, afg, padx, pady)
        self.btn_save  = Button(self.frame, text='Save', font=font, bg=bg, fg=fg2, relief=relief, activebackground=abg, activeforeground=afg,)
        self.btn_reset = Button(self.frame, text='Reset', font=font, bg=bg, fg=fg2, relief=relief, activebackground=abg, activeforeground=afg,)
        self.btn_save  .grid(row=101, column=1, sticky='news', padx=padx, pady=pady)
        self.btn_reset .grid(row=101, column=3, sticky='news', padx=padx, pady=pady)
