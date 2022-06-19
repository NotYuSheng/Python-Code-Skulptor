# https://py2.codeskulptor.org/#user45_PGwBEjnMQn_31.py

# 08/10/18

import simplegui

snake_vel_X = 25
snake_vel_Y = 0

snake = [[[50,  50], [75,  50], [75,  75], [50,  75]], 
         [[80,  50], [105, 50], [105, 75], [80,  75]], 
         [[110, 50], [135, 50], [135, 75], [110, 75]]]

# Variable declaration
up    = False
left  = False
down  = False
right = False

def timer1_handler():
    global snake
    global snake_vel_X, snake_vel_Y
    Snake.update_speed()
    a = len(snake)
    if up == True:
        #snake.pop(a - 1)
        snake_vel_Y -= 25
    if down == True:
        snake_vel_Y += 25
    if left == True:
        snake_vel_X -= 25
    if right == True:
        snake_vel_X += 25
    
class Snake:
    def update_speed():
        a = len(snake)
        my_list1 = range(0, a, 1)
        my_list2 = range(0, 4, 1)
        for i in my_list1:
            for j in my_list2:
                snake[i][j][0] += snake_vel_X
                snake[i][j][1] += snake_vel_Y
    
    def draw_snake(self, canvas):
        a = len(snake)
        my_list = range(0, a, 1)
        for i in my_list:
            canvas.draw_polygon(snake[i], 1, "White", "White")

def draw(canvas):
    Snake().draw_snake(canvas)
    canvas.draw_circle((800 / 2, 600 / 2), 12.5, 1, "White", "White")

def keydown_handler(key):
    global up, left, down, right
    if   key==simplegui.KEY_MAP["up"]:
        up    = True
    if   key==simplegui.KEY_MAP["left"]:
        left  = True
    if   key==simplegui.KEY_MAP["down"]:
        down  = True
    if   key==simplegui.KEY_MAP["right"]:
        right = True
    
def keyup_handler(key):
    global up, left, down, right
    if   key==simplegui.KEY_MAP["up"]:
        up    = False
    if   key==simplegui.KEY_MAP["left"]:
        left  = False
    if   key==simplegui.KEY_MAP["down"]:
        down  = False
    if   key==simplegui.KEY_MAP["right"]:
        right = False
    
frame = simplegui.create_frame("Snake", 800, 600)
frame.set_canvas_background('Black')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keydown_handler(keyup_handler)
timer1 = simplegui.create_timer(1000, timer1_handler)

timer1.start()
frame.start()
