'''size(1000,1000)
photo = loadImage("thatsprettygood.jpg")
image(photo,0,0,990,540)
'''
#print("Hey, that's pretty good!")


from random import *
x = 0
y = 0
speed =4
verticaldir = True # true means go up
horizontaldir = True # true means go right and false means go left
def setup():
    size(800,700)
    fill(0,0,0)
    frameRate(120)
def draw():
    global x
    global y
    global horizontaldir
    global verticaldir
    global speed
    background(255)
    noStroke()
    ellipse(x,y,100,100)
    '''photo = loadImage("thatsprettygood.jpg")
    image(photo, x, y, 100, 100)'''
    if x >= 750:# if it reaches to the end of the screen to the right
        horizontaldir = False
        speed = randint(1,20)
        fill(randint(0,255),randint(0,255),randint(0,255))
    if y >= 650:
        verticaldir = False
        speed = randint(1,20)
        fill(randint(0,255),randint(0,255),randint(0,255))
    if x <= 50:
        horizontaldir = True
        speed = randint(1,20)
        fill(randint(0,255),randint(0,255),randint(0,255))
    if y <= 50:
        verticaldir = True
        speed = randint(1,20)
        #fill(randint(0,255),randint(0,255),randint(0,255))
    if horizontaldir == True:
        x = x + speed
    else: 
        x = x - speed
    if verticaldir == True:
        y = y + speed
    else: 
        y = y - speed
    
    
   