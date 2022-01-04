from tkinter import *
from tkinter import messagebox


class B(Frame):
    img_6 = None
    img_7 = None
    img_8 = None
    img_2 = None
    img = None
    img_1 = None
    button_1 = None
    text = None
    background_label = None
    img_3 = None
    img_4 = None
    img_5 = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.geometry('1080x1080')
        master.resizable(False, False)
        self.pack()

        B.img = PhotoImage(file="Screens/ask_card.png")
        B.img2 = PhotoImage(file="r_b.png")
        B.img_1 = PhotoImage(file="Screens/pin.png")
        B.img_2 = PhotoImage(file="Screens/home.png")
        B.img_3 = PhotoImage(file="Screens/ask_c_nuber.png")
        B.img_4 = PhotoImage(file="Screens/ask_p_number.png")
        B.img_5 = PhotoImage(file="Screens/choice_func.png")
        B.img_6 = PhotoImage(file="Screens/ask_money.png")
        B.img_7 = PhotoImage(file="Screens/complite.png")
        B.img_8 = PhotoImage(file="Screens/ask_summ_money.png")

        """
        Экран вставь карту
        """
        B.background_label = Label(master, image=B.img)
        B.background_label.image = B.img
        B.background_label.pack(fill='both', expand=True)

        """
        Кнопки управления экран
        """
        B.button_1 = Button(B.background_label, image=B.img2, highlightthickness=0, bd=0, bg="#7d7c7c",
                            activebackground="#7d7c7c", command=B.choise_screen_1)
        B.button_1.image = B.img2
        B.button_1.place(x=83, y=289, heigh=47, width=47)

        B.button_2 = Button(B.background_label, image=B.img2, highlightthickness=0, bd=0, bg="#7d7c7c",
                            activebackground="#7d7c7c", command=B.choise_screen_2)
        B.button_2.image = B.img2
        B.button_2.place(x=83, y=515, heigh=47, width=47)

        B.button_3 = Button(B.background_label, image=B.img2, highlightthickness=0, bd=0, bg="#7d7c7c",
                            activebackground="#7d7c7c", command=B.exit_b)
        B.button_3.image = B.img2
        B.button_3.place(x=83, y=740, heigh=47, width=47)

        button_4 = Button(B.background_label, image=B.img2, highlightthickness=0, bd=0, bg="#7d7c7c",
                          activebackground="#7d7c7c", command=B.choise_screen_3)
        button_4.image = B.img2
        button_4.place(x=947, y=289, heigh=47, width=47)

        button_5 = Button(B.background_label, image=B.img2, highlightthickness=0, bd=0, bg="#7d7c7c",
                          activebackground="#7d7c7c", command=B.choise_screen_4)
        button_5.image = B.img2
        button_5.place(x=947, y=515, heigh=47, width=47)

        button_6 = Button(B.background_label, image=B.img2, highlightthickness=0, bd=0, bg="#7d7c7c",
                          activebackground="#7d7c7c", command=B.help)
        button_6.image = B.img2
        button_6.place(x=947, y=740, heigh=47, width=47)

    @staticmethod
    def help():
        if B.background_label.image == B.img_2:
            messagebox.showinfo("HELP", "Проверьте чат с поддержкой в приложении на вашем телефоне.")
        else:
            pass

    @staticmethod
    def enter_menu_click():
        """
        Нажатие кнопки enter
        """
        try:
            if B.background_label.image == B.img_1:
                if len(str(B.text.get())) < 4 or not str(B.text.get()).isdigit():
                    messagebox.showinfo("PIN", "Неверный PIN")
                    B.text.destroy()
                    B.ask_pin_screen()
                else:
                    B.text.destroy()
                    B.background_label.configure(image=B.img_2)
                    B.background_label.image = B.img_2
            elif B.background_label.image == B.img_3:
                if 7 < len(str(B.text.get())) < 12 and str(B.text.get()).isdigit():
                    B.text.destroy()
                    B.background_label.configure(image=B.img_8)
                    B.background_label.image = B.img_8
                    B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0)
                    B.text.place(height=40, x=387, y=600)
                    A.entry_(B.text)
                else:
                    messagebox.showinfo("CARD NUMBER", "Неверный номер карты")
                    A.button_clear()
            elif B.background_label.image == B.img_8:
                if 1 < len(str(B.text.get())) and str(B.text.get()).isdigit():
                    B.text.destroy()
                    B.succsess()
                else:
                    messagebox.showinfo("ERROR", "Неверная сумма")
                    A.button_clear()
            elif B.background_label.image == B.img_4:
                if 0 < len(str(B.text.get())) and str(B.text.get())[0] == '+':
                    B.text.destroy()
                    B.background_label.configure(image=B.img_8)
                    B.background_label.image = B.img_8
                    B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0)
                    B.text.place(height=40, x=387, y=600)
                    A.entry_(B.text)
                else:
                    messagebox.showinfo("CARD NUMBER",
                                        "Неверный номер телефона. Введите номер в международном формате начиная с '+'")
                    A.button_clear()
        except AttributeError:
            pass

    @staticmethod
    def succsess():
        B.background_label.configure(image=B.img_7)
        B.background_label.image = B.img_7
        messagebox.showinfo('INF', 'Спасибо за выбор нашего банка! Нажмите CANCEL.')

    @staticmethod
    def ask_pin_screen():
        """
        Экраан спросить пароль
        """
        B.background_label.configure(image=B.img_1)
        B.background_label.image = B.img_1
        B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0, show='*')
        B.text.place(height=40, x=387, y=600)
        A.entry_(B.text)

    @staticmethod
    def choise_screen_1():
        """
        Экран выбора действия оплата итд
        """

        try:
            if B.background_label.image == B.img_2:
                B.text.destroy()
                B.button_1.configure(command=None)
                B.background_label.configure(image=B.img_3)
                B.background_label.image = B.img_3
                B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0)
                B.text.place(height=40, x=387, y=600)
                A.entry_(B.text)
            elif B.background_label.image == B.img_5:
                B.text.destroy()
                B.background_label.configure(image=B.img_4)
                B.background_label.image = B.img_4
                B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0)
                B.text.place(height=40, x=387, y=600)
                A.entry_(B.text)
            else:
                pass
        except AttributeError:
            pass

    @staticmethod
    def choise_screen_2():
        """
        Выбор оплты телефона и налогов
        """
        try:
            if B.background_label.image == B.img_2:
                B.background_label.configure(image=B.img_5)
                B.background_label.image = B.img_5
            elif B.background_label.image == B.img_5:
                B.text.destroy()
                B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0)
                B.text.place(height=40, x=387, y=600)
                A.entry_(B.text)
                B.background_label.configure(image=B.img_4)
                B.background_label.image = B.img_4
            else:
                pass

        except AttributeError:
            pass

    @staticmethod
    def choise_screen_3():
        try:
            if B.background_label.image == B.img_2:
                B.text.destroy()
                B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0)
                B.text.place(height=40, x=387, y=600)
                A.entry_(B.text)
                B.background_label.configure(image=B.img_8)
                B.background_label.image = B.img_8
            elif B.background_label.image == B.img_5:
                B.text.destroy()
                B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0)
                B.text.place(height=40, x=387, y=600)
                A.entry_(B.text)
                B.background_label.configure(image=B.img_4)
                B.background_label.image = B.img_4
            else:
                pass

        except AttributeError:
            pass

    @staticmethod
    def choise_screen_4():
        """
        Выбор оплты телефона и налогов
        """
        try:
            if B.background_label.image == B.img_2:
                B.text.destroy()
                B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0)
                B.text.place(height=40, x=387, y=600)
                A.entry_(B.text)
                B.background_label.configure(image=B.img_6)
                B.background_label.image = B.img_6
            elif B.background_label.image == B.img_5:
                B.text.destroy()
                B.text = Entry(B.background_label, font='Helvetica 19', justify=CENTER, bd=0)
                B.text.place(height=40, x=387, y=600)
                A.entry_(B.text)
                B.background_label.configure(image=B.img_4)
                B.background_label.image = B.img_4
            else:
                pass

        except AttributeError:
            pass

    @staticmethod
    def exit_b():
        """
        3-я кнопка выход на нек-х экранах
        :return:
        """
        try:
            if B.background_label.image == B.img_5 or B.background_label.image == B.img_2:
                A.exit()
            else:
                pass
        except AttributeError:
            pass


