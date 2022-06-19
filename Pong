# http://www.codeskulptor.org/#user45_0yh8oz33Bw_0.py

# Yu Sheng 18/09/18
import simplegui
import random

by = 300
bx = 500
by_vel = 0
bx_vel = 0
center_point = [bx, by]
radius = 20
line_width = 5
p1_score = 0
p2_score = 0
p1_y = 265
p2_y = 265
p1_vel = 0 
p2_vel = 0
game_state = 0;
message1 = "PONG"
message2 = "18/09/18 | Yu Sheng"
message3 = "First to 11 Wins"
message4 = "Player 1 Wins"
message5 = "Player 2 Wins"
milli_s = 0

# Reset
def reset():
    global game_state, p1_score, p2_score, by, bx, by_vel, bx_xel, center_point
    game_state = 0;
    p1_score = 0
    p2_score = 0
    by = 300
    bx = 500
    by_vel = 0
    bx_vel = 0
    center_point = [bx, by]
    RNG()

# Ball RNG
def RNG():
    global lower, upper, range_width, by_RNG
    lower = 2
    upper = 3
    range_width = upper - lower
    by_RNG = round(random.random() * range_width + lower) # ball up or down

# 2 player setup
def player2():
    reset()
    frame.set_draw_handler(draw2)
    timer.start()

# timer
def update_timer():
    global milli_s
    milli_s += 1
    if(milli_s > 400):
        timer.stop()
        milli_s = 0
        frame.set_draw_handler(draw3)

# Handler to draw on canvas
def draw1(canvas):
    canvas.draw_text(message1, (425, 275), 50, 'White', 'sans-serif')
    canvas.draw_text(message2, (350, 325), 30, 'White', 'sans-serif')

def draw2(canvas):
    canvas.draw_text(message3, (350, 300), 50, 'White', 'sans-serif')
    timer.start()
    
def draw3(canvas):
    global game_state, p1_score, p2_score, by_RNG, p1_y, p1_vel, p2_y, p2_vel, by, bx, by_vel, bx_vel, center_point
    canvas.draw_line((500, 15), (500, 585), 10, 'White')
    my_list = range(0, 1000, 38)
    for i in my_list:
        canvas.draw_line((500, i+10), (500, i+25), 10, 'Black')
    canvas.draw_text(str(p1_score), (240, 100), 50, 'White', 'sans-serif')
    canvas.draw_text(str(p2_score), (750, 100), 50, 'White', 'sans-serif')
    
    # Ball velocity logic
    if(by_RNG == 2.0):
        by_vel = 3
        bx_vel = 3
        by_RNG = 4.0
    elif(by_RNG == 3.0):
        by_vel = -3
        bx_vel = -3
        by_RNG = 5.0
    bx += bx_vel
    by += by_vel
    
    # out of bounds logic
    if(by <= 25):
        by = 25
        by_vel *= -1
        by += by_vel
    elif(by >= 575):
        by = 575
        by_vel *= -1
        by += by_vel

    if(bx <= 0):
        bx = 500
        by = 300
        bx_vel = 3
        by_vel = 3
        bx += bx_vel
        by += by_vel
        p2_score += 1
    elif(bx >= 1000):
        bx = 500
        by = 300
        bx_vel = -3
        by_vel = -3
        bx += bx_vel
        by += by_vel
        p1_score += 1
    
    # gameover check
    if(p1_score == 11):
        canvas.draw_text(message4, (100, 300), 50, 'White', 'sans-serif')
        game_state = 1
    elif(p2_score == 11):
        canvas.draw_text(message5, (600, 300), 50, 'White', 'sans-serif')
        game_state = 1
    
    # p1 velocity logic
    p1_y += p1_vel;
    if(p1_y <= 10):
        p1_y = 10
    elif(p1_y >= 520):
        p1_y = 520
    
    # p2 velocity logic
    p2_y += p2_vel;
    if(p2_y <= 10):
        p2_y = 10
    elif(p2_y >= 520):
        p2_y = 520
    
    # paddle hit box
    if((by >= p1_y and by <= p1_y +70) and (bx <= 44 and bx >= 1)):
        by_vel = (by_vel * -1) + 1
        bx_vel = (bx_vel * -1) + 1
    if((by >= p2_y and by <= p2_y +70) and (bx <= 999 and bx >= 956)):
        by_vel = (by_vel * -1) - 1
        bx_vel = (bx_vel * -1) - 1
    center_point = [bx, by]
    
    # draw ball
    if(game_state == 0):
        canvas.draw_circle(center_point, 2, line_width, "White", "White")
    elif(game_state == 1):
        by_vel = 0
        bx_vel = 0
    # draw paddles
    canvas.draw_line((20, p1_y), (20, p1_y + 70), 12, 'White')
    canvas.draw_line((988, p2_y), (988, p2_y + 70), 12, 'White')

# Keys
def keydown(key):
    global p1_vel, p2_vel
    if key == simplegui.KEY_MAP['w']:
        p1_vel -= 8
    if key == simplegui.KEY_MAP['s']:
        p1_vel += 8
    if key == simplegui.KEY_MAP['up']:
        p2_vel -= 8
    if key == simplegui.KEY_MAP['down']:
        p2_vel += 8
   
def keyup(key):
    global p1_vel, p2_vel
    if key == simplegui.KEY_MAP['w']:
        p1_vel += 8
    if key == simplegui.KEY_MAP['s']:
        p1_vel -= 8
    if key == simplegui.KEY_MAP['up']:
        p2_vel += 8
    if key == simplegui.KEY_MAP['down']:
        p2_vel -= 8

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("PONG | 18/09/18 | Yu Sheng", 1000, 600)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("2 Players", player2)
timer = simplegui.create_timer(1, update_timer)

if(game_state == 0):
    frame.set_draw_handler(draw1)
# Start the frame animation
frame.start()

