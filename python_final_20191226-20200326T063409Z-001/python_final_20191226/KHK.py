# pgImage02.py
import pygame
import os
import random
import math
import db.db
import time
from tkinter import *

tup = ()

class SelectWindow:
    #create a constructor
    
    def __init__(self):
        # create a tkinter window
        self.win = Tk()

        #reset the window and baackground color
        self.canvas = Canvas(self.win,
                             width=600, height=400,
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
        self.win.title("Chose your mode")

    def add_frame(self):
        #create a inner frame
        self.frame = Frame(self.win, height=400, width=600)
        self.frame.place(x=0, y=0)

        x, y = 0, 20

        # place the photo in the frame
        # you can find the images from flaticon.com site
        
        
        self.labeltitle = Label(self.frame, text="選擇你的難易度")
        self.labeltitle.config(font=("Courier", 30, 'bold'))
        self.labeltitle.place(x=140, y=20)
        
        self.labeltitle = Label(self.frame, text="遊戲說明:利用滑鼠控制阿尼移動方向以閃避落下的刀子。")
        self.labeltitle.config(font=("Courier", 16, 'bold'))
        self.labeltitle.place(x=10, y=80)
        
        
        self.labeltitle = Label(self.frame, text="（刀子落到頭部以下位置時不會造成傷害。）")
        self.labeltitle.config(font=("Courier", 16, 'bold'))
        self.labeltitle.place(x=10, y=110)
        
        
        
        self.stan = PhotoImage(file='stan.png')
        self.button = Button(self.frame, 
                             image=self.stan,
                             text="Easy",
                             font=('helvetica', 20, 'underline italic'),
                              fg='green',
                             command=self.easy,
                             bd=0)
        self.button.place(x=25.5, y=y+130)
        self.labeltitle = Label(self.frame, text="Easy")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=54, y=y+336)
        
        
        
        
        
        self.kyle = PhotoImage(file='kyle.png')
        self.button = Button(self.frame, 
                             image=self.kyle,
                             text="Mid",
                             font=('helvetica', 20, 'underline italic'),
                              fg='dark blue',
                             command=self.mid,
                             bd=0)
        self.button.place(x=x+179, y=y+137)
        self.labeltitle = Label(self.frame, text="Mid")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=230, y=y+336)



        self.cartman = PhotoImage(file='cartman.png')
        self.button = Button(self.frame, 
                             image=self.cartman,
                             text="Hard",
                             font=('helvetica', 20, 'underline italic'),
                             fg='red',
                             command=self.hard,
                             bd=0)
        self.button.place(x=x+365.5, y=y+141)
        self.labeltitle = Label(self.frame, text="Hard")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=435, y=y+336)
        
        
        self.win.mainloop()

    #open a new window on button press
    def easy(self):
        global tup
        # destroy current window
        self.win.destroy()

        #open the new window
        maingame(tup,3,"easy",1)
        
    def mid(self):
        global tup
        # destroy current window
        self.win.destroy()

        #open the new window
        maingame(tup,8,"mid",1.5)
        
    def hard(self):
        global tup
        # destroy current window
        self.win.destroy()

        #open the new window
        maingame(tup,15,"hard",2)


