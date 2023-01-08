if 0: 
    from Processing3 import *


def setup():
    global pos, vel, wind_acc, grvity_acc
    size(1920,1080)
    pos=PVector(100,300)
    vel= PVector(0,0)


def draw():
    global pos,vel, wind_acc, grvity_acc

    pointer = PVector(mouseX, mouseY)
    vector = pointer - pos
    vector.normalize()
    vel = vel + vector
    if vel.mag() >= 10:
        vel.normalize()
        vel.mult(10)

    pos = pos + vel



    ellipse(pos.x,pos.y,10,10)