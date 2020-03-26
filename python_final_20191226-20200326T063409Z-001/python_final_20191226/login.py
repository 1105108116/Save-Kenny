# login.py
from tkinter import *
from tkinter import messagebox
import db.db
#import dashboard
import KHK
#import playgame

class LoginWindow:
    def __init__(self):
        self.win = Tk()
        # reset the window and background color
        self.canvas = Canvas(self.win,
                             width=600, height=500,
                             bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("Login Stage")

    def add_frame(self):
        self.frame = Frame(self.win, height=500, width=600)
        self.frame.place(x=0, y=0)

        x, y = 70, 20

        self.img = PhotoImage(file='login.png')
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x+100, y=y+0)

        # now create a login form
        self.label = Label(self.frame, text="Player Login")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=200, y=y+280)

        self.uidlabel = Label(self.frame, text="User ID:")
        self.uidlabel.config(font=("Courier", 12, 'bold'))
        self.uidlabel.place(x=150, y=y+320)

        self.userid = Entry(self.frame, font='Courier 12')
        self.userid.place(x=270, y=y+320)

        self.pwdlabel = Label(self.frame, text="Password:")
        self.pwdlabel.config(font=("Courier", 12, 'bold'))
        self.pwdlabel.place(x=150, y=y+350)

        self.password = Entry(self.frame, show='*',
                              font='Courier 12')
        self.password.place(x=270, y=y+350)

        self.button = Button(self.frame, text="Login",
                             font='Courier 15 bold',
                             command=self.login)
        self.button.place(x=270, y=y+400)

        self.win.mainloop()

    def login(self):
        # get the data and store it into tuple (data)
        data = (
            self.userid.get(),
            self.password.get()
        )
        # validations
        if self.userid.get() == "":
            messagebox.showinfo("Alert!","Enter UserID First")
        elif self.password.get() == "":
            messagebox.showinfo("Alert!", "Enter Password First")
        else:
            res = db.db.user_login(data)
            #userid = playgame.Player
            if res:
                messagebox.showinfo("Message", "Login Successfully")
                self.win.destroy()
                #x = dashboard.DashboardWindow()
                #x = KHK.main(data)
                KHK.main(data)
            else:
                messagebox.showinfo("ALert!", "Wrong username/password")