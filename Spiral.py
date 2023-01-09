if 0: 
    from Processing3 import *
from random import randint

def setup():
    global angle,length,c,cnum, timer
    size(1920,1080)
    background(0)
    angle=0
    length=-100
    c=0
    cnum=1
    timer=0

def draw():
    global angle,length,c,cnum, timer

    timer = timer+1
    if timer < 500:
        return

    r=20
    noStroke()
    x1=cos(angle)*length
    y1=sin(angle)*length

    x=x1+(width*1/4)
    y=y1+(height*1/4)
    fill(c)
    ellipse(x,y,r,r)

    x=x1+(width*3/4)
    y=y1+(height*1/4)
    fill(c,0,0)
    ellipse(x,y,r,r)

    x=x1+(width*1/4)
    y=y1+(height*3/4)
    fill(0,c,0)
    ellipse(x,y,r,r)

    x=x1+(width*3/4)
    y=y1+(height*3/4)
    fill(0,0,c)
    ellipse(x,y,r,r)
    angle=angle+0.1
    length=length+0.1
    c=c+cnum
    if c>=255:
        cnum=-1
    elif c<=0:
        cnum=1


    


