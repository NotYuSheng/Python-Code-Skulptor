# 25/09/18

import simplegui
import random

ballX_vel = 0
ballY_vel = 0

ballX = 300
ballY = 150

p1_win = False
p2_win = False

p1_score = 0
p2_score = 0

p1_vel = 0
p2_vel = 0

p1_Y = 150
p2_Y = 150

second = 0
minute = 0

Black = False
Bronze = False
Silver = False
Gold = False
Aqua = False
ball_color = "White"

# Randomize move ball left or right
direction = random.randint(1, 2)

instruction = False
endless = False
PvP = False
menu = True
board = True
hard = False
endless_win = False

# Endless button
def button1_handler():
    global instruction, endless, PvP, menu, board, Black
    instruction = False
    endless = True
    PvP = False
    menu = False
    board = True
    Black = False
    # Start Clock
    timer1.start()
    # Stop timer2 if ongoing
    timer2.stop()
    reset()

# ??? 
def button2_handler():
    global instruction, endless, PvP, menu, board, Black, hard, ball_color
    instruction = False
    endless = True
    PvP = False
    menu = False
    board = True
    hard = True
    if Aqua == False:
        Black = True
        ball_color = "Black"
    # Start Clock
    timer1.start()
    # Stop timer2 if ongoing
    timer2.stop()
    reset()
    
# PvP button
def button3_handler():
    global instruction, endless, PvP, menu, board, Black
    global p1_win, p2_win
    instruction = True
    endless = False
    PvP = False
    menu = False
    board = False
    Black = False
    p1_win = False
    p2_win = False
    timer2.start()

# Seconds for clock
def timer1_handler():
    global second
    second += 1

def timer2_handler():
    global instruction, PvP, board
    instruction = False
    PvP = True
    board = True
    reset()
    timer2.stop()

# Reset score, time, winstate and spawn a ball
def reset():
    global p1_Y, p2_Y
    global p1_score, p2_score
    global second, minute
    global p1_win, p2_win
    
    p1_Y = 150
    p2_Y = 150
    p1_score = 0
    p2_score = 0
    second = 0
    minute = 0
    p1_win = False
    p2_win = False
    
    # Randomize move ball left or right
    direction = random.randint(1, 2)
    
    spawn_ball(direction)
    
def spawn_ball(direction):
    global ballX_vel, ballY_vel
    global ballX, ballY
    global ball_color
    
    # Ball spawn position
    ballX = 300
    ballY = 150
    
    # Move ball left or right
    if direction == 1:
        ballX_vel = 3
        ballY_vel = 3
    elif direction == 2:
        ballX_vel = -3
        ballY_vel = -3
        
    # Ball color
    if   Aqua == True:
        ball_color = "Aqua"
    elif Black == True:
        ball_color = "Black"
    elif Gold == True:
        ball_color = "Gold"
    elif Silver == True:
        ball_color = "Silver"
    elif Bronze == True:
        ball_color = "Bronze"
    else:
        ball_color = "White"
        
def draw_menu(canvas):
    global p1_Y, p2_Y
    if menu == True:
        # Menu AI
        p1_Y = ballY
        p2_Y = ballY
        canvas.draw_line((300, 130), (300, 170), 6, 'Black')
        canvas.draw_text("PONG", (250, 160), 40, 'White')

def draw_instruction(canvas):
    if instruction == True:
        canvas.draw_text("First to 11 wins", (180, 160), 40, 'White')

def draw_endless(canvas):
    global ball_color, second, minute, p1_Y, endless_win
    global Bronze, Silver, Gold, Aqua
    if endless == True:
        # Impossible AI
        p1_Y = ballY
        
        # If player loses reset
        if ballX < 0:
            spawn_ball(1)
            second = 0
            minute = 0
        
        # Clock
        if second < 10:
            time_second = "0" + str(second)
        else:
            time_second = str(second)
        if second >= 60:
            if hard == False:
                if endless_win == False:
                    ball_color = "Maroon"
                    Bronze = True
            second = 0
            minute += 1
        if minute < 10:
            time_minute = "0" + str(minute)
        else:
            if hard == False:
                if endless_win == False:
                    ball_color = "Silver"
                    Silver = True
            time_minute = str(minute)
        if minute >= 60:
            endless_win = True
            minute = 0
        if   hard == True and endless_win == True:
            Aqua = True
            ball_color = "Aqua"
            canvas.draw_text("Congratulations?", (80, 150), 20, 'White')
            canvas.draw_text("Thanks for playing", (75, 180), 20, 'White')
        elif endless_win == True:
            canvas.draw_text("Why?", (120, 150), 20, 'White')
            Gold = True
            ball_color = "Yellow"
                
        time = time_minute + ":" + time_second
        canvas.draw_text(time, (430, 150), 20, 'White')
            
