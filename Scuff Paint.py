# https://py2.codeskulptor.org/#user45_pAzlT111Mb_5.py

# 6/11/18

import simplegui

radius = 1
color = "Black"

dots = []

def mouseclick_handler(pos):
    X = pos[0] 
    Y = pos[1]
    dots.append([X, Y, radius, color])
    
def mousedrag_handler(drag_pos):
    X = drag_pos[0] 
    Y = drag_pos[1]
    dots.append([X, Y, radius, color])
    
class Dot():
    def draw(self, canvas, pos_X, pos_Y, radius, color):
        self.pos_X  = pos_X
        self.pos_Y  = pos_Y
        self.radius = radius
        self.color  = color
        canvas.draw_circle((self.pos_X, self.pos_Y), self.radius, 1, self.color)
    
def draw_handler(canvas):
    # Draw dots
    a = len(dots)
    my_list = range(0, a, 1)
    for i in my_list:
        pos_X  = dots[i][0]
        pos_Y  = dots[i][1]
        radius = dots[i][2]
        color  = dots[i][3]
        Dot().draw(canvas, pos_X, pos_Y, radius, color)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Scuff Paint", 500, 500)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouseclick_handler)
frame.set_mousedrag_handler(mousedrag_handler)


frame.start()
