# https://py2.codeskulptor.org/#user45_Xzx1LC6xiF_18.py

# 07/10/18

import simplegui

# Spawn points
center_point_red  = [75, 300]
center_point_blue = [600 - 75, 300]


# Initial Values
red_vel_X = 0
red_vel_Y = 0

blue_vel_X = 0
blue_vel_Y = 0


# Decleration
w = False
a = False
s = False
d = False

up    = False
left  = False
down  = False
right = False

def main():
    global w, a ,s ,d
    global up, left, down, right
    global red_vel_X,  red_vel_Y
    global blue_vel_X, blue_vel_Y
    if   w == True:
        if red_vel_Y > -8:
            red_vel_Y -= 0.1
    if a == True:
        if red_vel_X > -8:
            red_vel_X -= 0.1     
    if s == True:
        if red_vel_Y < 8:
            red_vel_Y += 0.1  
    if d == True:
        if red_vel_X < 8:
            red_vel_X += 0.1
    if up == True:
        if blue_vel_Y > -8:
            blue_vel_Y -= 0.1
    if left == True:
        if blue_vel_X > -8:
            blue_vel_X -= 0.1        
    if down == True:
        if blue_vel_Y < 8:
            blue_vel_Y += 0.1  
    if right == True:
        if blue_vel_X < 8:
            blue_vel_X += 0.1     
            
# Handler to draw on canvas
def draw(canvas):
    global center_point_red, center_point_blue
    global red_vel_X,  red_vel_Y
    global blue_vel_X, blue_vel_Y    
    # Update
    center_point_red[0]  += red_vel_X
    center_point_red[1]  += red_vel_Y
    
    center_point_blue[0] += blue_vel_X
    center_point_blue[1] += blue_vel_Y
    
    # Collision
    if abs(center_point_red[0] - center_point_blue[0]) < 50 and abs(center_point_red[1] - center_point_blue[1]) < 50:
        if abs(red_vel_X) > abs(blue_vel_X):
            blue_vel_X *= -3
    
    # Red
    #canvas.draw_circle(center_point, radius, line_width, line_color, fill_color = color)
    canvas.draw_circle(center_point_red, 25, 1, "Black", "Red")

    # Blue
    canvas.draw_circle(center_point_blue, 25, 1, "Black", "Blue")
    
    # Ring
    canvas.draw_circle((600 / 2, 600 / 2), 275, 1, "Black")

    # Initialize     
    main()        
    
def keydown_handler(key):
    global w, a ,s ,d
    global up, left, down, right    
    global red_vel_X,  red_vel_Y
    global blue_vel_X, blue_vel_Y
    
    if   key==simplegui.KEY_MAP["w"]:
        w = True
    elif key==simplegui.KEY_MAP["a"]:
        a = True
    elif key==simplegui.KEY_MAP["s"]:
        s = True
    elif key==simplegui.KEY_MAP["d"]:
        d = True
    elif key==simplegui.KEY_MAP["up"]:
        up = True
    elif key==simplegui.KEY_MAP["left"]:
        left = True
    elif key==simplegui.KEY_MAP["down"]:
        down = True
    elif key==simplegui.KEY_MAP["right"]:
        right = True
        
def keyup_handler(key):
    global w, a ,s ,d
    global up, left, down, right
    global red_vel_X, red_vel_Y
    global blue_vel_X, blue_vel_Y
    
    if   key==simplegui.KEY_MAP["w"]:
        w = False
    elif key==simplegui.KEY_MAP["a"]:
        a = False
    elif key==simplegui.KEY_MAP["s"]:
        s = False
    elif key==simplegui.KEY_MAP["d"]:
        d = False

    elif key==simplegui.KEY_MAP["up"]:
        up = False

    elif key==simplegui.KEY_MAP["left"]:
        left = False

    elif key==simplegui.KEY_MAP["down"]:
        down = False

    elif key==simplegui.KEY_MAP["right"]:
        right = False


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ice Sumo", 600, 600)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)


# Start the frame animation
frame.start()
