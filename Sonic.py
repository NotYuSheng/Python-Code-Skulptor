# https://py2.codeskulptor.org/#user45_xuzZWrN6Hz_83.py

# sprite from Techokami https://www.spriters-resource.com/game_boy_advance/sonicthehedgehoggenesis/sheet/8892/
# sonic from SEGA
# project started on: 28/09/18
# Yu Sheng

import simplegui
import math

image1 = simplegui.load_image('https://i.imgur.com/etclt6v.png') # Sonic (Right)
image2 = simplegui.load_image('https://i.imgur.com/SWWcAof.png') # Sonic (Left)
image3 = simplegui.load_image('https://i.imgur.com/UmX586z.png') # Foreground
image4 = simplegui.load_image('https://i.imgur.com/KhTjDu4.png') # Background

# Default stance
current_image             = image1
current_center_source     = 48 / 2, 48 / 2
current_width_height      = 48, 48
current_width_height_dest = 48 * 2, 48 * 2

# Spawn location
pos_X = 50
pos_Y = 350

# Default Declaration
pos_X_vel = 0
pos_Y_vel = 0
feet_X = pos_X
feet_Y = pos_Y + 25

# Default declaration
right = False
left = False
up = False
down = False
space = False
gravity = False
grounded = True
check_ground = False

# Animation
animation_speed = 150
jump = 0
slowdown = 0
stride = 0

"""
print "timer1: ", timer1.is_running()
print "timer2: ", timer2.is_running()
print "timer3: ", timer3.is_running()
print "timer4: ", timer4.is_running()
print "timer5: ", timer5.is_running()
print "timer6: ", timer6.is_running()
print "timer7: ", timer7.is_running()
print "timer8: ", timer8.is_running()
print "timer9: ", timer9.is_running()
print "-----------------"
"""


# Patiences timer
def timer1_handler():
    global patience
    patience = 0
    timer2.start()

# Patience animation
def timer2_handler():
    timer1.stop()
    global current_center_source 
    global patience
    
    # Right
    if   current_image == image1:
        current_center_source = 24 + 48 + 48 * patience, 24         
    # Left
    elif current_image == image2:
        current_center_source = 24 + 48 * 9 - 48 * patience, 24 
    
    # Loop
    if patience == 3:
        patience = 1
    patience += 1
    
# Running animation
def timer3_handler():
    global animation_speed, stride
    global current_center_source
        
    # Right
    if   current_image == image1:
        current_center_source = 24 + 48 * (stride + 1), 24 + 48 * 3
        # Animation
        if pos_X_vel < 10:
            if stride == 4:
                stride = -1
        elif stride >= 8:
            stride = 4     
    # Left
    elif current_image == image2:
        current_center_source = 24 + 48 * 10 - (stride + 1)* 48, 24 + 48 * 3
        # Animation
        if pos_X_vel > - 10:
            if stride == 4:
                stride = -1
        elif stride >= 8:
            stride = 4
    stride += 1

# In air spin animation
def timer4_handler():
    global current_center_source, jump
    timer3.stop()
    # Right
    if current_image == image1: 
        current_center_source = 24 + 48 * 9 - 48 * jump, 24 
    # Left
    elif current_image == image2:
        current_center_source = 24 + 48 + 48 * jump, 24
    # Loop
    if jump == 3:
        jump = -1
    jump += 1
        
# Max jump time
def timer5_handler():
    timer6.start()
    timer5.stop()
    
# Decelerate in air upwards
def timer6_handler():
    global check_ground, gravity , grounded
    global pos_Y_vel
    # Decelerate until vel = 0
    if pos_Y_vel < 8:
        pos_Y_vel += 1
    else:
        if grounded == False:
            check_ground = True
            pos_Y_vel = 8
        else:
            timer6.stop()

# Decelerate in air downwards
def timer7_handler():
    global pos_Y_vel
    # Accelerate to top fall speed
    if pos_Y_vel < 8 and grounded == False:
        pos_Y_vel += 1
    else:
        timer7.stop()
        
