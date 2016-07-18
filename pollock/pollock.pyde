from random import *
def setup():
    size(1000,600)
    
def draw():
    rect(mouseX ,mouseY,randrange(1,100),randrange(1,100))
    fill(randrange(255),randrange(255),randrange(255))