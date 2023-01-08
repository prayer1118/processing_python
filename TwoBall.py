if 0: 
    from Processing3 import *

from random import randint

def setup():
    global aVec
    aVec=PVector(100,200)
    size(800,600)



def draw():
    fill(0,40)
    rect(0,0,width,height)

    bVec=PVector(mouseX,mouseY)
    cVec=bVec-aVec
    cmag=cVec.mag()
    cVec.normalize()
    cVec.mult(cmag/10)
    aVec.add(cVec)
    fill(255)
    ellipse(bVec.x,bVec.y,20,20)
    ellipse(aVec.x,aVec.y,20,20)
    

    