# Horizontal deceleration
def timer8_handler():
    global current_center_source, current_image
    global pos_X_vel
    global slowdown
    if pos_X_vel > 10 or pos_X_vel < - 10:
        # Right
        if   current_image == image1:
            if   pos_X_vel > 0:
                pos_X_vel -= 1
                current_center_source = 24 + 48 * 6 + slowdown * 48, 24 + 48
            elif pos_X_vel < 0:
                current_image = image1
            else:
                timer8.stop()
                slowdown = 0
        # Left
        elif current_image == image2:
            if   pos_X_vel < 0:
                pos_X_vel += 1
                current_center_source = 24 + 48 * 3 + slowdown * 48, 24 + 48
            else:
                timer8.stop()
                slowdown = 0
            if   slowdown == 0:
                slowdown += 1
            else:
                slowdown = 0
        if   slowdown == 0:
            slowdown += 1
        else:
            slowdown = 0
    else:
        # Right
        if   current_image == image1:
            current_center_source     = 48 / 2      , 48 / 2
        # Left
        elif current_image == image2:
            current_center_source     = 48 * 10 + 24, 48 / 2
        pos_X_vel = 0
        timer8.stop()
        slowdown = 0

# Vertical acceleration        
def timer9_handler():
    global animation_speed
    global current_center_source
    global pos_X_vel
        
    # Right
    if   current_image == image1:
        # Max Speed
        if pos_X_vel < 20:
            # Increase speed
            pos_X_vel += 1
            # For running animation
            animation_speed -= 1
    # Left
    elif current_image == image2:
        # Max speed
        if pos_X_vel > - 20:
            # Increase speed
            pos_X_vel -= 1
            # For running animation
            animation_speed -= 1

# Draw Sonic
class draw_sonic:
    # Class unnecessary change to function BOOKMARK
    def __init__(self):
        self.image             = current_image
        self.center_source     = current_center_source
        self.width_height      = current_width_height
        self.width_height_dest = current_width_height_dest
        
    def draw(self, canvas):
        global feet_Y, pos_X, pos_Y
        feet_Y = pos_Y + 25
        pos_X += pos_X_vel
        pos_Y += pos_Y_vel
        canvas.draw_image(self.image, (self.center_source), (self.width_height), (pos_X, pos_Y), (self.width_height_dest))

