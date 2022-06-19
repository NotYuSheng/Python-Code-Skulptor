# https://py2.codeskulptor.org/#user45_GlIniqqF8H_232.py

# 26/09/18
import simplegui

anti_ghost = False

chip = []
chip_X = 115
chip_Y = 50
chip_Y_destination = 700

image1 = simplegui.load_image('https://i.imgur.com/XaXQgGY.png')# Frame

turn = 0

gamestate = 1
winner = ""

def timer1_handler():
    global anti_ghost, chip_X, chip_Y, turn
    # Move chip to destination
    if chip_Y != chip_Y_destination:
        chip_Y += 10
    else:
        timer1.stop()
        # Add chip into list 
        add_chip()
        
        # Spawn next chip
        chip_X = 115
        chip_Y = 50

        # Flip turn Red / Navy
        if turn == 0:
            turn = 1
        elif turn == 1:
            turn = 0
            
        # Turn off anti_ghost
        anti_ghost = False

        # Sort chip
        chip.sort()
        
# Check if column already have 6 chips
def check_column():
    # Counting how many chips already in that column
    chip_X_num = 0
    a = len(chip)
    my_list = range(0, a, 1)
    for i in my_list:
        if chip[i][0] == chip_X:
            chip_X_num += 1
    if chip_X_num == 6:
        return False
    else:
        return True
            
def determine_chip_Y_destination():
    # Declare Global Variables
    global chip_Y_destination
    
    # Count how many chips already in that column
    chip_Y_num = 0
    a = len(chip)
    my_list1 = range(0, a, 1)
    for i in my_list1:
        if chip[i][0] == chip_X:
            chip_Y_num += 1
    chip_Y_destination = 700 - chip_Y_num * 100
    
def add_chip():
    # Add new chip into list
    if turn == 0:
        chip_color = "Red"
    elif turn == 1:
        chip_color = "Navy"
    chip.append([chip_X, chip_Y_destination, chip_color])
    
    # Check for winner
    print chip
    check_win()

def check_win():
    global gamestate, winner
    
    # Draw
    a = len(chip)
    my_list = range(0, a, 1)
    if a == 42:
        winner = "Draw"
        gamestate = 0
    
    # Vertical Win
    for i in my_list:
        for j in my_list:
            if chip[i][0] == chip[j][0] and chip[i][1] - 100 == chip[j][1] and chip[i][2] == chip[j][2]:
                for k in my_list:
                    if chip[j][0] == chip[k][0] and chip[j][1] - 100 == chip[k][1] and chip[j][2] == chip[k][2]:
                        for l in my_list:
                            if chip[k][0] == chip[l][0] and chip[k][1] - 100 == chip[l][1] and chip[k][2] == chip[l][2]:
                                if   chip[i][2] == "Red":
                                    winner = "Red"
                                elif chip[i][2] == "Navy":
                                    winner = "Navy"
                                gamestate = 0
                
    # Horizontal Win
    for i in my_list:
        for j in my_list:
            if chip[i][0] + 100 == chip[j][0] and chip[i][1] == chip[j][1] and chip[i][2] == chip[j][2]:
                for k in my_list:
                    if chip[j][0] + 100 == chip[k][0] and chip[j][1] == chip[k][1] and chip[j][2] == chip[k][2]:
                        for l in my_list:
                            if chip[k][0] + 100 == chip[l][0] and chip[k][1] == chip[l][1] and chip[k][2] == chip[l][2]:
                                if   chip[i][2] == "Red":
                                    winner = "Red"
                                elif chip[i][2] == "Navy":
                                    winner = "Navy"
                                gamestate = 0

    # Diagonal Right Win
    for i in my_list:
        for j in my_list:
            if chip[i][0] + 100 == chip[j][0] and chip[i][1] - 100 == chip[j][1] and chip[i][2] == chip[j][2]:
                for k in my_list:
                    if chip[j][0] + 100 == chip[k][0] and chip[j][1] - 100 == chip[k][1] and chip[j][2] == chip[k][2]:
                        for l in my_list:
                            if chip[k][0] + 100 == chip[l][0] and chip[k][1] - 100 == chip[l][1] and chip[k][2] == chip[l][2]:
                                if   chip[i][2] == "Red":
                                    winner = "Red"
                                elif chip[i][2] == "Navy":
                                    winner = "Navy"
                                gamestate = 0
                                
    # Diagonal Left Win
    for i in my_list:
        for j in my_list:
            if chip[i][0] + 100 == chip[j][0] and chip[i][1] + 100 == chip[j][1] and chip[i][2] == chip[j][2]:
                for k in my_list:
                    if chip[j][0] + 100 == chip[k][0] and chip[j][1] + 100 == chip[k][1] and chip[j][2] == chip[k][2]:
                        for l in my_list:
                            if chip[k][0] + 100 == chip[l][0] and chip[k][1] + 100 == chip[l][1] and chip[k][2] == chip[l][2]:
                                if   chip[i][2] == "Red":
                                    winner = "Red"
                                elif chip[i][2] == "Navy":
                                    winner = "Navy"
                                gamestate = 0

class Objects:
    def draw_chips(self, canvas):
        a = len(chip)
        my_list = range(0, a, 1)
        for i in my_list:
            self.chip_X     = chip[i][0]
            self.chip_Y     = chip[i][1]
            self.chip_color = chip[i][2]
            canvas.draw_circle((self.chip_X, self.chip_Y), 45, 1, "Black", self.chip_color)
            canvas.draw_circle((self.chip_X, self.chip_Y), 40, 1, "Black", self.chip_color)
    
    def chip(self, canvas):
        if   turn == 0:
            chip_color = "Red"
        elif turn == 1:
            chip_color = "Navy"
        canvas.draw_circle((chip_X, chip_Y), 45, 1, "Black", chip_color)
        canvas.draw_circle((chip_X, chip_Y), 40, 1, "Black", chip_color)
        
def draw_handler(canvas):
    # Draw chip used for selection
    if gamestate == 1:
        Objects().chip(canvas)
    
    # Draw chips
    Objects().draw_chips(canvas)
        
    # Draw Frame
    canvas.draw_image(image1, (830 / 2, 780 / 2), (830, 780), (830 / 2, 780 / 2), (830, 780))
    
    # Draw gameover
    if gamestate == 0:
        if winner == "Draw":
            canvas.draw_text("Out of moves, Draw", (80, 50), 20, 'Black', 'serif')
        else:
            canvas.draw_text(str(winner) + " Wins", (80, 50), 20, 'Black', 'serif')
        canvas.draw_text("Press space to start new game", (560, 50), 20, 'Black', 'serif')

def keydown_handler(key):
    # Anti_ghost old method of preventing multiple keys refer to sonic for new format
    global anti_ghost, gamestate, turn
    global chip, chip_X
    if   key == simplegui.KEY_MAP["space"]:
        if gamestate == 1:
            if check_column() == True:
                anti_ghost = True
                determine_chip_Y_destination()
                timer1.start()
        elif gamestate == 0:
            chip = []
            gamestate = 1
            turn = 0
        
    elif key == simplegui.KEY_MAP["right"] and anti_ghost == False:
        if chip_X < 715:
            chip_X += 100
        
    elif key == simplegui.KEY_MAP["left"] and anti_ghost == False:
        if chip_X > 115:
            chip_X -= 100
            
frame = simplegui.create_frame("Connect Four", 830, 780)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)
timer1 = simplegui.create_timer(1, timer1_handler)

frame.start()
