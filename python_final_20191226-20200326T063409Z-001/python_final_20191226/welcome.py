# welcome.py
from tkinter import *
import login

class WelcomeWindow:
    #create a constructor
    def __init__(self):
        # create a tkinter window
        self.win = Tk()

        #reset the window and baackground color
        self.canvas = Canvas(self.win,
                             width=1600, height=1200,
                             bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        #show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width/2-600/2)
        y = int(height/2-400/2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        #disable resize of the window
        self.win.resizable(width=False, height=False)

        #change the title of the window
        self.win.title("Welcome to our game!!!")

    def add_frame(self):
        #create a inner frame
        self.frame = Frame(self.win, height=600, width=900)
        self.frame.place(x=0, y=0)

        x, y = 70, 20
        self.img = PhotoImage(file='welcome(1).png')
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x-30, y=y-10)

        # place the photo in the frame
        # you can find the images from flaticon.com site
     

        #self.labeltitle = Label(self.frame, text="阿尼躲刀")
        #self.labeltitle.config(font=("Courier", 35, 'bold'))
        #self.labeltitle.place(x=120, y=y+50)

        self.button = Button(self.frame, text="Continue",
                             font=('helvetica', 20, 'underline italic'),
                             bg='dark blue', fg='white',
                             command=self.login)
        self.button.place(x=x+160, y=y+300)

        self.win.mainloop()

    #open a new window on button press
    def login(self):
        # destroy current window
        self.win.destroy()

        #open the new window
        log = login.LoginWindow()
        log.add_frame()


if __name__ == "__main__":
    x = WelcomeWindow()
    x.add_frame()