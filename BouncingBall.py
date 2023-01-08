if 0: 
    from Processing3 import *
from random import *


class Ball():
    def __init__(self):
        self.x=randint(0,width)
        self.y=randint(0,height)
        self.r=randint(10,50)
        self.xs=randint(-5,5)
        self.ys=randint(-5,5)
        self.c=color(randint(0,256),randint(0,256),randint(0,256))
    
    def draw(self):
        fill(self.c)
        noStroke()
        ellipse(self.x,self.y,self.r*2,self.r*2)
    
    def move(self):
        self.x=self.x+self.xs
        self.y=self.y+self.ys
        
    def checkEdge(self):
        if self.x>=width-self.r: 
            self.x=width-self.r
            self.xs=self.xs*-1
        elif self.x<=self.r:
            self.x=self.r
            self.xs=self.xs*-1

        if self.y>=height-self.r:
            self.y=height-self.r
            self.ys=self.ys*-1
        elif self.y<=self.r:
            self.y=self.r
            self.ys=self.ys*-1
        

def setup():
    global balls
    size(1920,1080)
    balls=[]
    for _ in range(1,81):
        ball=Ball()
        balls.append(ball)

def draw():
    global balls
    background(0)

    for ball in balls:
        ball.draw()
        ball.move()
        ball.checkEdge()
    drawText() 


def drawText():
    fill(255)
    txt="Bouncing Ball"
    ts=textWidth(txt)
    font=createFont("Arial bold",100)
    textFont(font)
    text("Bouncing Ball",width/2-(ts/2),height/2)
