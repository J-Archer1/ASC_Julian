from random import *
color_choice = 1
def setup():
    size(600,600)
    background(255,255,255)
    frameRate(120)
def draw():
    #Red
    fill(255,0,0)
    rect(0,0,75,75)
    #Magenta
    fill(255,0,255)
    rect(75,0,75,75)
    #Blue
    fill(0,0,255)
    rect(150,0,75,75)
    #Cyan
    fill(0,255,255)
    rect(225,0,75,75)
    #Green
    fill(0,255,0)
    rect(300,0,75,75)
    #Yellow
    fill(255,255,0)
    rect(375,0,75,75)
    #Orange
    fill(255,165,0)
    rect(450,0,75,75)
    #Random
    fill(randrange(255),randrange(255),randrange(255))
    rect(525,0,75,75)
    stroke(10,10,10,10)
    fill(255,255,255)
    rect(525,75,75,75)
#------------------------------------------------------------------------------
    if mouseButton == LEFT:
        if mouseY >75 and mouseY <150 and mouseX >525:
            global color_choice
            color_choice = 0
            #^^^^^ERASER Button^^^^^
        if mouseY < 75:
            global color_choice
            if mouseX >0 and mouseX <75:
                color_choice = 1
            elif mouseX >75 and mouseX <150:
                color_choice = 2
            elif mouseX >150 and mouseX <225:
                color_choice = 3
            elif mouseX >225 and mouseX <300:
                color_choice = 4
            elif mouseX >300 and mouseX <375:
                color_choice = 5
            elif mouseX >375 and mouseX <450:
                color_choice = 6
            elif mouseX >450 and mouseX <525:
                color_choice = 7
            elif mouseX >525 and mouseX <600:
                color_choice = 8
        else:
            if color_choice == 1:
                noStroke()
                fill(255,0,0)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 2:
                noStroke()
                fill(255,0,255)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 3:
                noStroke()
                fill(0,0,255)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 4:
                noStroke()
                fill(0,255,255)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 5:
                noStroke()
                fill(0,255,0)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 6:
                noStroke()
                fill(255,255,0)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 7:
                noStroke()
                fill(255,165,0)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 8:
                noStroke()
                fill(randrange(255),randrange(255),randrange(255))
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 0:
                noStroke()
                fill(255,255,255)
                rect(mouseX,mouseY,75,75)
             
                 