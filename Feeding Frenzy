# https://py2.codeskulptor.org/#user45_CgYPUlS4aw_2.py

# 02/10/18

import simplegui
import random

image = simplegui.load_image('https://i.imgur.com/dCH9S1v.png')
# 583 x 456

fish = []
species = []

def draw_handler(canvas):
    # LEFT
    # Green fish
    canvas.draw_image(image, (45.5, 92) ,(91, 34), (100, 100), (91 * 2, 34 * 2))
    
    # Light blue fish
    canvas.draw_image(image, (45.5, 127) ,(92, 30), (100, 200), (92 * 2, 30 * 2))

    # Spikey grey fish
    canvas.draw_image(image, (326, 36) ,(63, 64), (100, 300), (63 * 2, 64 * 2))

    # Yellow fish
    canvas.draw_image(image, (405, 371) ,(65, 38), (100, 400), (65 * 2, 38 * 2))
    
    # Catfish fish?
    canvas.draw_image(image, (139, 197) ,(94, 51), (100, 500), (94 * 2, 51 * 2))
    
    # RIGHT
    # Spikey white fish
    canvas.draw_image(image, (447, 41) ,(82, 53), (300, 100), (82 * 2, 53 * 2))
    
    # Red fish
    canvas.draw_image(image, (131, 297) ,(81, 46), (300, 200), (81 * 2, 46 * 2))
    
    # Dark blue fish
    canvas.draw_image(image, (138, 151) ,(89, 41), (300, 300), (89 * 2, 41 * 2))



    
        
    
    
frame = simplegui.create_frame('Feeding Frenzy', 800, 600)
frame.set_canvas_background('White')
frame.set_draw_handler(draw_handler)

frame.start()
