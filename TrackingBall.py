if 0: 
    from Processing3 import *

from random import randint

class Ball():
    def __init__(self,id):
        self.id=id
        self.pos=PVector(100,200)
        self.color=color(randint(0,255),randint(0,255),randint(0,255))
    
    def update(self,tVec):
        cVec=tVec-self.pos
        cmag=cVec.mag()
        cVec.normalize()
        cVec.mult(cmag/10.0)
        self.pos.add(cVec)
        
        fill(self.color)
        ellipse(self.pos.x,self.pos.y,20,20)        

def setup():
    global balls
    noStroke()
    size(1920,1080)

    balls=[]
    for num in range(0,31):
        ball=Ball(num)
        balls.append(ball)
    
def draw():
    global balls
    fill(0, 20)
    rect(0,0,width,height)

    # tVec=PVector(mouseX,mouseY)
    # ball.update(tVec)

    for ball in balls:
        if ball.id==0:
            tVec=PVector(mouseX,mouseY)
            ball.update(tVec)
        else:
            prevBall=balls[ball.id-1]
            tVec=prevBall.pos
            ball.update(tVec)
        

    
