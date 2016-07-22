ship_move = 0
FIRE = 525
alienx = 65
alienx1 = 65
alieny = 20
alieny1 = 120
Bullet = False
BULLETX = ship_move + 37.5
BULLETY = 525


def setup():
    background(0,0,0)
    size(600,600)
    frameRate(120)
        
def keyPressed():
    global ship_move
    global SHIP
    global Bullet, BULLETX
    print("pressed %s %d" % (key,keyCode))
    if keyCode == 39 and ship_move < 600 - 80:
        ship_move += 20
    if keyCode == 37 and ship_move > 0:
        ship_move -= 20
    if keyCode == 32:
        BULLETX = ship_move + 37.5
        Bullet = True
def draw():
    global ship_move
    global FIRE
    global Bullet, BULLETX, BULLETY
    global alienx
    global alienx1
    global alieny
    global alieny1
    
    background(0)
    noStroke()
    fill(255,0,0)
    rect(ship_move,550,80,30)
    rect(ship_move+30,535,20,15)
    if Bullet == True:
        fill(255,0,0)
        rect(BULLETX,BULLETY,5,10)
        
        BULLETY -= 10
        if BULLETY < 0:
            Bullet = False
            BULLETY = 525
    #ENEMIES
    for x in range(5):
        fill(0,255,0)
        rect(alienx+100*x,alieny,55,55) #change the (20) value = more aliens
        rect(alienx1+100*x,alieny1,55,55)
        
        
    #SHIP
    fill(255,0,0)
    rect(ship_move, 550, 80, 30) 
    
            
        
    
        