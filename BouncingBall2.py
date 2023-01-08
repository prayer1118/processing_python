if 0: 
    from Processing3 import *
from random import *



class Ball():
    def __init__(self):
        print(self)
        self.x=randint(0,width)
        self.y=randint(0,height)
        self.r=randint(10,50)
        self.rc=randint(0,256)
        self.gc=randint(0,256)
        self.bc=randint(0,256)
        self.xs=randint(-10,30)
        self.ys=randint(-10,30)
    
    def circle(self):
        fill(self.rc,self.gc,self.bc)
        ellipse(self.x,self.y,self.r*2,self.r*2)
    
    def move(self):
        self.x=self.x+self.xs
        self.y=self.y+self.ys
        if self.x>=width-self.r:
            self.x=width-self.r
            self.xs=self.xs*-1
        elif self.x<=self.r:
            self.x=self.r
            self.xs=self.xs*-1
        
        if self.y>=height-self.r:
            self.y=height-self.r
            self.ys=self.ys*-1
        elif self.y<self.r:
            self.y=self.r
            self.ys=self.ys*-1
        

def setup():
    global balls
    size(1920,1080)
    balls=[]
    for _ in range(1,101):
        global balls
        
        ball=Ball()
        balls.append(ball)
        

def draw():
    global balls
    fill(0,30)
    rect(0,0,width,height)
    for ball2 in balls:
        ball2.circle()
        ball2.move()

        