def draw_handler(canvas):
    global current_center_source, current_image
    global pos_X, pos_X_vel, pos_Y_vel
    global stride
    global grounded, check_ground
    
    # Jump
    if space == True and grounded == True:
        grounded = False
        pos_Y_vel -= 8
        # Jump animation
        timer4.start()
        # Jump
        timer5.start()
    
    # Brake if both right and left being pressed
    if right == True and left == True:
        # Only show brake animation if not mid-air
        if jump != True:
            if timer4.is_running == False:
                # Brake animation
                timer3.stop()
        # Decelerate
        timer8.start()
        
    # Move right
    elif right == True:
        if pos_X_vel > - 10 and pos_X_vel < 0:
            pos_X_vel = 0
        # If still moving left
        if pos_X_vel < 0:
            timer8.start()
            # After stopping timer3 reset stride
            timer3.stop()
            stride = 0
        else:
            current_image = image1
            # First stride
            if timer3.is_running() == False and timer9.is_running() == False:
                stride = 0
                pos_X_vel += 1
                current_center_source = 48 / 2, 48 * 3 + 24 
            # Jumping animation
            if space == True:
                # Stop running animation
                # After stopping timer3 reset stride
                timer3.stop()
                stride = 0
                # Acceleration
                timer9.start()
                # Start in air spin animation
                timer4.start()
            # Running animation
            else:
                if timer3.is_running() == False:
                    if pos_X_vel >= 10:
                        stride = 4
                # Running animation
                timer3.start()
                # Acceleration
                timer9.start()

    # Move left
    elif left == True:
        if pos_X_vel > 0 and pos_X_vel < 10:
            pos_X_vel = 0
        # If still moving right
        if pos_X_vel > 0:
            timer8.start()
            # After stopping timer3 reset stride
            timer3.stop()
            stride = 0
        else:
            current_image = image2
            # First stride
            if timer3.is_running() == False and timer9.is_running() == False:
                stride = 0
                pos_X_vel -= 1
                current_center_source = 48 / 2 + 48 * 10, 48 * 3 + 24
            # Jumping animation
            if space == True:
                # Stop running animation
                # After stopping timer3 reset stride
                timer3.stop()
                stride = 0
                # Acceleration
                timer9.start()
                # Start in air spin animation
                timer4.start()
            # Running animation
            else:        
                if timer3.is_running() == False:
                    if pos_X_vel <= -10:
                        stride = 4
                # Running animation
                timer3.start()
                # Acceleration
                timer9.start()
    

        
    # Look up
    elif up == True and right == False and left == False and down == False and space == False and pos_X_vel == 0 and grounded == True:
        # Right
        if   current_image == image1:
            current_center_source = 24 + 5 * 48, 24
        # Left
        elif current_image == image2:
            current_center_source = 24 + 5 * 48, 24
            
    # Look down
    elif up == False and right == False and left == False and down == True and space == False and pos_X_vel == 0 and grounded == True:
        # Right
        if   current_image == image1:
            current_center_source = 24 + 48 * 10, 24 + 48 * 3
        # Left
        elif current_image == image2:
            current_center_source = 24, 24 + 48 * 3
    
    # If no key is pressed and moving
    if up == False and right == False and left == False and down == False and space == False and pos_X_vel != 0:
        # Right
        if   pos_X_vel > 0:
            pos_X_vel -= 1
        # Left
        elif pos_X_vel < 0:
            pos_X_vel += 1
        
    # Idle
    if up == False and right == False and left == False and down == False and space == False and pos_X_vel == 0 and pos_Y_vel == 0:
        # Patience timer
        timer1.start()
        # Stop running animation
        # After stopping timer3 reset stride
        timer3.stop()
        stride = 0
        # Stop acceleration
        timer9.stop()
        if timer2.is_running() == False:
            # Right
            if   current_image == image1:
                current_center_source     = 48 / 2      , 48 / 2
            # Left
            elif current_image == image2:
                current_center_source     = 48 * 10 + 24, 48 / 2
    else:
        timer1.stop()
        timer2.stop()
        
    # Loop Sonic
    if pos_X < 0:
        pos_X = 625
    elif pos_X > 625:
        pos_X = 0        
        
    # Check ground
    if check_ground == True:
        if feet_Y < 375:
            grounded = False
        else:
            # Stop air spin animation
            timer4.stop()
            # Stop downward air deceleration
            timer6.stop()
            pos_Y_vel = 0
            grounded = True
            check_ground = False
        
    # Draw Background
    canvas.draw_image(image4, (625 / 2, 448 / 2), (625, 448), (625 , 448 ), (625 * 2, 448 * 2))
    
    # Draw Foreground BOOKMARK
    #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
    canvas.draw_image(image3, (347 , 168), (264, 160), (625 / 2 , 448 / 2), (264 * 2, 160 * 2))        
    canvas.draw_image(image3, (54, 127), (90, 82), (625.0 / 2, 135), (90 * 2, 82 * 2))

    # Draw Sonic
    draw_sonic().draw(canvas)

def keydown_handler(key):
    global right, left, up, down, space
    if   key == simplegui.KEY_MAP['right']:
        right = True
    elif key == simplegui.KEY_MAP['left']:
        left = True
    elif key == simplegui.KEY_MAP['up']:
        up = True
    elif key == simplegui.KEY_MAP['down']:
        down = True
    elif key == simplegui.KEY_MAP['space']:
        space = True
        
def keyup_handler(key):
    global right, left, up, down, space
    if   key == simplegui.KEY_MAP['right']:
        right = False
    elif key == simplegui.KEY_MAP['left']:
        left = False
    elif key == simplegui.KEY_MAP['up']:
        up = False
    elif key == simplegui.KEY_MAP['down']:
        down = False
    elif key == simplegui.KEY_MAP['space']:
        space = False

frame = simplegui.create_frame('Sonic', 625, 448)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)        
        
timer1 = simplegui.create_timer(3000, timer1_handler)
timer2 = simplegui.create_timer(500, timer2_handler)
timer3 = simplegui.create_timer(animation_speed, timer3_handler)
timer4 = simplegui.create_timer(50, timer4_handler)
timer5 = simplegui.create_timer(300, timer5_handler)
timer6 = simplegui.create_timer(50, timer6_handler)
timer7 = simplegui.create_timer(100, timer7_handler)
timer8 = simplegui.create_timer(40, timer8_handler)
timer9 = simplegui.create_timer(animation_speed, timer9_handler)

frame.start()        
