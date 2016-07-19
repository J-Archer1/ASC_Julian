from random import *
x = 0
y = 0
paddleX = 0
paddleY = 0
speed =4
verticaldir = True # true means go up
horizontaldir = True # true means go right and false means go left

def start_setup():
    global x
    global y
    global horizontaldir
    global verticaldir
    global speed
    x = 0
    y = 0
    paddleX = 0
    paddleY = 0
    speed =4
    verticaldir = True # true means go up
    horizontaldir = True # true means go right and false means go left

'''
'''
def keyPressed():
    global paddleX
    global paddleY
    print("pressed %s %d" % (key,keyCode))
    if keyCode == 39 and paddleX < 600:
        paddleX += 20
    if keyCode == 37 and paddleX > 0:
        paddleX -= 20
    if keyCode == 68 and paddleY < 600:
        paddleY += 20
    if keyCode == 65 and paddleY > 0:
        paddleY -= 20 
    if keyCode == 82:
        start_setup()
        text("New Game",100,300, 30) 
        
def setup():
    size(800,700)
    fill(0,0,0)
    start_setup()
    frameRate(120)
def draw():
    global x
    global y
    global horizontaldir
    global verticaldir
    global speed
    background(0)
    noStroke()
    fill(255)
    ball =rect(x,y,20,20)
    fill(255,255,255)
    player1 = rect(paddleX,20,200,20)
    player2 = rect(paddleY, 660,200,20)
    player1
    player2
    ball
    '''photo = loadImage("thatsprettygood.jpg")
    image(photo, x, y, 100, 100)'''
    if x >= 780: #if it reaches to the end of the screen to the right
        horizontaldir = False
        #speed = randint(1,20)
        #fill(randint(0,255),randint(0,255),randint(0,255))
    #if y >= 680:
     #   verticaldir = False
      #  speed = randint(1,2)
        #fill(randint(0,255),randint(0,255),randint(0,255))
    if x <= 0:
        horizontaldir = True
        #speed = randint(1,3)
        #fill(randint(0,255),randint(0,255),randint(0,255))
    if y ==40 and (paddleX<x<paddleX+200):#paddleX <= x and paddleX >= x+200:
        verticaldir = True
        speed = randint(2,3)
    elif y <= 40 and paddleX >= x and paddleX+200  <= x:
        verticaldir = False
    
    elif y <= 0:
        textSize(60)
        fill(255,255,255)
        text(" Player 2 Wins! Press (r) \n to restart \n made by Julian Archer",100,300, 30)

    elif paddleX >= x and paddleX + 200 <= x and y <= 35:
        verticaldir = True
    
    if y==640 and (paddleY<x<paddleY+200):
        verticaldir = False
    elif y<= 640 and paddleY >= x and paddleY+200 <= x:
        verticaldir = True
    elif y >= 700:
        textSize(40)
        fill(255)
        text(" Player 1 Wins! Press (r) \n to restart \n made by Julian Archer",100,300,50)
    
    
        
        #fill(randint(0,255),randint(0,255),randint(0,255))
    if horizontaldir == True:
        x = x + 2
    else: 
        x = x - 2
    if verticaldir == True:
        y = y + 2
    else: 
        y = y - 2
    
    
   