class A(B):
    current = 0
    entry = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.geometry('540x1080')
        master.resizable(False, False)
        self.pack()

        bgs = []
        for step in range(1, 13):
            lnk = 'LOADC ' + str(step) + '.png'
            bgs.append(lnk)
        self.bgs = bgs
        self.img = PhotoImage(file="KEYB.png")
        self.background = Label(master, image=self.img)
        self.background.pack(fill='both', expand=True)
        self.create_buttons()

    def create_buttons(self):
        img = PhotoImage(file="Buttons/CANCEL.png")
        button_CAN = Button(self.background, image=img, highlightthickness=0, bd=0, command=A.exit)
        button_CAN.image = img
        button_CAN.place(x=315, y=87, width=64)

        img = PhotoImage(file="Buttons/CLEAR.png")
        button_CLE = Button(self.background, image=img, highlightthickness=0, bd=0, command=A.button_clear)
        button_CLE.image = img
        button_CLE.place(x=315, y=144, width=64)

        img = PhotoImage(file="Buttons/ENTER.png")
        button_ENT = Button(self.background, image=img, highlightthickness=0, bd=0, command=B.enter_menu_click)
        button_ENT.image = img
        button_ENT.place(x=315, y=199, width=64)

        img = PhotoImage(file="Buttons/B_.png")  # do nothing
        button_CLE = Button(self.background, image=img, highlightthickness=0, bd=0)
        button_CLE.image = img
        button_CLE.place(x=315, y=255, width=64)

        img = PhotoImage(file="Buttons/B1.png")
        button_b1 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('1'))
        button_b1.image = img
        button_b1.place(x=145, y=87)

        img = PhotoImage(file="Buttons/B2.png")
        button_b2 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('2'))
        button_b2.image = img
        button_b2.place(x=202, y=87)

        img = PhotoImage(file="Buttons/B3.png")
        button_b3 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('3'))
        button_b3.image = img
        button_b3.place(x=256, y=87)

        img = PhotoImage(file="Buttons/B4.png")
        button_b4 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('4'))
        button_b4.image = img
        button_b4.place(x=145, y=144)

        img = PhotoImage(file="Buttons/B5.png")
        button_b5 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('5'))
        button_b5.image = img
        button_b5.place(x=202, y=144)

        img = PhotoImage(file="Buttons/B6.png")
        button_b6 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('6'))
        button_b6.image = img
        button_b6.place(x=256, y=144)

        img = PhotoImage(file="Buttons/B7.png")
        button_b7 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('7'))
        button_b7.image = img
        button_b7.place(x=145, y=199)

        img = PhotoImage(file="Buttons/B8.png")
        button_b8 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('8'))
        button_b8.image = img
        button_b8.place(x=202, y=199)

        img = PhotoImage(file="Buttons/B9.png")
        button_b9 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('9'))
        button_b9.image = img
        button_b9.place(x=256, y=199)

        img = PhotoImage(file="Buttons/B(-).png")
        button_b11 = Button(self.background, image=img, highlightthickness=0, bd=0,
                            command=lambda: A.button_click('-'))
        button_b11.image = img
        button_b11.place(x=145, y=255)

        img = PhotoImage(file="Buttons/B0.png")
        button_b0 = Button(self.background, image=img, highlightthickness=0, bd=0,
                           command=lambda: A.button_click('0'))
        button_b0.image = img
        button_b0.place(x=202, y=255)

        img = PhotoImage(file="Buttons/B(+).png")
        button_b12 = Button(self.background, image=img, highlightthickness=0, bd=0,
                            command=lambda: A.button_click('+'))
        button_b12.image = img
        button_b12.place(x=256, y=255)

        button_money = Button(self.background, bg="#252b29", activebackground="#404241",
                              highlightthickness=0, bd=0, command=A.btton_money)
        button_money.image = img
        button_money.place(x=117, y=443, width=302)

        button_card = Button(self.background, bg="#252b29", activebackground="#404241",
                             highlightthickness=0, bd=0)
        button_card.image = img
        button_card.place(x=302, y=599, width=176, height=28)

        def button_card_f():
            loading()
        if B.background_label.image == B.img:
            button_card.configure(command=button_card_f)

        def loading(i=1):
            if i < 10:
                img0 = self.bgs
                st = 'Loads/' + img0[i]
                img7 = PhotoImage(file=st)
                self.background.configure(image=img7)
                self.background.image = img7
                self.background.after(10, loading, i+1)
            else:
                self.background.configure(image=self.img)
                self.background.image = self.img
                B.ask_pin_screen()
                button_card.destroy()

    @classmethod
    def entry_(cls, entry):
        cls.entry = entry
        cls.current = entry.get()

    @classmethod
    def button_click(cls, number):
        if B.background_label.image == B.img_1:
            try:
                if B.background_label.image == B.img_1:
                    if len(str(cls.entry.get())) < 4:
                        cls.entry.insert(6, str(cls.current) + str(number))
                    else:
                        messagebox.showinfo("PIN", "Неверный PIN")
                        B.text.destroy()
                        B.ask_pin_screen()
                else:
                    if len(str(cls.entry.get())) < 10:
                        cls.entry.insert(12, str(cls.current) + str(number))
                    else:
                        messagebox.showinfo("CARD NUMBER", "Неверный номер карты")
                        cls.current = ''
            except AttributeError:
                pass
        else:
            cls.entry.insert(6, str(cls.current) + str(number))

    @staticmethod
    def button_clear():
        try:
            A.entry.delete(0, END)
        except AttributeError:
            pass

    @staticmethod
    def exit():
        exit()

    @staticmethod
    def btton_money():
        if B.background_label.image == B.img_6:
            B.succsess()