def draw_PvP(canvas):
    global PvP, p1_score, p2_score, p1_win, p2_win
    if   PvP == True:
        p1_win = False
        p2_win = False
        # Check either player score, add score
        if ballX < 0:
            p2_score += 1
        elif ballX > 600:
            p1_score += 1
        # Check either player reaches 11
        if   p1_score == 11:
            p1_win = True
            PvP = False
        elif p2_score == 11:
            p2_win = True
            PvP = False
        # If nobody won, continue
        elif ballX < 0:
            spawn_ball(1)
        elif ballX > 600:
            spawn_ball(2)
            
        # Draw Score
        canvas.draw_text(str(p1_score), (150, 50), 20, 'White')
        canvas.draw_text(str(p2_score), (450, 50), 20, 'White')
        
    # If either player won
    elif p1_win == True:
        canvas.draw_text("P1 Wins", (250, 160), 40, 'White')
    elif p2_win == True:
        canvas.draw_text("P2 Wins", (250, 160), 40, 'White')
            
def draw_board(canvas):
    global ballX, ballX_vel, ballY, ballY_vel, ball_color
    global p1_Y, p1_vel, p1_score
    global p2_Y, p2_vel, p2_score
    
    draw_menu(canvas)
    draw_instruction(canvas)
    draw_endless(canvas)
    draw_PvP(canvas)
    
    if board == True:                  
        # Rebounce ball from top and bottom
        if ballY < 1 or ballY > 299:
            ballY_vel *= -1 

        # Paddle contact
        if ballX > 585 and ballX < 595 and ballY < p1_Y + 30 and ballY > p1_Y - 30:
            ballX_vel *= -1
            # Ball max speed
            if ballX_vel > - 9 and ballX_vel < 9: 
                ballX_vel -= 1
        if ballX > 5 and ballX < 15 and ballY < p2_Y + 30 and ballY > p2_Y - 30:
            ballX_vel *= -1
            # Ball max speed
            if ballX_vel > - 9 and ballX_vel < 9:
                ballX_vel += 1

        # Paddle contact special cases
        if ballX < 15:
            if p2_Y - 30 > ballY and p2_Y + 30 < ballY:
                ballY_vel *= -1
        elif ballX > 585:
            if p1_Y - 30 > ballY and p1_Y + 30 < ballY:
                ballY_vel *= -1

        # Update
        ballX += ballX_vel
        ballY += ballY_vel
        p1_Y += p1_vel
        p2_Y += p2_vel

        # Paddle out of bounce
        if p1_Y - 30 <= 0:
            p1_Y = 30
        if p2_Y - 30 <= 0:
            p2_Y = 30
        if p1_Y + 30 >= 300:
            p1_Y = 270
        if p2_Y + 30 >= 300:
            p2_Y = 270

        # Draw Middle Line
        canvas.draw_line((300, 0), (300, 300), 5, 'White')
        my_list = range(0, 300, 10)
        for i in my_list: 
            canvas.draw_line((300, i+5), (300, i + 10), 6, 'Black')

        # Draw Ball
        canvas.draw_circle((ballX,ballY), 1, 5, ball_color, ball_color)

        # Draw Paddle
        canvas.draw_line((590, p1_Y - 30), (590, p1_Y + 30), 10, 'White')
        canvas.draw_line((10, p2_Y - 30), (10, p2_Y + 30), 10, 'White')
    
def keydown_handler(key):
    global p1_vel, p2_vel
    if key == simplegui.KEY_MAP['up']:
        p1_vel -= 5
    elif key == simplegui.KEY_MAP['down']:
        p1_vel += 5
    elif key == simplegui.KEY_MAP['w']:
        p2_vel -= 5
    elif key == simplegui.KEY_MAP['s']:
        p2_vel += 5

def keyup_handler(key):
    global p1_vel, p2_vel
    if key == simplegui.KEY_MAP['up']:
        p1_vel += 5
    elif key == simplegui.KEY_MAP['down']:
        p1_vel -= 5
    elif key == simplegui.KEY_MAP['w']:
        p2_vel += 5
    elif key == simplegui.KEY_MAP['s']:
        p2_vel -= 5
    
frame = simplegui.create_frame('PONG', 600, 300)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
spawn_ball(direction)
frame.set_draw_handler(draw_menu)
frame.set_draw_handler(draw_instruction)
frame.set_draw_handler(draw_endless)
frame.set_draw_handler(draw_PvP)
frame.set_draw_handler(draw_board)
button1 = frame.add_button('Endless', button1_handler,100)
button2 = frame.add_button('???', button2_handler, 100)
button23 = frame.add_button('PvP', button3_handler, 100)

timer1 = simplegui.create_timer(1000, timer1_handler)
timer2 = simplegui.create_timer(3000, timer2_handler)

frame.start()
