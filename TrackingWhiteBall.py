if 0: 
    from Processing3 import *

from random import randint


class Ball():
    def __init__(self,id):
        self.pos=PVector(100,200)
        self.id=id
        
    def update(self,tVec):     
        cVec=tVec-self.pos
        cmag=cVec.mag()
        cVec.normalize()
        cVec.mult(cmag/5.0)

        self.pos.add(cVec)      

def setup():
    global balls
    size(1920,1080)
    balls=[]
    for num in range(0,40):
        ball=Ball(num)
        balls.append(ball)

def draw():
    background(0)
    global balls
    for ball in balls:
        if ball.id==1:
            ball.update(PVector(mouseX,mouseY))               
        else:
            ball.update(balls[ball.id-1].pos)
        ellipse(ball.pos.x,ball.pos.y,20,20)
    
                



    
    

        
        
        
        