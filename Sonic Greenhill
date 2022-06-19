# https://py2.codeskulptor.org/#user45_UVNnhWEpMY_182.py

# sprite from Techokami https://www.spriters-resource.com/game_boy_advance/sonicthehedgehoggenesis/sheet/8892/
# sonic from SEGA
# project started on: 25/09/18
# project paused on: 28/09/18
# Yu Sheng

import simplegui
import math

image1 = simplegui.load_image('https://i.imgur.com/etclt6v.png') # Sonic (Right)
image2 = simplegui.load_image('https://i.imgur.com/SWWcAof.png') # Sonic (Left)
image3 = simplegui.load_image('https://i.imgur.com/7o0CIdH.jpg') # Background

# Default stance
current_image             = image1
current_center_source     = 48 / 2, 48 / 2
current_width_height      = 48, 48
current_width_height_dest = 48 * 2, 48 * 2

gravity = False
pos_X = 50
pos_X_vel = 0
pos_Y = 500
pos_Y_vel = 0
feet_X = pos_X
feet_Y = pos_Y + 25
animation_speed = 150
grounded = True

priority_stand = False
priority_jump = False

stride = 0
jump = 0
slowdown = 0

points = [(1191 / 2, 670 / 2)]
ground = [[0,597],[101,586],[184,593],[255,587],[346,588],[376,576],[446,570]
         ,[554,518],[675,509],[980,509],[1119,439],[1191,438]]

# Prevent ghosting
left = False
right = False
anti_ghosting = False

# BOOKMARK Temporary
def click(pos):
    if pos != points[-1]:
        points.append(pos)
        print "Next point:", pos

# Patiences timer
def timer1_handler():
    global patience
    patience = 0
    patience_right = 1
    timer2.start()
    
# Patience animation
def timer2_handler():
    timer1.stop()
    global current_center_source, patience
    global priority_stand
    priority_stand = True
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
    global animation_speed, current_center_source, pos_X_vel, stride
    global priority_stand, priority_jump
    priority_stand = True
    # Only run animation if not jumping
    if priority_jump == False:
        # Right
        if current_image == image1: 
            current_center_source = 24 + 48 * (stride + 1), 24 + 48 * 3
            # Max Speed
            if pos_X_vel < 20:
                # Increase speed
                pos_X_vel += 1
                animation_speed -= 1
            # Animation
            if pos_X_vel < 10:
                if stride == 4:
                    stride = -1
            elif stride == 8:
                stride = 4
        # Left
        elif current_image == image2:
            current_center_source = 24 + 48 * 10 - (stride + 1)* 48, 24 + 48 * 3
            # Max speed
            if pos_X_vel > - 20:
                # Increase speed
                pos_X_vel -= 1
                animation_speed -= 1
            # Animation
            if pos_X_vel > - 10:
                if stride == 4:
                    stride = -1
            elif stride == 8:
                stride = 4
        stride += 1

# In air spin animation
def timer4_handler():
    global current_center_source, jump
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
    global gravity, pos_Y_vel
    # Decelerate until vel = 0
    if pos_Y_vel < 0:
        pos_Y_vel += 1
    else:
        gravity = True
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
    global current_center_source, pos_X_vel, priority_stand, slowdown
    priority_stand = True
    if pos_X_vel > 10 or pos_X_vel < - 10:
        # Right
        if   current_image == image1:
            if   pos_X_vel > 0:
                pos_X_vel -= 1
                current_center_source = 24 + 48 * 6 + slowdown * 48, 24 + 48
            else:
                timer8.stop()
                priority_stand = False
                slowdown = 0
        # Left
        elif current_image == image2:
            if   pos_X_vel < 0:
                pos_X_vel += 1
                current_center_source = 24 + 48 * 3 + slowdown * 48, 24 + 48
            else:
                timer8.stop()
                priority_stand = False
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
        pos_X_vel = 0
        timer8.stop()
        priority_stand = False
        slowdown = 0
    
class draw_sonic:
    def __init__(self):
        self.image             = current_image
        self.center_source     = current_center_source
        self.width_height      = current_width_height
        self.width_height_dest = current_width_height_dest
        
    def draw(self, canvas):
        global pos_X, pos_Y
        pos_X += pos_X_vel
        pos_Y += pos_Y_vel
        canvas.draw_image(self.image, (self.center_source), (self.width_height), (pos_X, pos_Y), (self.width_height_dest))
        
