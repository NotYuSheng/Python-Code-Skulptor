# https://py2.codeskulptor.org/#user45_zB7LBmJ4Jd_82.py

# 24/09/18

import simplegui
import math
import random

# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
image1 = simplegui.load_image('https://i.imgur.com/s2bbkiW.png') # Background
image2 = simplegui.load_image('https://i.imgur.com/xoozlF5.png') # Moving Background
image3 = simplegui.load_image('https://i.imgur.com/Uosja1u.png') # Ship
image4 = simplegui.load_image('https://i.imgur.com/mEjUsd1.png') # Bullet
image5 = simplegui.load_image('https://i.imgur.com/dgoxHi3.png') # Asteroid
image6 = simplegui.load_image('https://i.imgur.com/a3MQ1ae.png') # Explosion

# Background
Background1_X = 400
Background2_X = -400
Background_vel = 0.5

# Initial values
angle = 0
angle_vel = 0

ship_image_X = 45

ship_vel_X = 0
ship_vel_Y = 0

ship_X = 400
ship_Y = 300
center_dest = [ship_X, ship_Y]

c = 0.01 # Friction / brakes

asteroid = []

# Variable declaration
thrust = False

def timer_handler():
    # Max asteroids
    if len(asteroid) <= 5:
        center_dest = [random.randint(100, 700), random.randint(100, 600)]
        angle       = random.randint(-50, 50)
        angle_vel   = random.randint(-50, 50)
        X_vel       = random.choice([-0.5, -0.25, 0.25, 0.5])
        Y_vel       = random.choice([-0.5, -0.25, 0.25, 0.5])
        asteroid.append([center_dest, angle, angle_vel, X_vel, Y_vel])
        random.randint(100, 700)

class Asteroid:
    def asteroid_handler(self, canvas):
        a = len(asteroid)
        my_list = range(0, a, 1)
        for i in my_list:
            # Variable declaration
            self.center_dest = asteroid[i][0]
            self.angle       = asteroid[i][1]
            self.angle_vel   = asteroid[i][2]
            self.X_vel       = asteroid[i][3]
            self.Y_vel       = asteroid[i][4]
            
            # Update
            self.center_dest[0] += self.X_vel
            self.center_dest[1] += self.Y_vel
            # Angle spin not working
            # BOOKMARK
            self.angle          += self.angle_vel
            
            # Loop asteroid
            if self.center_dest[0] > 800:
                self.center_dest[0] = 1
            if self.center_dest[0] < 1:
                self.center_dest[0] = 799
            if self.center_dest[1] > 600:
                self.center_dest[1] = 1
            if self.center_dest[1] < 0:
                self.center_dest[1] = 599
                
            # Draw asteroid
            canvas.draw_image(image5, (90 / 2, 90 /2), (90, 90), self.center_dest, (90, 90), self.angle)

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
    if ship_X > 800:
        ship_X = 1
    if ship_X < 1:
        ship_X = 799
    if ship_Y > 600:
        ship_Y = 1
    if ship_Y < 0:
        ship_Y = 599
        
    # Draw ship    
    canvas.draw_image(image3, (ship_image_X, 90 / 2), (90, 90), center_dest, (90, 90), angle)
        
# Background
def background_handler(canvas):
    global Background1_X, Background2_X
    # Draw background
    canvas.draw_image(image1, (800 / 2, 600 / 2), (800, 600), (800 / 2, 600 / 2), (800, 600))
    
    # Update background
    Background1_X += Background_vel
    Background2_X += Background_vel
    
    # Loop background
    if Background1_X  == 1200:
        Background1_X = -400
    if Background2_X == 1200:
        Background2_X = -400
    
    # Draw moving background
    canvas.draw_image(image2, (640 / 2, 480 / 2), (640, 480), (Background1_X, 600 / 2), (800, 600))
    canvas.draw_image(image2, (640 / 2, 480 / 2), (640, 480), (Background2_X, 600 / 2), (800, 600))
    
def main_handler(canvas):
    # Initializer
    background_handler(canvas)
    ship_handler(canvas)
    Asteroid(asteroid).asteroid_handler(canvas)
    
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
        
frame = simplegui.create_frame('Asteroids', 800, 600)
frame.set_draw_handler(main_handler)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
timer = simplegui.create_timer(1000, timer_handler)

timer.start()
frame.start()
