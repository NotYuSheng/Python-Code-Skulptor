# https://py2.codeskulptor.org/#user45_xs7Se89kII_98.py

# 24/09/18
# POSSIBLE FEATURES
# add fishes that moves around and blocks the way
# rock flow down river

import simplegui
import math

image1 = simplegui.load_image('https://i.imgur.com/vcBeMys.png') # Background River
image2 = simplegui.load_image('https://i.imgur.com/vvY1Dvq.png') # Background Beach
image3 = simplegui.load_image('https://i.imgur.com/b3faObk.png') # Rock
image4 = simplegui.load_image('https://i.imgur.com/S7CccrF.png') # Log
image5 = simplegui.load_image('https://i.imgur.com/uZjAWx0.png') # Bridge
image6 = simplegui.load_image('https://i.imgur.com/VBxYESA.png') # Monkey
image7 = simplegui.load_image('https://i.imgur.com/8aVRxvq.png') # Drown

river1_Y = 300
river2_Y = 900

rock   = []
boat   = []
bridge = []
monkey = [2, 6]
second = 0

bridge_remaining = 3
live_remaining = 3

status = image6

def timer1_handler():
    # Declare global variables
    global river1_Y, river2_Y
    if river1_Y == -300:
        river1_Y = 900
    else:
        river1_Y -= 1
    if river2_Y == -300:
        river2_Y = 900
    else:
        river2_Y -= 1

def timer2_handler():
    global second
    second += 1
    
def timer3_handler():
    respawn()

def stage1():
    global rock, boat
    rock = [[7, 3], [6, 6], [9, 9]]
    boat = [[5, 0], [7, 5], [9, 11], [9, 10], [9, 0], [10, 0], [8, 3]]

def check():
    global bridge_remaining
    if bridge_remaining > 0:
        if   monkey[0] > 2 and monkey[0] < 13:
            bridge_remaining -= 1
            bridge.append(monkey)
    else:
        drown()
    
def drown():
    global status
    status = image7
    timer3.start() 

def respawn():
    global live_remaining, monkey, status
    if live_remaining > 0:
        live_remaining -= 1
        monkey = [2, 6]
        status = image6
        timer3.stop()
    
class Objects:
    def draw(self, canvas):
        # Draw Rocks
        a = len(rock)
        my_list1 = range(0,a,1)
        for i in my_list1:
            self.rock_X = rock[i][0] * 50 + 25
            self.rock_Y = rock[i][1] * 50 + 25
            canvas.draw_image(image3, (47 / 2, 44 / 2), (47, 44), (self.rock_X, self.rock_Y), (50, 50))
        
        # Draw Boats
        b = len(boat)
        my_list2 = range(0,b,1)
        for i in my_list2:
            self.boat_X = boat[i][0] * 50 + 25
            self.boat_Y = boat[i][1] * 50 + 25
            canvas.draw_image(image4, (47 / 2, 44 / 2), (47, 44), (self.boat_X, self.boat_Y), (50, 50))
        
        # Draw Bridges
        c = len(bridge)
        my_list3 = range(0,c,1)
        for i in my_list3:
            self.bridge_X = bridge[i][0] * 50 + 25
            self.bridge_Y = bridge[i][1] * 50 + 25
            canvas.draw_image(image5, (47 / 2, 44 / 2), (47, 44), (self.bridge_X, self.bridge_Y), (50, 50))
        
        # Draw Monkey
        self.monkey_X = monkey[0] * 50 + 25
        self.monkey_Y = monkey[1] * 50 + 25
        canvas.draw_image(status, (47 / 2, 44 / 2), (47, 44), (self.monkey_X, self.monkey_Y), (50, 50))
         

def draw_handler(canvas):
    # Declare global variables
    
    #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
    # Draw Background
    canvas.draw_image(image1, (663 / 2, 656 / 2), (663, 656), (800 / 2, river1_Y), (600, 600))
    canvas.draw_image(image1, (663 / 2, 656 / 2), (663, 656), (800 / 2, river2_Y), (600, 600))
    canvas.draw_image(image2, (206 / 2, 656 / 2), (206, 656), (80, 600 / 2), (200, 600))
    canvas.draw_image(image2, (206 / 2, 656 / 2), (206, 656), (720, 600/2), (200, 600), math.pi)
    
    # Menu
    #canvas.draw_line(point1, point2, line_width, line_color)
    canvas.draw_image(image6, (47 / 2, 44 / 2), (47, 44), (925, 175), (50, 50))
    canvas.draw_text(str("X " + str(live_remaining)), (950, 180), 20, 'Black')
    canvas.draw_image(image5, (47 / 2, 44 / 2), (47, 44), (925, 275), (50, 50))
    canvas.draw_text(str("X " + str(bridge_remaining)), (950, 280), 20, 'Black')

    # Grid Temorary
    #color = 'Silver'
    color = 'Black'
    #canvas.draw_line(point1, point2, line_width, line_color)
    
    # Horizontal line
    my_list = range(0, 650, 50)
    for i in my_list:
        #canvas.draw_text(text, point, font_size, font_color)
        canvas.draw_text(str((i/50)-1), (30, i), 20, 'Black')
        canvas.draw_line((0, i), (800, i), 1, color)

    # Vertical line
    my_list = range(0, 850, 50)
    for i in my_list:
        canvas.draw_text(str((i/50)), (i, 50), 20, 'Black')
        canvas.draw_line((i, 0), (i, 600), 1, color)
        
    # Draw Objects
    Objects().draw(canvas)
    
    # Draw Clock
    minute = abs(second / 60)
    if minute < 10:
        time_minute = "0" + str(minute)
    else:
        time_minute = str(minute) 
    if(second < 10):
        time_second = "0" + str(second)
    else:
        time_second = str(second)
    time = time_minute + ":" + time_second  
    canvas.draw_text(time, (950, 500), 20, 'Black')

def keyup_handler(key):
    if status == image6:
        if   key == simplegui.KEY_MAP['w']:
            if monkey[1] > 0:
                monkey[1] -= 1
                check()

        elif key == simplegui.KEY_MAP['a']:
            if monkey[0] > 0:
                monkey[0] -= 1
                check()

        elif key == simplegui.KEY_MAP['s']:
            if monkey[1] < 11:
                monkey[1] += 1
                check()

        elif key == simplegui.KEY_MAP['d']:        
            if monkey[0] < 15:
                monkey[0] += 1
                check()

        if   key == simplegui.KEY_MAP['up']:
            if monkey[1] > 0:
                monkey[1] -= 1
                check()

        elif key == simplegui.KEY_MAP['left']:
            if monkey[0] > 0:
                monkey[0] -= 1
                check()

        elif key == simplegui.KEY_MAP['down']:
            if monkey[1] < 11:
                monkey[1] += 1
                check()

        elif key == simplegui.KEY_MAP['right']:        
            if monkey[0] < 15:
                monkey[0] += 1
                check()
    
stage1()

frame = simplegui.create_frame('River Cross', 1100, 600)
frame.set_canvas_background('White')
frame.set_draw_handler(draw_handler)
frame.set_keyup_handler(keyup_handler)
#frame.set_keydown_handler(keydown_handler)
timer1 = simplegui.create_timer(100, timer1_handler)
timer2 = simplegui.create_timer(1000, timer2_handler)
timer3 = simplegui.create_timer(3000, timer3_handler)


timer1.start()
timer2.start()
frame.start()