def draw_handler(canvas):
    global feet_X, feet_Y, gravity, grounded, pos_X, pos_Y_vel
    global current_center_source
    global priority_stand, priority_jump
    feet_X = pos_X
    feet_Y = pos_Y + 25
    
    if grounded == False and gravity == True:
        timer4.start()
        a = len(ground)
        my_list = range(0, a, 1)
        for i in my_list:
            if i+1 < len(ground):
                # Up slope
                if feet_X >= ground[i][0] and feet_X <= ground[i+1][0] and (feet_Y >= ground[i][1] and feet_Y >= ground [i+1][1]):
                    gravity = False
                    grounded = True
                    pos_Y_vel = 0
                    priority_jump = False
                    priority_stand = False
                # Down slope
                elif feet_X <= ground[i][0] and feet_X >= ground[i+1][0] and feet_Y >= ground[i][1] and feet_Y >= ground [i+1][1]:
                    gravity = False
                    grounded = True
                    pos_Y_vel = 0
                    priority_jump = False
                    priority_stand = False
    
    # BOOKMARK NOT WORKING
    if grounded == True and priority_stand == True and priority_jump == False:
        a = len(ground)
        my_list = range(0, a, 1)
        for i in my_list:
            if i+1 < len(ground):
                # Up slope
                if feet_Y < ground[i][1]:
                    feet_Y = ground[i]
                # Down slope
                elif feet_Y > ground[i][1]:
                    feet_Y = ground[i]
                    
    
    if grounded == True and priority_stand == False:
        timer4.stop()
        priority_jump = False
        if   current_image == image1:
            current_center_source     = 48 / 2, 48 / 2
        elif current_image == image2:
            current_center_source     = 48 * 10 + 24, 48 / 2
    
    if gravity == True:
        timer7.start()
        if grounded == True:
            gravity = False
    
    if feet_Y >= 670:
        feet_X = 0
        feet_Y = 0
    
    # Loop Sonic
    if pos_X < 0:
        pos_X = 1190
    elif pos_X > 1190:
        pos_X = 0

    # Draw Background
    canvas.draw_image(image3, (1191 / 2, 670 / 2), (1191, 670), (1191 / 2, 670 / 2), (1191, 670))

    # Draw Sonic
    draw_sonic().draw(canvas)

def keydown_handler(key):
    global current_center_source, current_image, current_width_height
    global anti_ghosting, left, right
    global pos_X, pos_X_vel, pos_Y, pos_Y_vel
    global grounded, priority_stand, priority_jump
    timer1.stop()
    timer2.stop()
    if   key == simplegui.KEY_MAP['right'] and anti_ghosting == False:
        priority_stand = True
        current_image = image1
        current_center_source = 48 / 2, 48 * 3 + 24 
        pos_X_vel += 1
        right = True
        anti_ghosting = True
        timer3.start()
        
    elif key == simplegui.KEY_MAP['left'] and anti_ghosting == False:
        priority_stand = True
        current_image = image2
        current_center_source = 48 / 2 + 48 * 10, 48 * 3 + 24 
        pos_X_vel -= 1
        left = True
        anti_ghosting = True
        timer3.start()
        
    elif key == simplegui.KEY_MAP['up']:
        priority_stand = True
        # Right
        if   current_image == image1:
            current_center_source = 24 + 5 * 48, 24
        # Left
        elif current_image == image2:
            current_center_source = 24 + 5 * 48, 24
    
    elif key == simplegui.KEY_MAP['space']:
        priority_stand = True
        priority_jump = True
        if grounded == True:
            grounded = False
            pos_Y_vel -= 8
            # After stopping timer3 reset stride
            timer3.stop()
            stride = 0
            # Animation
            timer4.start()
            # Jump
            timer5.start()
            
    elif key == simplegui.KEY_MAP['down']:
        priority_stand = True
        # Right
        if   current_image == image1:
            current_center_source = 24 + 48 * 10, 24 + 48 * 3
        # Left
        elif current_image == image2:
            current_center_source = 24, 24 + 48 * 3
            
def keyup_handler(key):
    global anti_ghosting, gravity, grounded, left, right, stride, priority_stand
    global current_center_source
    # BOOKMARK CHECK LEFT AND RIGHT KEYUP HANDLERS
    if   key == simplegui.KEY_MAP['right'] and right == True:
        # After stopping timer3 reset stride
        timer3.stop()
        stride = 0
        # Decelerate
        timer8.start()
        # Anti ghost
        right = False
        anti_ghosting = False
        
    elif key == simplegui.KEY_MAP['left'] and left == True:
        # After stopping timer3 reset stride        
        timer3.stop()
        stride = 0
        # Decelerate
        timer8.start()
        # Anti ghost
        left = False
        anti_ghosting = False
        
    elif key == simplegui.KEY_MAP['up']:
        priority_stand = False
        
    elif key == simplegui.KEY_MAP['space']:
        if grounded == False:
            timer6.start()
            timer5.stop()
    elif key == simplegui.KEY_MAP['down']:
        priority_stand = False
    timer1.start()
        
frame = simplegui.create_frame('Sonic', 1191, 670)
frame.set_canvas_background('Black')
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_mouseclick_handler(click)

timer1 = simplegui.create_timer(3000, timer1_handler)
timer2 = simplegui.create_timer(500, timer2_handler)
timer3 = simplegui.create_timer(animation_speed, timer3_handler)
timer4 = simplegui.create_timer(50, timer4_handler)
timer5 = simplegui.create_timer(300, timer5_handler)
timer6 = simplegui.create_timer(50, timer6_handler)
timer7 = simplegui.create_timer(100, timer7_handler)
timer8 = simplegui.create_timer(40, timer8_handler)

timer1.start()
frame.start()
