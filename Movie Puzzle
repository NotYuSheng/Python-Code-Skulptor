# https://py2.codeskulptor.org/#user45_rkYNgL4ZIt_28.py
#5/11/18
import simplegui
import random

FRAME_SIZE = 600, 600
SPAWN_LOCATION = [FRAME_SIZE[0] / 2, FRAME_SIZE[1] / 2]
BALL_RADIUS = 40
BALL_LINE_WIDTH = 1
BALL_COLOR = "Orange"
BALL_LINE_COLOR = "Black"
BALL_FILL_COLOR = BALL_COLOR

ball_center_point = SPAWN_LOCATION
ball_vel_x = 5
ball_vel_y = 5

def draw(canvas):
    global ball_vel_x, ball_vel_y
    
    # Rebounce
    if   ball_center_point[0] < 0 + BALL_RADIUS + BALL_LINE_WIDTH or ball_center_point[0] > FRAME_SIZE[0] - BALL_RADIUS - BALL_LINE_WIDTH:
        ball_vel_x *= -1
    elif ball_center_point[1] < 0 + BALL_RADIUS + BALL_LINE_WIDTH or ball_center_point[1] > FRAME_SIZE[1] - BALL_RADIUS:
        ball_vel_y *= -1
    
    # Update ball
    ball_center_point[0] += ball_vel_x
    ball_center_point[1] += ball_vel_y
    
    # Grid
    canvas.draw_line((FRAME_SIZE[0] / 3, 0), (FRAME_SIZE[0] / 3, FRAME_SIZE[1]), 1, "Black")
    canvas.draw_line((FRAME_SIZE[0] / 3 * 2, 0), (FRAME_SIZE[0] / 3 * 2, FRAME_SIZE[1]), 1, "Black")
    canvas.draw_line((0, FRAME_SIZE[1] / 3), (FRAME_SIZE[0], FRAME_SIZE[1] / 3), 1, "Black")
    canvas.draw_line((0, FRAME_SIZE[1] / 3 * 2), (FRAME_SIZE[0], FRAME_SIZE[1] / 3 * 2), 1, "Black")
    
    # Ball
    canvas.draw_circle(ball_center_point, BALL_RADIUS, BALL_LINE_WIDTH, BALL_LINE_COLOR, BALL_FILL_COLOR)

frame = simplegui.create_frame("Movie Puzzle", FRAME_SIZE[0], FRAME_SIZE[1])
frame.set_canvas_background('Navy')
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
