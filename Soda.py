# https://py2.codeskulptor.org/#user45_SWwrdtDluH_11.py

# Yu Sheng 24/09/18
# Bubbles has an 80% chance to spawn every 0.1 sec
# Clicking spawns a bubble
# Clicking and dragging spawns a bubble at cursor every 0.1 sec

import simplegui
import random

bubbles = []

def bubble_timer1():
    # Declare global variables
    global bubbles
    if len(bubbles) < 20:
        if(random.randint(1, 10) <= 8):
            X = random.randint(3 , 500)
            Y = random.randint(150, 650)
            radius = random.randint(3, 30)
            random_color = random.randint(1, 3)
            if   random_color == 1:
                color = "White"
            elif random_color == 2:
                color = "Silver"
            elif random_color == 3:
                color = "Gray"
            bubbles.append([X, Y, radius, color])

def bubble_timer2():
    X = drag_pos[0] 
    Y = drag_pos[1]
    radius = random.randint(3, 30)
    random_color = random.randint(1, 3)
    if   random_color == 1:
        color = "White"
    elif random_color == 2:
        color = "Silver"
    elif random_color == 3:
        color = "Gray"
    bubbles.append([X, Y, radius, color])
    timer2.stop()
        
def mouseclick_handler(pos):
    X = pos[0] 
    Y = pos[1]
    radius = random.randint(3, 30)
    random_color = random.randint(1, 3)
    if   random_color == 1:
        color = "White"
    elif random_color == 2:
        color = "Silver"
    elif random_color == 3:
        color = "Gray"
    bubbles.append([X, Y, radius, color])
    
def mousedrag_handler(pos):
    global drag_pos
    drag_pos = pos
    timer2.start()
    
def update():
    a = len(bubbles)
    my_list = range(0, a, 1)
    for i in my_list:
        if bubbles[i][1] <= -50:
            bubbles.pop(i)
            break
        else :
            bubbles[i][1] -= 3

class Bubble():
    def draw(self, canvas, pos_X, pos_Y, radius, color):
        self.pos_X  = pos_X
        self.pos_Y  = pos_Y
        self.radius = radius
        self.pos_Y -= 1
        self.color  = color
        canvas.draw_circle((self.pos_X, self.pos_Y), self.radius, 1, self.color)
    
def draw_handler(canvas):
    # Draw Bubbles
    a = len(bubbles)
    my_list = range(0, a, 1)
    for i in my_list:
        pos_X  = bubbles[i][0]
        pos_Y  = bubbles[i][1]
        radius = bubbles[i][2]
        color  = bubbles[i][3]
        Bubble().draw(canvas, pos_X, pos_Y, radius, color)
        
    # Move Bubble
    update()
    
    
frame = simplegui.create_frame('Soda', 500, 600)
frame.set_canvas_background('Maroon')
frame.set_mouseclick_handler(mouseclick_handler)
frame.set_mousedrag_handler(mousedrag_handler)
timer1 = simplegui.create_timer(200, bubble_timer1)
timer2 = simplegui.create_timer(100, bubble_timer2)
frame.set_draw_handler(draw_handler)

timer1.start()

frame.start()
