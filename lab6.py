file = open("file.txt", "w", newline="\n")
from tkinter import *
from random import randrange as rnd, choice
import time
print('YOUR NAME:')
name = str(input())

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
score = 0
Balls = []
speed = [-2, -1, 1, 2]
r=30
class Ball:

    def __init__(self):
        global r
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)

        self.Vx = choice(speed)
        self.Vy = choice(speed)

        self.obj = canv.create_oval(self.x - r, self.y - r, self.x + r,
                                    self.y + r, fill=choice(colors),  tag='ball')

    def Otskok(self):
        if self.x < r or self.x > 800 - r:
            self.Vx = - self.Vx
        if self.y < r or self.y > 600 - r:
            self.Vy = - self.Vy

    def Movement(self):
        self.x = self.x + self.Vx
        self.y = self.y + self.Vy
        canv.move(self.obj, self.Vx, self.Vy)

    def Delete(self):
        canv.delete(self.obj)


def First_create():
    for i in range(4):
        Balls.append(Ball())


def Create():
    Balls.append(Ball())


def moving():
    for i in Balls:
        i.Movement()
        i.Otskok()
    root.after(10, moving)



def New_balls():
    canv.delete('ball')
    First_create()
    moving()


def click(event):
    global score
    for i in Balls:
        if (event.x - i.x) ** 2 + (event.y - i.y) ** 2 < r ** 2:
            score+= 1
            canv.delete('score')
            canv.create_text(350, 50, text='score:' + str(score), font="times 28", tag='score')
            i.Delete()
            Create()

canv.bind('<Button-1>', click)

New_balls()
mainloop()
file.write(name +':' + str(score))

file.close()