# http://www.codeskulptor.org/#user45_dZLE3DUBfE_18.py

# 29/09/18

import simplegui
import math

image1 = simplegui.load_image('https://i.imgur.com/znztn3y.png') # Cash Register
image2 = simplegui.load_image('https://i.imgur.com/rQKODLi.png') # Keypad
image3 = simplegui.load_image('https://i.imgur.com/oLRG8fu.jpg') # People


def click(pos):
    print pos


class People:
    def __init__(self, center_source, width_height_source, center_dest, width_height_dest):
        self.center_source       = center_source
        self.width_height_source = width_height_source
        self.center_dest         = center_dest
        self.width_height_dest   = width_height_dest
        
    def draw_people(self, canvas):
        canvas.draw_image(image3, self.center_source, self.width_height_source, self.center_dest, self.width_height_dest)


def main():
    global red_shirt, black_shirt
    # Red shirt
    red_shirt   = People((60, 70), (120, 140), (200, 200), (60 * 5, 70 * 5))
    # Black shirt
    #black_shirt = People((150, 80), (70 , 130), (200, 200), (50 * 4, 75 * 4))
        
def draw(canvas):    
    #canvas.draw_line(point1, point2, line_width, line_color)
    
    
    red_shirt.draw_people(canvas)
    #black_shirt.draw_people(canvas)
    
    canvas.draw_line((0, 400), (1200, 400), 1, 'Black')
    #canvas.draw_image(image3, (60, 70), (120, 140), (200, 200), (60 * 5, 70 * 5)) # Red shirt

    #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
    canvas.draw_image(image1, (492 / 2, 454 / 2), (492, 454), (550, 560), (492, 454))
    canvas.draw_image(image2, (562 / 2, 771 / 2), (562, 771), (620, 600), (562 / 5, 771 / 5))
    canvas.draw_image(image2, (562 / 2, 771 / 2), (562, 771), (1000, 400), (562 / 1.5, 771 / 1.5))


main()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Convenient Store Simulator", 1200, 800)
frame.set_canvas_background('White')
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
