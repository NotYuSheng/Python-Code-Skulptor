# https://py2.codeskulptor.org/#user45_ZOFfgvlgQM_4.py

# 24/09/18

import simplegui
import math
import random

# Constant values
FRAME_SIZE = 1024, 749
CAR_SIZE = 319, 158
SPAWN_POINT = 105, 438

image1 = simplegui.load_image('https://i.imgur.com/8DLDq8P.png') # Background
image2 = simplegui.load_image('https://i.imgur.com/dbLASBv.png') # Car

# Initial values
angle = 3 * math.pi / 2
angle_vel = 0

ship_image_X = 45

ship_vel_X = 0
ship_vel_Y = 0

ship_X = SPAWN_POINT[0]
ship_Y = SPAWN_POINT[1]
center_dest = [ship_X, ship_Y]

c = 0.01 # Friction / brakes

# Variable declaration
thrust = False

# Ship
def ship_handler(canvas):
    global angle
    global center_dest
    global ship_image_X
    global ship_vel_X, ship_vel_Y
    global ship_X, ship_Y
    # Update angle
    angle += angle_vel
        
    # Thrust logic    
    if thrust == True:
        # Thrust image
        ship_image_X = 135
        # Max vel
        if ship_vel_X < 8 and ship_vel_X > -8:
            ship_vel_X += math.cos(angle) * 0.5
        if ship_vel_Y > -8 and  ship_vel_Y < 8:
            ship_vel_Y += math.sin(angle) * 0.5
    else:
        # Thrust image
        ship_image_X  = 45        
        
    # Update friction
    ship_vel_X *= 1 - c
    ship_vel_Y *= 1 - c

    # Update center_dest
    ship_X += ship_vel_X 
    ship_Y += ship_vel_Y
    center_dest = [ship_X, ship_Y]
            
    # Loop ship
    if ship_X > FRAME_SIZE[0]:
        ship_X = 1
    if ship_X < 1:
        ship_X = FRAME_SIZE[0]
    if ship_Y > FRAME_SIZE[1]:
        ship_Y = 1
    if ship_Y < 0:
        ship_Y = FRAME_SIZE[1]
        
    # Draw ship    
    #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
    canvas.draw_image(image2, (CAR_SIZE[0] / 2, CAR_SIZE[1] / 2), CAR_SIZE, center_dest, (CAR_SIZE[0] / 4, CAR_SIZE[1] / 4), angle)
        
# Background
def background_handler(canvas):
    # Draw background
    canvas.draw_image(image1, (FRAME_SIZE[0] / 2, FRAME_SIZE[1] / 2), FRAME_SIZE, (FRAME_SIZE[0] / 2, FRAME_SIZE[1] / 2), FRAME_SIZE)

def main_handler(canvas):
    # Initializer
    background_handler(canvas)
    ship_handler(canvas)
    
def key_down(key):
    global angle_vel, c, thrust
    if   key == simplegui.KEY_MAP['up']:
        thrust = True
    elif key == simplegui.KEY_MAP['left']:
        angle_vel -= 0.1
    elif key == simplegui.KEY_MAP['down']:
        c = 0.05
    elif key == simplegui.KEY_MAP['right']:
        angle_vel += 0.1
    elif key == simplegui.KEY_MAP['space']:
        print "space"
        
def key_up(key):
    global angle_vel, c, thrust
    global up, left, down, right
    if   key == simplegui.KEY_MAP['up']:
        thrust = False
    elif key == simplegui.KEY_MAP['left']:
        angle_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        c = 0.01
    elif key == simplegui.KEY_MAP['right']:
        angle_vel = 0
    elif key == simplegui.KEY_MAP['space']:
        print "space"
        
frame = simplegui.create_frame('Gas', FRAME_SIZE[0], FRAME_SIZE[1])
frame.set_draw_handler(main_handler)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)

frame.start()
