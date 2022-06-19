# https://py2.codeskulptor.org/#user45_Z9HkqLNEsR_2.py

import simplegui
import math

box   = []

image1 = simplegui.load_image('https://i.imgur.com/uBue4s9.gif') # Bomberman sprite
image2 = simplegui.load_image('https://i.imgur.com/vcBeMys.png') # Boxes


class Objects:
    def draw(self, canvas):
        a = len(box)
        my_list1 = range(0,a,1)
        for i in my_list1:
            self.box_X = box[i][0] * 50 + 25
            self.box_Y = box[i][1] * 50 + 25
            canvas.draw_image(image2, (47 / 2, 44 / 2), (47, 44), (self.box_X, self.box_Y), (50, 50))

def draw_handler(canvas):
    # Grid Temorary
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
        
    # Objects
    Objects().draw(canvas)
    
    # Bomberman facing up
    canvas.draw_image(image1, (9.5 + 17 * 6, 15), (18, 30), (425, 325), (18 * 2, 30 * 2))

    
frame = simplegui.create_frame('Bomberman', 800, 600)
frame.set_canvas_background('White')
frame.set_draw_handler(draw_handler)


frame.start()
