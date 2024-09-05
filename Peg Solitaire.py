# https://docs.google.com/document/d/1AKmfTuEGy02ltVkPhTKHoP70l1XFCSUB5s8-Y7BVf_g/edit

# 02/10/18
import simplegui
color = "Black"



def draw(canvas):
    #canvas.draw_circle(center_point, radius, line_width, line_color)
    
    #canvas.draw_circle((150, 150), 20, 1, "Black")
    
    # Frame
    canvas.draw_line((250,  50), (550,  50), 1, "Black")
    canvas.draw_line((250,  50), (250, 250), 1, "Black")
    canvas.draw_line((50 , 250), (250, 250), 1, "Black")
    canvas.draw_line((50 , 250), (50 , 550), 1, "Black")
    canvas.draw_line((50 , 550), (250, 550), 1, "Black")
    canvas.draw_line((250, 550), (250, 750), 1, "Black")
    canvas.draw_line((250, 750), (550, 750), 1, "Black")
    canvas.draw_line((550, 750), (550, 550), 1, "Black")
    canvas.draw_line((550, 550), (750, 550), 1, "Black")
    canvas.draw_line((750, 250), (750, 550), 1, "Black")
    canvas.draw_line((550,  50), (550, 250), 1, "Black")
    canvas.draw_line((550, 250), (750, 250), 1, "Black")




frame = simplegui.create_frame("Peg Solitaire", 800, 800)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)

frame.start()