def maingame(tup , myknife , level , speed):
    filePath = os.getcwd()
    background_image = filePath + "\\SPBG.jpg"
    mouse_image = filePath + "\\Kenny.png"
    dead_image = filePath + "\\Angel Kenny.png"
    knife_image = filePath + "\\knife.png"
    win_image = filePath +"\\Kenny_win.png"
    width = 960
    height = 540
    Knife_count=1 #initial Knife Count
    Max_Knife_count = myknife
    Knife_session=15
    
    pygame.init()
    screen = pygame.display.set_mode((width,height), 0, 32)
    background = pygame.image.load(background_image).convert()
    mouse_cursor = pygame.image.load(mouse_image).convert_alpha()
    pygame.display.set_caption("阿尼躲刀")
    
    class Knife(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(knife_image).convert_alpha()
            self.rect=self.image.get_rect()
            self.rect.height-=10
        def update(self):
        
            #print("* 移動前 self.rect.centery=", self.rect.centery)
            self.rect.centery += speed
            #print("* 移動後 self.rect.centery=", self.rect.centery)
            if self.rect.centery >= height:
                knife_pos.append(knife_used.pop(0))
                self.rect.centerx = x_generator()
                self.rect.centery = 0
    
    class Kenny(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image= pygame.image.load(mouse_image).convert_alpha()    
            self.rect = self.image.get_rect()
        def update(self,x):
            self.rect.centerx = x if x<(width -83) else width -83
            self.rect.centery = 420
    
    myfont = pygame.font.SysFont("Arial",30)
    
    
    #建立sprite群組
    def x_generator():
        knife_posX = math.floor(random.randrange(0,Knife_session))
        while knife_posX not in knife_pos:
            knife_posX = math.floor(random.randrange(0,Knife_session))
        knife_pos.remove(knife_posX)
        knife_used.append(knife_posX)
        return knife_posX * (width / Knife_session)+80
            
    knife_pos =[]
    knife_used=[]
    for i in range(Knife_session):
        knife_pos.append(i)
    
    def knife_add(knife_list):
        knife_icon=Knife()
        getCenterX = x_generator()
        knife_icon.rect.centerx =  getCenterX
        knife_icon.rect.centery =0
        knife_list.add(knife_icon)
    knife_list = pygame.sprite.Group()
    kenny = Kenny()
    kenny.rect.centerx = width/2
    kenny.rect.centery = 320
    
    for i in range(Knife_count):
        knife_add(knife_list)
    
    clock = pygame.time.Clock()
    
    screen.blit(background, (0,0))
    pygame.display.update()
    
    def animation_update():
        screen.blit(background,(0,0))
        screen.blit(textSurface,(850,10))
        knife_list.draw(screen)
        screen.blit(kenny.image,kenny.rect)
        pygame.display.update()
    
    def dead_animation(kenny):
        kenny.image = pygame.image.load(dead_image).convert_alpha()
        kenny.rect.centerx -=53
        while kenny.rect.top >height/4:
            clock.tick(240)
            kenny.rect.centery-=1
            animation_update()
            
    def win_animation(kenny):
        kenny.image = pygame.image.load(win_image).convert_alpha()
        while kenny.rect.top >height/3:
            clock.tick(300)
            kenny.rect.centery-=1
            animation_update()
    
    done = True
    timer = 0
    cal_time_milliSec = 0
    cal_time = 0
    
    textSurface=myfont.render("Time:0 s",False,(0,0,0))
    while done:  #退出事件處理
        clock.tick(240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
        screen.blit(background, (0,0))  # first layer
        screen.blit(textSurface,(850,10))
        x, y = pygame.mouse.get_pos()
        kenny.update(x)
        knife_list.draw(screen)
        screen.blit(kenny.image,kenny.rect) 
        cal_time_milliSec +=1
        if cal_time_milliSec == 240:
            cal_time +=1
            cal_time_milliSec=0
            textSurface=myfont.render("Time:"+str(cal_time) + " s",False,(0,0,0))
            
            if cal_time==30:  #結束時間
                win_animation(kenny)
                done = False
                
        for knife in knife_list:
            if pygame.sprite.collide_rect(knife,kenny):
                if knife.rect.top + knife.rect.height < kenny.rect.top+20:
                    dead_animation(kenny)
                    done = False
                    screen.blit(background, (0,0))
                    endfont = pygame.font.SysFont("Arial",60)
                    end = endfont.render("Game Over",False,(0,0,0))
                    screen.blit(end,(350,200))
                    
                    
                    
        timer+=1
        if(timer==120 and Knife_count<Max_Knife_count):
             knife_add(knife_list)
             timer =0
             Knife_count+=1
        knife_list.update()
        pygame.display.update()
    mytup = (tup[0] , time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  , cal_time , level)
    db.db.user_record(mytup)
    
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                
    
    pygame.quit()
    



def main(data):
    global tup
    tup = data
    x = SelectWindow()
    x.add_frame()
    
    
if __name__ == "__main__":
    main()
    