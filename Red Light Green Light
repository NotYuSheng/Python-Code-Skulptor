# https://py2.codeskulptor.org/#user45_9WfCpWKlhd_73.py

# 27/09/18 
# Yellow car use   d   to move
# Red    car use right to move
# Blue   car is an AI

import simplegui
import random
import math

image1 = simplegui.load_image('https://i.imgur.com/I8pp3Sp.png') # Cars 
image2 = simplegui.load_image('https://i.imgur.com/qjP6vpI.png') # Road
image3 = simplegui.load_image('https://i.imgur.com/IdfhySH.png') # Checkered Track
image4 = simplegui.load_image('https://i.imgur.com/weLDQso.jpg') # Traffic Light 

clear = 0
light = "red"

p1_vel_X = 0
p2_vel_X = 0
p3_vel_X = 0.5

p1_X = 125 / 2
p2_X = 125 / 2
p3_X = 125 / 2

winner = []
loser  = []

yellow_W = False
red_W	 = False
blue_W   = False

yellow_L = False
red_L	 = False

# 30% to change yellow/green light every 1 second
def timer1_handler():
    global clear, light
    light = "red"
    p1_check_lose()
    p2_check_lose()
    # Stay red for min 1 sec and turn green if 5 seconds went by without red
    if clear > 0 and (clear > 6 or random.randint(1, 10) > 7):
        clear = False
        #light = "yellow"
        timer2.start()
        timer1.stop()
    else:
        clear += 1
         
# 50% to change to red light every 1 second
def timer2_handler():
    global clear, light
    light = "green"
    # Stay green for min 1 sec
    if clear == True and random.randint(1, 10) > 5:
        clear = False
        light = "yellow"
        timer1.start()
        timer2.stop()
    else:
        clear = True

def check_win():
    global winner, yellow_W, red_W, blue_W
    if  p1_X > 565 and yellow_W == False:
        winner.append("Yellow Car")
        yellow_W = True
    if p2_X > 565 and red_W == False:
        winner.append("Red Car")
        red_W = True
    if p3_X > 565 and blue_W == False:
        winner.append("Blue Car")
        blue_W = True
        
def p1_check_lose():
    global loser, yellow_L, red_L, p1_vel_X, p2_vel_X
    if   light == "red" and yellow_W == False:
        if p1_vel_X > 0:
            loser.append("Yellow Car")
            yellow_L = True
            p1_vel_X = 0
        
def p2_check_lose():
    global loser, yellow_L, red_L, p1_vel_X, p2_vel_X
    if light == "red" and red_W == False:
        if p2_vel_X > 0:
            loser.append("Red Car")
            red_L = True
            p2_vel_X = 0        
        
def draw_light(canvas):
    if   light == "red":	 
        canvas.draw_image(image4, (255 / 2, 194 / 2), (255 / 3, 194), (700, 320), (255 / 3, 194))
    elif light == "yellow":
        canvas.draw_image(image4, (45, 194 / 2), (255 / 3, 194), (700, 320), (255 / 3, 194))
    elif light == "green":
        canvas.draw_image(image4, (210, 194 / 2), (255 / 3, 194), (700, 320), (255 / 3, 194))

def draw_cars(canvas):
    global p1_X, p2_X, p3_X
    p1_X += p1_vel_X
    p2_X += p2_vel_X
    p3_X += p3_vel_X
        
    canvas.draw_image(image1, (125 / 2, 172 / 6    ), (125, 172 / 3), (p1_X, 420), (125 * 2, 172 / 3 * 2))
    canvas.draw_image(image1, (125 / 2, 172 / 2    ), (125, 172 / 3), (p2_X, 470), (125 * 2, 172 / 3 * 2))
    canvas.draw_image(image1, (125 / 2, 172 / 6 * 5), (125, 172 / 3), (p3_X, 520), (125 * 2, 172 / 3 * 2))
    canvas.draw_text("POLICE", (p3_X - 30, 540), 20, 'Black')

def draw_results(canvas):
    a = len(winner)
    my_list1 = range(0, a, 1)
    for i in my_list1:
        canvas.draw_text(str(winner[i]), (100 , 100 + 50 * i), 20, 'Black')
    b = len(loser)
    my_list2 = range(0, b, 1)
    for i in my_list2:
        canvas.draw_text("Loser: " + str(loser[i]),  (550 , 100 + 50 * i), 20, 'Black')            
    
def draw(canvas):
    # Check win
    check_win()
    
    # Traffic light
    draw_light(canvas)

    # Road
    canvas.draw_image(image2, (2400 / 2, 722 / 2), (2400, 722), (400, 500), (800, 200))
    
    # Checked Track
    canvas.draw_image(image3, (1920 / 2, 200 / 2), (1920, 200), (700, 500), (200, 50), math.pi/2 )

    # Cars
    draw_cars(canvas)
    
    # Outcome
    draw_results(canvas)
    canvas.draw_text("First : ", (30 , 100 + 50 * 0), 20, 'Black')
    canvas.draw_text("Second: ", (30 , 100 + 50 * 1), 20, 'Black')
    canvas.draw_text("Third : ", (30 , 100 + 50 * 2), 20, 'Black')

def keydown_handler(key):
    global p1_vel_X, p2_vel_X, yellow_L, red_L
    if   key == simplegui.KEY_MAP['d'] and yellow_L == False:
        p1_vel_X += 3
        if light == "red" and yellow_W == False:
            p1_check_lose()
            
    elif key == simplegui.KEY_MAP['right'] and red_L == False:
        p2_vel_X += 3
        if light == "red" and red_W == False:
            p2_check_lose()
    
def keyup_handler(key):
    global p1_vel_X, p2_vel_X
    if   key == simplegui.KEY_MAP['d'] and yellow_L == False:
        p1_vel_X -= 3   
    elif key == simplegui.KEY_MAP['right'] and red_L == False:
        p2_vel_X -= 3    
    
frame = simplegui.create_frame("Red light, Green light", 800, 600)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
timer1 = simplegui.create_timer(1000, timer1_handler)
timer2 = simplegui.create_timer(1000, timer2_handler)

timer1.start()
frame.start()
